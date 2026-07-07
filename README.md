# Interactive MBTI Test Game 🐾

Visual novel tes kepribadian MBTI berbasis **Ren'Py** dengan **AI Companion** bertenaga OpenAI (GPT-4o). Pemain menjawab 20 soal cerita interaktif ditemani satu dari lima hewan companion — masing-masing merepresentasikan satu trait **Big Five (OCEAN)** — yang bereaksi secara real-time terhadap setiap pilihan pemain, lengkap dengan ekspresi emosi yang berubah-ubah.

> ⚠️ **Disclaimer:** Ini adalah tes kepribadian sederhana yang terinspirasi Myers-Briggs Type Indicator (MBTI). Hasilnya adalah cerminan awal / bahan refleksi, bukan diagnosis profesional.

Dibuat oleh **Fuzakis Project**.

---

## Fitur

- 🎲 **60 soal cerita** dalam 3 paket (A/B/C), diacak anti-ulang antar sesi
- 🦊 **5 AI Companion** dengan persona Big Five: Kitsuko (Openness), Onyen (Conscientiousness), Iwank (Extraversion), Susagi (Agreeableness), Jakouko (Neuroticism)
- 🎭 **Emotion parser** — ekspresi sprite companion berubah mengikuti tag emosi dari AI (model emosi Ekman)
- 🧮 **Skoring MBTI 4 dimensi** (I/E, S/N, T/F, J/P) + Spirit Animal per tipe
- 💬 **Free chat** dengan companion + **memori permanen** per pemain (JSON)
- 🏆 Achievement, music room, multi-profil, dwi-bahasa (ID/EN)
- 📊 Logging CSV otomatis (latency, token usage, hasil tes) untuk keperluan riset

---

## Setup Proyek

### 1. Prasyarat

- [Ren'Py SDK](https://www.renpy.org/latest.html) **8.5.x** (dikembangkan di 8.5.2)
- API key OpenAI (model default: `gpt-4o`)
- Windows/Mac/Linux (dikembangkan & diuji di Windows 11)

### 2. Clone & daftarkan ke Ren'Py

```bash
git clone https://github.com/fuzakis/Interactive-MBTI-Game.git
```

Buka **Ren'Py Launcher** → `preferences` → set *Projects Directory* ke folder induk hasil clone (atau pindahkan folder proyek ke projects directory kamu). Proyek akan muncul di daftar dengan nama foldernya.

### 3. Konfigurasi API Key (`game/.env`)

Buat file `game/.env` (tidak ikut ter-commit dan ter-build):

```
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxx
```

Loader ada di `game/definitions.rpy` — urutan pembacaan: `game/.env` → env var `OPENAI_API_KEY_2` → env var `OPENAI_API_KEY`. Kalau semuanya kosong, muncul warning di console dan setiap panggilan AI akan mengembalikan pesan error koneksi (game tetap jalan, tapi companion tidak bisa bicara).

### 4. SSL Fix (sudah termasuk, jangan dihapus)

Build Python di Ren'Py sering gagal memverifikasi sertifikat HTTPS. File `game/01_fix_ssl.rpy` (jalan di `init -999`) melakukan monkeypatch `certifi.where()` agar menunjuk ke `game/python-packages/certifi/cacert.pem`. Pastikan folder `game/python-packages/certifi/` ada.

### 5. Jalankan

Ren'Py Launcher → pilih proyek → **Launch Project**. Log debug (prompt AI, latency, skor MBTI berjalan) tampil di console/`log.txt`.

---

## Arsitektur Sistem

```
game/
├── 01_fix_ssl.rpy               # Monkeypatch certifi (init -999) untuk HTTPS
├── definitions.rpy              # Persona/system prompt, API call, .env loader,
│                                #   auto-generate image companion, memori AI (JSON)
├── script.rpy                   # Alur utama: splash → pilih companion → tutorial AI
│                                #   → tes → hasil & evaluasi → free chat → ending
├── questions_data.rpy           # [GENERATED] Daftar paket soal (A/B/C) + dimensi
├── questions_logic.rpy          # Pengacakan paket, loop soal, ai_react_logic,
│                                #   breakdown_ai_text (pemenggal kalimat)
├── questions_logic_generated.rpy# [GENERATED] 60 soal × 2 bahasa (label + menu + skor)
├── logger.rpy                   # Logging CSV (API chat, hasil MBTI, rekap token)
├── custom_screens.rpy           # Screen kustom (seleksi companion, diagram hasil,
│                                #   achievements, music room, profil, free chat hub)
├── screens.rpy / gui.rpy / options.rpy  # UI Ren'Py standar (sudah dimodifikasi)
└── .env                         # API key (JANGAN di-commit)
```

---

## Cara Kerja Tiap Sistem

### 1. Prompt Engineering & Personality

Setiap companion punya **system prompt persona** di `get_system_prompt()` (`definitions.rpy`), tersedia dalam 2 bahasa. Struktur tiap persona:

- **PERAN** — identitas karakter (mis. "Kamu adalah Jakouko yang mewakili sifat Neuroticism")
- **SIFAT** — trait kepribadian yang harus diperankan
- **GAYA BICARA** — pola bahasa khas (Iwank pakai "Guk!", Susagi gagap sopan, Jakouko paranoid dengan kalimat terputus)
- **ATURAN TAG** — kontrak format tag emosi (lihat Emotion Parser)
- **CONTOH DIALOG** — few-shot examples agar gaya konsisten

Ada persona khusus `"psychologist"` — mode objektif **tanpa** tag emosi, dipakai untuk penjelasan detail hasil MBTI.

Selain system prompt, tiap konteks punya **user prompt** tersendiri (di `script.rpy` / `questions_logic.rpy`): tutorial interaktif, reaksi per soal (dengan rekap 5 pilihan terakhir agar percakapan nyambung), evaluasi akhir 3 bagian (dipisah `###`), dan free chat (dengan sliding window memori 10-15 chat).

### 2. API Call

`get_ai_feedback(user_text, personality_key, lang, token_limit)` di `definitions.rpy`:

1. Rakit system prompt sesuai persona + user prompt sesuai konteks
2. POST ke `https://api.openai.com/v1/chat/completions` via `urllib` (model `gpt-4o`, `temperature 0.9`)
3. Sanitasi respons: `{` `}` → `(` `)` (karena `{}` adalah text tag Ren'Py), strip kutip terluar
4. Akumulasi token usage ke variabel sesi + tulis baris ke `PA_Log_API_Chat.csv`
5. Kalau error → return `"[NEUTRAL] (Error Koneksi: ...)"` sehingga game tidak crash

`token_limit` per konteks: reaksi soal 300 · tutorial 500 · free chat 800–1000 · evaluasi akhir 1500 · penjelasan psikolog 2000.

### 3. Emotion Parser

Kontrak dengan AI: sisipkan tag `[HAPPY] [SAD] [ANGRY] [FEAR] [SURPRISE] [DISGUST] [NEUTRAL]` di setiap perubahan nada.

Alur parsing (ada di tutorial, reaksi soal, evaluasi, dan chat):

1. **`breakdown_ai_text()`** memecah respons jadi kalimat-kalimat: per baris → buang kutip pembungkus paragraf → split di `.` `!` `?` (elipsis `...` tidak memecah) → split sebelum tag `[`
2. Tiap kalimat dicek regex `\[(.*?)\]` — tag "liar" dipetakan ke emosi valid (mis. `[WORRIED]`/`[ANXIOUS]` → fear, `[EXCITED]` → happy, `[GUK]` → neutral)
3. Kalau emosi berubah → `renpy.show("companion <personality> <emosi>")` mengganti sprite
4. Tag dihapus dari teks, lalu `renpy.say()` menampilkan kalimat bersih satu per satu (pacing klik-per-kalimat)

Sprite emosi di-generate otomatis saat init dari pola `images/<Folder>/<Nama> <emosi>.png`, dengan animasi kedip otomatis bila file `_blink.png` tersedia (anti-crash: fallback ke gambar statis).

Tag spesial `[SPIRIT]` pada evaluasi akhir memicu penampilan gambar Spirit Animal dengan animasi zoom.

### 4. MBTI Scoring

- 4 counter global: `IE`, `SN`, `TF`, `JP` (mulai 0)
- Setiap soal menguji **2 dimensi sekaligus** (mis. "E/I & S/N"); tiap pilihan menambah/mengurangi **±5** pada 2 dimensi tersebut
- 20 soal per sesi → tiap dimensi diuji ±10 kali
- Penentuan huruf di `scene_hasil_tes`: skor `>= 0` → **E / N / F / P**, skor negatif → **I / S / T / J**
- Persentase dominasi: `50 + (|skor| / 2)`
- Hasil 4 huruf dipetakan ke **Spirit Animal** (dict `spirit_animals`, 16 tipe × 2 bahasa)

### 5. Sistem Soal (Generated)

`questions_data.rpy` dan `questions_logic_generated.rpy` dihasilkan generator eksternal. Pola tiap soal:

```
label show_question_<id>_<lang>:
    scene bg <lokasi>
    $ narasi_asli = "..."          # disimpan untuk konteks prompt AI
    n "..."                        # narasi bertahap
    menu:
        "<pilihan A>":
            $ IE -= 5 / $ SN -= 5  # skor 2 dimensi
            $ user_choice_text = "..." ; $ last_answer = "Introvert & Sensing"
            jump <label>_A         # append user_journey_summary → call ai_react_logic
```

Pengacakan: pilih paket yang belum pernah dimainkan (`persistent.used_packet_titles`), lalu shuffle urutan soal dengan LCG sederhana.

### 6. Memori AI & Profil Pemain

- Per pasangan (pemain, companion) disimpan file JSON di save directory: `<nama>_<companion>.json` berisi `last_mbti`, `known_facts`, `chat_history`
- Free chat menyuntikkan 10 chat terakhir ke prompt (sliding window) sehingga companion "ingat" obrolan lintas sesi
- `profile_manager_screen` memindai semua JSON untuk daftar multi-profil

### 7. Logging Riset (CSV)

| File | Isi |
|---|---|
| `PA_Log_API_Chat.csv` | Timestamp, karakter, model, latency, token in/out/total, prompt, respons — per API call |
| `PA_Log_MBTI_Akhir.csv` | Nama, hasil MBTI, spirit animal, skor mentah, memori akhir — per sesi selesai |
| `PA_Rekap_10_Permainan.csv` | Rekap jumlah interaksi & total token per sesi |

File-file ini berisi data partisipan → **tidak di-commit** (lihat `.gitignore`).

---

## Build & Distribusi

- **PC:** Ren'Py Launcher → Build Distributions. `options.rpy` sudah meng-exclude package python besar (~3GB) dan `game/.env` dari build.
- **Android:** konfigurasi di `android.json` (landscape, permission `INTERNET` + `VIBRATE`). Keystore **tidak** disertakan di repo — generate milikmu sendiri via RAPT.
- Distribusi publik sebaiknya **tanpa API key** — pemain/penguji mengisi `game/.env` sendiri, atau gunakan proxy server.

## Catatan Pengembangan

- **`CATATAN_PENTING.md`** — hal-hal yang harus diperhatikan agar game tidak rusak (dependensi antar-file, kontrak tag emosi, persistent data, dll). **Baca sebelum mengubah kode.**
- **`catatan update ke game MBTI.md`** — daftar perbaikan berdasarkan masukan Expert Evaluator (SATGAS PPKS PENS) dan hasil user testing.
