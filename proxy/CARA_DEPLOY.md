# Cara Deploy Proxy API (Cloudflare Worker)

Panduan ini membuat "jembatan" gratis antara game dan OpenAI, supaya API key
tersimpan aman di server Cloudflare — **tidak pernah ikut di dalam build game**.
Tidak perlu install apa pun; semua lewat browser. (English summary at the bottom.)

## Langkah 1 — Daftar Cloudflare (gratis, tanpa kartu kredit)

1. Buka https://dash.cloudflare.com/sign-up dan buat akun.
2. Setelah login, di menu kiri pilih **Compute (Workers)** → **Workers & Pages**.

## Langkah 2 — Buat Worker

1. Klik **Create** → **Create Worker** (pilih template "Hello World" / Start from scratch).
2. Beri nama, misal `mbti-proxy` → **Deploy**. Kamu akan dapat URL seperti:
   `https://mbti-proxy.<akunmu>.workers.dev`
3. Klik **Edit code**, hapus semua isi editor, lalu **copy-paste seluruh isi
   file [`worker.js`](worker.js)** di folder ini → klik **Deploy**.

## Langkah 3 — Simpan API Key sebagai Secret

1. Kembali ke halaman worker → tab **Settings** → **Variables and Secrets**.
2. Klik **Add** :
   - Type: **Secret**
   - Variable name: `OPENAI_API_KEY`
   - Value: API key OpenAI kamu (`sk-proj-...`)
3. (Opsional tapi disarankan) Tambah satu lagi:
   - Type: **Secret**
   - Variable name: `APP_TOKEN`
   - Value: teks acak buatanmu sendiri, misal `mbti-game-x7k2p` — ini jadi
     "kata sandi" sederhana agar orang iseng tidak bisa memakai proxy-mu.
4. Klik **Deploy** lagi agar secret aktif.

## Langkah 4 — Arahkan Game ke Proxy

Isi `game/.env` (untuk development) dengan:

```
PROXY_URL=https://mbti-proxy.<akunmu>.workers.dev
PROXY_APP_TOKEN=mbti-game-x7k2p
```

- Kalau `PROXY_URL` ada → game memakai proxy, **API key tidak dibutuhkan sama sekali**.
- Kalau `PROXY_URL` kosong → game memakai `OPENAI_API_KEY` langsung (mode lama, tetap jalan).

**Untuk build publik** (karena `game/.env` di-exclude dari build): isi konstanta
`DEFAULT_PROXY_URL` (dan `DEFAULT_PROXY_APP_TOKEN` jika pakai) di bagian atas
`init python` pada `game/definitions.rpy`, lalu build seperti biasa. URL proxy
bukan rahasia, jadi aman ikut ter-build & ter-commit.

## Langkah 5 — Pasang Rem Darurat (WAJIB)

Proxy menyembunyikan key, tapi pemakaian token tetap dari akun OpenAI-mu:

1. Buka https://platform.openai.com/settings/organization/limits
2. Set **Monthly budget** (misal $10) — kalau tembus, API berhenti otomatis.
3. Set **Email alert** di angka lebih kecil (misal $5) sebagai peringatan dini.

## Uji Coba

Jalankan game → pilih companion → kalau tutorial AI muncul, proxy bekerja.
Cek juga dashboard Cloudflare (tab **Metrics** pada worker) untuk melihat
jumlah request masuk.

Kalau AI tidak merespons, urutan pengecekan:
1. `log.txt` di folder game — cari `[DEBUG: AI ERROR]`.
2. HTTP 401 → `PROXY_APP_TOKEN` di game tidak sama dengan `APP_TOKEN` di Cloudflare.
3. HTTP 400 → model/body tidak lolos validasi worker (cek whitelist model di `worker.js`).
4. Dashboard Cloudflare → worker → **Logs** (Live) untuk melihat error dari sisi server.

## Batas Gratis

- 100.000 request/hari (1 sesi main penuh ≈ 25–30 request → ±3.000 sesi/hari).
- Jika lewat, request ditolak sampai hari berikutnya (tidak ada tagihan mendadak).

---

## English Summary

Deploy `worker.js` as a Cloudflare Worker (free tier, no credit card):
**Workers & Pages → Create Worker → Edit code → paste `worker.js` → Deploy.**
Add secrets in *Settings → Variables and Secrets*: `OPENAI_API_KEY` (required)
and `APP_TOKEN` (optional shared token). Then point the game to it via
`game/.env` (`PROXY_URL=...`, `PROXY_APP_TOKEN=...`) for development, or the
`DEFAULT_PROXY_URL` constant in `game/definitions.rpy` for public builds.
Finally, set a monthly budget limit in your OpenAI dashboard as a hard stop.
