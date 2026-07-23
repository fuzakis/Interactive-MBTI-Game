# CATATAN PENTING — Hal-Hal yang Harus Diperhatikan Agar Game Tidak Rusak

> Dokumen ini dibuat sebagai panduan sebelum mengubah kode.
> Baca dulu sebelum edit, terutama bagian yang saling bergantung antar-file.

---

## 1. Rantai Sistem AI (paling rawan)

Alur teks AI dari request sampai tampil di layar:

```
Prompt (script.rpy / questions_logic.rpy)
   → get_ai_feedback()          [definitions.rpy]  — API call ke OpenAI
   → breakdown_ai_text()        [questions_logic.rpy] — pemenggal kalimat
   → loop parsing tag [EMOSI]   [4 lokasi, lihat di bawah]
   → renpy.say(ai, clean_sentence)
```

**Aturan yang TIDAK boleh dilanggar:**

- **Tag emosi harus format `[HAPPY]`, `[SAD]`, `[ANGRY]`, `[FEAR]`, `[SURPRISE]`, `[DISGUST]`, `[NEUTRAL]`.**
  Semua system prompt menginstruksikan ini. Kalau menambah emosi baru, harus update **4 tempat sekaligus**:
  1. Mapping `emo_map` di `definitions.rpy` (untuk generate image `companion <p> <emosi>`)
  2. Loop parsing di `label ai_react_logic` (`questions_logic.rpy`)
  3. Loop parsing di `label sesi_tutorial_ai` dan `scene_hasil_tes` (`script.rpy`)
  4. Loop parsing di `chat_loop` dan `free_chat_loop_khusus` (`script.rpy`)
  Plus: harus ada file gambar `images/<Folder>/<Nama> <emosi>.png` untuk **kelima** karakter, kalau tidak → crash saat `renpy.show`.

- **`get_ai_feedback()` mengganti `{` `}` menjadi `(` `)`. JANGAN DIHAPUS.** Ren'Py menganggap `{...}` sebagai text tag. Ini satu-satunya yang melindungi popup penjelasan psikolog di `custom_screens.rpy` (`text "[detailed_mbti_explanation]"`), karena di jalur screen teks tidak bisa di-escape (lihat poin berikut).

- **Semua teks AI WAJIB ditampilkan lewat `say_ai_safe()`** (`questions_logic.rpy`), jangan `renpy.say(ai, ...)` langsung. Fungsi itu melakukan dua hal:
  1. `sanitize_ai_text()` — menggandakan `[` → `[[` dan `{` → `{{`. Tanpa ini, teks AI yang mengandung kode program **membuat game CRASH**. Sudah diuji dengan runtime Ren'Py: `arr[i] = 5` → NameError, `arr[i` → open format, `[]` → ValueError, `if x {` → open text tag; dan `data[0]` tampil jadi `data0` (teks hilang diam-diam tanpa error).
  2. `chunk_long_text()` — memenggal teks di atas `MAX_SAY_CHARS` (300) pada batas kata, supaya balasan AI yang kebablasan tidak meluber keluar textbox.

- **Jangan pakai `sanitize_ai_text()` untuk teks yang masuk lewat interpolasi screen** (contoh: `text "[detailed_mbti_explanation]"`). Di jalur itu nilai disisipkan **setelah** substitusi, jadi `[[` akan terlihat mentah oleh pemain. Sudah diverifikasi: `[` di dalam nilai tidak diproses ulang, jadi jalur screen aman selama sanitasi `{`→`(` di atas tetap ada.

- **`breakdown_ai_text()`** (`questions_logic.rpy`) sekarang: memecah per baris → membuang kutip pembungkus paragraf → memecah per kalimat (`.` `!` `?`, opsional diikuti `"`), **elipsis `...` tidak memecah**, dan memecah sebelum tag `[`. Fungsi ini dipakai di 5 tempat (tutorial, reaksi soal, evaluasi akhir, chat pasca-tes, free chat). Ubah di satu tempat = berdampak ke semua.

- **Evaluasi akhir dipecah dengan `###`** (`eval_response.split("###")` di `script.rpy`). Prompt evaluasi WAJIB tetap menyuruh AI memisahkan 3 bagian dengan `###`, dan bagian 3 wajib mengandung tag `[SPIRIT]` (interceptor menampilkan gambar spirit animal). Kalau format prompt diubah, cek interceptor `[SPIRIT]`.

## 2. SSL Fix — jangan dihapus/dipindah

- `01_fix_ssl.rpy` berjalan di `init -999` (paling awal). Dia monkeypatch `certifi.where()` agar menunjuk `game/python-packages/certifi/cacert.pem`. Tanpa ini, request HTTPS ke OpenAI **gagal SSL error** di build Ren'Py.
- Folder `game/python-packages/` berisi `certifi` — jangan dihapus.
- Nama file diawali `01_` agar urutan load benar; `init -999` menjamin jalan sebelum init python lain.

## 3. API Key & Mode Proxy

- Key dibaca dari **`game/.env`** (format `OPENAI_API_KEY=sk-...`), fallback ke environment variable `OPENAI_API_KEY_2` / `OPENAI_API_KEY`. Loader ada di `definitions.rpy`.
- `game/.env` **di-ignore git** (`.gitignore`) dan **di-exclude dari build** (`build.classify('game/.env', None)` di `options.rpy`). Jangan hapus dua proteksi ini.
- ⚠️ Key lama sempat tertulis hardcode di komentar `definitions.rpy` (sudah dihapus). Karena pernah ada di file, **disarankan rotate/regenerate key** di dashboard OpenAI sebelum repo dipublikasikan.
- **Mode PROXY (untuk build publik):** jika `PROXY_URL` terisi (via `game/.env` atau konstanta `DEFAULT_PROXY_URL` di `definitions.rpy`), `get_ai_feedback()` mengirim request ke Cloudflare Worker (folder `proxy/`) **tanpa** header `Authorization` — key tersimpan sebagai secret di server. Jika `PROXY_URL` kosong, jalur lama (direct + key) tetap dipakai. Kalau mengubah format request/response API, **worker harus tetap transparan** (meneruskan body & respons apa adanya) — parser game (`choices[0].message.content` + `usage`) mengandalkan format OpenAI asli. Whitelist model & cap `max_tokens` di `worker.js` juga harus disesuaikan kalau ganti model / menaikkan `token_limit`.

## 4. Sistem Soal & Skoring MBTI

- `questions_data.rpy` dan `questions_logic_generated.rpy` adalah **file hasil generate** — jangan edit manual isi soalnya satu-satu; polanya kaku: `show_question_<id>_<lang>` → menu → set `IE/SN/TF/JP` ±5 → set `user_choice_text`, `last_answer`, append `user_journey_summary` → `call ai_react_logic`.
- Konvensi skor: `IE >= 0` = **E**, `SN >= 0` = **N**, `TF >= 0` = **F**, `JP >= 0` = **P** (lihat `scene_hasil_tes`). Nilai negatif = huruf satunya. Jangan ubah tanda ± di soal tanpa memahami ini.
- Pengacakan paket memakai `persistent.used_packet_titles` + `persistent.last_packet_title` (anti-ulang). Judul di `all_packet_titles` **harus** urut sama dengan `all_packets`.
- Nama label soal bergantung `persistent.cur_lang` (`id`/`en`). Menambah bahasa baru = harus generate ulang semua label soal.

## 5. Persistent & Save Data

- Achievement/award tersimpan di `persistent.unlocked_mbti` dan `persistent.unlocked_awards` — ID award (`"dog"`, `"cat"`, `"civet"`, `"rabbit"`, `"fox"`, `"chat"`, `"music"`, `"speed"`, `"all_mbti"`) dipakai lintas file (unlock di `script.rpy`, ditampilkan di `custom_screens.rpy`, syarat lagu di `music_tracks`). Ganti ID = achievement lama pemain hilang.
- Memori AI per pemain disimpan sebagai JSON di `renpy.config.savedir` dengan nama `<nama>_<companion>.json`. Struktur: `player_name`, `companion_id`, `last_mbti`, `known_facts`, `chat_history`. `get_all_profiles_data()` memindai folder save berdasarkan struktur ini.
- `config.save_directory = "MBTIGame-1763449699"` — jangan diubah, atau semua save/persistent pemain lama "hilang".

## 6. Logging Penelitian (CSV)

- `logger.rpy` menulis 3 CSV ke `renpy.config.gamedir`: `PA_Log_API_Chat.csv` (per API call), `PA_Log_MBTI_Akhir.csv` (hasil akhir), `PA_Rekap_10_Permainan.csv` (rekap token per sesi).
- File-file CSV ini berisi **data pemain (chat & nama)** → di-ignore dari git. Jangan commit data partisipan.
- `log_api_chat` dipanggil otomatis di dalam `get_ai_feedback` — kalau mengubah signature fungsi, update pemanggilnya.

## 7. Karakter & Aset Gambar

- 5 companion: `openness`=Kitsuko (rubah), `conscientiousness`=Onyen (kucing), `extraversion`=Iwank (anjing), `agreeableness`=Susagi (kelinci), `neuroticism`=Jakouko (musang/luwak). Key personality (huruf kecil) dipakai sebagai: key system prompt, bagian nama image, nama folder (`folder_map`), prefix file (`prefix_map`), dan nama BGM. Konsisten di semua tempat.
- Image companion di-generate otomatis di `definitions.rpy` dengan pola `companion <personality> <emosi>` dari file `images/<Folder>/<Prefix> <suffix>.png`. Ada anti-crash: kalau file `_blink` tidak ada, pakai gambar statis. Kalau file utama tidak ada → **crash saat show**. Cek kelengkapan file sebelum menambah emosi/karakter.
- Gambar hasil: `achieve_<mbti kecil>` (contoh `achieve_infp`) + fallback `achieve_locked`.

## 8. UI / Screens

- `custom_screens.rpy` berisi screen inti: `companion_selection_screen`, `mbti_result_diagram`, `ai_loading`, `progress_indicator`, `profile_manager_screen`, `achievements_screen`, `music_room_screen`, `free_chat_hub`, dst. `screens.rpy` = screen bawaan Ren'Py yang sudah dimodifikasi (quick menu sudah dipindah posisinya berdasarkan feedback user test).
- Mode chat memakai flag `is_chat_input` untuk memindahkan posisi input — selalu set `True` sebelum `renpy.input` dan `False` sesudahnya.
- `quick_menu` sengaja dimatikan (`$ quick_menu = False`) di menu awal & hasil tes, dinyalakan saat sesi soal. Jaga pasangannya (`show/hide screen quick_menu`).

## 9. Prompt Engineering (masukan Expert — lihat `catatan update ke game MBTI.md`)

- Framing hasil tes: jangan pakai "hanya untuk senang-senang", "tidak ilmiah", "tidak akurat" (tanpa kualifikasi), "tidak mendefinisikan". Gunakan framing "cerminan awal / bahan refleksi / tidak akurat 100%".
- Output companion memakai kata "kamu", bukan "pemain".
- Batas panjang respons dijaga lewat prompt (`Max 270/400/540 karakter`) **dan** `token_limit` per konteks: reaksi soal 300, tutorial 500, chat 800–1000, evaluasi 1500, penjelasan psikolog 2000. Menaikkan limit = biaya token naik & teks bisa kepanjangan di textbox.
- Mode `"psychologist"` adalah jalur khusus di `get_system_prompt()` **tanpa** tag emosi — dipakai untuk penjelasan detail MBTI. Jangan kirim output ini ke parser emosi.

## 10. Build / Distribusi

- `options.rpy` meng-exclude banyak package python besar (tensorflow, torch, dsb) dari build — menghemat ~3GB. Jangan dihapus.
- `android.json`: permission `INTERNET` wajib ada (API call). `android.keystore` & `bundle.keystore` = kunci signing, **jangan pernah di-commit**.
- Sebelum build: pastikan `game/.env` terisi di mesin build, atau distribusikan tanpa key (pemain isi sendiri).
