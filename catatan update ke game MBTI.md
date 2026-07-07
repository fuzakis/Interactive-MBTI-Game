# Catatan Update Game MBTI
## Berdasarkan Masukan Expert Evaluator

**Expert:** Okkie Puspitorini & Lutfifanti Purwaningtyas Wulan Sufandy
**Institusi:** SATGAS PPKS PENS (Satuan Tugas Pencegahan dan Penanganan Kekerasan Seksual), Politeknik Elektronika Negeri Surabaya
**Metode Evaluasi:** Nielsen Success Rate Assessment
**Tanggal Evaluasi:** Juni 2026 (bersamaan dengan sesi UAT Sidang 4)

---

> **PENTING:** Semua update di bawah berasal dari masukan prompt engineering yang tertanam di AI companion.
> Jangan ubah file game sebelum data demo/testing dikumpulkan (kondisi game harus sama dengan saat pengujian ke user dan expert).
> File ini adalah catatan untuk implementasi SETELAH sidang selesai.

---

## Daftar Update yang Perlu Dilakukan

### 1. Ganti Framing "Hanya untuk Senang-Senang"

**Lokasi di game:** System prompt companion / narasi pembuka sebelum tes dimulai
**Masalah:** Kalimat yang mengimplikasikan tujuan hanya hiburan semata, seolah tidak ada output bermakna dari tes ini.
**Alasan:** Meskipun belum tervalidasi oleh psikolog profesional, hasil output tes tetap dapat menjadi bahan pertimbangan awal bagi pemain mengenai kepribadian mereka. Framing yang salah bisa mengurangi trust pemain terhadap hasil tes.
**Solusi:** Ganti dengan kalimat yang menyatakan bahwa hasil tes dapat menjadi cerminan dan pertimbangan awal tentang kepribadian pemain.

Contoh kalimat lama (ganti):
> "Santai saja, ini hanya untuk senang-senang..."

Contoh kalimat baru:
> "Hasil dari perjalanan ini dapat menjadi cerminan awal tentang kepribadianmu. Gunakan sebagai bahan refleksi, ya!"

---

### 2. Hapus / Ganti Kata "Ilmiah" / "Tidak Ilmiah"

**Lokasi di game:** System prompt companion / disclaimer output hasil tes
**Masalah:** Penggunaan frasa "tidak ilmiah" atau sejenisnya menyesatkan, karena sistem ini dibangun di atas fondasi riset yang valid (Big Five Personality Traits, MBTI, Ekman's Emotion Model, MIRT-informed SJT).
**Alasan:** Meskipun ada aspek yang perlu diverifikasi ahli (seperti akurasi individual MBTI), sistem secara keseluruhan memiliki dasar ilmiah. Menggunakan kata "tidak ilmiah" bisa merusak kredibilitas riset.
**Solusi:** Ganti dengan kalimat yang lebih tepat — akui bahwa hasil perlu verifikasi ahli, tapi jangan sebut "tidak ilmiah".

Contoh kalimat lama (ganti):
> "Ini bukan tes ilmiah..."
> "Hasil ini tidak bersifat ilmiah..."

Contoh kalimat baru:
> "Hasil ini didasarkan pada kerangka psikologi yang valid, namun untuk interpretasi mendalam, konsultasi dengan profesional tetap disarankan."

---

### 3. Ganti "Tidak Akurat" menjadi "Tidak Akurat 100%"

**Lokasi di game:** System prompt companion / bagian disclaimer hasil MBTI
**Masalah:** Menyebut hasil tes sebagai "tidak akurat" secara general adalah pernyataan yang terlalu kuat dan tidak adil terhadap sistem.
**Alasan:** Tidak ada tes kepribadian yang 100% akurat (termasuk versi profesional). Hasil ini tetap berasal dari kalkulasi dan referensi yang valid. Yang tepat adalah mengakui keterbatasan tanpa mendiskreditkan seluruh hasil.
**Solusi:** Gunakan frasa "tidak akurat 100%" atau "memiliki keterbatasan akurasi" untuk memberikan nuansa yang lebih berimbang.

Contoh kalimat lama (ganti):
> "Hasil ini mungkin tidak akurat..."

Contoh kalimat baru:
> "Hasil ini mungkin tidak akurat 100%, karena setiap individu memiliki kompleksitas yang unik..."

---

### 4. Ganti "Tidak Mendefinisikan" menjadi "Mempertimbangkan"

**Lokasi di game:** System prompt companion / konteks output hasil kepribadian
**Masalah:** Frasa "tidak mendefinisikan kepribadianmu" terkesan menolak seluruh nilai output, padahal output tetap memiliki bobot pertimbangan ilmiah.
**Alasan:** Hasil dari sistem ini adalah hasil kalkulasi berdasarkan kerangka psikologi yang valid. Framing yang tepat adalah menempatkannya sebagai "pertimbangan" atau "bahan refleksi", bukan menafikannya.
**Solusi:** Ganti "tidak mendefinisikan" dengan "mempertimbangkan" atau "menjadi cerminan awal dari".

Contoh kalimat lama (ganti):
> "Ini tidak mendefinisikan siapa kamu sebenarnya..."

Contoh kalimat baru:
> "Ini adalah pertimbangan awal tentang kepribadianmu. Setiap orang selalu berkembang dan berubah."

---

### 5. Hapus / Ganti "Bersantai Saja" dan "Jangan Terlalu Serius"

**Lokasi di game:** System prompt companion / narasi pembuka atau transisi
**Masalah:** Kalimat ini membuat seolah-olah tes tidak menghasilkan output yang berarti — padahal di akhir game pemain mendapat saran dan edukasi berbasis kepribadian yang diperoleh.
**Alasan:** Game ini memberikan output nyata (hasil MBTI, insight kepribadian, saran dari companion AI). Mengajak pemain untuk "tidak serius" kontradiktif dengan tujuan edukatif ini.
**Solusi:** Ganti dengan kalimat yang mengajak pemain untuk terbuka dan jujur dalam menjawab, sambil meyakinkan bahwa prosesnya menyenangkan — tanpa mengurangi nilai outputnya.

Contoh kalimat lama (ganti):
> "Bersantai saja, jangan terlalu serius..."
> "Santai, ini hanya permainan..."

Contoh kalimat baru:
> "Jawab sejujur mungkin — tidak ada jawaban benar atau salah. Perjalanan ini adalah tentang mengenal dirimu sendiri."

---

### 6. Ganti "Pemain" dengan "Kamu" di Bagian Summary/Output

**Lokasi di game:** System prompt companion — khususnya bagian output hasil MBTI dan summary akhir yang dibacakan oleh companion
**Masalah:** Penggunaan kata "pemain" (third-person) dalam output companion mengurangi efek immersive dan kedekatan dengan karakter companion.
**Alasan:** Salah satu kekuatan utama sistem ini adalah hubungan emosional antara pemain dan companion AI. Menggunakan kata ganti orang pertama/kedua ("kamu") akan memperkuat koneksi ini secara signifikan.
**Solusi:** Dalam semua output summary dan feedback hasil, ganti "pemain" dengan "kamu" atau kata ganti orang kedua yang sesuai.

Contoh kalimat lama (ganti):
> "Pemain memiliki kecenderungan kepada tipe..."
> "Berdasarkan jawaban pemain..."

Contoh kalimat baru:
> "Kamu memiliki kecenderungan kepada tipe..."
> "Berdasarkan jawabanmu..."

**Note teknis:** Cari di semua file `.rpy` yang mengandung kata `pemain` dalam konteks output companion (bukan konteks kode/variabel).

---

### 7. Perbaiki Font untuk Teks Paragraf Panjang

**Lokasi di game:** `gui.rpy` — definisi font dialog, atau style yang digunakan untuk teks panjang
**Font saat ini:** `DePixelKlein.ttf` / `Pixeled.ttf` (pixel art font)
**Masalah:** Font pixel art cocok untuk estetika visual novel dan feel game, tapi sulit dibaca saat digunakan untuk paragraf teks yang panjang (hasil summary, dialog panjang companion, narasi).
**Masukan expert:** "Jenis font kurang mudah terbaca" — konsisten juga dengan temuan user testing.
**Sumber font saat ini:** `game/fonts/` — tersedia beberapa varian DePixel.

**Solusi yang disarankan:**
- Pertahankan font pixel art untuk elemen UI (nama karakter, pilihan dialog singkat, tombol)
- Ganti font untuk **teks dialog panjang** dan **output summary hasil MBTI** ke font yang lebih readable
- Alternatif font yang bisa dipertimbangkan: font serif/sans-serif yang tetap punya karakter (misalnya: Josefin Sans, Nunito, atau font yang sedikit dekoratif tapi tetap readable)
- Pastikan ukuran font cukup (minimal 18-20px untuk dialog)

**File yang perlu diubah:**
- `game/gui.rpy` — cari variabel `gui.text_font`, `gui.interface_text_font`, atau definisi `style say_dialogue`

---

## Catatan Tambahan

- **Font (poin 7)** juga dikonfirmasi oleh feedback user testing (UAT) — ini adalah temuan yang konsisten dari dua sumber berbeda.
- **Poin 1-6** semuanya adalah perubahan pada **system prompt AI companion** — tidak ada perubahan pada logika game, scoring MBTI, atau mekanik inti.
- Semua perubahan ini bersifat **low-risk** dan tidak mempengaruhi alur utama game.
- Prioritas implementasi yang disarankan: **6 → 1 → 3 → 4 → 5 → 2 → 7** (dari dampak immersive tertinggi ke refactor paling besar).
