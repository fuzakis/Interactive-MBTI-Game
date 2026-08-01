
# ================= BAHASA: ID =================

label show_question_q_a_01_id:
    scene bg taman with dissolve
    $ narasi_asli = "(Krucuk...) Aduh, lelah sekali setelah jalan-jalan hari ini! Energimu habis dan perutmu lapar. Apa yang tubuhmu butuhkan?"
    n "(Krucuk...) Aduh, lelah sekali setelah jalan-jalan hari ini!"
    n "Energimu habis dan perutmu lapar."
    n "Apa yang tubuhmu butuhkan?"

    menu:
        "(Krucuk...) Aduh, lelah sekali setelah jalan-jalan hari ini! Energimu habis dan perutmu lapar. Apa yang tubuhmu butuhkan?"

        "Pulang ke rumah sendiri (I) dan makan makanan bergizi untuk memulihkan fisik (S).":
            $ IE -= 5
            $ SN -= 5
            $ user_choice_text = "Pulang ke rumah sendiri (I) dan makan makanan bergizi untuk memulihkan fisik (S)."
            $ last_answer = "Introvert & Sensing"
            $ unchosen_choice_text = "Kumpul bareng teman dan bercerita (E) tentang ide perjalanan selanjutnya (N)."
            $ unchosen_answer = "Extrovert & Intuitive"
            jump show_question_q_a_01_id_A

        "Kumpul bareng teman dan bercerita (E) tentang ide perjalanan selanjutnya (N).":
            $ IE += 5
            $ SN += 5
            $ user_choice_text = "Kumpul bareng teman dan bercerita (E) tentang ide perjalanan selanjutnya (N)."
            $ last_answer = "Extrovert & Intuitive"
            $ unchosen_choice_text = "Pulang ke rumah sendiri (I) dan makan makanan bergizi untuk memulihkan fisik (S)."
            $ unchosen_answer = "Introvert & Sensing"
            jump show_question_q_a_01_id_B


label show_question_q_a_01_id_A:
    $ user_journey_summary.append("Di situasi (Krucuk...) Aduh, lelah sekali setelah jalan-jalan hari ini! Energimu habis dan perutmu lapar. Apa yang tubuhmu butuhkan?, user memilih: Pulang ke rumah sendiri (I) dan makan makanan bergizi untuk memulihkan fisik (S)., dengan poin MBTI: Introvert & Sensing")
    call ai_react_logic
    return

label show_question_q_a_01_id_B:
    $ user_journey_summary.append("Di situasi (Krucuk...) Aduh, lelah sekali setelah jalan-jalan hari ini! Energimu habis dan perutmu lapar. Apa yang tubuhmu butuhkan?, user memilih: Kumpul bareng teman dan bercerita (E) tentang ide perjalanan selanjutnya (N)., dengan poin MBTI: Extrovert & Intuitive")
    call ai_react_logic
    return

label show_question_q_a_02_id:
    scene bg kafe with dissolve
    $ narasi_asli = "(Kring!) Pintu kafe terbuka! Ada sosok misterius yang gayanya keren sekali masuk. Apa yang pertama kali menarik perhatianmu?"
    n "(Kring!) Pintu kafe terbuka!"
    n "Ada sosok misterius yang gayanya keren sekali masuk."
    n "Apa yang pertama kali menarik perhatianmu?"

    menu:
        "(Kring!) Pintu kafe terbuka! Ada sosok misterius yang gayanya keren sekali masuk. Apa yang pertama kali menarik perhatianmu?"

        "Perhatikan dia dari kursimu (I), sambil mengamati pergerakannya (S).":
            $ IE -= 5
            $ SN -= 5
            $ user_choice_text = "Perhatikan dia dari kursimu (I), sambil mengamati pergerakannya (S)."
            $ last_answer = "Introvert & Sensing"
            $ unchosen_choice_text = "Langsung sapa (E), dan tanya dia hendak pergi kemana dengan pakaian seperti itu (N)."
            $ unchosen_answer = "Extrovert & Intuitive"
            jump show_question_q_a_02_id_A

        "Langsung sapa (E), dan tanya dia hendak pergi kemana dengan pakaian seperti itu (N).":
            $ IE += 5
            $ SN += 5
            $ user_choice_text = "Langsung sapa (E), dan tanya dia hendak pergi kemana dengan pakaian seperti itu (N)."
            $ last_answer = "Extrovert & Intuitive"
            $ unchosen_choice_text = "Perhatikan dia dari kursimu (I), sambil mengamati pergerakannya (S)."
            $ unchosen_answer = "Introvert & Sensing"
            jump show_question_q_a_02_id_B


label show_question_q_a_02_id_A:
    $ user_journey_summary.append("Di situasi (Kring!) Pintu kafe terbuka! Ada sosok misterius yang gayanya keren sekali masuk. Apa yang pertama kali menarik perhatianmu?, user memilih: Perhatikan dia dari kursimu (I), sambil mengamati pergerakannya (S)., dengan poin MBTI: Introvert & Sensing")
    call ai_react_logic
    return

label show_question_q_a_02_id_B:
    $ user_journey_summary.append("Di situasi (Kring!) Pintu kafe terbuka! Ada sosok misterius yang gayanya keren sekali masuk. Apa yang pertama kali menarik perhatianmu?, user memilih: Langsung sapa (E), dan tanya dia hendak pergi kemana dengan pakaian seperti itu (N)., dengan poin MBTI: Extrovert & Intuitive")
    call ai_react_logic
    return

label show_question_q_a_03_id:
    scene bg kantor with dissolve
    $ narasi_asli = "(Gubrak!) Bos memberi tumpukan job setinggi gunung! Mustahil selesai sendirian hari ini."
    n "(Gubrak!) Bos memberi tumpukan job setinggi gunung!"
    n "Mustahil selesai sendirian hari ini."

    menu:
        "(Gubrak!) Bos memberi tumpukan job setinggi gunung! Mustahil selesai sendirian hari ini."

        "Panggil seluruh tim (E) untuk bagi tugas fisik (S) sekarang juga.":
            $ IE += 5
            $ SN -= 5
            $ user_choice_text = "Panggil seluruh tim (E) untuk bagi tugas fisik (S) sekarang juga."
            $ last_answer = "Extrovert & Sensing"
            $ unchosen_choice_text = "Panggil rekan kerja dekat (I) untuk coba program bantuan yang baru kamu kembangkan (N)"
            $ unchosen_answer = "Introvert & Intuitive"
            jump show_question_q_a_03_id_A

        "Panggil rekan kerja dekat (I) untuk coba program bantuan yang baru kamu kembangkan (N)":
            $ IE -= 5
            $ SN += 5
            $ user_choice_text = "Panggil rekan kerja dekat (I) untuk coba program bantuan yang baru kamu kembangkan (N)"
            $ last_answer = "Introvert & Intuitive"
            $ unchosen_choice_text = "Panggil seluruh tim (E) untuk bagi tugas fisik (S) sekarang juga."
            $ unchosen_answer = "Extrovert & Sensing"
            jump show_question_q_a_03_id_B


label show_question_q_a_03_id_A:
    $ user_journey_summary.append("Di situasi (Gubrak!) Bos memberi tumpukan job setinggi gunung! Mustahil selesai sendirian hari ini., user memilih: Panggil seluruh tim (E) untuk bagi tugas fisik (S) sekarang juga., dengan poin MBTI: Extrovert & Sensing")
    call ai_react_logic
    return

label show_question_q_a_03_id_B:
    $ user_journey_summary.append("Di situasi (Gubrak!) Bos memberi tumpukan job setinggi gunung! Mustahil selesai sendirian hari ini., user memilih: Panggil rekan kerja dekat (I) untuk coba program bantuan yang baru kamu kembangkan (N), dengan poin MBTI: Introvert & Intuitive")
    call ai_react_logic
    return

label show_question_q_a_04_id:
    scene bg dapur with dissolve
    $ narasi_asli = "(Waduh!) Kamu mau masak makanan spesial, tapi satu bahan utamanya habis, kamu lupa membelinya kemarin."
    n "(Waduh!) Kamu mau masak makanan spesial, tapi satu bahan utamanya habis, kamu lupa membelinya kemarin."

    menu:
        "(Waduh!) Kamu mau masak makanan spesial, tapi satu bahan utamanya habis, kamu lupa membelinya kemarin."

        "Hubungi dan tanya teman (E) untuk meminta bahan mentah yang kurang (S).":
            $ IE += 5
            $ SN -= 5
            $ user_choice_text = "Hubungi dan tanya teman (E) untuk meminta bahan mentah yang kurang (S)."
            $ last_answer = "Extrovert & Sensing"
            $ unchosen_choice_text = "Tetap di dapur (I) dan coba eksperimen (N) menggantinya dengan bahan lain."
            $ unchosen_answer = "Introvert & Intuitive"
            jump show_question_q_a_04_id_A

        "Tetap di dapur (I) dan coba eksperimen (N) menggantinya dengan bahan lain.":
            $ IE -= 5
            $ SN += 5
            $ user_choice_text = "Tetap di dapur (I) dan coba eksperimen (N) menggantinya dengan bahan lain."
            $ last_answer = "Introvert & Intuitive"
            $ unchosen_choice_text = "Hubungi dan tanya teman (E) untuk meminta bahan mentah yang kurang (S)."
            $ unchosen_answer = "Extrovert & Sensing"
            jump show_question_q_a_04_id_B


label show_question_q_a_04_id_A:
    $ user_journey_summary.append("Di situasi (Waduh!) Kamu mau masak makanan spesial, tapi satu bahan utamanya habis, kamu lupa membelinya kemarin., user memilih: Hubungi dan tanya teman (E) untuk meminta bahan mentah yang kurang (S)., dengan poin MBTI: Extrovert & Sensing")
    call ai_react_logic
    return

label show_question_q_a_04_id_B:
    $ user_journey_summary.append("Di situasi (Waduh!) Kamu mau masak makanan spesial, tapi satu bahan utamanya habis, kamu lupa membelinya kemarin., user memilih: Tetap di dapur (I) dan coba eksperimen (N) menggantinya dengan bahan lain., dengan poin MBTI: Introvert & Intuitive")
    call ai_react_logic
    return

label show_question_q_a_05_id:
    scene bg room with dissolve
    $ narasi_asli = "Ada poster 'Berita Hangat!' yang bikin heboh satu desa! Semua orang membicarakannya."
    n "Ada poster 'Berita Hangat!' yang bikin heboh satu desa!"
    n "Semua orang membicarakannya."

    menu:
        "Ada poster 'Berita Hangat!' yang bikin heboh satu desa! Semua orang membicarakannya."

        "Ikut komentar dengan warga lainnya (E) dan cari bukti (S) kejadiannya.":
            $ IE += 5
            $ SN -= 5
            $ user_choice_text = "Ikut komentar dengan warga lainnya (E) dan cari bukti (S) kejadiannya."
            $ last_answer = "Extrovert & Sensing"
            $ unchosen_choice_text = "Baca dan amati (I), coba bayangkan apa yang sebenarnya terjadi (N)."
            $ unchosen_answer = "Introvert & Intuitive"
            jump show_question_q_a_05_id_A

        "Baca dan amati (I), coba bayangkan apa yang sebenarnya terjadi (N).":
            $ IE -= 5
            $ SN += 5
            $ user_choice_text = "Baca dan amati (I), coba bayangkan apa yang sebenarnya terjadi (N)."
            $ last_answer = "Introvert & Intuitive"
            $ unchosen_choice_text = "Ikut komentar dengan warga lainnya (E) dan cari bukti (S) kejadiannya."
            $ unchosen_answer = "Extrovert & Sensing"
            jump show_question_q_a_05_id_B


label show_question_q_a_05_id_A:
    $ user_journey_summary.append("Di situasi Ada poster 'Berita Hangat!' yang bikin heboh satu desa! Semua orang membicarakannya., user memilih: Ikut komentar dengan warga lainnya (E) dan cari bukti (S) kejadiannya., dengan poin MBTI: Extrovert & Sensing")
    call ai_react_logic
    return

label show_question_q_a_05_id_B:
    $ user_journey_summary.append("Di situasi Ada poster 'Berita Hangat!' yang bikin heboh satu desa! Semua orang membicarakannya., user memilih: Baca dan amati (I), coba bayangkan apa yang sebenarnya terjadi (N)., dengan poin MBTI: Introvert & Intuitive")
    call ai_react_logic
    return

label show_question_q_a_06_id:
    scene bg kantor with dissolve
    $ narasi_asli = "Teman satu timmu tak sengaja menghilangkan barang penting perusahaan. Dia panik."
    n "Teman satu timmu tak sengaja menghilangkan barang penting perusahaan."
    n "Dia panik."

    menu:
        "Teman satu timmu tak sengaja menghilangkan barang penting perusahaan. Dia panik."

        "Ajak bicara di depan tim (E) untuk susun langkah perbaikan yang jelas (T).":
            $ IE += 5
            $ TF -= 5
            $ user_choice_text = "Ajak bicara di depan tim (E) untuk susun langkah perbaikan yang jelas (T)."
            $ last_answer = "Extrovert & Thinking"
            $ unchosen_choice_text = "Tarik dia menepi berdua (I) dan tenangkan dulu perasaannya (F)."
            $ unchosen_answer = "Introvert & Feeling"
            jump show_question_q_a_06_id_A

        "Tarik dia menepi berdua (I) dan tenangkan dulu perasaannya (F).":
            $ IE -= 5
            $ TF += 5
            $ user_choice_text = "Tarik dia menepi berdua (I) dan tenangkan dulu perasaannya (F)."
            $ last_answer = "Introvert & Feeling"
            $ unchosen_choice_text = "Ajak bicara di depan tim (E) untuk susun langkah perbaikan yang jelas (T)."
            $ unchosen_answer = "Extrovert & Thinking"
            jump show_question_q_a_06_id_B


label show_question_q_a_06_id_A:
    $ user_journey_summary.append("Di situasi Teman satu timmu tak sengaja menghilangkan barang penting perusahaan. Dia panik., user memilih: Ajak bicara di depan tim (E) untuk susun langkah perbaikan yang jelas (T)., dengan poin MBTI: Extrovert & Thinking")
    call ai_react_logic
    return

label show_question_q_a_06_id_B:
    $ user_journey_summary.append("Di situasi Teman satu timmu tak sengaja menghilangkan barang penting perusahaan. Dia panik., user memilih: Tarik dia menepi berdua (I) dan tenangkan dulu perasaannya (F)., dengan poin MBTI: Introvert & Feeling")
    call ai_react_logic
    return

label show_question_q_a_07_id:
    scene bg taman with dissolve
    $ narasi_asli = "Ada peraturan baru di taman: 'Dilarang Tertawa Keras'."
    n "Ada peraturan baru di taman: 'Dilarang Tertawa Keras'."

    menu:
        "Ada peraturan baru di taman: 'Dilarang Tertawa Keras'."

        "Protes ke petugas (E) karena aturannya tidak masuk akal (T).":
            $ IE += 5
            $ TF -= 5
            $ user_choice_text = "Protes ke petugas (E) karena aturannya tidak masuk akal (T)."
            $ last_answer = "Extrovert & Thinking"
            $ unchosen_choice_text = "Diam saja (I), karena mungkin benar, hal tersebut bisa merusak suasana yang damai (F)."
            $ unchosen_answer = "Introvert & Feeling"
            jump show_question_q_a_07_id_A

        "Diam saja (I), karena mungkin benar, hal tersebut bisa merusak suasana yang damai (F).":
            $ IE -= 5
            $ TF += 5
            $ user_choice_text = "Diam saja (I), karena mungkin benar, hal tersebut bisa merusak suasana yang damai (F)."
            $ last_answer = "Introvert & Feeling"
            $ unchosen_choice_text = "Protes ke petugas (E) karena aturannya tidak masuk akal (T)."
            $ unchosen_answer = "Extrovert & Thinking"
            jump show_question_q_a_07_id_B


label show_question_q_a_07_id_A:
    $ user_journey_summary.append("Di situasi Ada peraturan baru di taman: 'Dilarang Tertawa Keras'., user memilih: Protes ke petugas (E) karena aturannya tidak masuk akal (T)., dengan poin MBTI: Extrovert & Thinking")
    call ai_react_logic
    return

label show_question_q_a_07_id_B:
    $ user_journey_summary.append("Di situasi Ada peraturan baru di taman: 'Dilarang Tertawa Keras'., user memilih: Diam saja (I), karena mungkin benar, hal tersebut bisa merusak suasana yang damai (F)., dengan poin MBTI: Introvert & Feeling")
    call ai_react_logic
    return

label show_question_q_a_08_id:
    scene bg kafe with dissolve
    $ narasi_asli = "Pengunjung di meja sebelah terlihat sangat galau dan menghela napas panjang..."
    n "Pengunjung di meja sebelah terlihat sangat galau dan menghela napas panjang..."

    menu:
        "Pengunjung di meja sebelah terlihat sangat galau dan menghela napas panjang..."

        "Coba dekati dan tanya langsung (E), analisis masalahnya (T) agar ditemukan jalan keluarnya.":
            $ IE += 5
            $ TF -= 5
            $ user_choice_text = "Coba dekati dan tanya langsung (E), analisis masalahnya (T) agar ditemukan jalan keluarnya."
            $ last_answer = "Extrovert & Thinking"
            $ unchosen_choice_text = "Kasih tisu diam-diam (I) karena kasihan melihatnya (F)."
            $ unchosen_answer = "Introvert & Feeling"
            jump show_question_q_a_08_id_A

        "Kasih tisu diam-diam (I) karena kasihan melihatnya (F).":
            $ IE -= 5
            $ TF += 5
            $ user_choice_text = "Kasih tisu diam-diam (I) karena kasihan melihatnya (F)."
            $ last_answer = "Introvert & Feeling"
            $ unchosen_choice_text = "Coba dekati dan tanya langsung (E), analisis masalahnya (T) agar ditemukan jalan keluarnya."
            $ unchosen_answer = "Extrovert & Thinking"
            jump show_question_q_a_08_id_B


label show_question_q_a_08_id_A:
    $ user_journey_summary.append("Di situasi Pengunjung di meja sebelah terlihat sangat galau dan menghela napas panjang..., user memilih: Coba dekati dan tanya langsung (E), analisis masalahnya (T) agar ditemukan jalan keluarnya., dengan poin MBTI: Extrovert & Thinking")
    call ai_react_logic
    return

label show_question_q_a_08_id_B:
    $ user_journey_summary.append("Di situasi Pengunjung di meja sebelah terlihat sangat galau dan menghela napas panjang..., user memilih: Kasih tisu diam-diam (I) karena kasihan melihatnya (F)., dengan poin MBTI: Introvert & Feeling")
    call ai_react_logic
    return

label show_question_q_a_09_id:
    scene bg kantor with dissolve
    $ narasi_asli = "Kapten kapal membagikan harta karun, tapi bagianmu paling sedikit! Tidak adil!"
    n "Kapten kapal membagikan harta karun, tapi bagianmu paling sedikit!"
    n "Tidak adil!"

    menu:
        "Kapten kapal membagikan harta karun, tapi bagianmu paling sedikit! Tidak adil!"

        "Debat dengan Kapten (E) karena hitungannya salah (T).":
            $ IE += 5
            $ TF -= 5
            $ user_choice_text = "Debat dengan Kapten (E) karena hitungannya salah (T)."
            $ last_answer = "Extrovert & Thinking"
            $ unchosen_choice_text = "Terima saja (I) karena mungkin kapten sedang memerlukannya (F)."
            $ unchosen_answer = "Introvert & Feeling"
            jump show_question_q_a_09_id_A

        "Terima saja (I) karena mungkin kapten sedang memerlukannya (F).":
            $ IE -= 5
            $ TF += 5
            $ user_choice_text = "Terima saja (I) karena mungkin kapten sedang memerlukannya (F)."
            $ last_answer = "Introvert & Feeling"
            $ unchosen_choice_text = "Debat dengan Kapten (E) karena hitungannya salah (T)."
            $ unchosen_answer = "Extrovert & Thinking"
            jump show_question_q_a_09_id_B


label show_question_q_a_09_id_A:
    $ user_journey_summary.append("Di situasi Kapten kapal membagikan harta karun, tapi bagianmu paling sedikit! Tidak adil!, user memilih: Debat dengan Kapten (E) karena hitungannya salah (T)., dengan poin MBTI: Extrovert & Thinking")
    call ai_react_logic
    return

label show_question_q_a_09_id_B:
    $ user_journey_summary.append("Di situasi Kapten kapal membagikan harta karun, tapi bagianmu paling sedikit! Tidak adil!, user memilih: Terima saja (I) karena mungkin kapten sedang memerlukannya (F)., dengan poin MBTI: Introvert & Feeling")
    call ai_react_logic
    return

label show_question_q_a_10_id:
    scene bg abstrak with dissolve
    $ narasi_asli = "(Suara Misterius) 'Pilihlah takdirmu... Pintu Kiri atau Pintu Kanan?' Tanpa adanya petunjuk sama sekali!"
    n "(Suara Misterius) 'Pilihlah takdirmu..."
    n "Pintu Kiri atau Pintu Kanan?' Tanpa adanya petunjuk sama sekali!"

    menu:
        "(Suara Misterius) 'Pilihlah takdirmu... Pintu Kiri atau Pintu Kanan?' Tanpa adanya petunjuk sama sekali!"

        "Tanya kembali suara itu (E) 'kira-kira, mana pintu yang paling aman (T)?'":
            $ IE += 5
            $ TF -= 5
            $ user_choice_text = "Tanya kembali suara itu (E) 'kira-kira, mana pintu yang paling aman (T)?'"
            $ last_answer = "Extrovert & Thinking"
            $ unchosen_choice_text = "Pejamkan mata (I) dan ikuti kata hati (F)."
            $ unchosen_answer = "Introvert & Feeling"
            jump show_question_q_a_10_id_A

        "Pejamkan mata (I) dan ikuti kata hati (F).":
            $ IE -= 5
            $ TF += 5
            $ user_choice_text = "Pejamkan mata (I) dan ikuti kata hati (F)."
            $ last_answer = "Introvert & Feeling"
            $ unchosen_choice_text = "Tanya kembali suara itu (E) 'kira-kira, mana pintu yang paling aman (T)?'"
            $ unchosen_answer = "Extrovert & Thinking"
            jump show_question_q_a_10_id_B


label show_question_q_a_10_id_A:
    $ user_journey_summary.append("Di situasi (Suara Misterius) 'Pilihlah takdirmu... Pintu Kiri atau Pintu Kanan?' Tanpa adanya petunjuk sama sekali!, user memilih: Tanya kembali suara itu (E) 'kira-kira, mana pintu yang paling aman (T)?', dengan poin MBTI: Extrovert & Thinking")
    call ai_react_logic
    return

label show_question_q_a_10_id_B:
    $ user_journey_summary.append("Di situasi (Suara Misterius) 'Pilihlah takdirmu... Pintu Kiri atau Pintu Kanan?' Tanpa adanya petunjuk sama sekali!, user memilih: Pejamkan mata (I) dan ikuti kata hati (F)., dengan poin MBTI: Introvert & Feeling")
    call ai_react_logic
    return

label show_question_q_a_11_id:
    scene bg kafe with dissolve
    $ narasi_asli = "Tiba-tiba temanmu menarik tanganmu. 'Ayo kita jalan-jalan ke pantai SEKARANG JUGA!'"
    n "Tiba-tiba temanmu menarik tanganmu."
    n "'Ayo kita jalan-jalan ke pantai SEKARANG JUGA!'"

    menu:
        "Tiba-tiba temanmu menarik tanganmu. 'Ayo kita jalan-jalan ke pantai SEKARANG JUGA!'"

        "Gas! (E) urusan nanti dipikir belakangan (P).":
            $ IE += 5
            $ JP += 5
            $ user_choice_text = "Gas! (E) urusan nanti dipikir belakangan (P)."
            $ last_answer = "Extrovert & Perceiving"
            $ unchosen_choice_text = "Tolak (I) karena harus cek jadwal (J) dulu."
            $ unchosen_answer = "Introvert & Judging"
            jump show_question_q_a_11_id_A

        "Tolak (I) karena harus cek jadwal (J) dulu.":
            $ IE -= 5
            $ JP -= 5
            $ user_choice_text = "Tolak (I) karena harus cek jadwal (J) dulu."
            $ last_answer = "Introvert & Judging"
            $ unchosen_choice_text = "Gas! (E) urusan nanti dipikir belakangan (P)."
            $ unchosen_answer = "Extrovert & Perceiving"
            jump show_question_q_a_11_id_B


label show_question_q_a_11_id_A:
    $ user_journey_summary.append("Di situasi Tiba-tiba temanmu menarik tanganmu. 'Ayo kita jalan-jalan ke pantai SEKARANG JUGA!', user memilih: Gas! (E) urusan nanti dipikir belakangan (P)., dengan poin MBTI: Extrovert & Perceiving")
    call ai_react_logic
    return

label show_question_q_a_11_id_B:
    $ user_journey_summary.append("Di situasi Tiba-tiba temanmu menarik tanganmu. 'Ayo kita jalan-jalan ke pantai SEKARANG JUGA!', user memilih: Tolak (I) karena harus cek jadwal (J) dulu., dengan poin MBTI: Introvert & Judging")
    call ai_react_logic
    return

label show_question_q_a_12_id:
    scene bg stasiun with dissolve
    $ narasi_asli = "(Tuutt! Tuut!) Kereta terakhir sudah berangkat meninggalkanmu! Kamu ketinggalan kereta yang harusnya kamu naiki untuk pulang!"
    n "(Tuutt!"
    n "Tuut!) Kereta terakhir sudah berangkat meninggalkanmu!"
    n "Kamu ketinggalan kereta yang harusnya kamu naiki untuk pulang!"

    menu:
        "(Tuutt! Tuut!) Kereta terakhir sudah berangkat meninggalkanmu! Kamu ketinggalan kereta yang harusnya kamu naiki untuk pulang!"

        "Asik! (E) kita bisa bebas menjelajahi kota! (P).":
            $ IE += 5
            $ JP += 5
            $ user_choice_text = "Asik! (E) kita bisa bebas menjelajahi kota! (P)."
            $ last_answer = "Extrovert & Perceiving"
            $ unchosen_choice_text = "Waduh! (I) seharusnya aku datang lebih awal (J)."
            $ unchosen_answer = "Introvert & Judging"
            jump show_question_q_a_12_id_A

        "Waduh! (I) seharusnya aku datang lebih awal (J).":
            $ IE -= 5
            $ JP -= 5
            $ user_choice_text = "Waduh! (I) seharusnya aku datang lebih awal (J)."
            $ last_answer = "Introvert & Judging"
            $ unchosen_choice_text = "Asik! (E) kita bisa bebas menjelajahi kota! (P)."
            $ unchosen_answer = "Extrovert & Perceiving"
            jump show_question_q_a_12_id_B


label show_question_q_a_12_id_A:
    $ user_journey_summary.append("Di situasi (Tuutt! Tuut!) Kereta terakhir sudah berangkat meninggalkanmu! Kamu ketinggalan kereta yang harusnya kamu naiki untuk pulang!, user memilih: Asik! (E) kita bisa bebas menjelajahi kota! (P)., dengan poin MBTI: Extrovert & Perceiving")
    call ai_react_logic
    return

label show_question_q_a_12_id_B:
    $ user_journey_summary.append("Di situasi (Tuutt! Tuut!) Kereta terakhir sudah berangkat meninggalkanmu! Kamu ketinggalan kereta yang harusnya kamu naiki untuk pulang!, user memilih: Waduh! (I) seharusnya aku datang lebih awal (J)., dengan poin MBTI: Introvert & Judging")
    call ai_react_logic
    return

label show_question_q_a_13_id:
    scene bg taman with dissolve
    $ narasi_asli = "Kamu ditunjuk jadi pemimpin piknik besok. Apa rencanamu?"
    n "Kamu ditunjuk jadi pemimpin piknik besok."
    n "Apa rencanamu?"

    menu:
        "Kamu ditunjuk jadi pemimpin piknik besok. Apa rencanamu?"

        "Ajak semua teman! (E) bebas mau bawa apa saja (P).":
            $ IE += 5
            $ JP += 5
            $ user_choice_text = "Ajak semua teman! (E) bebas mau bawa apa saja (P)."
            $ last_answer = "Extrovert & Perceiving"
            $ unchosen_choice_text = "Coba pilih menu terbaik menurutmu (I) dan tentukan waktu pasti (J)."
            $ unchosen_answer = "Introvert & Judging"
            jump show_question_q_a_13_id_A

        "Coba pilih menu terbaik menurutmu (I) dan tentukan waktu pasti (J).":
            $ IE -= 5
            $ JP -= 5
            $ user_choice_text = "Coba pilih menu terbaik menurutmu (I) dan tentukan waktu pasti (J)."
            $ last_answer = "Introvert & Judging"
            $ unchosen_choice_text = "Ajak semua teman! (E) bebas mau bawa apa saja (P)."
            $ unchosen_answer = "Extrovert & Perceiving"
            jump show_question_q_a_13_id_B


label show_question_q_a_13_id_A:
    $ user_journey_summary.append("Di situasi Kamu ditunjuk jadi pemimpin piknik besok. Apa rencanamu?, user memilih: Ajak semua teman! (E) bebas mau bawa apa saja (P)., dengan poin MBTI: Extrovert & Perceiving")
    call ai_react_logic
    return

label show_question_q_a_13_id_B:
    $ user_journey_summary.append("Di situasi Kamu ditunjuk jadi pemimpin piknik besok. Apa rencanamu?, user memilih: Coba pilih menu terbaik menurutmu (I) dan tentukan waktu pasti (J)., dengan poin MBTI: Introvert & Judging")
    call ai_react_logic
    return

label show_question_q_a_14_id:
    scene bg room with dissolve
    $ narasi_asli = "Kamu melihat kamarmu. Rasanya auranya sudah basi dan membosankan."
    n "Kamu melihat kamarmu."
    n "Rasanya auranya sudah basi dan membosankan."

    menu:
        "Kamu melihat kamarmu. Rasanya auranya sudah basi dan membosankan."

        "Ganti cat (E) dan ubah barang-barang di kamar sekarang (P).":
            $ IE += 5
            $ JP += 5
            $ user_choice_text = "Ganti cat (E) dan ubah barang-barang di kamar sekarang (P)."
            $ last_answer = "Extrovert & Perceiving"
            $ unchosen_choice_text = "Biarkan saja (I) karena posisi ini sudah efisien (J)."
            $ unchosen_answer = "Introvert & Judging"
            jump show_question_q_a_14_id_A

        "Biarkan saja (I) karena posisi ini sudah efisien (J).":
            $ IE -= 5
            $ JP -= 5
            $ user_choice_text = "Biarkan saja (I) karena posisi ini sudah efisien (J)."
            $ last_answer = "Introvert & Judging"
            $ unchosen_choice_text = "Ganti cat (E) dan ubah barang-barang di kamar sekarang (P)."
            $ unchosen_answer = "Extrovert & Perceiving"
            jump show_question_q_a_14_id_B


label show_question_q_a_14_id_A:
    $ user_journey_summary.append("Di situasi Kamu melihat kamarmu. Rasanya auranya sudah basi dan membosankan., user memilih: Ganti cat (E) dan ubah barang-barang di kamar sekarang (P)., dengan poin MBTI: Extrovert & Perceiving")
    call ai_react_logic
    return

label show_question_q_a_14_id_B:
    $ user_journey_summary.append("Di situasi Kamu melihat kamarmu. Rasanya auranya sudah basi dan membosankan., user memilih: Biarkan saja (I) karena posisi ini sudah efisien (J)., dengan poin MBTI: Introvert & Judging")
    call ai_react_logic
    return

label show_question_q_a_15_id:
    scene bg stasiun with dissolve
    $ narasi_asli = "Kamu mampir di toko oleh-oleh stasiun. Banyak barang lucu dan menarik!"
    n "Kamu mampir di toko oleh-oleh stasiun."
    n "Banyak barang lucu dan menarik!"

    menu:
        "Kamu mampir di toko oleh-oleh stasiun. Banyak barang lucu dan menarik!"

        "Minta saran penjual (E) dan beli barang yang pertama kali terlihat (P).":
            $ IE += 5
            $ JP += 5
            $ user_choice_text = "Minta saran penjual (E) dan beli barang yang pertama kali terlihat (P)."
            $ last_answer = "Extrovert & Perceiving"
            $ unchosen_choice_text = "Coba berkeliling (I) dan beli sesuai kebutuhan (J)."
            $ unchosen_answer = "Introvert & Judging"
            jump show_question_q_a_15_id_A

        "Coba berkeliling (I) dan beli sesuai kebutuhan (J).":
            $ IE -= 5
            $ JP -= 5
            $ user_choice_text = "Coba berkeliling (I) dan beli sesuai kebutuhan (J)."
            $ last_answer = "Introvert & Judging"
            $ unchosen_choice_text = "Minta saran penjual (E) dan beli barang yang pertama kali terlihat (P)."
            $ unchosen_answer = "Extrovert & Perceiving"
            jump show_question_q_a_15_id_B


label show_question_q_a_15_id_A:
    $ user_journey_summary.append("Di situasi Kamu mampir di toko oleh-oleh stasiun. Banyak barang lucu dan menarik!, user memilih: Minta saran penjual (E) dan beli barang yang pertama kali terlihat (P)., dengan poin MBTI: Extrovert & Perceiving")
    call ai_react_logic
    return

label show_question_q_a_15_id_B:
    $ user_journey_summary.append("Di situasi Kamu mampir di toko oleh-oleh stasiun. Banyak barang lucu dan menarik!, user memilih: Coba berkeliling (I) dan beli sesuai kebutuhan (J)., dengan poin MBTI: Introvert & Judging")
    call ai_react_logic
    return

label show_question_q_a_16_id:
    scene bg kantor with dissolve
    $ narasi_asli = "Temanmu marah-marah padamu tanpa alasan yang jelas! Mukanya merah padam!"
    n "Temanmu marah-marah padamu tanpa alasan yang jelas!"
    n "Mukanya merah padam!"

    menu:
        "Temanmu marah-marah padamu tanpa alasan yang jelas! Mukanya merah padam!"

        "Redam amarahnya (T) dan jelaskan buktinya dulu (J).":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "Redam amarahnya (T) dan jelaskan buktinya dulu (J)."
            $ last_answer = "Thinking & Judging"
            $ unchosen_choice_text = "'Kok aku dimarahin? (F) Apa mungkin aku ada salah? (P)'."
            $ unchosen_answer = "Feeling & Perceiving"
            jump show_question_q_a_16_id_A

        "'Kok aku dimarahin? (F) Apa mungkin aku ada salah? (P)'.":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "'Kok aku dimarahin? (F) Apa mungkin aku ada salah? (P)'."
            $ last_answer = "Feeling & Perceiving"
            $ unchosen_choice_text = "Redam amarahnya (T) dan jelaskan buktinya dulu (J)."
            $ unchosen_answer = "Thinking & Judging"
            jump show_question_q_a_16_id_B


label show_question_q_a_16_id_A:
    $ user_journey_summary.append("Di situasi Temanmu marah-marah padamu tanpa alasan yang jelas! Mukanya merah padam!, user memilih: Redam amarahnya (T) dan jelaskan buktinya dulu (J)., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic
    return

label show_question_q_a_16_id_B:
    $ user_journey_summary.append("Di situasi Temanmu marah-marah padamu tanpa alasan yang jelas! Mukanya merah padam!, user memilih: 'Kok aku dimarahin? (F) Apa mungkin aku ada salah? (P)'., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic
    return

label show_question_q_a_17_id:
    scene bg dapur with dissolve
    $ narasi_asli = "Kue ulang tahun buatan kalian hasilnya gosong dan kurang rapi."
    n "Kue ulang tahun buatan kalian hasilnya gosong dan kurang rapi."

    menu:
        "Kue ulang tahun buatan kalian hasilnya gosong dan kurang rapi."

        "Ulangi dari awal sesuai resep (J) supaya hasilnya pas (T).":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "Ulangi dari awal sesuai resep (J) supaya hasilnya pas (T)."
            $ last_answer = "Thinking & Judging"
            $ unchosen_choice_text = "Pakai yang sudah ada saja (P), yang penting dibuat dengan tulus (F)."
            $ unchosen_answer = "Feeling & Perceiving"
            jump show_question_q_a_17_id_A

        "Pakai yang sudah ada saja (P), yang penting dibuat dengan tulus (F).":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "Pakai yang sudah ada saja (P), yang penting dibuat dengan tulus (F)."
            $ last_answer = "Feeling & Perceiving"
            $ unchosen_choice_text = "Ulangi dari awal sesuai resep (J) supaya hasilnya pas (T)."
            $ unchosen_answer = "Thinking & Judging"
            jump show_question_q_a_17_id_B


label show_question_q_a_17_id_A:
    $ user_journey_summary.append("Di situasi Kue ulang tahun buatan kalian hasilnya gosong dan kurang rapi., user memilih: Ulangi dari awal sesuai resep (J) supaya hasilnya pas (T)., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic
    return

label show_question_q_a_17_id_B:
    $ user_journey_summary.append("Di situasi Kue ulang tahun buatan kalian hasilnya gosong dan kurang rapi., user memilih: Pakai yang sudah ada saja (P), yang penting dibuat dengan tulus (F)., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic
    return

label show_question_q_a_18_id:
    scene bg abstrak with dissolve
    $ narasi_asli = "Kamu menemukan sebuah Lukisan Pemandangan Misterius. Kira-kira apa yang membuatnya bagus?"
    n "Kamu menemukan sebuah Lukisan Pemandangan Misterius."
    n "Kira-kira apa yang membuatnya bagus?"

    menu:
        "Kamu menemukan sebuah Lukisan Pemandangan Misterius. Kira-kira apa yang membuatnya bagus?"

        "Komposisi warnanya (T), tekniknya, semua sempurna dan rapi! (J).":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "Komposisi warnanya (T), tekniknya, semua sempurna dan rapi! (J)."
            $ last_answer = "Thinking & Judging"
            $ unchosen_choice_text = "Lukisan ini (F) memiliki emosi yang dalam dan juga indah (P)."
            $ unchosen_answer = "Feeling & Perceiving"
            jump show_question_q_a_18_id_A

        "Lukisan ini (F) memiliki emosi yang dalam dan juga indah (P).":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "Lukisan ini (F) memiliki emosi yang dalam dan juga indah (P)."
            $ last_answer = "Feeling & Perceiving"
            $ unchosen_choice_text = "Komposisi warnanya (T), tekniknya, semua sempurna dan rapi! (J)."
            $ unchosen_answer = "Thinking & Judging"
            jump show_question_q_a_18_id_B


label show_question_q_a_18_id_A:
    $ user_journey_summary.append("Di situasi Kamu menemukan sebuah Lukisan Pemandangan Misterius. Kira-kira apa yang membuatnya bagus?, user memilih: Komposisi warnanya (T), tekniknya, semua sempurna dan rapi! (J)., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic
    return

label show_question_q_a_18_id_B:
    $ user_journey_summary.append("Di situasi Kamu menemukan sebuah Lukisan Pemandangan Misterius. Kira-kira apa yang membuatnya bagus?, user memilih: Lukisan ini (F) memiliki emosi yang dalam dan juga indah (P)., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic
    return

label show_question_q_a_19_id:
    scene bg abstrak with dissolve
    $ narasi_asli = "Kamu jadi wasit. Di menit akhir, temanmu melanggar aturan tipis yang mungkin tak sengaja."
    n "Kamu jadi wasit."
    n "Di menit akhir, temanmu melanggar aturan tipis yang mungkin tak sengaja."

    menu:
        "Kamu jadi wasit. Di menit akhir, temanmu melanggar aturan tipis yang mungkin tak sengaja."

        "Tetap tiup peluit (T), adil bagi semua yang bermain jujur (J).":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "Tetap tiup peluit (T), adil bagi semua yang bermain jujur (J)."
            $ last_answer = "Thinking & Judging"
            $ unchosen_choice_text = "Beri kelonggaran sekali ini (F), dia jelas tak sengaja (P)."
            $ unchosen_answer = "Feeling & Perceiving"
            jump show_question_q_a_19_id_A

        "Beri kelonggaran sekali ini (F), dia jelas tak sengaja (P).":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "Beri kelonggaran sekali ini (F), dia jelas tak sengaja (P)."
            $ last_answer = "Feeling & Perceiving"
            $ unchosen_choice_text = "Tetap tiup peluit (T), adil bagi semua yang bermain jujur (J)."
            $ unchosen_answer = "Thinking & Judging"
            jump show_question_q_a_19_id_B


label show_question_q_a_19_id_A:
    $ user_journey_summary.append("Di situasi Kamu jadi wasit. Di menit akhir, temanmu melanggar aturan tipis yang mungkin tak sengaja., user memilih: Tetap tiup peluit (T), adil bagi semua yang bermain jujur (J)., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic
    return

label show_question_q_a_19_id_B:
    $ user_journey_summary.append("Di situasi Kamu jadi wasit. Di menit akhir, temanmu melanggar aturan tipis yang mungkin tak sengaja., user memilih: Beri kelonggaran sekali ini (F), dia jelas tak sengaja (P)., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic
    return

label show_question_q_a_20_id:
    scene bg kantor with dissolve
    $ narasi_asli = "Timmu lesu hari ini, semangatnya hilang entah ke mana."
    n "Timmu lesu hari ini, semangatnya hilang entah ke mana."

    menu:
        "Timmu lesu hari ini, semangatnya hilang entah ke mana."

        "Beri target jelas (T) dan tetapkan tolok ukur yang terukur (J).":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "Beri target jelas (T) dan tetapkan tolok ukur yang terukur (J)."
            $ last_answer = "Thinking & Judging"
            $ unchosen_choice_text = "Bangkitkan semangat (F), ajak mereka bergerak bareng demi tim (P)."
            $ unchosen_answer = "Feeling & Perceiving"
            jump show_question_q_a_20_id_A

        "Bangkitkan semangat (F), ajak mereka bergerak bareng demi tim (P).":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "Bangkitkan semangat (F), ajak mereka bergerak bareng demi tim (P)."
            $ last_answer = "Feeling & Perceiving"
            $ unchosen_choice_text = "Beri target jelas (T) dan tetapkan tolok ukur yang terukur (J)."
            $ unchosen_answer = "Thinking & Judging"
            jump show_question_q_a_20_id_B


label show_question_q_a_20_id_A:
    $ user_journey_summary.append("Di situasi Timmu lesu hari ini, semangatnya hilang entah ke mana., user memilih: Beri target jelas (T) dan tetapkan tolok ukur yang terukur (J)., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic
    return

label show_question_q_a_20_id_B:
    $ user_journey_summary.append("Di situasi Timmu lesu hari ini, semangatnya hilang entah ke mana., user memilih: Bangkitkan semangat (F), ajak mereka bergerak bareng demi tim (P)., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic
    return

label show_question_q_b_21_id:
    scene bg dapur with dissolve
    $ narasi_asli = "(Bingung!) Kamu menemukan Buku resep kuno yang bentuknya aneh. Saat itu kamu lapar sekali. Kira-kira bagaimana cara masaknya?"
    n "(Bingung!) Kamu menemukan Buku resep kuno yang bentuknya aneh."
    n "Saat itu kamu lapar sekali."
    n "Kira-kira bagaimana cara masaknya?"

    menu:
        "(Bingung!) Kamu menemukan Buku resep kuno yang bentuknya aneh. Saat itu kamu lapar sekali. Kira-kira bagaimana cara masaknya?"

        "Baca sendiri dengan tenang (I) dan ikuti instruksi takarannya secara presisi (S).":
            $ IE -= 5
            $ SN -= 5
            $ user_choice_text = "Baca sendiri dengan tenang (I) dan ikuti instruksi takarannya secara presisi (S)."
            $ last_answer = "Introvert & Sensing"
            $ unchosen_choice_text = "Panggil teman-teman (E) untuk menebak dan meracik rasa baru (N)."
            $ unchosen_answer = "Extrovert & Intuitive"
            jump show_question_q_b_21_id_A

        "Panggil teman-teman (E) untuk menebak dan meracik rasa baru (N).":
            $ IE += 5
            $ SN += 5
            $ user_choice_text = "Panggil teman-teman (E) untuk menebak dan meracik rasa baru (N)."
            $ last_answer = "Extrovert & Intuitive"
            $ unchosen_choice_text = "Baca sendiri dengan tenang (I) dan ikuti instruksi takarannya secara presisi (S)."
            $ unchosen_answer = "Introvert & Sensing"
            jump show_question_q_b_21_id_B


label show_question_q_b_21_id_A:
    $ user_journey_summary.append("Di situasi (Bingung!) Kamu menemukan Buku resep kuno yang bentuknya aneh. Saat itu kamu lapar sekali. Kira-kira bagaimana cara masaknya?, user memilih: Baca sendiri dengan tenang (I) dan ikuti instruksi takarannya secara presisi (S)., dengan poin MBTI: Introvert & Sensing")
    call ai_react_logic
    return

label show_question_q_b_21_id_B:
    $ user_journey_summary.append("Di situasi (Bingung!) Kamu menemukan Buku resep kuno yang bentuknya aneh. Saat itu kamu lapar sekali. Kira-kira bagaimana cara masaknya?, user memilih: Panggil teman-teman (E) untuk menebak dan meracik rasa baru (N)., dengan poin MBTI: Extrovert & Intuitive")
    call ai_react_logic
    return

label show_question_q_b_22_id:
    scene bg kantor with dissolve
    $ narasi_asli = "(Mendadak!) Klien datang minta ide yang fresh sekarang juga! sedangkan Kamu belum menyiapkan materi apapun."
    n "(Mendadak!) Klien datang minta ide yang fresh sekarang juga!"
    n "sedangkan Kamu belum menyiapkan materi apapun."

    menu:
        "(Mendadak!) Klien datang minta ide yang fresh sekarang juga! sedangkan Kamu belum menyiapkan materi apapun."

        "Minta waktu menyendiri (I) untuk menyusun fakta dan data yang ada (S).":
            $ IE -= 5
            $ SN -= 5
            $ user_choice_text = "Minta waktu menyendiri (I) untuk menyusun fakta dan data yang ada (S)."
            $ last_answer = "Introvert & Sensing"
            $ unchosen_choice_text = "Ajak diskusi santai (E) dan sampaikan idemu tentang visi masa depan (N)."
            $ unchosen_answer = "Extrovert & Intuitive"
            jump show_question_q_b_22_id_A

        "Ajak diskusi santai (E) dan sampaikan idemu tentang visi masa depan (N).":
            $ IE += 5
            $ SN += 5
            $ user_choice_text = "Ajak diskusi santai (E) dan sampaikan idemu tentang visi masa depan (N)."
            $ last_answer = "Extrovert & Intuitive"
            $ unchosen_choice_text = "Minta waktu menyendiri (I) untuk menyusun fakta dan data yang ada (S)."
            $ unchosen_answer = "Introvert & Sensing"
            jump show_question_q_b_22_id_B


label show_question_q_b_22_id_A:
    $ user_journey_summary.append("Di situasi (Mendadak!) Klien datang minta ide yang fresh sekarang juga! sedangkan Kamu belum menyiapkan materi apapun., user memilih: Minta waktu menyendiri (I) untuk menyusun fakta dan data yang ada (S)., dengan poin MBTI: Introvert & Sensing")
    call ai_react_logic
    return

label show_question_q_b_22_id_B:
    $ user_journey_summary.append("Di situasi (Mendadak!) Klien datang minta ide yang fresh sekarang juga! sedangkan Kamu belum menyiapkan materi apapun., user memilih: Ajak diskusi santai (E) dan sampaikan idemu tentang visi masa depan (N)., dengan poin MBTI: Extrovert & Intuitive")
    call ai_react_logic
    return

label show_question_q_b_23_id:
    scene bg abstrak with dissolve
    $ narasi_asli = "Kamu masuk ke perpustakaan Internasional. Buku mana yang kamu ambil duluan?"
    n "Kamu masuk ke perpustakaan Internasional."
    n "Buku mana yang kamu ambil duluan?"

    menu:
        "Kamu masuk ke perpustakaan Internasional. Buku mana yang kamu ambil duluan?"

        "'Ensiklopedia bergambar' (S)  yang bisa dibaca bareng teman (E).":
            $ IE += 5
            $ SN -= 5
            $ user_choice_text = "'Ensiklopedia bergambar' (S)  yang bisa dibaca bareng teman (E)."
            $ last_answer = "Extrovert & Sensing"
            $ unchosen_choice_text = "'Filosofi tebal' (N)  yang menarik untuk dibaca di tempat sepi (I)."
            $ unchosen_answer = "Introvert & Intuitive"
            jump show_question_q_b_23_id_A

        "'Filosofi tebal' (N)  yang menarik untuk dibaca di tempat sepi (I).":
            $ IE -= 5
            $ SN += 5
            $ user_choice_text = "'Filosofi tebal' (N)  yang menarik untuk dibaca di tempat sepi (I)."
            $ last_answer = "Introvert & Intuitive"
            $ unchosen_choice_text = "'Ensiklopedia bergambar' (S)  yang bisa dibaca bareng teman (E)."
            $ unchosen_answer = "Extrovert & Sensing"
            jump show_question_q_b_23_id_B


label show_question_q_b_23_id_A:
    $ user_journey_summary.append("Di situasi Kamu masuk ke perpustakaan Internasional. Buku mana yang kamu ambil duluan?, user memilih: 'Ensiklopedia bergambar' (S)  yang bisa dibaca bareng teman (E)., dengan poin MBTI: Extrovert & Sensing")
    call ai_react_logic
    return

label show_question_q_b_23_id_B:
    $ user_journey_summary.append("Di situasi Kamu masuk ke perpustakaan Internasional. Buku mana yang kamu ambil duluan?, user memilih: 'Filosofi tebal' (N)  yang menarik untuk dibaca di tempat sepi (I)., dengan poin MBTI: Introvert & Intuitive")
    call ai_react_logic
    return

label show_question_q_b_24_id:
    scene bg kafe with dissolve
    $ narasi_asli = "Perutmu lapar, tapi dompetmu tipis. Sementara itu teman-temanmu mengajakmu makan diluar."
    n "Perutmu lapar, tapi dompetmu tipis."
    n "Sementara itu teman-temanmu mengajakmu makan diluar."

    menu:
        "Perutmu lapar, tapi dompetmu tipis. Sementara itu teman-temanmu mengajakmu makan diluar."

        "Ikut mereka (E) tapi cari warung langganan yang sudah pasti murah dan enak (S).":
            $ IE += 5
            $ SN -= 5
            $ user_choice_text = "Ikut mereka (E) tapi cari warung langganan yang sudah pasti murah dan enak (S)."
            $ last_answer = "Extrovert & Sensing"
            $ unchosen_choice_text = "Tolak dahulu (I), mau coba cari makanan murah dan unik yang mungkin ada disekitar tempatmu (N)."
            $ unchosen_answer = "Introvert & Intuitive"
            jump show_question_q_b_24_id_A

        "Tolak dahulu (I), mau coba cari makanan murah dan unik yang mungkin ada disekitar tempatmu (N).":
            $ IE -= 5
            $ SN += 5
            $ user_choice_text = "Tolak dahulu (I), mau coba cari makanan murah dan unik yang mungkin ada disekitar tempatmu (N)."
            $ last_answer = "Introvert & Intuitive"
            $ unchosen_choice_text = "Ikut mereka (E) tapi cari warung langganan yang sudah pasti murah dan enak (S)."
            $ unchosen_answer = "Extrovert & Sensing"
            jump show_question_q_b_24_id_B


label show_question_q_b_24_id_A:
    $ user_journey_summary.append("Di situasi Perutmu lapar, tapi dompetmu tipis. Sementara itu teman-temanmu mengajakmu makan diluar., user memilih: Ikut mereka (E) tapi cari warung langganan yang sudah pasti murah dan enak (S)., dengan poin MBTI: Extrovert & Sensing")
    call ai_react_logic
    return

label show_question_q_b_24_id_B:
    $ user_journey_summary.append("Di situasi Perutmu lapar, tapi dompetmu tipis. Sementara itu teman-temanmu mengajakmu makan diluar., user memilih: Tolak dahulu (I), mau coba cari makanan murah dan unik yang mungkin ada disekitar tempatmu (N)., dengan poin MBTI: Introvert & Intuitive")
    call ai_react_logic
    return

label show_question_q_b_25_id:
    scene bg stasiun with dissolve
    $ narasi_asli = "Ada koper mencurigakan tertinggal di stasiun sepi."
    n "Ada koper mencurigakan tertinggal di stasiun sepi."

    menu:
        "Ada koper mencurigakan tertinggal di stasiun sepi."

        "Panggil petugas (E) untuk mengecek isinya secara aman (S).":
            $ IE += 5
            $ SN -= 5
            $ user_choice_text = "Panggil petugas (E) untuk mengecek isinya secara aman (S)."
            $ last_answer = "Extrovert & Sensing"
            $ unchosen_choice_text = "Perhatikan dari jauh (I) sambil membayangkan apa isi sebenarnya dari koper tersebut (N)."
            $ unchosen_answer = "Introvert & Intuitive"
            jump show_question_q_b_25_id_A

        "Perhatikan dari jauh (I) sambil membayangkan apa isi sebenarnya dari koper tersebut (N).":
            $ IE -= 5
            $ SN += 5
            $ user_choice_text = "Perhatikan dari jauh (I) sambil membayangkan apa isi sebenarnya dari koper tersebut (N)."
            $ last_answer = "Introvert & Intuitive"
            $ unchosen_choice_text = "Panggil petugas (E) untuk mengecek isinya secara aman (S)."
            $ unchosen_answer = "Extrovert & Sensing"
            jump show_question_q_b_25_id_B


label show_question_q_b_25_id_A:
    $ user_journey_summary.append("Di situasi Ada koper mencurigakan tertinggal di stasiun sepi., user memilih: Panggil petugas (E) untuk mengecek isinya secara aman (S)., dengan poin MBTI: Extrovert & Sensing")
    call ai_react_logic
    return

label show_question_q_b_25_id_B:
    $ user_journey_summary.append("Di situasi Ada koper mencurigakan tertinggal di stasiun sepi., user memilih: Perhatikan dari jauh (I) sambil membayangkan apa isi sebenarnya dari koper tersebut (N)., dengan poin MBTI: Introvert & Intuitive")
    call ai_react_logic
    return

label show_question_q_b_26_id:
    scene bg kantor with dissolve
    $ narasi_asli = "Rekan timmu melakukan kesalahan fatal yang merugikan semua orang."
    n "Rekan timmu melakukan kesalahan fatal yang merugikan semua orang."

    menu:
        "Rekan timmu melakukan kesalahan fatal yang merugikan semua orang."

        "Hadapi langsung! (E) dan minta dia jelaskan ada apa sebenarnya(T).":
            $ IE += 5
            $ TF -= 5
            $ user_choice_text = "Hadapi langsung! (E) dan minta dia jelaskan ada apa sebenarnya(T)."
            $ last_answer = "Extrovert & Thinking"
            $ unchosen_choice_text = "Kirim dia pesan pribadi (I), lalu tanya apakah dia baik-baik saja (F)."
            $ unchosen_answer = "Introvert & Feeling"
            jump show_question_q_b_26_id_A

        "Kirim dia pesan pribadi (I), lalu tanya apakah dia baik-baik saja (F).":
            $ IE -= 5
            $ TF += 5
            $ user_choice_text = "Kirim dia pesan pribadi (I), lalu tanya apakah dia baik-baik saja (F)."
            $ last_answer = "Introvert & Feeling"
            $ unchosen_choice_text = "Hadapi langsung! (E) dan minta dia jelaskan ada apa sebenarnya(T)."
            $ unchosen_answer = "Extrovert & Thinking"
            jump show_question_q_b_26_id_B


label show_question_q_b_26_id_A:
    $ user_journey_summary.append("Di situasi Rekan timmu melakukan kesalahan fatal yang merugikan semua orang., user memilih: Hadapi langsung! (E) dan minta dia jelaskan ada apa sebenarnya(T)., dengan poin MBTI: Extrovert & Thinking")
    call ai_react_logic
    return

label show_question_q_b_26_id_B:
    $ user_journey_summary.append("Di situasi Rekan timmu melakukan kesalahan fatal yang merugikan semua orang., user memilih: Kirim dia pesan pribadi (I), lalu tanya apakah dia baik-baik saja (F)., dengan poin MBTI: Introvert & Feeling")
    call ai_react_logic
    return

label show_question_q_b_27_id:
    scene bg kantor with dissolve
    $ narasi_asli = "Temanmu minta pendapat jujur soal karyanya yang... bisa dibilang...hancur lebur menurutmu."
    n "Temanmu minta pendapat jujur soal karyanya yang..."
    n "bisa dibilang...hancur lebur menurutmu."

    menu:
        "Temanmu minta pendapat jujur soal karyanya yang... bisa dibilang...hancur lebur menurutmu."

        "Bilang terus terang (E) bagian mana yang salah agar bisa diperbaiki (T).":
            $ IE += 5
            $ TF -= 5
            $ user_choice_text = "Bilang terus terang (E) bagian mana yang salah agar bisa diperbaiki (T)."
            $ last_answer = "Extrovert & Thinking"
            $ unchosen_choice_text = "Diam atau senyum saja (I), nggak tega menyakiti perasaannya (F)."
            $ unchosen_answer = "Introvert & Feeling"
            jump show_question_q_b_27_id_A

        "Diam atau senyum saja (I), nggak tega menyakiti perasaannya (F).":
            $ IE -= 5
            $ TF += 5
            $ user_choice_text = "Diam atau senyum saja (I), nggak tega menyakiti perasaannya (F)."
            $ last_answer = "Introvert & Feeling"
            $ unchosen_choice_text = "Bilang terus terang (E) bagian mana yang salah agar bisa diperbaiki (T)."
            $ unchosen_answer = "Extrovert & Thinking"
            jump show_question_q_b_27_id_B


label show_question_q_b_27_id_A:
    $ user_journey_summary.append("Di situasi Temanmu minta pendapat jujur soal karyanya yang... bisa dibilang...hancur lebur menurutmu., user memilih: Bilang terus terang (E) bagian mana yang salah agar bisa diperbaiki (T)., dengan poin MBTI: Extrovert & Thinking")
    call ai_react_logic
    return

label show_question_q_b_27_id_B:
    $ user_journey_summary.append("Di situasi Temanmu minta pendapat jujur soal karyanya yang... bisa dibilang...hancur lebur menurutmu., user memilih: Diam atau senyum saja (I), nggak tega menyakiti perasaannya (F)., dengan poin MBTI: Introvert & Feeling")
    call ai_react_logic
    return

label show_question_q_b_28_id:
    scene bg kafe with dissolve
    $ narasi_asli = "Dua orang asing berdebat keras di meja sebelah. Mengganggu banget!"
    n "Dua orang asing berdebat keras di meja sebelah."
    n "Mengganggu banget!"

    menu:
        "Dua orang asing berdebat keras di meja sebelah. Mengganggu banget!"

        "Tegur mereka (E), 'Tolong tenang, argumen kalian nggak logis!' (T).":
            $ IE += 5
            $ TF -= 5
            $ user_choice_text = "Tegur mereka (E), 'Tolong tenang, argumen kalian nggak logis!' (T)."
            $ last_answer = "Extrovert & Thinking"
            $ unchosen_choice_text = "Pindah meja (I), menjauh karena energinya negatif banget (F)."
            $ unchosen_answer = "Introvert & Feeling"
            jump show_question_q_b_28_id_A

        "Pindah meja (I), menjauh karena energinya negatif banget (F).":
            $ IE -= 5
            $ TF += 5
            $ user_choice_text = "Pindah meja (I), menjauh karena energinya negatif banget (F)."
            $ last_answer = "Introvert & Feeling"
            $ unchosen_choice_text = "Tegur mereka (E), 'Tolong tenang, argumen kalian nggak logis!' (T)."
            $ unchosen_answer = "Extrovert & Thinking"
            jump show_question_q_b_28_id_B


label show_question_q_b_28_id_A:
    $ user_journey_summary.append("Di situasi Dua orang asing berdebat keras di meja sebelah. Mengganggu banget!, user memilih: Tegur mereka (E), 'Tolong tenang, argumen kalian nggak logis!' (T)., dengan poin MBTI: Extrovert & Thinking")
    call ai_react_logic
    return

label show_question_q_b_28_id_B:
    $ user_journey_summary.append("Di situasi Dua orang asing berdebat keras di meja sebelah. Mengganggu banget!, user memilih: Pindah meja (I), menjauh karena energinya negatif banget (F)., dengan poin MBTI: Introvert & Feeling")
    call ai_react_logic
    return

label show_question_q_b_29_id:
    scene bg abstrak with dissolve
    $ narasi_asli = "Kamu harus memilih pemimpin untuk misi berbahaya."
    n "Kamu harus memilih pemimpin untuk misi berbahaya."

    menu:
        "Kamu harus memilih pemimpin untuk misi berbahaya."

        "Debat terbuka (E), pilih yang statistiknya paling kuat (T).":
            $ IE += 5
            $ TF -= 5
            $ user_choice_text = "Debat terbuka (E), pilih yang statistiknya paling kuat (T)."
            $ last_answer = "Extrovert & Thinking"
            $ unchosen_choice_text = "Renungkan dengan beberapa teman dekat (I), lalu pilih yang hatinya paling tulus (F)."
            $ unchosen_answer = "Introvert & Feeling"
            jump show_question_q_b_29_id_A

        "Renungkan dengan beberapa teman dekat (I), lalu pilih yang hatinya paling tulus (F).":
            $ IE -= 5
            $ TF += 5
            $ user_choice_text = "Renungkan dengan beberapa teman dekat (I), lalu pilih yang hatinya paling tulus (F)."
            $ last_answer = "Introvert & Feeling"
            $ unchosen_choice_text = "Debat terbuka (E), pilih yang statistiknya paling kuat (T)."
            $ unchosen_answer = "Extrovert & Thinking"
            jump show_question_q_b_29_id_B


label show_question_q_b_29_id_A:
    $ user_journey_summary.append("Di situasi Kamu harus memilih pemimpin untuk misi berbahaya., user memilih: Debat terbuka (E), pilih yang statistiknya paling kuat (T)., dengan poin MBTI: Extrovert & Thinking")
    call ai_react_logic
    return

label show_question_q_b_29_id_B:
    $ user_journey_summary.append("Di situasi Kamu harus memilih pemimpin untuk misi berbahaya., user memilih: Renungkan dengan beberapa teman dekat (I), lalu pilih yang hatinya paling tulus (F)., dengan poin MBTI: Introvert & Feeling")
    call ai_react_logic
    return

label show_question_q_b_30_id:
    scene bg taman with dissolve
    $ narasi_asli = "Ada kerumunan orang sedang sedih karena pohon tua ditebang oleh pemerintah sekitar."
    n "Ada kerumunan orang sedang sedih karena pohon tua ditebang oleh pemerintah sekitar."

    menu:
        "Ada kerumunan orang sedang sedih karena pohon tua ditebang oleh pemerintah sekitar."

        "Kumpulkan mereka (E) untuk buat petisi protes ke pemerintah (T).":
            $ IE += 5
            $ TF -= 5
            $ user_choice_text = "Kumpulkan mereka (E) untuk buat petisi protes ke pemerintah (T)."
            $ last_answer = "Extrovert & Thinking"
            $ unchosen_choice_text = "Duduk diam (I) di sana sebagai tanda solidaritas (F)."
            $ unchosen_answer = "Introvert & Feeling"
            jump show_question_q_b_30_id_A

        "Duduk diam (I) di sana sebagai tanda solidaritas (F).":
            $ IE -= 5
            $ TF += 5
            $ user_choice_text = "Duduk diam (I) di sana sebagai tanda solidaritas (F)."
            $ last_answer = "Introvert & Feeling"
            $ unchosen_choice_text = "Kumpulkan mereka (E) untuk buat petisi protes ke pemerintah (T)."
            $ unchosen_answer = "Extrovert & Thinking"
            jump show_question_q_b_30_id_B


label show_question_q_b_30_id_A:
    $ user_journey_summary.append("Di situasi Ada kerumunan orang sedang sedih karena pohon tua ditebang oleh pemerintah sekitar., user memilih: Kumpulkan mereka (E) untuk buat petisi protes ke pemerintah (T)., dengan poin MBTI: Extrovert & Thinking")
    call ai_react_logic
    return

label show_question_q_b_30_id_B:
    $ user_journey_summary.append("Di situasi Ada kerumunan orang sedang sedih karena pohon tua ditebang oleh pemerintah sekitar., user memilih: Duduk diam (I) di sana sebagai tanda solidaritas (F)., dengan poin MBTI: Introvert & Feeling")
    call ai_react_logic
    return

label show_question_q_b_31_id:
    scene bg stasiun with dissolve
    $ narasi_asli = "(Telat!) Kereta terakhir berangkat 1 menit lagi! Kamu masih di lobi!"
    n "(Telat!) Kereta terakhir berangkat 1 menit lagi!"
    n "Kamu masih di lobi!"

    menu:
        "(Telat!) Kereta terakhir berangkat 1 menit lagi! Kamu masih di lobi!"

        "Teriak 'Tunggu!' (E) dan lari menerobos gerbang tanpa pikir panjang (P).":
            $ IE += 5
            $ JP += 5
            $ user_choice_text = "Teriak 'Tunggu!' (E) dan lari menerobos gerbang tanpa pikir panjang (P)."
            $ last_answer = "Extrovert & Perceiving"
            $ unchosen_choice_text = "Pasrah (I). Ini salahku karena tidak cek jadwal tadi pagi (J)."
            $ unchosen_answer = "Introvert & Judging"
            jump show_question_q_b_31_id_A

        "Pasrah (I). Ini salahku karena tidak cek jadwal tadi pagi (J).":
            $ IE -= 5
            $ JP -= 5
            $ user_choice_text = "Pasrah (I). Ini salahku karena tidak cek jadwal tadi pagi (J)."
            $ last_answer = "Introvert & Judging"
            $ unchosen_choice_text = "Teriak 'Tunggu!' (E) dan lari menerobos gerbang tanpa pikir panjang (P)."
            $ unchosen_answer = "Extrovert & Perceiving"
            jump show_question_q_b_31_id_B


label show_question_q_b_31_id_A:
    $ user_journey_summary.append("Di situasi (Telat!) Kereta terakhir berangkat 1 menit lagi! Kamu masih di lobi!, user memilih: Teriak 'Tunggu!' (E) dan lari menerobos gerbang tanpa pikir panjang (P)., dengan poin MBTI: Extrovert & Perceiving")
    call ai_react_logic
    return

label show_question_q_b_31_id_B:
    $ user_journey_summary.append("Di situasi (Telat!) Kereta terakhir berangkat 1 menit lagi! Kamu masih di lobi!, user memilih: Pasrah (I). Ini salahku karena tidak cek jadwal tadi pagi (J)., dengan poin MBTI: Introvert & Judging")
    call ai_react_logic
    return

label show_question_q_b_32_id:
    scene bg kafe with dissolve
    $ narasi_asli = "Kamu dan rombongan besar bingung mau pesan apa di Restoran. Pelayan yang menunggu mulai kesal."
    n "Kamu dan rombongan besar bingung mau pesan apa di Restoran."
    n "Pelayan yang menunggu mulai kesal."

    menu:
        "Kamu dan rombongan besar bingung mau pesan apa di Restoran. Pelayan yang menunggu mulai kesal."

        "Tanya ke yang lain! (E), 'Mau makanan apa? Bebas deh!' (P).":
            $ IE += 5
            $ JP += 5
            $ user_choice_text = "Tanya ke yang lain! (E), 'Mau makanan apa? Bebas deh!' (P)."
            $ last_answer = "Extrovert & Perceiving"
            $ unchosen_choice_text = "Ambil alih (J), 'Oke, aku pesankan menu paket buat semua agar lebih cepat ya' (I)."
            $ unchosen_answer = "Introvert & Judging"
            jump show_question_q_b_32_id_A

        "Ambil alih (J), 'Oke, aku pesankan menu paket buat semua agar lebih cepat ya' (I).":
            $ IE -= 5
            $ JP -= 5
            $ user_choice_text = "Ambil alih (J), 'Oke, aku pesankan menu paket buat semua agar lebih cepat ya' (I)."
            $ last_answer = "Introvert & Judging"
            $ unchosen_choice_text = "Tanya ke yang lain! (E), 'Mau makanan apa? Bebas deh!' (P)."
            $ unchosen_answer = "Extrovert & Perceiving"
            jump show_question_q_b_32_id_B


label show_question_q_b_32_id_A:
    $ user_journey_summary.append("Di situasi Kamu dan rombongan besar bingung mau pesan apa di Restoran. Pelayan yang menunggu mulai kesal., user memilih: Tanya ke yang lain! (E), 'Mau makanan apa? Bebas deh!' (P)., dengan poin MBTI: Extrovert & Perceiving")
    call ai_react_logic
    return

label show_question_q_b_32_id_B:
    $ user_journey_summary.append("Di situasi Kamu dan rombongan besar bingung mau pesan apa di Restoran. Pelayan yang menunggu mulai kesal., user memilih: Ambil alih (J), 'Oke, aku pesankan menu paket buat semua agar lebih cepat ya' (I)., dengan poin MBTI: Introvert & Judging")
    call ai_react_logic
    return

label show_question_q_b_33_id:
    scene bg kafe with dissolve
    $ narasi_asli = "Kamu lihat jaket yang keren banget dipajang di toko, tapi harganya mahal."
    n "Kamu lihat jaket yang keren banget dipajang di toko, tapi harganya mahal."

    menu:
        "Kamu lihat jaket yang keren banget dipajang di toko, tapi harganya mahal."

        "Tanya pendapat orang lain (E), kalau bagus langsung beli aja! (P).":
            $ IE += 5
            $ JP += 5
            $ user_choice_text = "Tanya pendapat orang lain (E), kalau bagus langsung beli aja! (P)."
            $ last_answer = "Extrovert & Perceiving"
            $ unchosen_choice_text = "Tanyakan diri sendiri (I), 'lagi tidak ada di budget. jangan dulu deh' (J)."
            $ unchosen_answer = "Introvert & Judging"
            jump show_question_q_b_33_id_A

        "Tanyakan diri sendiri (I), 'lagi tidak ada di budget. jangan dulu deh' (J).":
            $ IE -= 5
            $ JP -= 5
            $ user_choice_text = "Tanyakan diri sendiri (I), 'lagi tidak ada di budget. jangan dulu deh' (J)."
            $ last_answer = "Introvert & Judging"
            $ unchosen_choice_text = "Tanya pendapat orang lain (E), kalau bagus langsung beli aja! (P)."
            $ unchosen_answer = "Extrovert & Perceiving"
            jump show_question_q_b_33_id_B


label show_question_q_b_33_id_A:
    $ user_journey_summary.append("Di situasi Kamu lihat jaket yang keren banget dipajang di toko, tapi harganya mahal., user memilih: Tanya pendapat orang lain (E), kalau bagus langsung beli aja! (P)., dengan poin MBTI: Extrovert & Perceiving")
    call ai_react_logic
    return

label show_question_q_b_33_id_B:
    $ user_journey_summary.append("Di situasi Kamu lihat jaket yang keren banget dipajang di toko, tapi harganya mahal., user memilih: Tanyakan diri sendiri (I), 'lagi tidak ada di budget. jangan dulu deh' (J)., dengan poin MBTI: Introvert & Judging")
    call ai_react_logic
    return

label show_question_q_b_34_id:
    scene bg room with dissolve
    $ narasi_asli = "Temanmu bilang kamarmu membosankan. Lalu apa reaksimu?"
    n "Temanmu bilang kamarmu membosankan."
    n "Lalu apa reaksimu?"

    menu:
        "Temanmu bilang kamarmu membosankan. Lalu apa reaksimu?"

        "'Benar juga!' Mumpung ada teman, ajak dia (E) geser-geser furnitur sekarang juga (P).":
            $ IE += 5
            $ JP += 5
            $ user_choice_text = "'Benar juga!' Mumpung ada teman, ajak dia (E) geser-geser furnitur sekarang juga (P)."
            $ last_answer = "Extrovert & Perceiving"
            $ unchosen_choice_text = "Biarkan. (I) 'Aku lebih suka, karena semuanya sudah ada di tempat yang seharusnya'(J)."
            $ unchosen_answer = "Introvert & Judging"
            jump show_question_q_b_34_id_A

        "Biarkan. (I) 'Aku lebih suka, karena semuanya sudah ada di tempat yang seharusnya'(J).":
            $ IE -= 5
            $ JP -= 5
            $ user_choice_text = "Biarkan. (I) 'Aku lebih suka, karena semuanya sudah ada di tempat yang seharusnya'(J)."
            $ last_answer = "Introvert & Judging"
            $ unchosen_choice_text = "'Benar juga!' Mumpung ada teman, ajak dia (E) geser-geser furnitur sekarang juga (P)."
            $ unchosen_answer = "Extrovert & Perceiving"
            jump show_question_q_b_34_id_B


label show_question_q_b_34_id_A:
    $ user_journey_summary.append("Di situasi Temanmu bilang kamarmu membosankan. Lalu apa reaksimu?, user memilih: 'Benar juga!' Mumpung ada teman, ajak dia (E) geser-geser furnitur sekarang juga (P)., dengan poin MBTI: Extrovert & Perceiving")
    call ai_react_logic
    return

label show_question_q_b_34_id_B:
    $ user_journey_summary.append("Di situasi Temanmu bilang kamarmu membosankan. Lalu apa reaksimu?, user memilih: Biarkan. (I) 'Aku lebih suka, karena semuanya sudah ada di tempat yang seharusnya'(J)., dengan poin MBTI: Introvert & Judging")
    call ai_react_logic
    return

label show_question_q_b_35_id:
    scene bg kantor with dissolve
    $ narasi_asli = "Kamu harus pidato dadakan di depan umum! bagaimana ini?!"
    n "Kamu harus pidato dadakan di depan umum!"
    n "bagaimana ini?!"

    menu:
        "Kamu harus pidato dadakan di depan umum! bagaimana ini?!"

        "Maju dengan percaya diri (E), ngomong mengalir, dengan lihat situasi (P).":
            $ IE += 5
            $ JP += 5
            $ user_choice_text = "Maju dengan percaya diri (E), ngomong mengalir, dengan lihat situasi (P)."
            $ last_answer = "Extrovert & Perceiving"
            $ unchosen_choice_text = "Mundur sebentar (I), minta waktu buat mencatat poin-poin penting dahulu (J)."
            $ unchosen_answer = "Introvert & Judging"
            jump show_question_q_b_35_id_A

        "Mundur sebentar (I), minta waktu buat mencatat poin-poin penting dahulu (J).":
            $ IE -= 5
            $ JP -= 5
            $ user_choice_text = "Mundur sebentar (I), minta waktu buat mencatat poin-poin penting dahulu (J)."
            $ last_answer = "Introvert & Judging"
            $ unchosen_choice_text = "Maju dengan percaya diri (E), ngomong mengalir, dengan lihat situasi (P)."
            $ unchosen_answer = "Extrovert & Perceiving"
            jump show_question_q_b_35_id_B


label show_question_q_b_35_id_A:
    $ user_journey_summary.append("Di situasi Kamu harus pidato dadakan di depan umum! bagaimana ini?!, user memilih: Maju dengan percaya diri (E), ngomong mengalir, dengan lihat situasi (P)., dengan poin MBTI: Extrovert & Perceiving")
    call ai_react_logic
    return

label show_question_q_b_35_id_B:
    $ user_journey_summary.append("Di situasi Kamu harus pidato dadakan di depan umum! bagaimana ini?!, user memilih: Mundur sebentar (I), minta waktu buat mencatat poin-poin penting dahulu (J)., dengan poin MBTI: Introvert & Judging")
    call ai_react_logic
    return

label show_question_q_b_36_id:
    scene bg abstrak with dissolve
    $ narasi_asli = "Gerbang benteng harus ditutup sebelum badai tiba. Beberapa orang masih mengumpulkan barang di luar."
    n "Gerbang benteng harus ditutup sebelum badai tiba."
    n "Beberapa orang masih mengumpulkan barang di luar."

    menu:
        "Gerbang benteng harus ditutup sebelum badai tiba. Beberapa orang masih mengumpulkan barang di luar."

        "Tutup tepat waktu (J), lindungi mayoritas yang sudah di dalam (T).":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "Tutup tepat waktu (J), lindungi mayoritas yang sudah di dalam (T)."
            $ last_answer = "Thinking & Judging"
            $ unchosen_choice_text = "Tahan sebentar lagi (P), beri mereka kesempatan masuk dulu (F)."
            $ unchosen_answer = "Feeling & Perceiving"
            jump show_question_q_b_36_id_A

        "Tahan sebentar lagi (P), beri mereka kesempatan masuk dulu (F).":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "Tahan sebentar lagi (P), beri mereka kesempatan masuk dulu (F)."
            $ last_answer = "Feeling & Perceiving"
            $ unchosen_choice_text = "Tutup tepat waktu (J), lindungi mayoritas yang sudah di dalam (T)."
            $ unchosen_answer = "Thinking & Judging"
            jump show_question_q_b_36_id_B


label show_question_q_b_36_id_A:
    $ user_journey_summary.append("Di situasi Gerbang benteng harus ditutup sebelum badai tiba. Beberapa orang masih mengumpulkan barang di luar., user memilih: Tutup tepat waktu (J), lindungi mayoritas yang sudah di dalam (T)., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic
    return

label show_question_q_b_36_id_B:
    $ user_journey_summary.append("Di situasi Gerbang benteng harus ditutup sebelum badai tiba. Beberapa orang masih mengumpulkan barang di luar., user memilih: Tahan sebentar lagi (P), beri mereka kesempatan masuk dulu (F)., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic
    return

label show_question_q_b_37_id:
    scene bg kantor with dissolve
    $ narasi_asli = "Anggota timmu sedang berat hati dan susah fokus, padahal tenggat sudah dekat."
    n "Anggota timmu sedang berat hati dan susah fokus, padahal tenggat sudah dekat."

    menu:
        "Anggota timmu sedang berat hati dan susah fokus, padahal tenggat sudah dekat."

        "Bantu pecah tugasnya jadi langkah kecil (T) agar tetap jalan sesuai tenggat (J).":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "Bantu pecah tugasnya jadi langkah kecil (T) agar tetap jalan sesuai tenggat (J)."
            $ last_answer = "Thinking & Judging"
            $ unchosen_choice_text = "Bebaskan dia rehat dulu (F), sisanya kita atur ulang nanti (P)."
            $ unchosen_answer = "Feeling & Perceiving"
            jump show_question_q_b_37_id_A

        "Bebaskan dia rehat dulu (F), sisanya kita atur ulang nanti (P).":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "Bebaskan dia rehat dulu (F), sisanya kita atur ulang nanti (P)."
            $ last_answer = "Feeling & Perceiving"
            $ unchosen_choice_text = "Bantu pecah tugasnya jadi langkah kecil (T) agar tetap jalan sesuai tenggat (J)."
            $ unchosen_answer = "Thinking & Judging"
            jump show_question_q_b_37_id_B


label show_question_q_b_37_id_A:
    $ user_journey_summary.append("Di situasi Anggota timmu sedang berat hati dan susah fokus, padahal tenggat sudah dekat., user memilih: Bantu pecah tugasnya jadi langkah kecil (T) agar tetap jalan sesuai tenggat (J)., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic
    return

label show_question_q_b_37_id_B:
    $ user_journey_summary.append("Di situasi Anggota timmu sedang berat hati dan susah fokus, padahal tenggat sudah dekat., user memilih: Bebaskan dia rehat dulu (F), sisanya kita atur ulang nanti (P)., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic
    return

label show_question_q_b_38_id:
    scene bg dapur with dissolve
    $ narasi_asli = "Kamu jadi juri lomba masak. Masakan temanmu gosong, padahal usahanya besar sekali."
    n "Kamu jadi juri lomba masak."
    n "Masakan temanmu gosong, padahal usahanya besar sekali."

    menu:
        "Kamu jadi juri lomba masak. Masakan temanmu gosong, padahal usahanya besar sekali."

        "Nilai apa adanya dari rasa (T), adil bagi semua peserta lain (J).":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "Nilai apa adanya dari rasa (T), adil bagi semua peserta lain (J)."
            $ last_answer = "Thinking & Judging"
            $ unchosen_choice_text = "Selipkan poin usaha (F), hargai proses kerasnya (P)."
            $ unchosen_answer = "Feeling & Perceiving"
            jump show_question_q_b_38_id_A

        "Selipkan poin usaha (F), hargai proses kerasnya (P).":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "Selipkan poin usaha (F), hargai proses kerasnya (P)."
            $ last_answer = "Feeling & Perceiving"
            $ unchosen_choice_text = "Nilai apa adanya dari rasa (T), adil bagi semua peserta lain (J)."
            $ unchosen_answer = "Thinking & Judging"
            jump show_question_q_b_38_id_B


label show_question_q_b_38_id_A:
    $ user_journey_summary.append("Di situasi Kamu jadi juri lomba masak. Masakan temanmu gosong, padahal usahanya besar sekali., user memilih: Nilai apa adanya dari rasa (T), adil bagi semua peserta lain (J)., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic
    return

label show_question_q_b_38_id_B:
    $ user_journey_summary.append("Di situasi Kamu jadi juri lomba masak. Masakan temanmu gosong, padahal usahanya besar sekali., user memilih: Selipkan poin usaha (F), hargai proses kerasnya (P)., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic
    return

label show_question_q_b_39_id:
    scene bg stasiun with dissolve
    $ narasi_asli = "Kamu petugas stasiun. Seorang turis salah jalur karena bingung membaca papan. Aturannya, ada denda."
    n "Kamu petugas stasiun."
    n "Seorang turis salah jalur karena bingung membaca papan."
    n "Aturannya, ada denda."

    menu:
        "Kamu petugas stasiun. Seorang turis salah jalur karena bingung membaca papan. Aturannya, ada denda."

        "Jalankan aturan (T), sama untuk setiap penumpang (J).":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "Jalankan aturan (T), sama untuk setiap penumpang (J)."
            $ last_answer = "Thinking & Judging"
            $ unchosen_choice_text = "Bantu keringankan (F), dia jelas tersesat, bukan sengaja melanggar (P)."
            $ unchosen_answer = "Feeling & Perceiving"
            jump show_question_q_b_39_id_A

        "Bantu keringankan (F), dia jelas tersesat, bukan sengaja melanggar (P).":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "Bantu keringankan (F), dia jelas tersesat, bukan sengaja melanggar (P)."
            $ last_answer = "Feeling & Perceiving"
            $ unchosen_choice_text = "Jalankan aturan (T), sama untuk setiap penumpang (J)."
            $ unchosen_answer = "Thinking & Judging"
            jump show_question_q_b_39_id_B


label show_question_q_b_39_id_A:
    $ user_journey_summary.append("Di situasi Kamu petugas stasiun. Seorang turis salah jalur karena bingung membaca papan. Aturannya, ada denda., user memilih: Jalankan aturan (T), sama untuk setiap penumpang (J)., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic
    return

label show_question_q_b_39_id_B:
    $ user_journey_summary.append("Di situasi Kamu petugas stasiun. Seorang turis salah jalur karena bingung membaca papan. Aturannya, ada denda., user memilih: Bantu keringankan (F), dia jelas tersesat, bukan sengaja melanggar (P)., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic
    return

label show_question_q_b_40_id:
    scene bg kantor with dissolve
    $ narasi_asli = "Kamu membuat jadwal piket baru, tapi ada teman yang protes karena jadwalnya bentrok."
    n "Kamu membuat jadwal piket baru, tapi ada teman yang protes karena jadwalnya bentrok."

    menu:
        "Kamu membuat jadwal piket baru, tapi ada teman yang protes karena jadwalnya bentrok."

        "Pertahankan sistemnya (T), sudah dihitung paling adil beban kerjanya (J).":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "Pertahankan sistemnya (T), sudah dihitung paling adil beban kerjanya (J)."
            $ last_answer = "Thinking & Judging"
            $ unchosen_choice_text = "Longgarkan, atur tukar jadwal (P) biar semua tetap nyaman (F)."
            $ unchosen_answer = "Feeling & Perceiving"
            jump show_question_q_b_40_id_A

        "Longgarkan, atur tukar jadwal (P) biar semua tetap nyaman (F).":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "Longgarkan, atur tukar jadwal (P) biar semua tetap nyaman (F)."
            $ last_answer = "Feeling & Perceiving"
            $ unchosen_choice_text = "Pertahankan sistemnya (T), sudah dihitung paling adil beban kerjanya (J)."
            $ unchosen_answer = "Thinking & Judging"
            jump show_question_q_b_40_id_B


label show_question_q_b_40_id_A:
    $ user_journey_summary.append("Di situasi Kamu membuat jadwal piket baru, tapi ada teman yang protes karena jadwalnya bentrok., user memilih: Pertahankan sistemnya (T), sudah dihitung paling adil beban kerjanya (J)., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic
    return

label show_question_q_b_40_id_B:
    $ user_journey_summary.append("Di situasi Kamu membuat jadwal piket baru, tapi ada teman yang protes karena jadwalnya bentrok., user memilih: Longgarkan, atur tukar jadwal (P) biar semua tetap nyaman (F)., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic
    return

label show_question_q_c_41_id:
    scene bg taman with dissolve
    $ narasi_asli = "Libur telah tiba. Teman-teman mengajakmu pergi jalan-jalan, tapi belum tahu pasti mau ke mana."
    n "Libur telah tiba."
    n "Teman-teman mengajakmu pergi jalan-jalan, tapi belum tahu pasti mau ke mana."

    menu:
        "Libur telah tiba. Teman-teman mengajakmu pergi jalan-jalan, tapi belum tahu pasti mau ke mana."

        "Pergi sendiri (I) mengunjungi museum sejarah untuk melihat artefak bersejarah (S).":
            $ IE -= 5
            $ SN -= 5
            $ user_choice_text = "Pergi sendiri (I) mengunjungi museum sejarah untuk melihat artefak bersejarah (S)."
            $ last_answer = "Introvert & Sensing"
            $ unchosen_choice_text = "Ikut rombongan (E) menjelajahi hutan mitos yang penuh misteri (N)."
            $ unchosen_answer = "Extrovert & Intuitive"
            jump show_question_q_c_41_id_A

        "Ikut rombongan (E) menjelajahi hutan mitos yang penuh misteri (N).":
            $ IE += 5
            $ SN += 5
            $ user_choice_text = "Ikut rombongan (E) menjelajahi hutan mitos yang penuh misteri (N)."
            $ last_answer = "Extrovert & Intuitive"
            $ unchosen_choice_text = "Pergi sendiri (I) mengunjungi museum sejarah untuk melihat artefak bersejarah (S)."
            $ unchosen_answer = "Introvert & Sensing"
            jump show_question_q_c_41_id_B


label show_question_q_c_41_id_A:
    $ user_journey_summary.append("Di situasi Libur telah tiba. Teman-teman mengajakmu pergi jalan-jalan, tapi belum tahu pasti mau ke mana., user memilih: Pergi sendiri (I) mengunjungi museum sejarah untuk melihat artefak bersejarah (S)., dengan poin MBTI: Introvert & Sensing")
    call ai_react_logic
    return

label show_question_q_c_41_id_B:
    $ user_journey_summary.append("Di situasi Libur telah tiba. Teman-teman mengajakmu pergi jalan-jalan, tapi belum tahu pasti mau ke mana., user memilih: Ikut rombongan (E) menjelajahi hutan mitos yang penuh misteri (N)., dengan poin MBTI: Extrovert & Intuitive")
    call ai_react_logic
    return

label show_question_q_c_42_id:
    scene bg kafe with dissolve
    $ narasi_asli = "Kamu menang lotre besar! Memenangkan sekantong koin emas."
    n "Kamu menang lotre besar!"
    n "Memenangkan sekantong koin emas."

    menu:
        "Kamu menang lotre besar! Memenangkan sekantong koin emas."

        "Simpan sendiri di brankas (I) sebagai aset fisik yang aman (S).":
            $ IE -= 5
            $ SN -= 5
            $ user_choice_text = "Simpan sendiri di brankas (I) sebagai aset fisik yang aman (S)."
            $ last_answer = "Introvert & Sensing"
            $ unchosen_choice_text = "Traktir semua orang (E) sambil memikirkan kekayaanmu yang semakin bertambah (N)."
            $ unchosen_answer = "Extrovert & Intuitive"
            jump show_question_q_c_42_id_A

        "Traktir semua orang (E) sambil memikirkan kekayaanmu yang semakin bertambah (N).":
            $ IE += 5
            $ SN += 5
            $ user_choice_text = "Traktir semua orang (E) sambil memikirkan kekayaanmu yang semakin bertambah (N)."
            $ last_answer = "Extrovert & Intuitive"
            $ unchosen_choice_text = "Simpan sendiri di brankas (I) sebagai aset fisik yang aman (S)."
            $ unchosen_answer = "Introvert & Sensing"
            jump show_question_q_c_42_id_B


label show_question_q_c_42_id_A:
    $ user_journey_summary.append("Di situasi Kamu menang lotre besar! Memenangkan sekantong koin emas., user memilih: Simpan sendiri di brankas (I) sebagai aset fisik yang aman (S)., dengan poin MBTI: Introvert & Sensing")
    call ai_react_logic
    return

label show_question_q_c_42_id_B:
    $ user_journey_summary.append("Di situasi Kamu menang lotre besar! Memenangkan sekantong koin emas., user memilih: Traktir semua orang (E) sambil memikirkan kekayaanmu yang semakin bertambah (N)., dengan poin MBTI: Extrovert & Intuitive")
    call ai_react_logic
    return

label show_question_q_c_43_id:
    scene bg room with dissolve
    $ narasi_asli = "Kamu melihat lukisan abstrak yang 'cuma coretan beberapa garis'."
    n "Kamu melihat lukisan abstrak yang 'cuma coretan beberapa garis'."

    menu:
        "Kamu melihat lukisan abstrak yang 'cuma coretan beberapa garis'."

        "Tanya orang lain (E), 'Ini gambar apa sih? Maksudnya apaan?' (S).":
            $ IE += 5
            $ SN -= 5
            $ user_choice_text = "Tanya orang lain (E), 'Ini gambar apa sih? Maksudnya apaan?' (S)."
            $ last_answer = "Extrovert & Sensing"
            $ unchosen_choice_text = "Diam (I) dan mencoba merasakan emosi pelukisnya (N)."
            $ unchosen_answer = "Introvert & Intuitive"
            jump show_question_q_c_43_id_A

        "Diam (I) dan mencoba merasakan emosi pelukisnya (N).":
            $ IE -= 5
            $ SN += 5
            $ user_choice_text = "Diam (I) dan mencoba merasakan emosi pelukisnya (N)."
            $ last_answer = "Introvert & Intuitive"
            $ unchosen_choice_text = "Tanya orang lain (E), 'Ini gambar apa sih? Maksudnya apaan?' (S)."
            $ unchosen_answer = "Extrovert & Sensing"
            jump show_question_q_c_43_id_B


label show_question_q_c_43_id_A:
    $ user_journey_summary.append("Di situasi Kamu melihat lukisan abstrak yang 'cuma coretan beberapa garis'., user memilih: Tanya orang lain (E), 'Ini gambar apa sih? Maksudnya apaan?' (S)., dengan poin MBTI: Extrovert & Sensing")
    call ai_react_logic
    return

label show_question_q_c_43_id_B:
    $ user_journey_summary.append("Di situasi Kamu melihat lukisan abstrak yang 'cuma coretan beberapa garis'., user memilih: Diam (I) dan mencoba merasakan emosi pelukisnya (N)., dengan poin MBTI: Introvert & Intuitive")
    call ai_react_logic
    return

label show_question_q_c_44_id:
    scene bg arcade with dissolve
    $ narasi_asli = "Temanmu minta diajari main game, yang jago banget kamu mainkan."
    n "Temanmu minta diajari main game, yang jago banget kamu mainkan."

    menu:
        "Temanmu minta diajari main game, yang jago banget kamu mainkan."

        "'Sini, tekan tombol maju, lalu lompat.' (S) Pandu dia langsung (E).":
            $ IE += 5
            $ SN -= 5
            $ user_choice_text = "'Sini, tekan tombol maju, lalu lompat.' (S) Pandu dia langsung (E)."
            $ last_answer = "Extrovert & Sensing"
            $ unchosen_choice_text = "'Kamu pahami dulu konsepnya.' (N) Biarkan dia belajar sendiri (I)."
            $ unchosen_answer = "Introvert & Intuitive"
            jump show_question_q_c_44_id_A

        "'Kamu pahami dulu konsepnya.' (N) Biarkan dia belajar sendiri (I).":
            $ IE -= 5
            $ SN += 5
            $ user_choice_text = "'Kamu pahami dulu konsepnya.' (N) Biarkan dia belajar sendiri (I)."
            $ last_answer = "Introvert & Intuitive"
            $ unchosen_choice_text = "'Sini, tekan tombol maju, lalu lompat.' (S) Pandu dia langsung (E)."
            $ unchosen_answer = "Extrovert & Sensing"
            jump show_question_q_c_44_id_B


label show_question_q_c_44_id_A:
    $ user_journey_summary.append("Di situasi Temanmu minta diajari main game, yang jago banget kamu mainkan., user memilih: 'Sini, tekan tombol maju, lalu lompat.' (S) Pandu dia langsung (E)., dengan poin MBTI: Extrovert & Sensing")
    call ai_react_logic
    return

label show_question_q_c_44_id_B:
    $ user_journey_summary.append("Di situasi Temanmu minta diajari main game, yang jago banget kamu mainkan., user memilih: 'Kamu pahami dulu konsepnya.' (N) Biarkan dia belajar sendiri (I)., dengan poin MBTI: Introvert & Intuitive")
    call ai_react_logic
    return

label show_question_q_c_45_id:
    scene bg abstrak with dissolve
    $ narasi_asli = "Kamu punya waktu luang 1 jam hari ini. Kamu mau ngapain?"
    n "Kamu punya waktu luang 1 jam hari ini."
    n "Kamu mau ngapain?"

    menu:
        "Kamu punya waktu luang 1 jam hari ini. Kamu mau ngapain?"

        "Olahraga atau beres-beres (S) bareng di rumah (E).":
            $ IE += 5
            $ SN -= 5
            $ user_choice_text = "Olahraga atau beres-beres (S) bareng di rumah (E)."
            $ last_answer = "Extrovert & Sensing"
            $ unchosen_choice_text = "Melakukan hal yang kamu suka, (I) sambil membayangkan apa yang bisa kamu lakukan di kemudian hari (N)."
            $ unchosen_answer = "Introvert & Intuitive"
            jump show_question_q_c_45_id_A

        "Melakukan hal yang kamu suka, (I) sambil membayangkan apa yang bisa kamu lakukan di kemudian hari (N).":
            $ IE -= 5
            $ SN += 5
            $ user_choice_text = "Melakukan hal yang kamu suka, (I) sambil membayangkan apa yang bisa kamu lakukan di kemudian hari (N)."
            $ last_answer = "Introvert & Intuitive"
            $ unchosen_choice_text = "Olahraga atau beres-beres (S) bareng di rumah (E)."
            $ unchosen_answer = "Extrovert & Sensing"
            jump show_question_q_c_45_id_B


label show_question_q_c_45_id_A:
    $ user_journey_summary.append("Di situasi Kamu punya waktu luang 1 jam hari ini. Kamu mau ngapain?, user memilih: Olahraga atau beres-beres (S) bareng di rumah (E)., dengan poin MBTI: Extrovert & Sensing")
    call ai_react_logic
    return

label show_question_q_c_45_id_B:
    $ user_journey_summary.append("Di situasi Kamu punya waktu luang 1 jam hari ini. Kamu mau ngapain?, user memilih: Melakukan hal yang kamu suka, (I) sambil membayangkan apa yang bisa kamu lakukan di kemudian hari (N)., dengan poin MBTI: Introvert & Intuitive")
    call ai_react_logic
    return

label show_question_q_c_46_id:
    scene bg room with dissolve
    $ narasi_asli = "Temanmu menangis karena baru saja putus cinta."
    n "Temanmu menangis karena baru saja putus cinta."

    menu:
        "Temanmu menangis karena baru saja putus cinta."

        "Bantu lihat faktanya (T) dan tawarkan langkah konkret untuk melangkah maju (S).":
            $ SN -= 5
            $ TF -= 5
            $ user_choice_text = "Bantu lihat faktanya (T) dan tawarkan langkah konkret untuk melangkah maju (S)."
            $ last_answer = "Sensing & Thinking"
            $ unchosen_choice_text = "Temani dulu (N) dan dengarkan perasaannya tanpa buru-buru menilai (F)."
            $ unchosen_answer = "Intuitive & Feeling"
            jump show_question_q_c_46_id_A

        "Temani dulu (N) dan dengarkan perasaannya tanpa buru-buru menilai (F).":
            $ SN += 5
            $ TF += 5
            $ user_choice_text = "Temani dulu (N) dan dengarkan perasaannya tanpa buru-buru menilai (F)."
            $ last_answer = "Intuitive & Feeling"
            $ unchosen_choice_text = "Bantu lihat faktanya (T) dan tawarkan langkah konkret untuk melangkah maju (S)."
            $ unchosen_answer = "Sensing & Thinking"
            jump show_question_q_c_46_id_B


label show_question_q_c_46_id_A:
    $ user_journey_summary.append("Di situasi Temanmu menangis karena baru saja putus cinta., user memilih: Bantu lihat faktanya (T) dan tawarkan langkah konkret untuk melangkah maju (S)., dengan poin MBTI: Sensing & Thinking")
    call ai_react_logic
    return

label show_question_q_c_46_id_B:
    $ user_journey_summary.append("Di situasi Temanmu menangis karena baru saja putus cinta., user memilih: Temani dulu (N) dan dengarkan perasaannya tanpa buru-buru menilai (F)., dengan poin MBTI: Intuitive & Feeling")
    call ai_react_logic
    return

label show_question_q_c_47_id:
    scene bg room with dissolve
    $ narasi_asli = "Film yang kalian tonton ending-nya gantung dan nggak jelas!"
    n "Film yang kalian tonton ending-nya gantung dan nggak jelas!"

    menu:
        "Film yang kalian tonton ending-nya gantung dan nggak jelas!"

        "'Ah..Jelek banget! (T) Banyak adegan yang nggak dijelaskan kaitannya! (S).'":
            $ SN -= 5
            $ TF -= 5
            $ user_choice_text = "'Ah..Jelek banget! (T) Banyak adegan yang nggak dijelaskan kaitannya! (S).'"
            $ last_answer = "Sensing & Thinking"
            $ unchosen_choice_text = "'Keren... (F) Maknanya dalam banget, soal harapan yang sirna (N).'"
            $ unchosen_answer = "Intuitive & Feeling"
            jump show_question_q_c_47_id_A

        "'Keren... (F) Maknanya dalam banget, soal harapan yang sirna (N).'":
            $ SN += 5
            $ TF += 5
            $ user_choice_text = "'Keren... (F) Maknanya dalam banget, soal harapan yang sirna (N).'"
            $ last_answer = "Intuitive & Feeling"
            $ unchosen_choice_text = "'Ah..Jelek banget! (T) Banyak adegan yang nggak dijelaskan kaitannya! (S).'"
            $ unchosen_answer = "Sensing & Thinking"
            jump show_question_q_c_47_id_B


label show_question_q_c_47_id_A:
    $ user_journey_summary.append("Di situasi Film yang kalian tonton ending-nya gantung dan nggak jelas!, user memilih: 'Ah..Jelek banget! (T) Banyak adegan yang nggak dijelaskan kaitannya! (S).', dengan poin MBTI: Sensing & Thinking")
    call ai_react_logic
    return

label show_question_q_c_47_id_B:
    $ user_journey_summary.append("Di situasi Film yang kalian tonton ending-nya gantung dan nggak jelas!, user memilih: 'Keren... (F) Maknanya dalam banget, soal harapan yang sirna (N).', dengan poin MBTI: Intuitive & Feeling")
    call ai_react_logic
    return

label show_question_q_c_48_id:
    scene bg kantor with dissolve
    $ narasi_asli = "Ada tawaran job dengan Gaji besar, tapi kamu belum tau apa kerjaannya. Orang tersebut juga cukup mencurigakan"
    n "Ada tawaran job dengan Gaji besar, tapi kamu belum tau apa kerjaannya."
    n "Orang tersebut juga cukup mencurigakan"

    menu:
        "Ada tawaran job dengan Gaji besar, tapi kamu belum tau apa kerjaannya. Orang tersebut juga cukup mencurigakan"

        "Tolak (F). 'Tawarannya belum jelas' (N) tidak yakin bakal dibawa kemana.":
            $ SN += 5
            $ TF += 5
            $ user_choice_text = "Tolak (F). 'Tawarannya belum jelas' (N) tidak yakin bakal dibawa kemana."
            $ last_answer = "Intuitive & Feeling"
            $ unchosen_choice_text = "Terima aja (T). Secara finansial (S) kita lagi butuh uangnya."
            $ unchosen_answer = "Sensing & Thinking"
            jump show_question_q_c_48_id_A

        "Terima aja (T). Secara finansial (S) kita lagi butuh uangnya.":
            $ SN -= 5
            $ TF -= 5
            $ user_choice_text = "Terima aja (T). Secara finansial (S) kita lagi butuh uangnya."
            $ last_answer = "Sensing & Thinking"
            $ unchosen_choice_text = "Tolak (F). 'Tawarannya belum jelas' (N) tidak yakin bakal dibawa kemana."
            $ unchosen_answer = "Intuitive & Feeling"
            jump show_question_q_c_48_id_B


label show_question_q_c_48_id_A:
    $ user_journey_summary.append("Di situasi Ada tawaran job dengan Gaji besar, tapi kamu belum tau apa kerjaannya. Orang tersebut juga cukup mencurigakan, user memilih: Tolak (F). 'Tawarannya belum jelas' (N) tidak yakin bakal dibawa kemana., dengan poin MBTI: Intuitive & Feeling")
    call ai_react_logic
    return

label show_question_q_c_48_id_B:
    $ user_journey_summary.append("Di situasi Ada tawaran job dengan Gaji besar, tapi kamu belum tau apa kerjaannya. Orang tersebut juga cukup mencurigakan, user memilih: Terima aja (T). Secara finansial (S) kita lagi butuh uangnya., dengan poin MBTI: Sensing & Thinking")
    call ai_react_logic
    return

label show_question_q_c_49_id:
    scene bg abstrak with dissolve
    $ narasi_asli = "Kamu harus memilih satu skill untuk dipelajari seumur hidup."
    n "Kamu harus memilih satu skill untuk dipelajari seumur hidup."

    menu:
        "Kamu harus memilih satu skill untuk dipelajari seumur hidup."

        "Skill teknis (S) yang berguna buat cari kerja (T).":
            $ SN -= 5
            $ TF -= 5
            $ user_choice_text = "Skill teknis (S) yang berguna buat cari kerja (T)."
            $ last_answer = "Sensing & Thinking"
            $ unchosen_choice_text = "Skill seni (N) yang bisa menyentuh hati orang (F)."
            $ unchosen_answer = "Intuitive & Feeling"
            jump show_question_q_c_49_id_A

        "Skill seni (N) yang bisa menyentuh hati orang (F).":
            $ SN += 5
            $ TF += 5
            $ user_choice_text = "Skill seni (N) yang bisa menyentuh hati orang (F)."
            $ last_answer = "Intuitive & Feeling"
            $ unchosen_choice_text = "Skill teknis (S) yang berguna buat cari kerja (T)."
            $ unchosen_answer = "Sensing & Thinking"
            jump show_question_q_c_49_id_B


label show_question_q_c_49_id_A:
    $ user_journey_summary.append("Di situasi Kamu harus memilih satu skill untuk dipelajari seumur hidup., user memilih: Skill teknis (S) yang berguna buat cari kerja (T)., dengan poin MBTI: Sensing & Thinking")
    call ai_react_logic
    return

label show_question_q_c_49_id_B:
    $ user_journey_summary.append("Di situasi Kamu harus memilih satu skill untuk dipelajari seumur hidup., user memilih: Skill seni (N) yang bisa menyentuh hati orang (F)., dengan poin MBTI: Intuitive & Feeling")
    call ai_react_logic
    return

label show_question_q_c_50_id:
    scene bg kafe with dissolve
    $ narasi_asli = "Temanmu debat soal fakta sains tapi datanya salah semua."
    n "Temanmu debat soal fakta sains tapi datanya salah semua."

    menu:
        "Temanmu debat soal fakta sains tapi datanya salah semua."

        "Koreksi dia (T). Tunjukkan data asli (S) agar dia tidak membuat dirinya malu.":
            $ SN -= 5
            $ TF -= 5
            $ user_choice_text = "Koreksi dia (T). Tunjukkan data asli (S) agar dia tidak membuat dirinya malu."
            $ last_answer = "Sensing & Thinking"
            $ unchosen_choice_text = "Biarkan saja (F). Nanti dia sadar sendiri (N), daripada ribut di sini."
            $ unchosen_answer = "Intuitive & Feeling"
            jump show_question_q_c_50_id_A

        "Biarkan saja (F). Nanti dia sadar sendiri (N), daripada ribut di sini.":
            $ SN += 5
            $ TF += 5
            $ user_choice_text = "Biarkan saja (F). Nanti dia sadar sendiri (N), daripada ribut di sini."
            $ last_answer = "Intuitive & Feeling"
            $ unchosen_choice_text = "Koreksi dia (T). Tunjukkan data asli (S) agar dia tidak membuat dirinya malu."
            $ unchosen_answer = "Sensing & Thinking"
            jump show_question_q_c_50_id_B


label show_question_q_c_50_id_A:
    $ user_journey_summary.append("Di situasi Temanmu debat soal fakta sains tapi datanya salah semua., user memilih: Koreksi dia (T). Tunjukkan data asli (S) agar dia tidak membuat dirinya malu., dengan poin MBTI: Sensing & Thinking")
    call ai_react_logic
    return

label show_question_q_c_50_id_B:
    $ user_journey_summary.append("Di situasi Temanmu debat soal fakta sains tapi datanya salah semua., user memilih: Biarkan saja (F). Nanti dia sadar sendiri (N), daripada ribut di sini., dengan poin MBTI: Intuitive & Feeling")
    call ai_react_logic
    return

label show_question_q_c_51_id:
    scene bg stasiun with dissolve
    $ narasi_asli = "(Hilang!) Tiket keretamu hilang! Kereta berangkat 5 menit lagi."
    n "(Hilang!) Tiket keretamu hilang!"
    n "Kereta berangkat 5 menit lagi."

    menu:
        "(Hilang!) Tiket keretamu hilang! Kereta berangkat 5 menit lagi."

        "Cek saku, tas, lantai secara urut (S). Jangan panik, coba ingat kembali (J).":
            $ SN -= 5
            $ JP -= 5
            $ user_choice_text = "Cek saku, tas, lantai secara urut (S). Jangan panik, coba ingat kembali (J)."
            $ last_answer = "Sensing & Judging"
            $ unchosen_choice_text = "Cari tiket di tempat yang mungkin terselip (P). Bisa jadi jatuh di jalan(N)."
            $ unchosen_answer = "Intuitive & Perceiving"
            jump show_question_q_c_51_id_A

        "Cari tiket di tempat yang mungkin terselip (P). Bisa jadi jatuh di jalan(N).":
            $ SN += 5
            $ JP += 5
            $ user_choice_text = "Cari tiket di tempat yang mungkin terselip (P). Bisa jadi jatuh di jalan(N)."
            $ last_answer = "Intuitive & Perceiving"
            $ unchosen_choice_text = "Cek saku, tas, lantai secara urut (S). Jangan panik, coba ingat kembali (J)."
            $ unchosen_answer = "Sensing & Judging"
            jump show_question_q_c_51_id_B


label show_question_q_c_51_id_A:
    $ user_journey_summary.append("Di situasi (Hilang!) Tiket keretamu hilang! Kereta berangkat 5 menit lagi., user memilih: Cek saku, tas, lantai secara urut (S). Jangan panik, coba ingat kembali (J)., dengan poin MBTI: Sensing & Judging")
    call ai_react_logic
    return

label show_question_q_c_51_id_B:
    $ user_journey_summary.append("Di situasi (Hilang!) Tiket keretamu hilang! Kereta berangkat 5 menit lagi., user memilih: Cari tiket di tempat yang mungkin terselip (P). Bisa jadi jatuh di jalan(N)., dengan poin MBTI: Intuitive & Perceiving")
    call ai_react_logic
    return

label show_question_q_c_52_id:
    scene bg dapur with dissolve
    $ narasi_asli = "Kamu lapar, tapi di kulkas cuma ada telur, selai, dan daging."
    n "Kamu lapar, tapi di kulkas cuma ada telur, selai, dan daging."

    menu:
        "Kamu lapar, tapi di kulkas cuma ada telur, selai, dan daging."

        "Masak telur dadar aja (S). Pasti enak dan sudah jelas rasanya (J).":
            $ SN -= 5
            $ JP -= 5
            $ user_choice_text = "Masak telur dadar aja (S). Pasti enak dan sudah jelas rasanya (J)."
            $ last_answer = "Sensing & Judging"
            $ unchosen_choice_text = "Campur semuanya! (N) Siapa tahu jadi masterpiece baru (P)."
            $ unchosen_answer = "Intuitive & Perceiving"
            jump show_question_q_c_52_id_A

        "Campur semuanya! (N) Siapa tahu jadi masterpiece baru (P).":
            $ SN += 5
            $ JP += 5
            $ user_choice_text = "Campur semuanya! (N) Siapa tahu jadi masterpiece baru (P)."
            $ last_answer = "Intuitive & Perceiving"
            $ unchosen_choice_text = "Masak telur dadar aja (S). Pasti enak dan sudah jelas rasanya (J)."
            $ unchosen_answer = "Sensing & Judging"
            jump show_question_q_c_52_id_B


label show_question_q_c_52_id_A:
    $ user_journey_summary.append("Di situasi Kamu lapar, tapi di kulkas cuma ada telur, selai, dan daging., user memilih: Masak telur dadar aja (S). Pasti enak dan sudah jelas rasanya (J)., dengan poin MBTI: Sensing & Judging")
    call ai_react_logic
    return

label show_question_q_c_52_id_B:
    $ user_journey_summary.append("Di situasi Kamu lapar, tapi di kulkas cuma ada telur, selai, dan daging., user memilih: Campur semuanya! (N) Siapa tahu jadi masterpiece baru (P)., dengan poin MBTI: Intuitive & Perceiving")
    call ai_react_logic
    return

label show_question_q_c_53_id:
    scene bg room with dissolve
    $ narasi_asli = "Kamu ada ujian besok, tapi kamu baru ingat 1 hari sebelum hari-H"
    n "Kamu ada ujian besok, tapi kamu baru ingat 1 hari sebelum hari-H"

    menu:
        "Kamu ada ujian besok, tapi kamu baru ingat 1 hari sebelum hari-H"

        "Baca rangkuman bab (S) sesuai apa yang mungkin keluar di ujian (J).":
            $ SN -= 5
            $ JP -= 5
            $ user_choice_text = "Baca rangkuman bab (S) sesuai apa yang mungkin keluar di ujian (J)."
            $ last_answer = "Sensing & Judging"
            $ unchosen_choice_text = "Baca bagian yang paling kamu pahami saja (N), sisanya bisa dipikir saat ujian (P)."
            $ unchosen_answer = "Intuitive & Perceiving"
            jump show_question_q_c_53_id_A

        "Baca bagian yang paling kamu pahami saja (N), sisanya bisa dipikir saat ujian (P).":
            $ SN += 5
            $ JP += 5
            $ user_choice_text = "Baca bagian yang paling kamu pahami saja (N), sisanya bisa dipikir saat ujian (P)."
            $ last_answer = "Intuitive & Perceiving"
            $ unchosen_choice_text = "Baca rangkuman bab (S) sesuai apa yang mungkin keluar di ujian (J)."
            $ unchosen_answer = "Sensing & Judging"
            jump show_question_q_c_53_id_B


label show_question_q_c_53_id_A:
    $ user_journey_summary.append("Di situasi Kamu ada ujian besok, tapi kamu baru ingat 1 hari sebelum hari-H, user memilih: Baca rangkuman bab (S) sesuai apa yang mungkin keluar di ujian (J)., dengan poin MBTI: Sensing & Judging")
    call ai_react_logic
    return

label show_question_q_c_53_id_B:
    $ user_journey_summary.append("Di situasi Kamu ada ujian besok, tapi kamu baru ingat 1 hari sebelum hari-H, user memilih: Baca bagian yang paling kamu pahami saja (N), sisanya bisa dipikir saat ujian (P)., dengan poin MBTI: Intuitive & Perceiving")
    call ai_react_logic
    return

label show_question_q_c_54_id:
    scene bg kantor with dissolve
    $ narasi_asli = "Bos minta kamu kerjakan proyek 'Rahasia' tanpa petunjuk jelas."
    n "Bos minta kamu kerjakan proyek 'Rahasia' tanpa petunjuk jelas."

    menu:
        "Bos minta kamu kerjakan proyek 'Rahasia' tanpa petunjuk jelas."

        "Tolak halus. 'Saya butuh detail (S) dan deadline yang jelas (J).'":
            $ SN -= 5
            $ JP -= 5
            $ user_choice_text = "Tolak halus. 'Saya butuh detail (S) dan deadline yang jelas (J).'"
            $ last_answer = "Sensing & Judging"
            $ unchosen_choice_text = "Terima! 'Siap, saya akan improvisasi (N) sambil jalan (P).'"
            $ unchosen_answer = "Intuitive & Perceiving"
            jump show_question_q_c_54_id_A

        "Terima! 'Siap, saya akan improvisasi (N) sambil jalan (P).'":
            $ SN += 5
            $ JP += 5
            $ user_choice_text = "Terima! 'Siap, saya akan improvisasi (N) sambil jalan (P).'"
            $ last_answer = "Intuitive & Perceiving"
            $ unchosen_choice_text = "Tolak halus. 'Saya butuh detail (S) dan deadline yang jelas (J).'"
            $ unchosen_answer = "Sensing & Judging"
            jump show_question_q_c_54_id_B


label show_question_q_c_54_id_A:
    $ user_journey_summary.append("Di situasi Bos minta kamu kerjakan proyek 'Rahasia' tanpa petunjuk jelas., user memilih: Tolak halus. 'Saya butuh detail (S) dan deadline yang jelas (J).', dengan poin MBTI: Sensing & Judging")
    call ai_react_logic
    return

label show_question_q_c_54_id_B:
    $ user_journey_summary.append("Di situasi Bos minta kamu kerjakan proyek 'Rahasia' tanpa petunjuk jelas., user memilih: Terima! 'Siap, saya akan improvisasi (N) sambil jalan (P).', dengan poin MBTI: Intuitive & Perceiving")
    call ai_react_logic
    return

label show_question_q_c_55_id:
    scene bg stasiun with dissolve
    $ narasi_asli = "Kamu mau pindah kota, tapi barangmu kebanyakan!"
    n "Kamu mau pindah kota, tapi barangmu kebanyakan!"

    menu:
        "Kamu mau pindah kota, tapi barangmu kebanyakan!"

        "Sortir barang (S). Buang yang menurutmu kurang penting (J).":
            $ SN -= 5
            $ JP -= 5
            $ user_choice_text = "Sortir barang (S). Buang yang menurutmu kurang penting (J)."
            $ last_answer = "Sensing & Judging"
            $ unchosen_choice_text = "'Kita gak tahu, mungkin butuh barang ini di kemudian hari, jadi bawa semua! (N)'. Nanti semua bisa diatur lagi di sana (P)."
            $ unchosen_answer = "Intuitive & Perceiving"
            jump show_question_q_c_55_id_A

        "'Kita gak tahu, mungkin butuh barang ini di kemudian hari, jadi bawa semua! (N)'. Nanti semua bisa diatur lagi di sana (P).":
            $ SN += 5
            $ JP += 5
            $ user_choice_text = "'Kita gak tahu, mungkin butuh barang ini di kemudian hari, jadi bawa semua! (N)'. Nanti semua bisa diatur lagi di sana (P)."
            $ last_answer = "Intuitive & Perceiving"
            $ unchosen_choice_text = "Sortir barang (S). Buang yang menurutmu kurang penting (J)."
            $ unchosen_answer = "Sensing & Judging"
            jump show_question_q_c_55_id_B


label show_question_q_c_55_id_A:
    $ user_journey_summary.append("Di situasi Kamu mau pindah kota, tapi barangmu kebanyakan!, user memilih: Sortir barang (S). Buang yang menurutmu kurang penting (J)., dengan poin MBTI: Sensing & Judging")
    call ai_react_logic
    return

label show_question_q_c_55_id_B:
    $ user_journey_summary.append("Di situasi Kamu mau pindah kota, tapi barangmu kebanyakan!, user memilih: 'Kita gak tahu, mungkin butuh barang ini di kemudian hari, jadi bawa semua! (N)'. Nanti semua bisa diatur lagi di sana (P)., dengan poin MBTI: Intuitive & Perceiving")
    call ai_react_logic
    return

label show_question_q_c_56_id:
    scene bg room with dissolve
    $ narasi_asli = "Adikmu tak sengaja memecahkan vas kesayangan ibu. Dia ketakutan."
    n "Adikmu tak sengaja memecahkan vas kesayangan ibu."
    n "Dia ketakutan."

    menu:
        "Adikmu tak sengaja memecahkan vas kesayangan ibu. Dia ketakutan."

        "Dorong dia jujur bercerita ke ibu (J) dan hadapi dengan tenang (T).":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "Dorong dia jujur bercerita ke ibu (J) dan hadapi dengan tenang (T)."
            $ last_answer = "Thinking & Judging"
            $ unchosen_choice_text = "Temani dia bicara ke ibu (P), tekankan bahwa itu murni kecelakaan (F)."
            $ unchosen_answer = "Feeling & Perceiving"
            jump show_question_q_c_56_id_A

        "Temani dia bicara ke ibu (P), tekankan bahwa itu murni kecelakaan (F).":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "Temani dia bicara ke ibu (P), tekankan bahwa itu murni kecelakaan (F)."
            $ last_answer = "Feeling & Perceiving"
            $ unchosen_choice_text = "Dorong dia jujur bercerita ke ibu (J) dan hadapi dengan tenang (T)."
            $ unchosen_answer = "Thinking & Judging"
            jump show_question_q_c_56_id_B


label show_question_q_c_56_id_A:
    $ user_journey_summary.append("Di situasi Adikmu tak sengaja memecahkan vas kesayangan ibu. Dia ketakutan., user memilih: Dorong dia jujur bercerita ke ibu (J) dan hadapi dengan tenang (T)., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic
    return

label show_question_q_c_56_id_B:
    $ user_journey_summary.append("Di situasi Adikmu tak sengaja memecahkan vas kesayangan ibu. Dia ketakutan., user memilih: Temani dia bicara ke ibu (P), tekankan bahwa itu murni kecelakaan (F)., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic
    return

label show_question_q_c_57_id:
    scene bg kafe with dissolve
    $ narasi_asli = "Kamu punya ide bisnis aneh tapi inovatif. Kapan kamu mau mulai mewujudkannya?"
    n "Kamu punya ide bisnis aneh tapi inovatif."
    n "Kapan kamu mau mulai mewujudkannya?"

    menu:
        "Kamu punya ide bisnis aneh tapi inovatif. Kapan kamu mau mulai mewujudkannya?"

        "Nanti, setelah analisis untung-rugi (T) selesai 100%% (J).":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "Nanti, setelah analisis untung-rugi (T) selesai 100%% (J)."
            $ last_answer = "Thinking & Judging"
            $ unchosen_choice_text = "Sekarang! (P) Yang penting banyak orang suka idenya (F)."
            $ unchosen_answer = "Feeling & Perceiving"
            jump show_question_q_c_57_id_A

        "Sekarang! (P) Yang penting banyak orang suka idenya (F).":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "Sekarang! (P) Yang penting banyak orang suka idenya (F)."
            $ last_answer = "Feeling & Perceiving"
            $ unchosen_choice_text = "Nanti, setelah analisis untung-rugi (T) selesai 100%% (J)."
            $ unchosen_answer = "Thinking & Judging"
            jump show_question_q_c_57_id_B


label show_question_q_c_57_id_A:
    $ user_journey_summary.append("Di situasi Kamu punya ide bisnis aneh tapi inovatif. Kapan kamu mau mulai mewujudkannya?, user memilih: Nanti, setelah analisis untung-rugi (T) selesai 100%% (J)., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic
    return

label show_question_q_c_57_id_B:
    $ user_journey_summary.append("Di situasi Kamu punya ide bisnis aneh tapi inovatif. Kapan kamu mau mulai mewujudkannya?, user memilih: Sekarang! (P) Yang penting banyak orang suka idenya (F)., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic
    return

label show_question_q_c_58_id:
    scene bg kantor with dissolve
    $ narasi_asli = "Tim olahragamu kalah terus. Sebagai kapten, apa yang kamu katakan?"
    n "Tim olahragamu kalah terus."
    n "Sebagai kapten, apa yang kamu katakan?"

    menu:
        "Tim olahragamu kalah terus. Sebagai kapten, apa yang kamu katakan?"

        "Tambah latihan terjadwal (J), fokus perbaiki hal yang terukur (T).":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "Tambah latihan terjadwal (J), fokus perbaiki hal yang terukur (T)."
            $ last_answer = "Thinking & Judging"
            $ unchosen_choice_text = "Santai dulu, guys (P), jaga semangat biar kita tetap solid bermain bareng (F)."
            $ unchosen_answer = "Feeling & Perceiving"
            jump show_question_q_c_58_id_A

        "Santai dulu, guys (P), jaga semangat biar kita tetap solid bermain bareng (F).":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "Santai dulu, guys (P), jaga semangat biar kita tetap solid bermain bareng (F)."
            $ last_answer = "Feeling & Perceiving"
            $ unchosen_choice_text = "Tambah latihan terjadwal (J), fokus perbaiki hal yang terukur (T)."
            $ unchosen_answer = "Thinking & Judging"
            jump show_question_q_c_58_id_B


label show_question_q_c_58_id_A:
    $ user_journey_summary.append("Di situasi Tim olahragamu kalah terus. Sebagai kapten, apa yang kamu katakan?, user memilih: Tambah latihan terjadwal (J), fokus perbaiki hal yang terukur (T)., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic
    return

label show_question_q_c_58_id_B:
    $ user_journey_summary.append("Di situasi Tim olahragamu kalah terus. Sebagai kapten, apa yang kamu katakan?, user memilih: Santai dulu, guys (P), jaga semangat biar kita tetap solid bermain bareng (F)., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic
    return

label show_question_q_c_59_id:
    scene bg abstrak with dissolve
    $ narasi_asli = "Kamu menemukan Senjata Kuno dalam eksplorasi. Apa yang jadi perhatianmu?"
    n "Kamu menemukan Senjata Kuno dalam eksplorasi."
    n "Apa yang jadi perhatianmu?"

    menu:
        "Kamu menemukan Senjata Kuno dalam eksplorasi. Apa yang jadi perhatianmu?"

        "Kekuatannya (T) dan kondisinya yang masih utuh (J).":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "Kekuatannya (T) dan kondisinya yang masih utuh (J)."
            $ last_answer = "Thinking & Judging"
            $ unchosen_choice_text = "Cerita legendanya (F) dan misteri siapa pemiliknya dulu (P)."
            $ unchosen_answer = "Feeling & Perceiving"
            jump show_question_q_c_59_id_A

        "Cerita legendanya (F) dan misteri siapa pemiliknya dulu (P).":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "Cerita legendanya (F) dan misteri siapa pemiliknya dulu (P)."
            $ last_answer = "Feeling & Perceiving"
            $ unchosen_choice_text = "Kekuatannya (T) dan kondisinya yang masih utuh (J)."
            $ unchosen_answer = "Thinking & Judging"
            jump show_question_q_c_59_id_B


label show_question_q_c_59_id_A:
    $ user_journey_summary.append("Di situasi Kamu menemukan Senjata Kuno dalam eksplorasi. Apa yang jadi perhatianmu?, user memilih: Kekuatannya (T) dan kondisinya yang masih utuh (J)., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic
    return

label show_question_q_c_59_id_B:
    $ user_journey_summary.append("Di situasi Kamu menemukan Senjata Kuno dalam eksplorasi. Apa yang jadi perhatianmu?, user memilih: Cerita legendanya (F) dan misteri siapa pemiliknya dulu (P)., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic
    return

label show_question_q_c_60_id:
    scene bg kantor with dissolve
    $ narasi_asli = "Ada aturan kantor baru yang menyusahkan karyawan."
    n "Ada aturan kantor baru yang menyusahkan karyawan."

    menu:
        "Ada aturan kantor baru yang menyusahkan karyawan."

        "Ajukan revisi resmi (J). Tunjukkan poin yang tidak efisien (T).":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "Ajukan revisi resmi (J). Tunjukkan poin yang tidak efisien (T)."
            $ last_answer = "Thinking & Judging"
            $ unchosen_choice_text = "Bikin petisi secara emosional (F). Minta kelonggaran aturan (P)."
            $ unchosen_answer = "Feeling & Perceiving"
            jump show_question_q_c_60_id_A

        "Bikin petisi secara emosional (F). Minta kelonggaran aturan (P).":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "Bikin petisi secara emosional (F). Minta kelonggaran aturan (P)."
            $ last_answer = "Feeling & Perceiving"
            $ unchosen_choice_text = "Ajukan revisi resmi (J). Tunjukkan poin yang tidak efisien (T)."
            $ unchosen_answer = "Thinking & Judging"
            jump show_question_q_c_60_id_B


label show_question_q_c_60_id_A:
    $ user_journey_summary.append("Di situasi Ada aturan kantor baru yang menyusahkan karyawan., user memilih: Ajukan revisi resmi (J). Tunjukkan poin yang tidak efisien (T)., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic
    return

label show_question_q_c_60_id_B:
    $ user_journey_summary.append("Di situasi Ada aturan kantor baru yang menyusahkan karyawan., user memilih: Bikin petisi secara emosional (F). Minta kelonggaran aturan (P)., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic
    return

# ================= BAHASA: EN =================

label show_question_q_a_01_en:
    scene bg taman with dissolve
    $ narasi_asli = "(Rumble...) Oh, so tired after walking around today! Your energy is depleted and you are hungry. What does your body need?"
    n "(Rumble...) Oh, so tired after walking around today!"
    n "Your energy is depleted and you are hungry."
    n "What does your body need?"

    menu:
        "(Rumble...) Oh, so tired after walking around today! Your energy is depleted and you are hungry. What does your body need?"

        "Go home alone (I) and eat nutritious food to recover physically (S).":
            $ IE -= 5
            $ SN -= 5
            $ user_choice_text = "Go home alone (I) and eat nutritious food to recover physically (S)."
            $ last_answer = "Introvert & Sensing"
            $ unchosen_choice_text = "Gather with friends and talk (E) about the idea for the next trip (N)."
            $ unchosen_answer = "Extrovert & Intuitive"
            jump show_question_q_a_01_en_A

        "Gather with friends and talk (E) about the idea for the next trip (N).":
            $ IE += 5
            $ SN += 5
            $ user_choice_text = "Gather with friends and talk (E) about the idea for the next trip (N)."
            $ last_answer = "Extrovert & Intuitive"
            $ unchosen_choice_text = "Go home alone (I) and eat nutritious food to recover physically (S)."
            $ unchosen_answer = "Introvert & Sensing"
            jump show_question_q_a_01_en_B


label show_question_q_a_01_en_A:
    $ user_journey_summary.append("Di situasi (Rumble...) Oh, so tired after walking around today! Your energy is depleted and you are hungry. What does your body need?, user memilih: Go home alone (I) and eat nutritious food to recover physically (S)., dengan poin MBTI: Introvert & Sensing")
    call ai_react_logic
    return

label show_question_q_a_01_en_B:
    $ user_journey_summary.append("Di situasi (Rumble...) Oh, so tired after walking around today! Your energy is depleted and you are hungry. What does your body need?, user memilih: Gather with friends and talk (E) about the idea for the next trip (N)., dengan poin MBTI: Extrovert & Intuitive")
    call ai_react_logic
    return

label show_question_q_a_02_en:
    scene bg kafe with dissolve
    $ narasi_asli = "(Ring!) The cafe door opens! A cool, mysterious figure enters. What is the first thing that catches your attention?"
    n "(Ring!) The cafe door opens!"
    n "A cool, mysterious figure enters."
    n "What is the first thing that catches your attention?"

    menu:
        "(Ring!) The cafe door opens! A cool, mysterious figure enters. What is the first thing that catches your attention?"

        "Observe them from your seat (I), while monitoring their movements (S).":
            $ IE -= 5
            $ SN -= 5
            $ user_choice_text = "Observe them from your seat (I), while monitoring their movements (S)."
            $ last_answer = "Introvert & Sensing"
            $ unchosen_choice_text = "Immediately greet them (E), and ask where they are going with such an outfit (N)."
            $ unchosen_answer = "Extrovert & Intuitive"
            jump show_question_q_a_02_en_A

        "Immediately greet them (E), and ask where they are going with such an outfit (N).":
            $ IE += 5
            $ SN += 5
            $ user_choice_text = "Immediately greet them (E), and ask where they are going with such an outfit (N)."
            $ last_answer = "Extrovert & Intuitive"
            $ unchosen_choice_text = "Observe them from your seat (I), while monitoring their movements (S)."
            $ unchosen_answer = "Introvert & Sensing"
            jump show_question_q_a_02_en_B


label show_question_q_a_02_en_A:
    $ user_journey_summary.append("Di situasi (Ring!) The cafe door opens! A cool, mysterious figure enters. What is the first thing that catches your attention?, user memilih: Observe them from your seat (I), while monitoring their movements (S)., dengan poin MBTI: Introvert & Sensing")
    call ai_react_logic
    return

label show_question_q_a_02_en_B:
    $ user_journey_summary.append("Di situasi (Ring!) The cafe door opens! A cool, mysterious figure enters. What is the first thing that catches your attention?, user memilih: Immediately greet them (E), and ask where they are going with such an outfit (N)., dengan poin MBTI: Extrovert & Intuitive")
    call ai_react_logic
    return

label show_question_q_a_03_en:
    scene bg kantor with dissolve
    $ narasi_asli = "(Thud!) The boss gives you a mountain-high stack of jobs! Impossible to finish alone today."
    n "(Thud!) The boss gives you a mountain-high stack of jobs!"
    n "Impossible to finish alone today."

    menu:
        "(Thud!) The boss gives you a mountain-high stack of jobs! Impossible to finish alone today."

        "Call the whole team (E) to divide the physical tasks (S) right now.":
            $ IE += 5
            $ SN -= 5
            $ user_choice_text = "Call the whole team (E) to divide the physical tasks (S) right now."
            $ last_answer = "Extrovert & Sensing"
            $ unchosen_choice_text = "Call a close colleague (I) to try out the assistance program you just developed (N)."
            $ unchosen_answer = "Introvert & Intuitive"
            jump show_question_q_a_03_en_A

        "Call a close colleague (I) to try out the assistance program you just developed (N).":
            $ IE -= 5
            $ SN += 5
            $ user_choice_text = "Call a close colleague (I) to try out the assistance program you just developed (N)."
            $ last_answer = "Introvert & Intuitive"
            $ unchosen_choice_text = "Call the whole team (E) to divide the physical tasks (S) right now."
            $ unchosen_answer = "Extrovert & Sensing"
            jump show_question_q_a_03_en_B


label show_question_q_a_03_en_A:
    $ user_journey_summary.append("Di situasi (Thud!) The boss gives you a mountain-high stack of jobs! Impossible to finish alone today., user memilih: Call the whole team (E) to divide the physical tasks (S) right now., dengan poin MBTI: Extrovert & Sensing")
    call ai_react_logic
    return

label show_question_q_a_03_en_B:
    $ user_journey_summary.append("Di situasi (Thud!) The boss gives you a mountain-high stack of jobs! Impossible to finish alone today., user memilih: Call a close colleague (I) to try out the assistance program you just developed (N)., dengan poin MBTI: Introvert & Intuitive")
    call ai_react_logic
    return

label show_question_q_a_04_en:
    scene bg dapur with dissolve
    $ narasi_asli = "(Oh no!) You want to cook a special meal, but one main ingredient is gone—you forgot to buy it yesterday."
    n "(Oh no!) You want to cook a special meal, but one main ingredient is gone—you forgot to buy it yesterday."

    menu:
        "(Oh no!) You want to cook a special meal, but one main ingredient is gone—you forgot to buy it yesterday."

        "Contact and ask a friend (E) to ask for the missing raw ingredient (S).":
            $ IE += 5
            $ SN -= 5
            $ user_choice_text = "Contact and ask a friend (E) to ask for the missing raw ingredient (S)."
            $ last_answer = "Extrovert & Sensing"
            $ unchosen_choice_text = "Stay in the kitchen (I) and try experimenting (N) by replacing it with another ingredient."
            $ unchosen_answer = "Introvert & Intuitive"
            jump show_question_q_a_04_en_A

        "Stay in the kitchen (I) and try experimenting (N) by replacing it with another ingredient.":
            $ IE -= 5
            $ SN += 5
            $ user_choice_text = "Stay in the kitchen (I) and try experimenting (N) by replacing it with another ingredient."
            $ last_answer = "Introvert & Intuitive"
            $ unchosen_choice_text = "Contact and ask a friend (E) to ask for the missing raw ingredient (S)."
            $ unchosen_answer = "Extrovert & Sensing"
            jump show_question_q_a_04_en_B


label show_question_q_a_04_en_A:
    $ user_journey_summary.append("Di situasi (Oh no!) You want to cook a special meal, but one main ingredient is gone—you forgot to buy it yesterday., user memilih: Contact and ask a friend (E) to ask for the missing raw ingredient (S)., dengan poin MBTI: Extrovert & Sensing")
    call ai_react_logic
    return

label show_question_q_a_04_en_B:
    $ user_journey_summary.append("Di situasi (Oh no!) You want to cook a special meal, but one main ingredient is gone—you forgot to buy it yesterday., user memilih: Stay in the kitchen (I) and try experimenting (N) by replacing it with another ingredient., dengan poin MBTI: Introvert & Intuitive")
    call ai_react_logic
    return

label show_question_q_a_05_en:
    scene bg room with dissolve
    $ narasi_asli = "There is a 'Hot News!' poster that causes an uproar in the whole village! Everyone is talking about it."
    n "There is a 'Hot News!' poster that causes an uproar in the whole village!"
    n "Everyone is talking about it."

    menu:
        "There is a 'Hot News!' poster that causes an uproar in the whole village! Everyone is talking about it."

        "Join the comments with other residents (E) and look for evidence (S) of the incident.":
            $ IE += 5
            $ SN -= 5
            $ user_choice_text = "Join the comments with other residents (E) and look for evidence (S) of the incident."
            $ last_answer = "Extrovert & Sensing"
            $ unchosen_choice_text = "Read and observe (I), try to imagine what really happened (N)."
            $ unchosen_answer = "Introvert & Intuitive"
            jump show_question_q_a_05_en_A

        "Read and observe (I), try to imagine what really happened (N).":
            $ IE -= 5
            $ SN += 5
            $ user_choice_text = "Read and observe (I), try to imagine what really happened (N)."
            $ last_answer = "Introvert & Intuitive"
            $ unchosen_choice_text = "Join the comments with other residents (E) and look for evidence (S) of the incident."
            $ unchosen_answer = "Extrovert & Sensing"
            jump show_question_q_a_05_en_B


label show_question_q_a_05_en_A:
    $ user_journey_summary.append("Di situasi There is a 'Hot News!' poster that causes an uproar in the whole village! Everyone is talking about it., user memilih: Join the comments with other residents (E) and look for evidence (S) of the incident., dengan poin MBTI: Extrovert & Sensing")
    call ai_react_logic
    return

label show_question_q_a_05_en_B:
    $ user_journey_summary.append("Di situasi There is a 'Hot News!' poster that causes an uproar in the whole village! Everyone is talking about it., user memilih: Read and observe (I), try to imagine what really happened (N)., dengan poin MBTI: Introvert & Intuitive")
    call ai_react_logic
    return

label show_question_q_a_06_en:
    scene bg kantor with dissolve
    $ narasi_asli = "A teammate accidentally lost an important company item. He is panicking."
    n "A teammate accidentally lost an important company item."
    n "He is panicking."

    menu:
        "A teammate accidentally lost an important company item. He is panicking."

        "Talk it out in front of the team (E) to map a clear fix (T).":
            $ IE += 5
            $ TF -= 5
            $ user_choice_text = "Talk it out in front of the team (E) to map a clear fix (T)."
            $ last_answer = "Extrovert & Thinking"
            $ unchosen_choice_text = "Pull him aside privately (I) and calm his nerves first (F)."
            $ unchosen_answer = "Introvert & Feeling"
            jump show_question_q_a_06_en_A

        "Pull him aside privately (I) and calm his nerves first (F).":
            $ IE -= 5
            $ TF += 5
            $ user_choice_text = "Pull him aside privately (I) and calm his nerves first (F)."
            $ last_answer = "Introvert & Feeling"
            $ unchosen_choice_text = "Talk it out in front of the team (E) to map a clear fix (T)."
            $ unchosen_answer = "Extrovert & Thinking"
            jump show_question_q_a_06_en_B


label show_question_q_a_06_en_A:
    $ user_journey_summary.append("Di situasi A teammate accidentally lost an important company item. He is panicking., user memilih: Talk it out in front of the team (E) to map a clear fix (T)., dengan poin MBTI: Extrovert & Thinking")
    call ai_react_logic
    return

label show_question_q_a_06_en_B:
    $ user_journey_summary.append("Di situasi A teammate accidentally lost an important company item. He is panicking., user memilih: Pull him aside privately (I) and calm his nerves first (F)., dengan poin MBTI: Introvert & Feeling")
    call ai_react_logic
    return

label show_question_q_a_07_en:
    scene bg taman with dissolve
    $ narasi_asli = "There is a new rule in the park: 'No Loud Laughter'."
    n "There is a new rule in the park: 'No Loud Laughter'."

    menu:
        "There is a new rule in the park: 'No Loud Laughter'."

        "Protest to the officer (E) because the rule is illogical (T).":
            $ IE += 5
            $ TF -= 5
            $ user_choice_text = "Protest to the officer (E) because the rule is illogical (T)."
            $ last_answer = "Extrovert & Thinking"
            $ unchosen_choice_text = "Remain silent (I), because maybe it's true, it could ruin the peaceful atmosphere (F)."
            $ unchosen_answer = "Introvert & Feeling"
            jump show_question_q_a_07_en_A

        "Remain silent (I), because maybe it's true, it could ruin the peaceful atmosphere (F).":
            $ IE -= 5
            $ TF += 5
            $ user_choice_text = "Remain silent (I), because maybe it's true, it could ruin the peaceful atmosphere (F)."
            $ last_answer = "Introvert & Feeling"
            $ unchosen_choice_text = "Protest to the officer (E) because the rule is illogical (T)."
            $ unchosen_answer = "Extrovert & Thinking"
            jump show_question_q_a_07_en_B


label show_question_q_a_07_en_A:
    $ user_journey_summary.append("Di situasi There is a new rule in the park: 'No Loud Laughter'., user memilih: Protest to the officer (E) because the rule is illogical (T)., dengan poin MBTI: Extrovert & Thinking")
    call ai_react_logic
    return

label show_question_q_a_07_en_B:
    $ user_journey_summary.append("Di situasi There is a new rule in the park: 'No Loud Laughter'., user memilih: Remain silent (I), because maybe it's true, it could ruin the peaceful atmosphere (F)., dengan poin MBTI: Introvert & Feeling")
    call ai_react_logic
    return

label show_question_q_a_08_en:
    scene bg kafe with dissolve
    $ narasi_asli = "The visitor at the next table looks very worried and sighs deeply..."
    n "The visitor at the next table looks very worried and sighs deeply..."

    menu:
        "The visitor at the next table looks very worried and sighs deeply..."

        "Try to approach and ask directly (E), analyze the problem (T) to find a solution.":
            $ IE += 5
            $ TF -= 5
            $ user_choice_text = "Try to approach and ask directly (E), analyze the problem (T) to find a solution."
            $ last_answer = "Extrovert & Thinking"
            $ unchosen_choice_text = "Quietly give them a tissue (I) because you feel sorry for them (F)."
            $ unchosen_answer = "Introvert & Feeling"
            jump show_question_q_a_08_en_A

        "Quietly give them a tissue (I) because you feel sorry for them (F).":
            $ IE -= 5
            $ TF += 5
            $ user_choice_text = "Quietly give them a tissue (I) because you feel sorry for them (F)."
            $ last_answer = "Introvert & Feeling"
            $ unchosen_choice_text = "Try to approach and ask directly (E), analyze the problem (T) to find a solution."
            $ unchosen_answer = "Extrovert & Thinking"
            jump show_question_q_a_08_en_B


label show_question_q_a_08_en_A:
    $ user_journey_summary.append("Di situasi The visitor at the next table looks very worried and sighs deeply..., user memilih: Try to approach and ask directly (E), analyze the problem (T) to find a solution., dengan poin MBTI: Extrovert & Thinking")
    call ai_react_logic
    return

label show_question_q_a_08_en_B:
    $ user_journey_summary.append("Di situasi The visitor at the next table looks very worried and sighs deeply..., user memilih: Quietly give them a tissue (I) because you feel sorry for them (F)., dengan poin MBTI: Introvert & Feeling")
    call ai_react_logic
    return

label show_question_q_a_09_en:
    scene bg kantor with dissolve
    $ narasi_asli = "The ship captain distributes the treasure, but your share is the least! Unfair!"
    n "The ship captain distributes the treasure, but your share is the least!"
    n "Unfair!"

    menu:
        "The ship captain distributes the treasure, but your share is the least! Unfair!"

        "Debate with the Captain (E) because the calculation is wrong (T).":
            $ IE += 5
            $ TF -= 5
            $ user_choice_text = "Debate with the Captain (E) because the calculation is wrong (T)."
            $ last_answer = "Extrovert & Thinking"
            $ unchosen_choice_text = "Just accept it (I) because maybe the captain needs it more (F)."
            $ unchosen_answer = "Introvert & Feeling"
            jump show_question_q_a_09_en_A

        "Just accept it (I) because maybe the captain needs it more (F).":
            $ IE -= 5
            $ TF += 5
            $ user_choice_text = "Just accept it (I) because maybe the captain needs it more (F)."
            $ last_answer = "Introvert & Feeling"
            $ unchosen_choice_text = "Debate with the Captain (E) because the calculation is wrong (T)."
            $ unchosen_answer = "Extrovert & Thinking"
            jump show_question_q_a_09_en_B


label show_question_q_a_09_en_A:
    $ user_journey_summary.append("Di situasi The ship captain distributes the treasure, but your share is the least! Unfair!, user memilih: Debate with the Captain (E) because the calculation is wrong (T)., dengan poin MBTI: Extrovert & Thinking")
    call ai_react_logic
    return

label show_question_q_a_09_en_B:
    $ user_journey_summary.append("Di situasi The ship captain distributes the treasure, but your share is the least! Unfair!, user memilih: Just accept it (I) because maybe the captain needs it more (F)., dengan poin MBTI: Introvert & Feeling")
    call ai_react_logic
    return

label show_question_q_a_10_en:
    scene bg abstrak with dissolve
    $ narasi_asli = "(Mysterious Voice) 'Choose your destiny... Left Door or Right Door?' Without any clues at all!"
    n "(Mysterious Voice) 'Choose your destiny..."
    n "Left Door or Right Door?' Without any clues at all!"

    menu:
        "(Mysterious Voice) 'Choose your destiny... Left Door or Right Door?' Without any clues at all!"

        "Ask the voice back (E) 'approximately, which door is the safest (T)?'":
            $ IE += 5
            $ TF -= 5
            $ user_choice_text = "Ask the voice back (E) 'approximately, which door is the safest (T)?'"
            $ last_answer = "Extrovert & Thinking"
            $ unchosen_choice_text = "Close your eyes (I) and follow your heart (F)."
            $ unchosen_answer = "Introvert & Feeling"
            jump show_question_q_a_10_en_A

        "Close your eyes (I) and follow your heart (F).":
            $ IE -= 5
            $ TF += 5
            $ user_choice_text = "Close your eyes (I) and follow your heart (F)."
            $ last_answer = "Introvert & Feeling"
            $ unchosen_choice_text = "Ask the voice back (E) 'approximately, which door is the safest (T)?'"
            $ unchosen_answer = "Extrovert & Thinking"
            jump show_question_q_a_10_en_B


label show_question_q_a_10_en_A:
    $ user_journey_summary.append("Di situasi (Mysterious Voice) 'Choose your destiny... Left Door or Right Door?' Without any clues at all!, user memilih: Ask the voice back (E) 'approximately, which door is the safest (T)?', dengan poin MBTI: Extrovert & Thinking")
    call ai_react_logic
    return

label show_question_q_a_10_en_B:
    $ user_journey_summary.append("Di situasi (Mysterious Voice) 'Choose your destiny... Left Door or Right Door?' Without any clues at all!, user memilih: Close your eyes (I) and follow your heart (F)., dengan poin MBTI: Introvert & Feeling")
    call ai_react_logic
    return

label show_question_q_a_11_en:
    scene bg kafe with dissolve
    $ narasi_asli = "Suddenly your friend pulls your hand. 'Let's go to the beach RIGHT NOW!'"
    n "Suddenly your friend pulls your hand."
    n "'Let's go to the beach RIGHT NOW!'"

    menu:
        "Suddenly your friend pulls your hand. 'Let's go to the beach RIGHT NOW!'"

        "Go! (E) We’ll think about the consequences later (P).":
            $ IE += 5
            $ JP += 5
            $ user_choice_text = "Go! (E) We’ll think about the consequences later (P)."
            $ last_answer = "Extrovert & Perceiving"
            $ unchosen_choice_text = "Refuse (I) because you have to check the schedule (J) first."
            $ unchosen_answer = "Introvert & Judging"
            jump show_question_q_a_11_en_A

        "Refuse (I) because you have to check the schedule (J) first.":
            $ IE -= 5
            $ JP -= 5
            $ user_choice_text = "Refuse (I) because you have to check the schedule (J) first."
            $ last_answer = "Introvert & Judging"
            $ unchosen_choice_text = "Go! (E) We’ll think about the consequences later (P)."
            $ unchosen_answer = "Extrovert & Perceiving"
            jump show_question_q_a_11_en_B


label show_question_q_a_11_en_A:
    $ user_journey_summary.append("Di situasi Suddenly your friend pulls your hand. 'Let's go to the beach RIGHT NOW!', user memilih: Go! (E) We’ll think about the consequences later (P)., dengan poin MBTI: Extrovert & Perceiving")
    call ai_react_logic
    return

label show_question_q_a_11_en_B:
    $ user_journey_summary.append("Di situasi Suddenly your friend pulls your hand. 'Let's go to the beach RIGHT NOW!', user memilih: Refuse (I) because you have to check the schedule (J) first., dengan poin MBTI: Introvert & Judging")
    call ai_react_logic
    return

label show_question_q_a_12_en:
    scene bg stasiun with dissolve
    $ narasi_asli = "(Toot! Toot!) The last train has left without you! You missed the train you were supposed to take home!"
    n "(Toot!"
    n "Toot!) The last train has left without you!"
    n "You missed the train you were supposed to take home!"

    menu:
        "(Toot! Toot!) The last train has left without you! You missed the train you were supposed to take home!"

        "Awesome! (E) We are free to explore the city! (P).":
            $ IE += 5
            $ JP += 5
            $ user_choice_text = "Awesome! (E) We are free to explore the city! (P)."
            $ last_answer = "Extrovert & Perceiving"
            $ unchosen_choice_text = "Oh dear! (I) I should have arrived earlier (J)."
            $ unchosen_answer = "Introvert & Judging"
            jump show_question_q_a_12_en_A

        "Oh dear! (I) I should have arrived earlier (J).":
            $ IE -= 5
            $ JP -= 5
            $ user_choice_text = "Oh dear! (I) I should have arrived earlier (J)."
            $ last_answer = "Introvert & Judging"
            $ unchosen_choice_text = "Awesome! (E) We are free to explore the city! (P)."
            $ unchosen_answer = "Extrovert & Perceiving"
            jump show_question_q_a_12_en_B


label show_question_q_a_12_en_A:
    $ user_journey_summary.append("Di situasi (Toot! Toot!) The last train has left without you! You missed the train you were supposed to take home!, user memilih: Awesome! (E) We are free to explore the city! (P)., dengan poin MBTI: Extrovert & Perceiving")
    call ai_react_logic
    return

label show_question_q_a_12_en_B:
    $ user_journey_summary.append("Di situasi (Toot! Toot!) The last train has left without you! You missed the train you were supposed to take home!, user memilih: Oh dear! (I) I should have arrived earlier (J)., dengan poin MBTI: Introvert & Judging")
    call ai_react_logic
    return

label show_question_q_a_13_en:
    scene bg taman with dissolve
    $ narasi_asli = "You are appointed as the picnic leader tomorrow. What is your plan?"
    n "You are appointed as the picnic leader tomorrow."
    n "What is your plan?"

    menu:
        "You are appointed as the picnic leader tomorrow. What is your plan?"

        "Invite all friends! (E) They are free to bring whatever they want (P).":
            $ IE += 5
            $ JP += 5
            $ user_choice_text = "Invite all friends! (E) They are free to bring whatever they want (P)."
            $ last_answer = "Extrovert & Perceiving"
            $ unchosen_choice_text = "Try to choose the best menu according to you (I) and determine the exact time (J)."
            $ unchosen_answer = "Introvert & Judging"
            jump show_question_q_a_13_en_A

        "Try to choose the best menu according to you (I) and determine the exact time (J).":
            $ IE -= 5
            $ JP -= 5
            $ user_choice_text = "Try to choose the best menu according to you (I) and determine the exact time (J)."
            $ last_answer = "Introvert & Judging"
            $ unchosen_choice_text = "Invite all friends! (E) They are free to bring whatever they want (P)."
            $ unchosen_answer = "Extrovert & Perceiving"
            jump show_question_q_a_13_en_B


label show_question_q_a_13_en_A:
    $ user_journey_summary.append("Di situasi You are appointed as the picnic leader tomorrow. What is your plan?, user memilih: Invite all friends! (E) They are free to bring whatever they want (P)., dengan poin MBTI: Extrovert & Perceiving")
    call ai_react_logic
    return

label show_question_q_a_13_en_B:
    $ user_journey_summary.append("Di situasi You are appointed as the picnic leader tomorrow. What is your plan?, user memilih: Try to choose the best menu according to you (I) and determine the exact time (J)., dengan poin MBTI: Introvert & Judging")
    call ai_react_logic
    return

label show_question_q_a_14_en:
    scene bg room with dissolve
    $ narasi_asli = "You look at your room. It feels dull and boring."
    n "You look at your room."
    n "It feels dull and boring."

    menu:
        "You look at your room. It feels dull and boring."

        "Change the paint (E) and reorganize the items in the room now (P).":
            $ IE += 5
            $ JP += 5
            $ user_choice_text = "Change the paint (E) and reorganize the items in the room now (P)."
            $ last_answer = "Extrovert & Perceiving"
            $ unchosen_choice_text = "Just let it be (I) because this position is already efficient (J)."
            $ unchosen_answer = "Introvert & Judging"
            jump show_question_q_a_14_en_A

        "Just let it be (I) because this position is already efficient (J).":
            $ IE -= 5
            $ JP -= 5
            $ user_choice_text = "Just let it be (I) because this position is already efficient (J)."
            $ last_answer = "Introvert & Judging"
            $ unchosen_choice_text = "Change the paint (E) and reorganize the items in the room now (P)."
            $ unchosen_answer = "Extrovert & Perceiving"
            jump show_question_q_a_14_en_B


label show_question_q_a_14_en_A:
    $ user_journey_summary.append("Di situasi You look at your room. It feels dull and boring., user memilih: Change the paint (E) and reorganize the items in the room now (P)., dengan poin MBTI: Extrovert & Perceiving")
    call ai_react_logic
    return

label show_question_q_a_14_en_B:
    $ user_journey_summary.append("Di situasi You look at your room. It feels dull and boring., user memilih: Just let it be (I) because this position is already efficient (J)., dengan poin MBTI: Introvert & Judging")
    call ai_react_logic
    return

label show_question_q_a_15_en:
    scene bg stasiun with dissolve
    $ narasi_asli = "You stop by the station souvenir shop. Many cute and interesting items!"
    n "You stop by the station souvenir shop."
    n "Many cute and interesting items!"

    menu:
        "You stop by the station souvenir shop. Many cute and interesting items!"

        "Ask the seller for advice (E) and buy the first item you see (P).":
            $ IE += 5
            $ JP += 5
            $ user_choice_text = "Ask the seller for advice (E) and buy the first item you see (P)."
            $ last_answer = "Extrovert & Perceiving"
            $ unchosen_choice_text = "Try to look around (I) and buy according to your needs (J)."
            $ unchosen_answer = "Introvert & Judging"
            jump show_question_q_a_15_en_A

        "Try to look around (I) and buy according to your needs (J).":
            $ IE -= 5
            $ JP -= 5
            $ user_choice_text = "Try to look around (I) and buy according to your needs (J)."
            $ last_answer = "Introvert & Judging"
            $ unchosen_choice_text = "Ask the seller for advice (E) and buy the first item you see (P)."
            $ unchosen_answer = "Extrovert & Perceiving"
            jump show_question_q_a_15_en_B


label show_question_q_a_15_en_A:
    $ user_journey_summary.append("Di situasi You stop by the station souvenir shop. Many cute and interesting items!, user memilih: Ask the seller for advice (E) and buy the first item you see (P)., dengan poin MBTI: Extrovert & Perceiving")
    call ai_react_logic
    return

label show_question_q_a_15_en_B:
    $ user_journey_summary.append("Di situasi You stop by the station souvenir shop. Many cute and interesting items!, user memilih: Try to look around (I) and buy according to your needs (J)., dengan poin MBTI: Introvert & Judging")
    call ai_react_logic
    return

label show_question_q_a_16_en:
    scene bg kantor with dissolve
    $ narasi_asli = "Your friend is angry at you for no clear reason! Their face is red with rage!"
    n "Your friend is angry at you for no clear reason!"
    n "Their face is red with rage!"

    menu:
        "Your friend is angry at you for no clear reason! Their face is red with rage!"

        "Diffuse their anger (T) and explain the evidence first (J).":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "Diffuse their anger (T) and explain the evidence first (J)."
            $ last_answer = "Thinking & Judging"
            $ unchosen_choice_text = "'Why am I being yelled at? (F) Did I do something wrong? (P)'."
            $ unchosen_answer = "Feeling & Perceiving"
            jump show_question_q_a_16_en_A

        "'Why am I being yelled at? (F) Did I do something wrong? (P)'.":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "'Why am I being yelled at? (F) Did I do something wrong? (P)'."
            $ last_answer = "Feeling & Perceiving"
            $ unchosen_choice_text = "Diffuse their anger (T) and explain the evidence first (J)."
            $ unchosen_answer = "Thinking & Judging"
            jump show_question_q_a_16_en_B


label show_question_q_a_16_en_A:
    $ user_journey_summary.append("Di situasi Your friend is angry at you for no clear reason! Their face is red with rage!, user memilih: Diffuse their anger (T) and explain the evidence first (J)., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic
    return

label show_question_q_a_16_en_B:
    $ user_journey_summary.append("Di situasi Your friend is angry at you for no clear reason! Their face is red with rage!, user memilih: 'Why am I being yelled at? (F) Did I do something wrong? (P)'., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic
    return

label show_question_q_a_17_en:
    scene bg dapur with dissolve
    $ narasi_asli = "The birthday cake you made came out burnt and messy."
    n "The birthday cake you made came out burnt and messy."

    menu:
        "The birthday cake you made came out burnt and messy."

        "Start over by the recipe (J) so it turns out right (T).":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "Start over by the recipe (J) so it turns out right (T)."
            $ last_answer = "Thinking & Judging"
            $ unchosen_choice_text = "Use the one you have (P), what matters is it was made sincerely (F)."
            $ unchosen_answer = "Feeling & Perceiving"
            jump show_question_q_a_17_en_A

        "Use the one you have (P), what matters is it was made sincerely (F).":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "Use the one you have (P), what matters is it was made sincerely (F)."
            $ last_answer = "Feeling & Perceiving"
            $ unchosen_choice_text = "Start over by the recipe (J) so it turns out right (T)."
            $ unchosen_answer = "Thinking & Judging"
            jump show_question_q_a_17_en_B


label show_question_q_a_17_en_A:
    $ user_journey_summary.append("Di situasi The birthday cake you made came out burnt and messy., user memilih: Start over by the recipe (J) so it turns out right (T)., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic
    return

label show_question_q_a_17_en_B:
    $ user_journey_summary.append("Di situasi The birthday cake you made came out burnt and messy., user memilih: Use the one you have (P), what matters is it was made sincerely (F)., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic
    return

label show_question_q_a_18_en:
    scene bg abstrak with dissolve
    $ narasi_asli = "You find a Mysterious Landscape Painting. What do you think makes it good?"
    n "You find a Mysterious Landscape Painting."
    n "What do you think makes it good?"

    menu:
        "You find a Mysterious Landscape Painting. What do you think makes it good?"

        "The color composition (T), the technique, everything is perfect and neat! (J).":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "The color composition (T), the technique, everything is perfect and neat! (J)."
            $ last_answer = "Thinking & Judging"
            $ unchosen_choice_text = "This painting (F) has deep and beautiful emotion (P)."
            $ unchosen_answer = "Feeling & Perceiving"
            jump show_question_q_a_18_en_A

        "This painting (F) has deep and beautiful emotion (P).":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "This painting (F) has deep and beautiful emotion (P)."
            $ last_answer = "Feeling & Perceiving"
            $ unchosen_choice_text = "The color composition (T), the technique, everything is perfect and neat! (J)."
            $ unchosen_answer = "Thinking & Judging"
            jump show_question_q_a_18_en_B


label show_question_q_a_18_en_A:
    $ user_journey_summary.append("Di situasi You find a Mysterious Landscape Painting. What do you think makes it good?, user memilih: The color composition (T), the technique, everything is perfect and neat! (J)., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic
    return

label show_question_q_a_18_en_B:
    $ user_journey_summary.append("Di situasi You find a Mysterious Landscape Painting. What do you think makes it good?, user memilih: This painting (F) has deep and beautiful emotion (P)., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic
    return

label show_question_q_a_19_en:
    scene bg abstrak with dissolve
    $ narasi_asli = "You are the referee. In the final minute, your friend commits a tiny, maybe-accidental foul."
    n "You are the referee."
    n "In the final minute, your friend commits a tiny, maybe-accidental foul."

    menu:
        "You are the referee. In the final minute, your friend commits a tiny, maybe-accidental foul."

        "Blow the whistle anyway (T), fair to everyone who played clean (J).":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "Blow the whistle anyway (T), fair to everyone who played clean (J)."
            $ last_answer = "Thinking & Judging"
            $ unchosen_choice_text = "Let it slide just this once (F), he clearly did not mean it (P)."
            $ unchosen_answer = "Feeling & Perceiving"
            jump show_question_q_a_19_en_A

        "Let it slide just this once (F), he clearly did not mean it (P).":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "Let it slide just this once (F), he clearly did not mean it (P)."
            $ last_answer = "Feeling & Perceiving"
            $ unchosen_choice_text = "Blow the whistle anyway (T), fair to everyone who played clean (J)."
            $ unchosen_answer = "Thinking & Judging"
            jump show_question_q_a_19_en_B


label show_question_q_a_19_en_A:
    $ user_journey_summary.append("Di situasi You are the referee. In the final minute, your friend commits a tiny, maybe-accidental foul., user memilih: Blow the whistle anyway (T), fair to everyone who played clean (J)., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic
    return

label show_question_q_a_19_en_B:
    $ user_journey_summary.append("Di situasi You are the referee. In the final minute, your friend commits a tiny, maybe-accidental foul., user memilih: Let it slide just this once (F), he clearly did not mean it (P)., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic
    return

label show_question_q_a_20_en:
    scene bg kantor with dissolve
    $ narasi_asli = "Your team is sluggish today, all the spirit gone somewhere."
    n "Your team is sluggish today, all the spirit gone somewhere."

    menu:
        "Your team is sluggish today, all the spirit gone somewhere."

        "Set a clear target (T) and lay out measurable milestones (J).":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "Set a clear target (T) and lay out measurable milestones (J)."
            $ last_answer = "Thinking & Judging"
            $ unchosen_choice_text = "Lift their spirits (F), rally them to move together for the team (P)."
            $ unchosen_answer = "Feeling & Perceiving"
            jump show_question_q_a_20_en_A

        "Lift their spirits (F), rally them to move together for the team (P).":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "Lift their spirits (F), rally them to move together for the team (P)."
            $ last_answer = "Feeling & Perceiving"
            $ unchosen_choice_text = "Set a clear target (T) and lay out measurable milestones (J)."
            $ unchosen_answer = "Thinking & Judging"
            jump show_question_q_a_20_en_B


label show_question_q_a_20_en_A:
    $ user_journey_summary.append("Di situasi Your team is sluggish today, all the spirit gone somewhere., user memilih: Set a clear target (T) and lay out measurable milestones (J)., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic
    return

label show_question_q_a_20_en_B:
    $ user_journey_summary.append("Di situasi Your team is sluggish today, all the spirit gone somewhere., user memilih: Lift their spirits (F), rally them to move together for the team (P)., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic
    return

label show_question_q_b_21_en:
    scene bg dapur with dissolve
    $ narasi_asli = "(Confusion!) You found a strange-looking ancient recipe book. You are starving right now. How do you decide to cook?"
    n "(Confusion!) You found a strange-looking ancient recipe book."
    n "You are starving right now."
    n "How do you decide to cook?"

    menu:
        "(Confusion!) You found a strange-looking ancient recipe book. You are starving right now. How do you decide to cook?"

        "Read it alone calmly (I) and follow the measurements precisely (S).":
            $ IE -= 5
            $ SN -= 5
            $ user_choice_text = "Read it alone calmly (I) and follow the measurements precisely (S)."
            $ last_answer = "Introvert & Sensing"
            $ unchosen_choice_text = "Call friends (E) to guess and create a new magical flavor (N)."
            $ unchosen_answer = "Extrovert & Intuitive"
            jump show_question_q_b_21_en_A

        "Call friends (E) to guess and create a new magical flavor (N).":
            $ IE += 5
            $ SN += 5
            $ user_choice_text = "Call friends (E) to guess and create a new magical flavor (N)."
            $ last_answer = "Extrovert & Intuitive"
            $ unchosen_choice_text = "Read it alone calmly (I) and follow the measurements precisely (S)."
            $ unchosen_answer = "Introvert & Sensing"
            jump show_question_q_b_21_en_B


label show_question_q_b_21_en_A:
    $ user_journey_summary.append("Di situasi (Confusion!) You found a strange-looking ancient recipe book. You are starving right now. How do you decide to cook?, user memilih: Read it alone calmly (I) and follow the measurements precisely (S)., dengan poin MBTI: Introvert & Sensing")
    call ai_react_logic
    return

label show_question_q_b_21_en_B:
    $ user_journey_summary.append("Di situasi (Confusion!) You found a strange-looking ancient recipe book. You are starving right now. How do you decide to cook?, user memilih: Call friends (E) to guess and create a new magical flavor (N)., dengan poin MBTI: Extrovert & Intuitive")
    call ai_react_logic
    return

label show_question_q_b_22_en:
    scene bg kantor with dissolve
    $ narasi_asli = "(Suddenly!) A client comes asking for fresh ideas right now! You haven't prepared any material yet."
    n "(Suddenly!) A client comes asking for fresh ideas right now!"
    n "You haven't prepared any material yet."

    menu:
        "(Suddenly!) A client comes asking for fresh ideas right now! You haven't prepared any material yet."

        "Ask for time alone (I) to compile existing facts and data (S).":
            $ IE -= 5
            $ SN -= 5
            $ user_choice_text = "Ask for time alone (I) to compile existing facts and data (S)."
            $ last_answer = "Introvert & Sensing"
            $ unchosen_choice_text = "Have a casual discussion (E) and convey your idea about the vision for the future (N)."
            $ unchosen_answer = "Extrovert & Intuitive"
            jump show_question_q_b_22_en_A

        "Have a casual discussion (E) and convey your idea about the vision for the future (N).":
            $ IE += 5
            $ SN += 5
            $ user_choice_text = "Have a casual discussion (E) and convey your idea about the vision for the future (N)."
            $ last_answer = "Extrovert & Intuitive"
            $ unchosen_choice_text = "Ask for time alone (I) to compile existing facts and data (S)."
            $ unchosen_answer = "Introvert & Sensing"
            jump show_question_q_b_22_en_B


label show_question_q_b_22_en_A:
    $ user_journey_summary.append("Di situasi (Suddenly!) A client comes asking for fresh ideas right now! You haven't prepared any material yet., user memilih: Ask for time alone (I) to compile existing facts and data (S)., dengan poin MBTI: Introvert & Sensing")
    call ai_react_logic
    return

label show_question_q_b_22_en_B:
    $ user_journey_summary.append("Di situasi (Suddenly!) A client comes asking for fresh ideas right now! You haven't prepared any material yet., user memilih: Have a casual discussion (E) and convey your idea about the vision for the future (N)., dengan poin MBTI: Extrovert & Intuitive")
    call ai_react_logic
    return

label show_question_q_b_23_en:
    scene bg abstrak with dissolve
    $ narasi_asli = "You enter an International library. Which book do you pick up first?"
    n "You enter an International library."
    n "Which book do you pick up first?"

    menu:
        "You enter an International library. Which book do you pick up first?"

        "'Illustrated Encyclopedia' (S) which can be read with friends (E).":
            $ IE += 5
            $ SN -= 5
            $ user_choice_text = "'Illustrated Encyclopedia' (S) which can be read with friends (E)."
            $ last_answer = "Extrovert & Sensing"
            $ unchosen_choice_text = "'Thick Philosophy' (N) which is interesting to read in a quiet place (I)."
            $ unchosen_answer = "Introvert & Intuitive"
            jump show_question_q_b_23_en_A

        "'Thick Philosophy' (N) which is interesting to read in a quiet place (I).":
            $ IE -= 5
            $ SN += 5
            $ user_choice_text = "'Thick Philosophy' (N) which is interesting to read in a quiet place (I)."
            $ last_answer = "Introvert & Intuitive"
            $ unchosen_choice_text = "'Illustrated Encyclopedia' (S) which can be read with friends (E)."
            $ unchosen_answer = "Extrovert & Sensing"
            jump show_question_q_b_23_en_B


label show_question_q_b_23_en_A:
    $ user_journey_summary.append("Di situasi You enter an International library. Which book do you pick up first?, user memilih: 'Illustrated Encyclopedia' (S) which can be read with friends (E)., dengan poin MBTI: Extrovert & Sensing")
    call ai_react_logic
    return

label show_question_q_b_23_en_B:
    $ user_journey_summary.append("Di situasi You enter an International library. Which book do you pick up first?, user memilih: 'Thick Philosophy' (N) which is interesting to read in a quiet place (I)., dengan poin MBTI: Introvert & Intuitive")
    call ai_react_logic
    return

label show_question_q_b_24_en:
    scene bg kafe with dissolve
    $ narasi_asli = "You are hungry, but your wallet is thin. Meanwhile, your friends invite you to eat out."
    n "You are hungry, but your wallet is thin."
    n "Meanwhile, your friends invite you to eat out."

    menu:
        "You are hungry, but your wallet is thin. Meanwhile, your friends invite you to eat out."

        "Join them (E) but look for a regular stall that is definitely cheap and delicious (S).":
            $ IE += 5
            $ SN -= 5
            $ user_choice_text = "Join them (E) but look for a regular stall that is definitely cheap and delicious (S)."
            $ last_answer = "Extrovert & Sensing"
            $ unchosen_choice_text = "Refuse first (I), you want to try looking for cheap and unique food that might be around your place (N)."
            $ unchosen_answer = "Introvert & Intuitive"
            jump show_question_q_b_24_en_A

        "Refuse first (I), you want to try looking for cheap and unique food that might be around your place (N).":
            $ IE -= 5
            $ SN += 5
            $ user_choice_text = "Refuse first (I), you want to try looking for cheap and unique food that might be around your place (N)."
            $ last_answer = "Introvert & Intuitive"
            $ unchosen_choice_text = "Join them (E) but look for a regular stall that is definitely cheap and delicious (S)."
            $ unchosen_answer = "Extrovert & Sensing"
            jump show_question_q_b_24_en_B


label show_question_q_b_24_en_A:
    $ user_journey_summary.append("Di situasi You are hungry, but your wallet is thin. Meanwhile, your friends invite you to eat out., user memilih: Join them (E) but look for a regular stall that is definitely cheap and delicious (S)., dengan poin MBTI: Extrovert & Sensing")
    call ai_react_logic
    return

label show_question_q_b_24_en_B:
    $ user_journey_summary.append("Di situasi You are hungry, but your wallet is thin. Meanwhile, your friends invite you to eat out., user memilih: Refuse first (I), you want to try looking for cheap and unique food that might be around your place (N)., dengan poin MBTI: Introvert & Intuitive")
    call ai_react_logic
    return

label show_question_q_b_25_en:
    scene bg stasiun with dissolve
    $ narasi_asli = "There is a suspicious suitcase left behind at a quiet station."
    n "There is a suspicious suitcase left behind at a quiet station."

    menu:
        "There is a suspicious suitcase left behind at a quiet station."

        "Call an officer (E) to safely check its contents (S).":
            $ IE += 5
            $ SN -= 5
            $ user_choice_text = "Call an officer (E) to safely check its contents (S)."
            $ last_answer = "Extrovert & Sensing"
            $ unchosen_choice_text = "Observe from a distance (I) while imagining what the contents of the suitcase really are (N)."
            $ unchosen_answer = "Introvert & Intuitive"
            jump show_question_q_b_25_en_A

        "Observe from a distance (I) while imagining what the contents of the suitcase really are (N).":
            $ IE -= 5
            $ SN += 5
            $ user_choice_text = "Observe from a distance (I) while imagining what the contents of the suitcase really are (N)."
            $ last_answer = "Introvert & Intuitive"
            $ unchosen_choice_text = "Call an officer (E) to safely check its contents (S)."
            $ unchosen_answer = "Extrovert & Sensing"
            jump show_question_q_b_25_en_B


label show_question_q_b_25_en_A:
    $ user_journey_summary.append("Di situasi There is a suspicious suitcase left behind at a quiet station., user memilih: Call an officer (E) to safely check its contents (S)., dengan poin MBTI: Extrovert & Sensing")
    call ai_react_logic
    return

label show_question_q_b_25_en_B:
    $ user_journey_summary.append("Di situasi There is a suspicious suitcase left behind at a quiet station., user memilih: Observe from a distance (I) while imagining what the contents of the suitcase really are (N)., dengan poin MBTI: Introvert & Intuitive")
    call ai_react_logic
    return

label show_question_q_b_26_en:
    scene bg kantor with dissolve
    $ narasi_asli = "Your teammate made a fatal mistake that cost everyone."
    n "Your teammate made a fatal mistake that cost everyone."

    menu:
        "Your teammate made a fatal mistake that cost everyone."

        "Confront them directly! (E) and ask them to logically explain what happened (T).":
            $ IE += 5
            $ TF -= 5
            $ user_choice_text = "Confront them directly! (E) and ask them to logically explain what happened (T)."
            $ last_answer = "Extrovert & Thinking"
            $ unchosen_choice_text = "Send them a private message (I), then ask if they are okay (F)."
            $ unchosen_answer = "Introvert & Feeling"
            jump show_question_q_b_26_en_A

        "Send them a private message (I), then ask if they are okay (F).":
            $ IE -= 5
            $ TF += 5
            $ user_choice_text = "Send them a private message (I), then ask if they are okay (F)."
            $ last_answer = "Introvert & Feeling"
            $ unchosen_choice_text = "Confront them directly! (E) and ask them to logically explain what happened (T)."
            $ unchosen_answer = "Extrovert & Thinking"
            jump show_question_q_b_26_en_B


label show_question_q_b_26_en_A:
    $ user_journey_summary.append("Di situasi Your teammate made a fatal mistake that cost everyone., user memilih: Confront them directly! (E) and ask them to logically explain what happened (T)., dengan poin MBTI: Extrovert & Thinking")
    call ai_react_logic
    return

label show_question_q_b_26_en_B:
    $ user_journey_summary.append("Di situasi Your teammate made a fatal mistake that cost everyone., user memilih: Send them a private message (I), then ask if they are okay (F)., dengan poin MBTI: Introvert & Feeling")
    call ai_react_logic
    return

label show_question_q_b_27_en:
    scene bg kantor with dissolve
    $ narasi_asli = "Your friend asks for an honest opinion about their work, which you would say... is terrible."
    n "Your friend asks for an honest opinion about their work, which you would say..."
    n "is terrible."

    menu:
        "Your friend asks for an honest opinion about their work, which you would say... is terrible."

        "Tell them straight (E) which part is wrong so they can fix it (T).":
            $ IE += 5
            $ TF -= 5
            $ user_choice_text = "Tell them straight (E) which part is wrong so they can fix it (T)."
            $ last_answer = "Extrovert & Thinking"
            $ unchosen_choice_text = "Just keep quiet or smile (I), you can't bear to hurt their feelings (F)."
            $ unchosen_answer = "Introvert & Feeling"
            jump show_question_q_b_27_en_A

        "Just keep quiet or smile (I), you can't bear to hurt their feelings (F).":
            $ IE -= 5
            $ TF += 5
            $ user_choice_text = "Just keep quiet or smile (I), you can't bear to hurt their feelings (F)."
            $ last_answer = "Introvert & Feeling"
            $ unchosen_choice_text = "Tell them straight (E) which part is wrong so they can fix it (T)."
            $ unchosen_answer = "Extrovert & Thinking"
            jump show_question_q_b_27_en_B


label show_question_q_b_27_en_A:
    $ user_journey_summary.append("Di situasi Your friend asks for an honest opinion about their work, which you would say... is terrible., user memilih: Tell them straight (E) which part is wrong so they can fix it (T)., dengan poin MBTI: Extrovert & Thinking")
    call ai_react_logic
    return

label show_question_q_b_27_en_B:
    $ user_journey_summary.append("Di situasi Your friend asks for an honest opinion about their work, which you would say... is terrible., user memilih: Just keep quiet or smile (I), you can't bear to hurt their feelings (F)., dengan poin MBTI: Introvert & Feeling")
    call ai_react_logic
    return

label show_question_q_b_28_en:
    scene bg kafe with dissolve
    $ narasi_asli = "Two strangers are arguing loudly at the next table. It's very annoying!"
    n "Two strangers are arguing loudly at the next table."
    n "It's very annoying!"

    menu:
        "Two strangers are arguing loudly at the next table. It's very annoying!"

        "Confront them (E), 'Please be quiet, your arguments are illogical!' (T).":
            $ IE += 5
            $ TF -= 5
            $ user_choice_text = "Confront them (E), 'Please be quiet, your arguments are illogical!' (T)."
            $ last_answer = "Extrovert & Thinking"
            $ unchosen_choice_text = "Move tables (I), move away because the energy is too negative (F)."
            $ unchosen_answer = "Introvert & Feeling"
            jump show_question_q_b_28_en_A

        "Move tables (I), move away because the energy is too negative (F).":
            $ IE -= 5
            $ TF += 5
            $ user_choice_text = "Move tables (I), move away because the energy is too negative (F)."
            $ last_answer = "Introvert & Feeling"
            $ unchosen_choice_text = "Confront them (E), 'Please be quiet, your arguments are illogical!' (T)."
            $ unchosen_answer = "Extrovert & Thinking"
            jump show_question_q_b_28_en_B


label show_question_q_b_28_en_A:
    $ user_journey_summary.append("Di situasi Two strangers are arguing loudly at the next table. It's very annoying!, user memilih: Confront them (E), 'Please be quiet, your arguments are illogical!' (T)., dengan poin MBTI: Extrovert & Thinking")
    call ai_react_logic
    return

label show_question_q_b_28_en_B:
    $ user_journey_summary.append("Di situasi Two strangers are arguing loudly at the next table. It's very annoying!, user memilih: Move tables (I), move away because the energy is too negative (F)., dengan poin MBTI: Introvert & Feeling")
    call ai_react_logic
    return

label show_question_q_b_29_en:
    scene bg abstrak with dissolve
    $ narasi_asli = "You must choose a leader for a dangerous mission."
    n "You must choose a leader for a dangerous mission."

    menu:
        "You must choose a leader for a dangerous mission."

        "Open debate (E), choose the one with the strongest statistics (T).":
            $ IE += 5
            $ TF -= 5
            $ user_choice_text = "Open debate (E), choose the one with the strongest statistics (T)."
            $ last_answer = "Extrovert & Thinking"
            $ unchosen_choice_text = "Reflect with a few close friends (I), then choose the one with the most sincere heart (F)."
            $ unchosen_answer = "Introvert & Feeling"
            jump show_question_q_b_29_en_A

        "Reflect with a few close friends (I), then choose the one with the most sincere heart (F).":
            $ IE -= 5
            $ TF += 5
            $ user_choice_text = "Reflect with a few close friends (I), then choose the one with the most sincere heart (F)."
            $ last_answer = "Introvert & Feeling"
            $ unchosen_choice_text = "Open debate (E), choose the one with the strongest statistics (T)."
            $ unchosen_answer = "Extrovert & Thinking"
            jump show_question_q_b_29_en_B


label show_question_q_b_29_en_A:
    $ user_journey_summary.append("Di situasi You must choose a leader for a dangerous mission., user memilih: Open debate (E), choose the one with the strongest statistics (T)., dengan poin MBTI: Extrovert & Thinking")
    call ai_react_logic
    return

label show_question_q_b_29_en_B:
    $ user_journey_summary.append("Di situasi You must choose a leader for a dangerous mission., user memilih: Reflect with a few close friends (I), then choose the one with the most sincere heart (F)., dengan poin MBTI: Introvert & Feeling")
    call ai_react_logic
    return

label show_question_q_b_30_en:
    scene bg taman with dissolve
    $ narasi_asli = "There is a crowd of people grieving because an old tree was cut down by the local government."
    n "There is a crowd of people grieving because an old tree was cut down by the local government."

    menu:
        "There is a crowd of people grieving because an old tree was cut down by the local government."

        "Gather them (E) to create a protest petition to the government (T).":
            $ IE += 5
            $ TF -= 5
            $ user_choice_text = "Gather them (E) to create a protest petition to the government (T)."
            $ last_answer = "Extrovert & Thinking"
            $ unchosen_choice_text = "Sit quietly (I) there as a sign of solidarity (F)."
            $ unchosen_answer = "Introvert & Feeling"
            jump show_question_q_b_30_en_A

        "Sit quietly (I) there as a sign of solidarity (F).":
            $ IE -= 5
            $ TF += 5
            $ user_choice_text = "Sit quietly (I) there as a sign of solidarity (F)."
            $ last_answer = "Introvert & Feeling"
            $ unchosen_choice_text = "Gather them (E) to create a protest petition to the government (T)."
            $ unchosen_answer = "Extrovert & Thinking"
            jump show_question_q_b_30_en_B


label show_question_q_b_30_en_A:
    $ user_journey_summary.append("Di situasi There is a crowd of people grieving because an old tree was cut down by the local government., user memilih: Gather them (E) to create a protest petition to the government (T)., dengan poin MBTI: Extrovert & Thinking")
    call ai_react_logic
    return

label show_question_q_b_30_en_B:
    $ user_journey_summary.append("Di situasi There is a crowd of people grieving because an old tree was cut down by the local government., user memilih: Sit quietly (I) there as a sign of solidarity (F)., dengan poin MBTI: Introvert & Feeling")
    call ai_react_logic
    return

label show_question_q_b_31_en:
    scene bg stasiun with dissolve
    $ narasi_asli = "(Late!) The last train leaves in 1 minute! You are still in the lobby!"
    n "(Late!) The last train leaves in 1 minute!"
    n "You are still in the lobby!"

    menu:
        "(Late!) The last train leaves in 1 minute! You are still in the lobby!"

        "Shout 'Wait!' (E) and run through the gate without thinking (P).":
            $ IE += 5
            $ JP += 5
            $ user_choice_text = "Shout 'Wait!' (E) and run through the gate without thinking (P)."
            $ last_answer = "Extrovert & Perceiving"
            $ unchosen_choice_text = "Resign (I). 'This is my fault for not checking the schedule this morning' (J)."
            $ unchosen_answer = "Introvert & Judging"
            jump show_question_q_b_31_en_A

        "Resign (I). 'This is my fault for not checking the schedule this morning' (J).":
            $ IE -= 5
            $ JP -= 5
            $ user_choice_text = "Resign (I). 'This is my fault for not checking the schedule this morning' (J)."
            $ last_answer = "Introvert & Judging"
            $ unchosen_choice_text = "Shout 'Wait!' (E) and run through the gate without thinking (P)."
            $ unchosen_answer = "Extrovert & Perceiving"
            jump show_question_q_b_31_en_B


label show_question_q_b_31_en_A:
    $ user_journey_summary.append("Di situasi (Late!) The last train leaves in 1 minute! You are still in the lobby!, user memilih: Shout 'Wait!' (E) and run through the gate without thinking (P)., dengan poin MBTI: Extrovert & Perceiving")
    call ai_react_logic
    return

label show_question_q_b_31_en_B:
    $ user_journey_summary.append("Di situasi (Late!) The last train leaves in 1 minute! You are still in the lobby!, user memilih: Resign (I). 'This is my fault for not checking the schedule this morning' (J)., dengan poin MBTI: Introvert & Judging")
    call ai_react_logic
    return

label show_question_q_b_32_en:
    scene bg kafe with dissolve
    $ narasi_asli = "You and a large group are confused about what to order at the Restaurant. The waiter is getting annoyed."
    n "You and a large group are confused about what to order at the Restaurant."
    n "The waiter is getting annoyed."

    menu:
        "You and a large group are confused about what to order at the Restaurant. The waiter is getting annoyed."

        "Ask everyone! (E), 'What food do you want? Anything goes!' (P).":
            $ IE += 5
            $ JP += 5
            $ user_choice_text = "Ask everyone! (E), 'What food do you want? Anything goes!' (P)."
            $ last_answer = "Extrovert & Perceiving"
            $ unchosen_choice_text = "Take charge (J), 'Okay, I'll order the package menu for everyone to speed things up' (I)."
            $ unchosen_answer = "Introvert & Judging"
            jump show_question_q_b_32_en_A

        "Take charge (J), 'Okay, I'll order the package menu for everyone to speed things up' (I).":
            $ IE -= 5
            $ JP -= 5
            $ user_choice_text = "Take charge (J), 'Okay, I'll order the package menu for everyone to speed things up' (I)."
            $ last_answer = "Introvert & Judging"
            $ unchosen_choice_text = "Ask everyone! (E), 'What food do you want? Anything goes!' (P)."
            $ unchosen_answer = "Extrovert & Perceiving"
            jump show_question_q_b_32_en_B


label show_question_q_b_32_en_A:
    $ user_journey_summary.append("Di situasi You and a large group are confused about what to order at the Restaurant. The waiter is getting annoyed., user memilih: Ask everyone! (E), 'What food do you want? Anything goes!' (P)., dengan poin MBTI: Extrovert & Perceiving")
    call ai_react_logic
    return

label show_question_q_b_32_en_B:
    $ user_journey_summary.append("Di situasi You and a large group are confused about what to order at the Restaurant. The waiter is getting annoyed., user memilih: Take charge (J), 'Okay, I'll order the package menu for everyone to speed things up' (I)., dengan poin MBTI: Introvert & Judging")
    call ai_react_logic
    return

label show_question_q_b_33_en:
    scene bg kafe with dissolve
    $ narasi_asli = "You see a really cool jacket displayed in the store, but it's expensive."
    n "You see a really cool jacket displayed in the store, but it's expensive."

    menu:
        "You see a really cool jacket displayed in the store, but it's expensive."

        "Ask others' opinions (E), if it's good, just buy it! (P).":
            $ IE += 5
            $ JP += 5
            $ user_choice_text = "Ask others' opinions (E), if it's good, just buy it! (P)."
            $ last_answer = "Extrovert & Perceiving"
            $ unchosen_choice_text = "Ask yourself (I), 'It's not in the budget. Don't do it yet' (J)."
            $ unchosen_answer = "Introvert & Judging"
            jump show_question_q_b_33_en_A

        "Ask yourself (I), 'It's not in the budget. Don't do it yet' (J).":
            $ IE -= 5
            $ JP -= 5
            $ user_choice_text = "Ask yourself (I), 'It's not in the budget. Don't do it yet' (J)."
            $ last_answer = "Introvert & Judging"
            $ unchosen_choice_text = "Ask others' opinions (E), if it's good, just buy it! (P)."
            $ unchosen_answer = "Extrovert & Perceiving"
            jump show_question_q_b_33_en_B


label show_question_q_b_33_en_A:
    $ user_journey_summary.append("Di situasi You see a really cool jacket displayed in the store, but it's expensive., user memilih: Ask others' opinions (E), if it's good, just buy it! (P)., dengan poin MBTI: Extrovert & Perceiving")
    call ai_react_logic
    return

label show_question_q_b_33_en_B:
    $ user_journey_summary.append("Di situasi You see a really cool jacket displayed in the store, but it's expensive., user memilih: Ask yourself (I), 'It's not in the budget. Don't do it yet' (J)., dengan poin MBTI: Introvert & Judging")
    call ai_react_logic
    return

label show_question_q_b_34_en:
    scene bg room with dissolve
    $ narasi_asli = "Your friend says your room is boring. What is your reaction?"
    n "Your friend says your room is boring."
    n "What is your reaction?"

    menu:
        "Your friend says your room is boring. What is your reaction?"

        "'That's right!' Since a friend is here, ask them (E) to move the furniture around right now (P).":
            $ IE += 5
            $ JP += 5
            $ user_choice_text = "'That's right!' Since a friend is here, ask them (E) to move the furniture around right now (P)."
            $ last_answer = "Extrovert & Perceiving"
            $ unchosen_choice_text = "Leave it. (I) 'I prefer it, because everything is already in its proper place' (J)."
            $ unchosen_answer = "Introvert & Judging"
            jump show_question_q_b_34_en_A

        "Leave it. (I) 'I prefer it, because everything is already in its proper place' (J).":
            $ IE -= 5
            $ JP -= 5
            $ user_choice_text = "Leave it. (I) 'I prefer it, because everything is already in its proper place' (J)."
            $ last_answer = "Introvert & Judging"
            $ unchosen_choice_text = "'That's right!' Since a friend is here, ask them (E) to move the furniture around right now (P)."
            $ unchosen_answer = "Extrovert & Perceiving"
            jump show_question_q_b_34_en_B


label show_question_q_b_34_en_A:
    $ user_journey_summary.append("Di situasi Your friend says your room is boring. What is your reaction?, user memilih: 'That's right!' Since a friend is here, ask them (E) to move the furniture around right now (P)., dengan poin MBTI: Extrovert & Perceiving")
    call ai_react_logic
    return

label show_question_q_b_34_en_B:
    $ user_journey_summary.append("Di situasi Your friend says your room is boring. What is your reaction?, user memilih: Leave it. (I) 'I prefer it, because everything is already in its proper place' (J)., dengan poin MBTI: Introvert & Judging")
    call ai_react_logic
    return

label show_question_q_b_35_en:
    scene bg kantor with dissolve
    $ narasi_asli = "You have to give a spontaneous public speech! What now?!"
    n "You have to give a spontaneous public speech!"
    n "What now?!"

    menu:
        "You have to give a spontaneous public speech! What now?!"

        "Step forward confidently (E), speak freely, watching the situation (P).":
            $ IE += 5
            $ JP += 5
            $ user_choice_text = "Step forward confidently (E), speak freely, watching the situation (P)."
            $ last_answer = "Extrovert & Perceiving"
            $ unchosen_choice_text = "Step back for a moment (I), ask for time to jot down key points first (J)."
            $ unchosen_answer = "Introvert & Judging"
            jump show_question_q_b_35_en_A

        "Step back for a moment (I), ask for time to jot down key points first (J).":
            $ IE -= 5
            $ JP -= 5
            $ user_choice_text = "Step back for a moment (I), ask for time to jot down key points first (J)."
            $ last_answer = "Introvert & Judging"
            $ unchosen_choice_text = "Step forward confidently (E), speak freely, watching the situation (P)."
            $ unchosen_answer = "Extrovert & Perceiving"
            jump show_question_q_b_35_en_B


label show_question_q_b_35_en_A:
    $ user_journey_summary.append("Di situasi You have to give a spontaneous public speech! What now?!, user memilih: Step forward confidently (E), speak freely, watching the situation (P)., dengan poin MBTI: Extrovert & Perceiving")
    call ai_react_logic
    return

label show_question_q_b_35_en_B:
    $ user_journey_summary.append("Di situasi You have to give a spontaneous public speech! What now?!, user memilih: Step back for a moment (I), ask for time to jot down key points first (J)., dengan poin MBTI: Introvert & Judging")
    call ai_react_logic
    return

label show_question_q_b_36_en:
    scene bg abstrak with dissolve
    $ narasi_asli = "The fort gate must close before the storm hits. A few are still gathering supplies outside."
    n "The fort gate must close before the storm hits."
    n "A few are still gathering supplies outside."

    menu:
        "The fort gate must close before the storm hits. A few are still gathering supplies outside."

        "Close it on time (J), protect the majority already inside (T).":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "Close it on time (J), protect the majority already inside (T)."
            $ last_answer = "Thinking & Judging"
            $ unchosen_choice_text = "Hold it a bit longer (P), give them a chance to get in first (F)."
            $ unchosen_answer = "Feeling & Perceiving"
            jump show_question_q_b_36_en_A

        "Hold it a bit longer (P), give them a chance to get in first (F).":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "Hold it a bit longer (P), give them a chance to get in first (F)."
            $ last_answer = "Feeling & Perceiving"
            $ unchosen_choice_text = "Close it on time (J), protect the majority already inside (T)."
            $ unchosen_answer = "Thinking & Judging"
            jump show_question_q_b_36_en_B


label show_question_q_b_36_en_A:
    $ user_journey_summary.append("Di situasi The fort gate must close before the storm hits. A few are still gathering supplies outside., user memilih: Close it on time (J), protect the majority already inside (T)., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic
    return

label show_question_q_b_36_en_B:
    $ user_journey_summary.append("Di situasi The fort gate must close before the storm hits. A few are still gathering supplies outside., user memilih: Hold it a bit longer (P), give them a chance to get in first (F)., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic
    return

label show_question_q_b_37_en:
    scene bg kantor with dissolve
    $ narasi_asli = "A teammate is heavy-hearted and can't focus, yet the deadline is close."
    n "A teammate is heavy-hearted and can't focus, yet the deadline is close."

    menu:
        "A teammate is heavy-hearted and can't focus, yet the deadline is close."

        "Help break his task into small steps (T) to keep it on schedule (J).":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "Help break his task into small steps (T) to keep it on schedule (J)."
            $ last_answer = "Thinking & Judging"
            $ unchosen_choice_text = "Let him rest first (F), we can rearrange the rest later (P)."
            $ unchosen_answer = "Feeling & Perceiving"
            jump show_question_q_b_37_en_A

        "Let him rest first (F), we can rearrange the rest later (P).":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "Let him rest first (F), we can rearrange the rest later (P)."
            $ last_answer = "Feeling & Perceiving"
            $ unchosen_choice_text = "Help break his task into small steps (T) to keep it on schedule (J)."
            $ unchosen_answer = "Thinking & Judging"
            jump show_question_q_b_37_en_B


label show_question_q_b_37_en_A:
    $ user_journey_summary.append("Di situasi A teammate is heavy-hearted and can't focus, yet the deadline is close., user memilih: Help break his task into small steps (T) to keep it on schedule (J)., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic
    return

label show_question_q_b_37_en_B:
    $ user_journey_summary.append("Di situasi A teammate is heavy-hearted and can't focus, yet the deadline is close., user memilih: Let him rest first (F), we can rearrange the rest later (P)., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic
    return

label show_question_q_b_38_en:
    scene bg dapur with dissolve
    $ narasi_asli = "You judge a cooking contest. Your friend's dish burned, despite enormous effort."
    n "You judge a cooking contest."
    n "Your friend's dish burned, despite enormous effort."

    menu:
        "You judge a cooking contest. Your friend's dish burned, despite enormous effort."

        "Score it honestly on taste (T), fair to all the other contestants (J).":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "Score it honestly on taste (T), fair to all the other contestants (J)."
            $ last_answer = "Thinking & Judging"
            $ unchosen_choice_text = "Add points for effort (F), honor the hard work behind it (P)."
            $ unchosen_answer = "Feeling & Perceiving"
            jump show_question_q_b_38_en_A

        "Add points for effort (F), honor the hard work behind it (P).":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "Add points for effort (F), honor the hard work behind it (P)."
            $ last_answer = "Feeling & Perceiving"
            $ unchosen_choice_text = "Score it honestly on taste (T), fair to all the other contestants (J)."
            $ unchosen_answer = "Thinking & Judging"
            jump show_question_q_b_38_en_B


label show_question_q_b_38_en_A:
    $ user_journey_summary.append("Di situasi You judge a cooking contest. Your friend's dish burned, despite enormous effort., user memilih: Score it honestly on taste (T), fair to all the other contestants (J)., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic
    return

label show_question_q_b_38_en_B:
    $ user_journey_summary.append("Di situasi You judge a cooking contest. Your friend's dish burned, despite enormous effort., user memilih: Add points for effort (F), honor the hard work behind it (P)., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic
    return

label show_question_q_b_39_en:
    scene bg stasiun with dissolve
    $ narasi_asli = "You are a station officer. A tourist took the wrong lane, confused by the signs. Rules say there's a fine."
    n "You are a station officer."
    n "A tourist took the wrong lane, confused by the signs."
    n "Rules say there's a fine."

    menu:
        "You are a station officer. A tourist took the wrong lane, confused by the signs. Rules say there's a fine."

        "Apply the rule (T), the same for every passenger (J).":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "Apply the rule (T), the same for every passenger (J)."
            $ last_answer = "Thinking & Judging"
            $ unchosen_choice_text = "Help waive it (F), he was clearly lost, not breaking it on purpose (P)."
            $ unchosen_answer = "Feeling & Perceiving"
            jump show_question_q_b_39_en_A

        "Help waive it (F), he was clearly lost, not breaking it on purpose (P).":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "Help waive it (F), he was clearly lost, not breaking it on purpose (P)."
            $ last_answer = "Feeling & Perceiving"
            $ unchosen_choice_text = "Apply the rule (T), the same for every passenger (J)."
            $ unchosen_answer = "Thinking & Judging"
            jump show_question_q_b_39_en_B


label show_question_q_b_39_en_A:
    $ user_journey_summary.append("Di situasi You are a station officer. A tourist took the wrong lane, confused by the signs. Rules say there's a fine., user memilih: Apply the rule (T), the same for every passenger (J)., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic
    return

label show_question_q_b_39_en_B:
    $ user_journey_summary.append("Di situasi You are a station officer. A tourist took the wrong lane, confused by the signs. Rules say there's a fine., user memilih: Help waive it (F), he was clearly lost, not breaking it on purpose (P)., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic
    return

label show_question_q_b_40_en:
    scene bg kantor with dissolve
    $ narasi_asli = "You made a new duty roster, but a friend protests over a clash in the schedule."
    n "You made a new duty roster, but a friend protests over a clash in the schedule."

    menu:
        "You made a new duty roster, but a friend protests over a clash in the schedule."

        "Keep the system (T), it was calculated to spread the load most fairly (J).":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "Keep the system (T), it was calculated to spread the load most fairly (J)."
            $ last_answer = "Thinking & Judging"
            $ unchosen_choice_text = "Ease it, arrange a swap (P) so everyone stays comfortable (F)."
            $ unchosen_answer = "Feeling & Perceiving"
            jump show_question_q_b_40_en_A

        "Ease it, arrange a swap (P) so everyone stays comfortable (F).":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "Ease it, arrange a swap (P) so everyone stays comfortable (F)."
            $ last_answer = "Feeling & Perceiving"
            $ unchosen_choice_text = "Keep the system (T), it was calculated to spread the load most fairly (J)."
            $ unchosen_answer = "Thinking & Judging"
            jump show_question_q_b_40_en_B


label show_question_q_b_40_en_A:
    $ user_journey_summary.append("Di situasi You made a new duty roster, but a friend protests over a clash in the schedule., user memilih: Keep the system (T), it was calculated to spread the load most fairly (J)., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic
    return

label show_question_q_b_40_en_B:
    $ user_journey_summary.append("Di situasi You made a new duty roster, but a friend protests over a clash in the schedule., user memilih: Ease it, arrange a swap (P) so everyone stays comfortable (F)., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic
    return

label show_question_q_c_41_en:
    scene bg taman with dissolve
    $ narasi_asli = "Holidays have arrived. Friends invite you to go traveling, but don't know exactly where to go yet."
    n "Holidays have arrived."
    n "Friends invite you to go traveling, but don't know exactly where to go yet."

    menu:
        "Holidays have arrived. Friends invite you to go traveling, but don't know exactly where to go yet."

        "Go solo (I) to visit a history museum to see historical artifacts (S).":
            $ IE -= 5
            $ SN -= 5
            $ user_choice_text = "Go solo (I) to visit a history museum to see historical artifacts (S)."
            $ last_answer = "Introvert & Sensing"
            $ unchosen_choice_text = "Join the group (E) to explore a mythical forest full of mysteries (N)."
            $ unchosen_answer = "Extrovert & Intuitive"
            jump show_question_q_c_41_en_A

        "Join the group (E) to explore a mythical forest full of mysteries (N).":
            $ IE += 5
            $ SN += 5
            $ user_choice_text = "Join the group (E) to explore a mythical forest full of mysteries (N)."
            $ last_answer = "Extrovert & Intuitive"
            $ unchosen_choice_text = "Go solo (I) to visit a history museum to see historical artifacts (S)."
            $ unchosen_answer = "Introvert & Sensing"
            jump show_question_q_c_41_en_B


label show_question_q_c_41_en_A:
    $ user_journey_summary.append("Di situasi Holidays have arrived. Friends invite you to go traveling, but don't know exactly where to go yet., user memilih: Go solo (I) to visit a history museum to see historical artifacts (S)., dengan poin MBTI: Introvert & Sensing")
    call ai_react_logic
    return

label show_question_q_c_41_en_B:
    $ user_journey_summary.append("Di situasi Holidays have arrived. Friends invite you to go traveling, but don't know exactly where to go yet., user memilih: Join the group (E) to explore a mythical forest full of mysteries (N)., dengan poin MBTI: Extrovert & Intuitive")
    call ai_react_logic
    return

label show_question_q_c_42_en:
    scene bg kafe with dissolve
    $ narasi_asli = "You won a huge lottery! Winning a bag of gold coins."
    n "You won a huge lottery!"
    n "Winning a bag of gold coins."

    menu:
        "You won a huge lottery! Winning a bag of gold coins."

        "Keep it in a safe (I) as a secure physical asset (S).":
            $ IE -= 5
            $ SN -= 5
            $ user_choice_text = "Keep it in a safe (I) as a secure physical asset (S)."
            $ last_answer = "Introvert & Sensing"
            $ unchosen_choice_text = "Treat everyone (E) while thinking about your increasing wealth (N)."
            $ unchosen_answer = "Extrovert & Intuitive"
            jump show_question_q_c_42_en_A

        "Treat everyone (E) while thinking about your increasing wealth (N).":
            $ IE += 5
            $ SN += 5
            $ user_choice_text = "Treat everyone (E) while thinking about your increasing wealth (N)."
            $ last_answer = "Extrovert & Intuitive"
            $ unchosen_choice_text = "Keep it in a safe (I) as a secure physical asset (S)."
            $ unchosen_answer = "Introvert & Sensing"
            jump show_question_q_c_42_en_B


label show_question_q_c_42_en_A:
    $ user_journey_summary.append("Di situasi You won a huge lottery! Winning a bag of gold coins., user memilih: Keep it in a safe (I) as a secure physical asset (S)., dengan poin MBTI: Introvert & Sensing")
    call ai_react_logic
    return

label show_question_q_c_42_en_B:
    $ user_journey_summary.append("Di situasi You won a huge lottery! Winning a bag of gold coins., user memilih: Treat everyone (E) while thinking about your increasing wealth (N)., dengan poin MBTI: Extrovert & Intuitive")
    call ai_react_logic
    return

label show_question_q_c_43_en:
    scene bg room with dissolve
    $ narasi_asli = "You see an abstract painting that is 'just a few line scribbles'."
    n "You see an abstract painting that is 'just a few line scribbles'."

    menu:
        "You see an abstract painting that is 'just a few line scribbles'."

        "Ask others (E), 'What is this picture? What does it mean?' (S).":
            $ IE += 5
            $ SN -= 5
            $ user_choice_text = "Ask others (E), 'What is this picture? What does it mean?' (S)."
            $ last_answer = "Extrovert & Sensing"
            $ unchosen_choice_text = "Stay silent (I) and try to feel the painter's emotion (N)."
            $ unchosen_answer = "Introvert & Intuitive"
            jump show_question_q_c_43_en_A

        "Stay silent (I) and try to feel the painter's emotion (N).":
            $ IE -= 5
            $ SN += 5
            $ user_choice_text = "Stay silent (I) and try to feel the painter's emotion (N)."
            $ last_answer = "Introvert & Intuitive"
            $ unchosen_choice_text = "Ask others (E), 'What is this picture? What does it mean?' (S)."
            $ unchosen_answer = "Extrovert & Sensing"
            jump show_question_q_c_43_en_B


label show_question_q_c_43_en_A:
    $ user_journey_summary.append("Di situasi You see an abstract painting that is 'just a few line scribbles'., user memilih: Ask others (E), 'What is this picture? What does it mean?' (S)., dengan poin MBTI: Extrovert & Sensing")
    call ai_react_logic
    return

label show_question_q_c_43_en_B:
    $ user_journey_summary.append("Di situasi You see an abstract painting that is 'just a few line scribbles'., user memilih: Stay silent (I) and try to feel the painter's emotion (N)., dengan poin MBTI: Introvert & Intuitive")
    call ai_react_logic
    return

label show_question_q_c_44_en:
    scene bg arcade with dissolve
    $ narasi_asli = "Your friend asks you to teach them a game that you are really good at playing."
    n "Your friend asks you to teach them a game that you are really good at playing."

    menu:
        "Your friend asks you to teach them a game that you are really good at playing."

        "'Here, press the forward button, then jump.' (S) Guide them directly (E).":
            $ IE += 5
            $ SN -= 5
            $ user_choice_text = "'Here, press the forward button, then jump.' (S) Guide them directly (E)."
            $ last_answer = "Extrovert & Sensing"
            $ unchosen_choice_text = "'Understand the concept first.' (N) Let them learn on their own (I)."
            $ unchosen_answer = "Introvert & Intuitive"
            jump show_question_q_c_44_en_A

        "'Understand the concept first.' (N) Let them learn on their own (I).":
            $ IE -= 5
            $ SN += 5
            $ user_choice_text = "'Understand the concept first.' (N) Let them learn on their own (I)."
            $ last_answer = "Introvert & Intuitive"
            $ unchosen_choice_text = "'Here, press the forward button, then jump.' (S) Guide them directly (E)."
            $ unchosen_answer = "Extrovert & Sensing"
            jump show_question_q_c_44_en_B


label show_question_q_c_44_en_A:
    $ user_journey_summary.append("Di situasi Your friend asks you to teach them a game that you are really good at playing., user memilih: 'Here, press the forward button, then jump.' (S) Guide them directly (E)., dengan poin MBTI: Extrovert & Sensing")
    call ai_react_logic
    return

label show_question_q_c_44_en_B:
    $ user_journey_summary.append("Di situasi Your friend asks you to teach them a game that you are really good at playing., user memilih: 'Understand the concept first.' (N) Let them learn on their own (I)., dengan poin MBTI: Introvert & Intuitive")
    call ai_react_logic
    return

label show_question_q_c_45_en:
    scene bg abstrak with dissolve
    $ narasi_asli = "You have 1 hour of free time today. What do you want to do?"
    n "You have 1 hour of free time today."
    n "What do you want to do?"

    menu:
        "You have 1 hour of free time today. What do you want to do?"

        "Exercise or clean up (S) together at home (E).":
            $ IE += 5
            $ SN -= 5
            $ user_choice_text = "Exercise or clean up (S) together at home (E)."
            $ last_answer = "Extrovert & Sensing"
            $ unchosen_choice_text = "Do something you like (I), while imagining what you can do in the future (N)."
            $ unchosen_answer = "Introvert & Intuitive"
            jump show_question_q_c_45_en_A

        "Do something you like (I), while imagining what you can do in the future (N).":
            $ IE -= 5
            $ SN += 5
            $ user_choice_text = "Do something you like (I), while imagining what you can do in the future (N)."
            $ last_answer = "Introvert & Intuitive"
            $ unchosen_choice_text = "Exercise or clean up (S) together at home (E)."
            $ unchosen_answer = "Extrovert & Sensing"
            jump show_question_q_c_45_en_B


label show_question_q_c_45_en_A:
    $ user_journey_summary.append("Di situasi You have 1 hour of free time today. What do you want to do?, user memilih: Exercise or clean up (S) together at home (E)., dengan poin MBTI: Extrovert & Sensing")
    call ai_react_logic
    return

label show_question_q_c_45_en_B:
    $ user_journey_summary.append("Di situasi You have 1 hour of free time today. What do you want to do?, user memilih: Do something you like (I), while imagining what you can do in the future (N)., dengan poin MBTI: Introvert & Intuitive")
    call ai_react_logic
    return

label show_question_q_c_46_en:
    scene bg room with dissolve
    $ narasi_asli = "Your friend is crying over a fresh breakup."
    n "Your friend is crying over a fresh breakup."

    menu:
        "Your friend is crying over a fresh breakup."

        "Help her see the facts (T) and offer concrete steps to move on (S).":
            $ SN -= 5
            $ TF -= 5
            $ user_choice_text = "Help her see the facts (T) and offer concrete steps to move on (S)."
            $ last_answer = "Sensing & Thinking"
            $ unchosen_choice_text = "Just be there (N) and listen to her feelings without rushing to judge (F)."
            $ unchosen_answer = "Intuitive & Feeling"
            jump show_question_q_c_46_en_A

        "Just be there (N) and listen to her feelings without rushing to judge (F).":
            $ SN += 5
            $ TF += 5
            $ user_choice_text = "Just be there (N) and listen to her feelings without rushing to judge (F)."
            $ last_answer = "Intuitive & Feeling"
            $ unchosen_choice_text = "Help her see the facts (T) and offer concrete steps to move on (S)."
            $ unchosen_answer = "Sensing & Thinking"
            jump show_question_q_c_46_en_B


label show_question_q_c_46_en_A:
    $ user_journey_summary.append("Di situasi Your friend is crying over a fresh breakup., user memilih: Help her see the facts (T) and offer concrete steps to move on (S)., dengan poin MBTI: Sensing & Thinking")
    call ai_react_logic
    return

label show_question_q_c_46_en_B:
    $ user_journey_summary.append("Di situasi Your friend is crying over a fresh breakup., user memilih: Just be there (N) and listen to her feelings without rushing to judge (F)., dengan poin MBTI: Intuitive & Feeling")
    call ai_react_logic
    return

label show_question_q_c_47_en:
    scene bg room with dissolve
    $ narasi_asli = "The movie you watched has a vague and unclear ending!"
    n "The movie you watched has a vague and unclear ending!"

    menu:
        "The movie you watched has a vague and unclear ending!"

        "'Ugh... It's terrible! (T) Many scenes weren't logically explained! (S).'":
            $ SN -= 5
            $ TF -= 5
            $ user_choice_text = "'Ugh... It's terrible! (T) Many scenes weren't logically explained! (S).'"
            $ last_answer = "Sensing & Thinking"
            $ unchosen_choice_text = "'Cool... (F) The meaning is so deep, about hope that is lost (N).'"
            $ unchosen_answer = "Intuitive & Feeling"
            jump show_question_q_c_47_en_A

        "'Cool... (F) The meaning is so deep, about hope that is lost (N).'":
            $ SN += 5
            $ TF += 5
            $ user_choice_text = "'Cool... (F) The meaning is so deep, about hope that is lost (N).'"
            $ last_answer = "Intuitive & Feeling"
            $ unchosen_choice_text = "'Ugh... It's terrible! (T) Many scenes weren't logically explained! (S).'"
            $ unchosen_answer = "Sensing & Thinking"
            jump show_question_q_c_47_en_B


label show_question_q_c_47_en_A:
    $ user_journey_summary.append("Di situasi The movie you watched has a vague and unclear ending!, user memilih: 'Ugh... It's terrible! (T) Many scenes weren't logically explained! (S).', dengan poin MBTI: Sensing & Thinking")
    call ai_react_logic
    return

label show_question_q_c_47_en_B:
    $ user_journey_summary.append("Di situasi The movie you watched has a vague and unclear ending!, user memilih: 'Cool... (F) The meaning is so deep, about hope that is lost (N).', dengan poin MBTI: Intuitive & Feeling")
    call ai_react_logic
    return

label show_question_q_c_48_en:
    scene bg kantor with dissolve
    $ narasi_asli = "There is a job offer with a large salary, but you don't know what the job is. The person looks quite promising.."
    n "There is a job offer with a large salary, but you don't know what the job is."
    n "The person looks quite promising.."

    menu:
        "There is a job offer with a large salary, but you don't know what the job is. The person looks quite promising.."

        "Refuse (F). 'The offer is vague' (N) and you are not sure where it will lead.":
            $ SN += 5
            $ TF += 5
            $ user_choice_text = "Refuse (F). 'The offer is vague' (N) and you are not sure where it will lead."
            $ last_answer = "Intuitive & Feeling"
            $ unchosen_choice_text = "Just accept it (T). Financially (S) you need the money."
            $ unchosen_answer = "Sensing & Thinking"
            jump show_question_q_c_48_en_A

        "Just accept it (T). Financially (S) you need the money.":
            $ SN -= 5
            $ TF -= 5
            $ user_choice_text = "Just accept it (T). Financially (S) you need the money."
            $ last_answer = "Sensing & Thinking"
            $ unchosen_choice_text = "Refuse (F). 'The offer is vague' (N) and you are not sure where it will lead."
            $ unchosen_answer = "Intuitive & Feeling"
            jump show_question_q_c_48_en_B


label show_question_q_c_48_en_A:
    $ user_journey_summary.append("Di situasi There is a job offer with a large salary, but you don't know what the job is. The person looks quite promising.., user memilih: Refuse (F). 'The offer is vague' (N) and you are not sure where it will lead., dengan poin MBTI: Intuitive & Feeling")
    call ai_react_logic
    return

label show_question_q_c_48_en_B:
    $ user_journey_summary.append("Di situasi There is a job offer with a large salary, but you don't know what the job is. The person looks quite promising.., user memilih: Just accept it (T). Financially (S) you need the money., dengan poin MBTI: Sensing & Thinking")
    call ai_react_logic
    return

label show_question_q_c_49_en:
    scene bg abstrak with dissolve
    $ narasi_asli = "You must choose one skill to learn for life."
    n "You must choose one skill to learn for life."

    menu:
        "You must choose one skill to learn for life."

        "Technical skill (S) that is useful for finding work (T).":
            $ SN -= 5
            $ TF -= 5
            $ user_choice_text = "Technical skill (S) that is useful for finding work (T)."
            $ last_answer = "Sensing & Thinking"
            $ unchosen_choice_text = "Art skill (N) that can touch people's hearts (F)."
            $ unchosen_answer = "Intuitive & Feeling"
            jump show_question_q_c_49_en_A

        "Art skill (N) that can touch people's hearts (F).":
            $ SN += 5
            $ TF += 5
            $ user_choice_text = "Art skill (N) that can touch people's hearts (F)."
            $ last_answer = "Intuitive & Feeling"
            $ unchosen_choice_text = "Technical skill (S) that is useful for finding work (T)."
            $ unchosen_answer = "Sensing & Thinking"
            jump show_question_q_c_49_en_B


label show_question_q_c_49_en_A:
    $ user_journey_summary.append("Di situasi You must choose one skill to learn for life., user memilih: Technical skill (S) that is useful for finding work (T)., dengan poin MBTI: Sensing & Thinking")
    call ai_react_logic
    return

label show_question_q_c_49_en_B:
    $ user_journey_summary.append("Di situasi You must choose one skill to learn for life., user memilih: Art skill (N) that can touch people's hearts (F)., dengan poin MBTI: Intuitive & Feeling")
    call ai_react_logic
    return

label show_question_q_c_50_en:
    scene bg kafe with dissolve
    $ narasi_asli = "Your friend is debating a science fact but all their data is wrong."
    n "Your friend is debating a science fact but all their data is wrong."

    menu:
        "Your friend is debating a science fact but all their data is wrong."

        "Correct them (T). Show the original data (S) so they don't embarrass themselves.":
            $ SN -= 5
            $ TF -= 5
            $ user_choice_text = "Correct them (T). Show the original data (S) so they don't embarrass themselves."
            $ last_answer = "Sensing & Thinking"
            $ unchosen_choice_text = "Just let it be (F). They will realize it themselves (N), rather than fighting here."
            $ unchosen_answer = "Intuitive & Feeling"
            jump show_question_q_c_50_en_A

        "Just let it be (F). They will realize it themselves (N), rather than fighting here.":
            $ SN += 5
            $ TF += 5
            $ user_choice_text = "Just let it be (F). They will realize it themselves (N), rather than fighting here."
            $ last_answer = "Intuitive & Feeling"
            $ unchosen_choice_text = "Correct them (T). Show the original data (S) so they don't embarrass themselves."
            $ unchosen_answer = "Sensing & Thinking"
            jump show_question_q_c_50_en_B


label show_question_q_c_50_en_A:
    $ user_journey_summary.append("Di situasi Your friend is debating a science fact but all their data is wrong., user memilih: Correct them (T). Show the original data (S) so they don't embarrass themselves., dengan poin MBTI: Sensing & Thinking")
    call ai_react_logic
    return

label show_question_q_c_50_en_B:
    $ user_journey_summary.append("Di situasi Your friend is debating a science fact but all their data is wrong., user memilih: Just let it be (F). They will realize it themselves (N), rather than fighting here., dengan poin MBTI: Intuitive & Feeling")
    call ai_react_logic
    return

label show_question_q_c_51_en:
    scene bg stasiun with dissolve
    $ narasi_asli = "(Lost!) Your train ticket is missing! The train leaves in 5 minutes."
    n "(Lost!) Your train ticket is missing!"
    n "The train leaves in 5 minutes."

    menu:
        "(Lost!) Your train ticket is missing! The train leaves in 5 minutes."

        "Check pockets, bags, floor sequentially (S). Don't panic, try to recall (J).":
            $ SN -= 5
            $ JP -= 5
            $ user_choice_text = "Check pockets, bags, floor sequentially (S). Don't panic, try to recall (J)."
            $ last_answer = "Sensing & Judging"
            $ unchosen_choice_text = "Look for the ticket where it might be tucked away (P). It might have fallen on the street (N)."
            $ unchosen_answer = "Intuitive & Perceiving"
            jump show_question_q_c_51_en_A

        "Look for the ticket where it might be tucked away (P). It might have fallen on the street (N).":
            $ SN += 5
            $ JP += 5
            $ user_choice_text = "Look for the ticket where it might be tucked away (P). It might have fallen on the street (N)."
            $ last_answer = "Intuitive & Perceiving"
            $ unchosen_choice_text = "Check pockets, bags, floor sequentially (S). Don't panic, try to recall (J)."
            $ unchosen_answer = "Sensing & Judging"
            jump show_question_q_c_51_en_B


label show_question_q_c_51_en_A:
    $ user_journey_summary.append("Di situasi (Lost!) Your train ticket is missing! The train leaves in 5 minutes., user memilih: Check pockets, bags, floor sequentially (S). Don't panic, try to recall (J)., dengan poin MBTI: Sensing & Judging")
    call ai_react_logic
    return

label show_question_q_c_51_en_B:
    $ user_journey_summary.append("Di situasi (Lost!) Your train ticket is missing! The train leaves in 5 minutes., user memilih: Look for the ticket where it might be tucked away (P). It might have fallen on the street (N)., dengan poin MBTI: Intuitive & Perceiving")
    call ai_react_logic
    return

label show_question_q_c_52_en:
    scene bg dapur with dissolve
    $ narasi_asli = "You are hungry, but the fridge only has eggs, jam, and meat."
    n "You are hungry, but the fridge only has eggs, jam, and meat."

    menu:
        "You are hungry, but the fridge only has eggs, jam, and meat."

        "Just cook a scrambled egg (S). It's definitely delicious and the taste is clear (J).":
            $ SN -= 5
            $ JP -= 5
            $ user_choice_text = "Just cook a scrambled egg (S). It's definitely delicious and the taste is clear (J)."
            $ last_answer = "Sensing & Judging"
            $ unchosen_choice_text = "Mix everything! (N) Who knows, it might become a new masterpiece (P)."
            $ unchosen_answer = "Intuitive & Perceiving"
            jump show_question_q_c_52_en_A

        "Mix everything! (N) Who knows, it might become a new masterpiece (P).":
            $ SN += 5
            $ JP += 5
            $ user_choice_text = "Mix everything! (N) Who knows, it might become a new masterpiece (P)."
            $ last_answer = "Intuitive & Perceiving"
            $ unchosen_choice_text = "Just cook a scrambled egg (S). It's definitely delicious and the taste is clear (J)."
            $ unchosen_answer = "Sensing & Judging"
            jump show_question_q_c_52_en_B


label show_question_q_c_52_en_A:
    $ user_journey_summary.append("Di situasi You are hungry, but the fridge only has eggs, jam, and meat., user memilih: Just cook a scrambled egg (S). It's definitely delicious and the taste is clear (J)., dengan poin MBTI: Sensing & Judging")
    call ai_react_logic
    return

label show_question_q_c_52_en_B:
    $ user_journey_summary.append("Di situasi You are hungry, but the fridge only has eggs, jam, and meat., user memilih: Mix everything! (N) Who knows, it might become a new masterpiece (P)., dengan poin MBTI: Intuitive & Perceiving")
    call ai_react_logic
    return

label show_question_q_c_53_en:
    scene bg room with dissolve
    $ narasi_asli = "You have an exam tomorrow, but you only remembered 1 day before the date."
    n "You have an exam tomorrow, but you only remembered 1 day before the date."

    menu:
        "You have an exam tomorrow, but you only remembered 1 day before the date."

        "Read the summary of chapters (S) according to what is likely to appear on the exam (J).":
            $ SN -= 5
            $ JP -= 5
            $ user_choice_text = "Read the summary of chapters (S) according to what is likely to appear on the exam (J)."
            $ last_answer = "Sensing & Judging"
            $ unchosen_choice_text = "Read only the parts you understand best (N), the rest can be figured out during the exam (P)."
            $ unchosen_answer = "Intuitive & Perceiving"
            jump show_question_q_c_53_en_A

        "Read only the parts you understand best (N), the rest can be figured out during the exam (P).":
            $ SN += 5
            $ JP += 5
            $ user_choice_text = "Read only the parts you understand best (N), the rest can be figured out during the exam (P)."
            $ last_answer = "Intuitive & Perceiving"
            $ unchosen_choice_text = "Read the summary of chapters (S) according to what is likely to appear on the exam (J)."
            $ unchosen_answer = "Sensing & Judging"
            jump show_question_q_c_53_en_B


label show_question_q_c_53_en_A:
    $ user_journey_summary.append("Di situasi You have an exam tomorrow, but you only remembered 1 day before the date., user memilih: Read the summary of chapters (S) according to what is likely to appear on the exam (J)., dengan poin MBTI: Sensing & Judging")
    call ai_react_logic
    return

label show_question_q_c_53_en_B:
    $ user_journey_summary.append("Di situasi You have an exam tomorrow, but you only remembered 1 day before the date., user memilih: Read only the parts you understand best (N), the rest can be figured out during the exam (P)., dengan poin MBTI: Intuitive & Perceiving")
    call ai_react_logic
    return

label show_question_q_c_54_en:
    scene bg kantor with dissolve
    $ narasi_asli = "The boss asks you to work on a 'Secret' project without clear instructions."
    n "The boss asks you to work on a 'Secret' project without clear instructions."

    menu:
        "The boss asks you to work on a 'Secret' project without clear instructions."

        "Gently refuse. 'I need clear details (S) and a deadline (J).'":
            $ SN -= 5
            $ JP -= 5
            $ user_choice_text = "Gently refuse. 'I need clear details (S) and a deadline (J).'"
            $ last_answer = "Sensing & Judging"
            $ unchosen_choice_text = "Accept! 'Ready, I will improvise (N) as I go (P).'"
            $ unchosen_answer = "Intuitive & Perceiving"
            jump show_question_q_c_54_en_A

        "Accept! 'Ready, I will improvise (N) as I go (P).'":
            $ SN += 5
            $ JP += 5
            $ user_choice_text = "Accept! 'Ready, I will improvise (N) as I go (P).'"
            $ last_answer = "Intuitive & Perceiving"
            $ unchosen_choice_text = "Gently refuse. 'I need clear details (S) and a deadline (J).'"
            $ unchosen_answer = "Sensing & Judging"
            jump show_question_q_c_54_en_B


label show_question_q_c_54_en_A:
    $ user_journey_summary.append("Di situasi The boss asks you to work on a 'Secret' project without clear instructions., user memilih: Gently refuse. 'I need clear details (S) and a deadline (J).', dengan poin MBTI: Sensing & Judging")
    call ai_react_logic
    return

label show_question_q_c_54_en_B:
    $ user_journey_summary.append("Di situasi The boss asks you to work on a 'Secret' project without clear instructions., user memilih: Accept! 'Ready, I will improvise (N) as I go (P).', dengan poin MBTI: Intuitive & Perceiving")
    call ai_react_logic
    return

label show_question_q_c_55_en:
    scene bg stasiun with dissolve
    $ narasi_asli = "You want to move cities, but you have too many items!"
    n "You want to move cities, but you have too many items!"

    menu:
        "You want to move cities, but you have too many items!"

        "Sort the items (S). Throw away what you think is less important (J).":
            $ SN -= 5
            $ JP -= 5
            $ user_choice_text = "Sort the items (S). Throw away what you think is less important (J)."
            $ last_answer = "Sensing & Judging"
            $ unchosen_choice_text = "'We don't know, we might need this item later, so bring everything! (N)'. Everything can be arranged again there (P)."
            $ unchosen_answer = "Intuitive & Perceiving"
            jump show_question_q_c_55_en_A

        "'We don't know, we might need this item later, so bring everything! (N)'. Everything can be arranged again there (P).":
            $ SN += 5
            $ JP += 5
            $ user_choice_text = "'We don't know, we might need this item later, so bring everything! (N)'. Everything can be arranged again there (P)."
            $ last_answer = "Intuitive & Perceiving"
            $ unchosen_choice_text = "Sort the items (S). Throw away what you think is less important (J)."
            $ unchosen_answer = "Sensing & Judging"
            jump show_question_q_c_55_en_B


label show_question_q_c_55_en_A:
    $ user_journey_summary.append("Di situasi You want to move cities, but you have too many items!, user memilih: Sort the items (S). Throw away what you think is less important (J)., dengan poin MBTI: Sensing & Judging")
    call ai_react_logic
    return

label show_question_q_c_55_en_B:
    $ user_journey_summary.append("Di situasi You want to move cities, but you have too many items!, user memilih: 'We don't know, we might need this item later, so bring everything! (N)'. Everything can be arranged again there (P)., dengan poin MBTI: Intuitive & Perceiving")
    call ai_react_logic
    return

label show_question_q_c_56_en:
    scene bg room with dissolve
    $ narasi_asli = "Your little sibling accidentally broke mom's favorite vase. He is terrified."
    n "Your little sibling accidentally broke mom's favorite vase."
    n "He is terrified."

    menu:
        "Your little sibling accidentally broke mom's favorite vase. He is terrified."

        "Encourage him to come clean to mom (J) and face it calmly (T).":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "Encourage him to come clean to mom (J) and face it calmly (T)."
            $ last_answer = "Thinking & Judging"
            $ unchosen_choice_text = "Go with him to tell mom (P), stressing it was purely an accident (F)."
            $ unchosen_answer = "Feeling & Perceiving"
            jump show_question_q_c_56_en_A

        "Go with him to tell mom (P), stressing it was purely an accident (F).":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "Go with him to tell mom (P), stressing it was purely an accident (F)."
            $ last_answer = "Feeling & Perceiving"
            $ unchosen_choice_text = "Encourage him to come clean to mom (J) and face it calmly (T)."
            $ unchosen_answer = "Thinking & Judging"
            jump show_question_q_c_56_en_B


label show_question_q_c_56_en_A:
    $ user_journey_summary.append("Di situasi Your little sibling accidentally broke mom's favorite vase. He is terrified., user memilih: Encourage him to come clean to mom (J) and face it calmly (T)., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic
    return

label show_question_q_c_56_en_B:
    $ user_journey_summary.append("Di situasi Your little sibling accidentally broke mom's favorite vase. He is terrified., user memilih: Go with him to tell mom (P), stressing it was purely an accident (F)., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic
    return

label show_question_q_c_57_en:
    scene bg kafe with dissolve
    $ narasi_asli = "You have a strange but innovative business idea. When do you want to start making it happen?"
    n "You have a strange but innovative business idea."
    n "When do you want to start making it happen?"

    menu:
        "You have a strange but innovative business idea. When do you want to start making it happen?"

        "Later, after the profit-loss analysis (T) is 100%% complete (J).":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "Later, after the profit-loss analysis (T) is 100%% complete (J)."
            $ last_answer = "Thinking & Judging"
            $ unchosen_choice_text = "Now! (P) The important thing is that many people like the idea (F)."
            $ unchosen_answer = "Feeling & Perceiving"
            jump show_question_q_c_57_en_A

        "Now! (P) The important thing is that many people like the idea (F).":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "Now! (P) The important thing is that many people like the idea (F)."
            $ last_answer = "Feeling & Perceiving"
            $ unchosen_choice_text = "Later, after the profit-loss analysis (T) is 100%% complete (J)."
            $ unchosen_answer = "Thinking & Judging"
            jump show_question_q_c_57_en_B


label show_question_q_c_57_en_A:
    $ user_journey_summary.append("Di situasi You have a strange but innovative business idea. When do you want to start making it happen?, user memilih: Later, after the profit-loss analysis (T) is 100%% complete (J)., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic
    return

label show_question_q_c_57_en_B:
    $ user_journey_summary.append("Di situasi You have a strange but innovative business idea. When do you want to start making it happen?, user memilih: Now! (P) The important thing is that many people like the idea (F)., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic
    return

label show_question_q_c_58_en:
    scene bg kantor with dissolve
    $ narasi_asli = "Your sports team keeps losing. As captain, what do you say?"
    n "Your sports team keeps losing."
    n "As captain, what do you say?"

    menu:
        "Your sports team keeps losing. As captain, what do you say?"

        "Add scheduled practice (J), focus on fixing measurable things (T).":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "Add scheduled practice (J), focus on fixing measurable things (T)."
            $ last_answer = "Thinking & Judging"
            $ unchosen_choice_text = "Easy, guys (P), keep the spirit up so we stay solid playing together (F)."
            $ unchosen_answer = "Feeling & Perceiving"
            jump show_question_q_c_58_en_A

        "Easy, guys (P), keep the spirit up so we stay solid playing together (F).":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "Easy, guys (P), keep the spirit up so we stay solid playing together (F)."
            $ last_answer = "Feeling & Perceiving"
            $ unchosen_choice_text = "Add scheduled practice (J), focus on fixing measurable things (T)."
            $ unchosen_answer = "Thinking & Judging"
            jump show_question_q_c_58_en_B


label show_question_q_c_58_en_A:
    $ user_journey_summary.append("Di situasi Your sports team keeps losing. As captain, what do you say?, user memilih: Add scheduled practice (J), focus on fixing measurable things (T)., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic
    return

label show_question_q_c_58_en_B:
    $ user_journey_summary.append("Di situasi Your sports team keeps losing. As captain, what do you say?, user memilih: Easy, guys (P), keep the spirit up so we stay solid playing together (F)., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic
    return

label show_question_q_c_59_en:
    scene bg abstrak with dissolve
    $ narasi_asli = "You find an Ancient Weapon during an exploration. What is your focus?"
    n "You find an Ancient Weapon during an exploration."
    n "What is your focus?"

    menu:
        "You find an Ancient Weapon during an exploration. What is your focus?"

        "Its power (T) and its intact condition (J).":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "Its power (T) and its intact condition (J)."
            $ last_answer = "Thinking & Judging"
            $ unchosen_choice_text = "Its legendary story (F) and the mystery of who its former owner was (P)."
            $ unchosen_answer = "Feeling & Perceiving"
            jump show_question_q_c_59_en_A

        "Its legendary story (F) and the mystery of who its former owner was (P).":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "Its legendary story (F) and the mystery of who its former owner was (P)."
            $ last_answer = "Feeling & Perceiving"
            $ unchosen_choice_text = "Its power (T) and its intact condition (J)."
            $ unchosen_answer = "Thinking & Judging"
            jump show_question_q_c_59_en_B


label show_question_q_c_59_en_A:
    $ user_journey_summary.append("Di situasi You find an Ancient Weapon during an exploration. What is your focus?, user memilih: Its power (T) and its intact condition (J)., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic
    return

label show_question_q_c_59_en_B:
    $ user_journey_summary.append("Di situasi You find an Ancient Weapon during an exploration. What is your focus?, user memilih: Its legendary story (F) and the mystery of who its former owner was (P)., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic
    return

label show_question_q_c_60_en:
    scene bg kantor with dissolve
    $ narasi_asli = "There is a new office rule that is inconvenient for employees."
    n "There is a new office rule that is inconvenient for employees."

    menu:
        "There is a new office rule that is inconvenient for employees."

        "Propose an official revision (J). Show the points that are inefficient (T).":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "Propose an official revision (J). Show the points that are inefficient (T)."
            $ last_answer = "Thinking & Judging"
            $ unchosen_choice_text = "Create an emotional petition (F). Ask for leniency on the rules (P)."
            $ unchosen_answer = "Feeling & Perceiving"
            jump show_question_q_c_60_en_A

        "Create an emotional petition (F). Ask for leniency on the rules (P).":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "Create an emotional petition (F). Ask for leniency on the rules (P)."
            $ last_answer = "Feeling & Perceiving"
            $ unchosen_choice_text = "Propose an official revision (J). Show the points that are inefficient (T)."
            $ unchosen_answer = "Thinking & Judging"
            jump show_question_q_c_60_en_B


label show_question_q_c_60_en_A:
    $ user_journey_summary.append("Di situasi There is a new office rule that is inconvenient for employees., user memilih: Propose an official revision (J). Show the points that are inefficient (T)., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic
    return

label show_question_q_c_60_en_B:
    $ user_journey_summary.append("Di situasi There is a new office rule that is inconvenient for employees., user memilih: Create an emotional petition (F). Ask for leniency on the rules (P)., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic
    return
