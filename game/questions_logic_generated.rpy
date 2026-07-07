
# ================= BAHASA: ID =================

label show_question_q_a_01_id:
    scene bg taman with dissolve
    $ narasi_asli = "(Krucuk...) Aduh, lelah sekali setelah jalan-jalan hari ini! Energimu habis dan perutmu lapar. Apa yang tubuhmu butuhkan?"
    n "(Krucuk...) Aduh, lelah sekali setelah jalan-jalan hari ini!"
    n "Energimu habis dan perutmu lapar."
    n "Apa yang tubuhmu butuhkan?"

    menu:
        "(Krucuk...) Aduh, lelah sekali setelah jalan-jalan hari ini! Energimu habis dan perutmu lapar. Apa yang tubuhmu butuhkan?"

        "Pulang ke rumah sendiri dan makan makanan bergizi untuk memulihkan fisik.":
            $ IE -= 5
            $ SN -= 5
            $ user_choice_text = "Pulang ke rumah sendiri dan makan makanan bergizi untuk memulihkan fisik."
            $ last_answer = "Introvert & Sensing"
            jump show_question_q_a_01_id_A

        "Kumpul bareng teman dan bercerita tentang ide perjalanan selanjutnya.":
            $ IE += 5
            $ SN += 5
            $ user_choice_text = "Kumpul bareng teman dan bercerita tentang ide perjalanan selanjutnya."
            $ last_answer = "Extrovert & Intuitive"
            jump show_question_q_a_01_id_B


label show_question_q_a_01_id_A:
    $ user_journey_summary.append("Di situasi (Krucuk...) Aduh, lelah sekali setelah jalan-jalan hari ini! Energimu habis dan perutmu lapar. Apa yang tubuhmu butuhkan?, user memilih: Pulang ke rumah sendiri dan makan makanan bergizi untuk memulihkan fisik., dengan poin MBTI: Introvert & Sensing")
    call ai_react_logic from _call_ai_react_logic
    return

label show_question_q_a_01_id_B:
    $ user_journey_summary.append("Di situasi (Krucuk...) Aduh, lelah sekali setelah jalan-jalan hari ini! Energimu habis dan perutmu lapar. Apa yang tubuhmu butuhkan?, user memilih: Kumpul bareng teman dan bercerita tentang ide perjalanan selanjutnya., dengan poin MBTI: Extrovert & Intuitive")
    call ai_react_logic from _call_ai_react_logic_1
    return

label show_question_q_a_02_id:
    scene bg kafe with dissolve
    $ narasi_asli = "(Kring!) Pintu kafe terbuka! Ada sosok misterius yang gayanya keren sekali masuk. Apa yang pertama kali menarik perhatianmu?"
    n "(Kring!) Pintu kafe terbuka!"
    n "Ada sosok misterius yang gayanya keren sekali masuk."
    n "Apa yang pertama kali menarik perhatianmu?"

    menu:
        "(Kring!) Pintu kafe terbuka! Ada sosok misterius yang gayanya keren sekali masuk. Apa yang pertama kali menarik perhatianmu?"

        "Perhatikan dia dari kursimu, sambil mengamati pergerakannya.":
            $ IE -= 5
            $ SN -= 5
            $ user_choice_text = "Perhatikan dia dari kursimu, sambil mengamati pergerakannya."
            $ last_answer = "Introvert & Sensing"
            jump show_question_q_a_02_id_A

        "Langsung sapa, dan tanya dia hendak pergi kemana dengan pakaian seperti itu.":
            $ IE += 5
            $ SN += 5
            $ user_choice_text = "Langsung sapa, dan tanya dia hendak pergi kemana dengan pakaian seperti itu."
            $ last_answer = "Extrovert & Intuitive"
            jump show_question_q_a_02_id_B


label show_question_q_a_02_id_A:
    $ user_journey_summary.append("Di situasi (Kring!) Pintu kafe terbuka! Ada sosok misterius yang gayanya keren sekali masuk. Apa yang pertama kali menarik perhatianmu? user memilih: Perhatikan dia dari kursimu, sambil mengamati pergerakannya., dengan poin MBTI: Introvert & Sensing")
    call ai_react_logic from _call_ai_react_logic_2
    return

label show_question_q_a_02_id_B:
    $ user_journey_summary.append("Di situasi (Kring!) Pintu kafe terbuka! Ada sosok misterius yang gayanya keren sekali masuk. Apa yang pertama kali menarik perhatianmu? user memilih: Langsung sapa, dan tanya dia hendak pergi kemana dengan pakaian seperti itu., dengan poin MBTI: Extrovert & Intuitive")
    call ai_react_logic from _call_ai_react_logic_3
    return

label show_question_q_a_03_id:
    scene bg kantor with dissolve
    $ narasi_asli = "(Gubrak!) Bos memberi tumpukan job setinggi gunung! Mustahil selesai sendirian hari ini."
    n "(Gubrak!) Bos memberi tumpukan job setinggi gunung!"
    n "Mustahil selesai sendirian hari ini."

    menu:
        "(Gubrak!) Bos memberi tumpukan job setinggi gunung! Mustahil selesai sendirian hari ini."

        "Panggil seluruh tim untuk bagi tugas fisik sekarang juga.":
            $ IE += 5
            $ SN -= 5
            $ user_choice_text = "Panggil seluruh tim untuk bagi tugas fisik sekarang juga."
            $ last_answer = "Extrovert & Sensing"
            jump show_question_q_a_03_id_A

        "Panggil rekan kerja dekat untuk coba program bantuan yang baru kamu kembangkan":
            $ IE -= 5
            $ SN += 5
            $ user_choice_text = "Panggil rekan kerja dekat untuk coba program bantuan yang baru kamu kembangkan"
            $ last_answer = "Introvert & Intuitive"
            jump show_question_q_a_03_id_B


label show_question_q_a_03_id_A:
    $ user_journey_summary.append("Di situasi (Gubrak!) Bos memberi tumpukan job setinggi gunung! Mustahil selesai sendirian hari ini., user memilih: Panggil seluruh tim untuk bagi tugas fisik sekarang juga., dengan poin MBTI: Extrovert & Sensing")
    call ai_react_logic from _call_ai_react_logic_4
    return

label show_question_q_a_03_id_B:
    $ user_journey_summary.append("Di situasi (Gubrak!) Bos memberi tumpukan job setinggi gunung! Mustahil selesai sendirian hari ini., user memilih: Panggil rekan kerja dekat untuk coba program bantuan yang baru kamu kembangkan, dengan poin MBTI: Introvert & Intuitive")
    call ai_react_logic from _call_ai_react_logic_5
    return

label show_question_q_a_04_id:
    scene bg dapur with dissolve
    $ narasi_asli = "(Waduh!) Kamu mau masak makanan spesial, tapi satu bahan utamanya habis, kamu lupa membelinya kemarin."
    n "(Waduh!) Kamu mau masak makanan spesial, tapi satu bahan utamanya habis, kamu lupa membelinya kemarin."

    menu:
        "(Waduh!) Kamu mau masak makanan spesial, tapi satu bahan utamanya habis, kamu lupa membelinya kemarin."

        "Hubungi dan tanya teman untuk meminta bahan mentah yang kurang.":
            $ IE += 5
            $ SN -= 5
            $ user_choice_text = "Hubungi dan tanya teman untuk meminta bahan mentah yang kurang."
            $ last_answer = "Extrovert & Sensing"
            jump show_question_q_a_04_id_A

        "Tetap di dapur dan coba eksperimen menggantinya dengan bahan lain.":
            $ IE -= 5
            $ SN += 5
            $ user_choice_text = "Tetap di dapur dan coba eksperimen menggantinya dengan bahan lain."
            $ last_answer = "Introvert & Intuitive"
            jump show_question_q_a_04_id_B


label show_question_q_a_04_id_A:
    $ user_journey_summary.append("Di situasi (Waduh!) Kamu mau masak makanan spesial, tapi satu bahan utamanya habis, kamu lupa membelinya kemarin., user memilih: Hubungi dan tanya teman untuk meminta bahan mentah yang kurang., dengan poin MBTI: Extrovert & Sensing")
    call ai_react_logic from _call_ai_react_logic_6
    return

label show_question_q_a_04_id_B:
    $ user_journey_summary.append("Di situasi (Waduh!) Kamu mau masak makanan spesial, tapi satu bahan utamanya habis, kamu lupa membelinya kemarin., user memilih: Tetap di dapur dan coba eksperimen menggantinya dengan bahan lain., dengan poin MBTI: Introvert & Intuitive")
    call ai_react_logic from _call_ai_react_logic_7
    return

label show_question_q_a_05_id:
    scene bg room with dissolve
    $ narasi_asli = "Ada poster 'Berita Hangat!' yang bikin heboh satu desa! Semua orang membicarakannya."
    n "Ada poster 'Berita Hangat!' yang bikin heboh satu desa!"
    n "Semua orang membicarakannya."

    menu:
        "Ada poster 'Berita Hangat!' yang bikin heboh satu desa! Semua orang membicarakannya."

        "Ikut komentar dengan warga lainnya dan cari bukti kejadiannya.":
            $ IE += 5
            $ SN -= 5
            $ user_choice_text = "Ikut komentar dengan warga lainnya dan cari bukti kejadiannya."
            $ last_answer = "Extrovert & Sensing"
            jump show_question_q_a_05_id_A

        "Baca dan amati, coba bayangkan apa yang sebenarnya terjadi.":
            $ IE -= 5
            $ SN += 5
            $ user_choice_text = "Baca dan amati, coba bayangkan apa yang sebenarnya terjadi."
            $ last_answer = "Introvert & Intuitive"
            jump show_question_q_a_05_id_B


label show_question_q_a_05_id_A:
    $ user_journey_summary.append("Di situasi Ada poster 'Berita Hangat!' yang bikin heboh satu desa! Semua orang membicarakannya., user memilih: Ikut komentar dengan warga lainnya dan cari bukti kejadiannya., dengan poin MBTI: Extrovert & Sensing")
    call ai_react_logic from _call_ai_react_logic_8
    return

label show_question_q_a_05_id_B:
    $ user_journey_summary.append("Di situasi Ada poster 'Berita Hangat!' yang bikin heboh satu desa! Semua orang membicarakannya., user memilih: Baca dan amati, coba bayangkan apa yang sebenarnya terjadi., dengan poin MBTI: Introvert & Intuitive")
    call ai_react_logic from _call_ai_react_logic_9
    return

label show_question_q_a_06_id:
    scene bg kantor with dissolve
    $ narasi_asli = "(Gawat!) Teman satu timmu tidak sengaja menghilangkan barang berharga milik perusahaan! Dia terlihat mau menangis."
    n "(Gawat!) Teman satu timmu tidak sengaja menghilangkan barang berharga milik perusahaan!"
    n "Dia terlihat mau menangis."

    menu:
        "(Gawat!) Teman satu timmu tidak sengaja menghilangkan barang berharga milik perusahaan! Dia terlihat mau menangis."

        "Tegur dia langsung agar dia tanggung jawab.":
            $ IE += 5
            $ TF -= 5
            $ user_choice_text = "Tegur dia langsung agar dia tanggung jawab."
            $ last_answer = "Extrovert & Thinking"
            jump show_question_q_a_06_id_A

        "Tarik dia menjauh dan bilang 'gapapa, kita cari sama-sama jalan keluarnya'":
            $ IE -= 5
            $ TF += 5
            $ user_choice_text = "Tarik dia menjauh dan bilang 'gapapa, kita cari sama-sama jalan keluarnya'"
            $ last_answer = "Introvert & Feeling"
            jump show_question_q_a_06_id_B


label show_question_q_a_06_id_A:
    $ user_journey_summary.append("Di situasi (Gawat!) Teman satu timmu tidak sengaja menghilangkan barang berharga milik perusahaan! Dia terlihat mau menangis., user memilih: Tegur dia langsung agar dia tanggung jawab., dengan poin MBTI: Extrovert & Thinking")
    call ai_react_logic from _call_ai_react_logic_10
    return

label show_question_q_a_06_id_B:
    $ user_journey_summary.append("Di situasi (Gawat!) Teman satu timmu tidak sengaja menghilangkan barang berharga milik perusahaan! Dia terlihat mau menangis., user memilih: Tarik dia menjauh dan bilang 'gapapa, kita cari sama-sama jalan keluarnya', dengan poin MBTI: Introvert & Feeling")
    call ai_react_logic from _call_ai_react_logic_11
    return

label show_question_q_a_07_id:
    scene bg taman with dissolve
    $ narasi_asli = "Ada peraturan baru di taman: 'Dilarang Tertawa Keras'."
    n "Ada peraturan baru di taman: 'Dilarang Tertawa Keras'."

    menu:
        "Ada peraturan baru di taman: 'Dilarang Tertawa Keras'."

        "Protes ke petugas karena aturannya tidak masuk akal.":
            $ IE += 5
            $ TF -= 5
            $ user_choice_text = "Protes ke petugas karena aturannya tidak masuk akal."
            $ last_answer = "Extrovert & Thinking"
            jump show_question_q_a_07_id_A

        "Diam saja, karena mungkin benar, hal tersebut bisa merusak suasana yang damai.":
            $ IE -= 5
            $ TF += 5
            $ user_choice_text = "Diam saja, karena mungkin benar, hal tersebut bisa merusak suasana yang damai."
            $ last_answer = "Introvert & Feeling"
            jump show_question_q_a_07_id_B


label show_question_q_a_07_id_A:
    $ user_journey_summary.append("Di situasi Ada peraturan baru di taman: 'Dilarang Tertawa Keras'., user memilih: Protes ke petugas karena aturannya tidak masuk akal., dengan poin MBTI: Extrovert & Thinking")
    call ai_react_logic from _call_ai_react_logic_12
    return

label show_question_q_a_07_id_B:
    $ user_journey_summary.append("Di situasi Ada peraturan baru di taman: 'Dilarang Tertawa Keras'., user memilih: Diam saja, karena mungkin benar, hal tersebut bisa merusak suasana yang damai., dengan poin MBTI: Introvert & Feeling")
    call ai_react_logic from _call_ai_react_logic_13
    return

label show_question_q_a_08_id:
    scene bg kafe with dissolve
    $ narasi_asli = "Pengunjung di meja sebelah terlihat sangat galau dan menghela napas panjang..."
    n "Pengunjung di meja sebelah terlihat sangat galau dan menghela napas panjang..."

    menu:
        "Pengunjung di meja sebelah terlihat sangat galau dan menghela napas panjang..."

        "Coba dekati dan tanya langsung, analisis masalahnya agar ditemukan jalan keluarnya.":
            $ IE += 5
            $ TF -= 5
            $ user_choice_text = "Coba dekati dan tanya langsung, analisis masalahnya agar ditemukan jalan keluarnya."
            $ last_answer = "Extrovert & Thinking"
            jump show_question_q_a_08_id_A

        "Kasih tisu diam-diam karena kasihan melihatnya.":
            $ IE -= 5
            $ TF += 5
            $ user_choice_text = "Kasih tisu diam-diam karena kasihan melihatnya."
            $ last_answer = "Introvert & Feeling"
            jump show_question_q_a_08_id_B


label show_question_q_a_08_id_A:
    $ user_journey_summary.append("Di situasi Pengunjung di meja sebelah terlihat sangat galau dan menghela napas panjang..., user memilih: Coba dekati dan tanya langsung, analisis masalahnya agar ditemukan jalan keluarnya., dengan poin MBTI: Extrovert & Thinking")
    call ai_react_logic from _call_ai_react_logic_14
    return

label show_question_q_a_08_id_B:
    $ user_journey_summary.append("Di situasi Pengunjung di meja sebelah terlihat sangat galau dan menghela napas panjang..., user memilih: Kasih tisu diam-diam karena kasihan melihatnya., dengan poin MBTI: Introvert & Feeling")
    call ai_react_logic from _call_ai_react_logic_15
    return

label show_question_q_a_09_id:
    scene bg kantor with dissolve
    $ narasi_asli = "Kapten kapal membagikan harta karun, tapi bagianmu paling sedikit! Tidak adil!"
    n "Kapten kapal membagikan harta karun, tapi bagianmu paling sedikit!"
    n "Tidak adil!"

    menu:
        "Kapten kapal membagikan harta karun, tapi bagianmu paling sedikit! Tidak adil!"

        "Debat dengan Kapten karena hitungannya salah.":
            $ IE += 5
            $ TF -= 5
            $ user_choice_text = "Debat dengan Kapten karena hitungannya salah."
            $ last_answer = "Extrovert & Thinking"
            jump show_question_q_a_09_id_A

        "Terima saja karena mungkin kapten sedang memerlukannya.":
            $ IE -= 5
            $ TF += 5
            $ user_choice_text = "Terima saja karena mungkin kapten sedang memerlukannya."
            $ last_answer = "Introvert & Feeling"
            jump show_question_q_a_09_id_B


label show_question_q_a_09_id_A:
    $ user_journey_summary.append("Di situasi Kapten kapal membagikan harta karun, tapi bagianmu paling sedikit! Tidak adil!, user memilih: Debat dengan Kapten karena hitungannya salah., dengan poin MBTI: Extrovert & Thinking")
    call ai_react_logic from _call_ai_react_logic_16
    return

label show_question_q_a_09_id_B:
    $ user_journey_summary.append("Di situasi Kapten kapal membagikan harta karun, tapi bagianmu paling sedikit! Tidak adil!, user memilih: Terima saja karena mungkin kapten sedang memerlukannya., dengan poin MBTI: Introvert & Feeling")
    call ai_react_logic from _call_ai_react_logic_17
    return

label show_question_q_a_10_id:
    scene bg abstrak with dissolve
    $ narasi_asli = "(Suara Misterius) 'Pilihlah takdirmu... Pintu Kiri atau Pintu Kanan?' Tanpa adanya petunjuk sama sekali!"
    n "(Suara Misterius) 'Pilihlah takdirmu..."
    n "Pintu Kiri atau Pintu Kanan?' Tanpa adanya petunjuk sama sekali!"

    menu:
        "(Suara Misterius) 'Pilihlah takdirmu... Pintu Kiri atau Pintu Kanan?' Tanpa adanya petunjuk sama sekali!"

        "Tanya kembali suara itu 'kira-kira, mana pintu yang paling aman?'":
            $ IE += 5
            $ TF -= 5
            $ user_choice_text = "Tanya kembali suara itu 'kira-kira, mana pintu yang paling aman?'"
            $ last_answer = "Extrovert & Thinking"
            jump show_question_q_a_10_id_A

        "Pejamkan mata dan ikuti kata hati.":
            $ IE -= 5
            $ TF += 5
            $ user_choice_text = "Pejamkan mata dan ikuti kata hati."
            $ last_answer = "Introvert & Feeling"
            jump show_question_q_a_10_id_B


label show_question_q_a_10_id_A:
    $ user_journey_summary.append("Di situasi (Suara Misterius) 'Pilihlah takdirmu... Pintu Kiri atau Pintu Kanan?' Tanpa adanya petunjuk sama sekali!, user memilih: Tanya kembali suara itu 'kira-kira, mana pintu yang paling aman?', dengan poin MBTI: Extrovert & Thinking")
    call ai_react_logic from _call_ai_react_logic_18
    return

label show_question_q_a_10_id_B:
    $ user_journey_summary.append("Di situasi (Suara Misterius) 'Pilihlah takdirmu... Pintu Kiri atau Pintu Kanan?' Tanpa adanya petunjuk sama sekali!, user memilih: Pejamkan mata dan ikuti kata hati., dengan poin MBTI: Introvert & Feeling")
    call ai_react_logic from _call_ai_react_logic_19
    return

label show_question_q_a_11_id:
    scene bg kafe with dissolve
    $ narasi_asli = "Tiba-tiba temanmu menarik tanganmu. 'Ayo kita jalan-jalan ke pantai SEKARANG JUGA!'"
    n "Tiba-tiba temanmu menarik tanganmu."
    n "'Ayo kita jalan-jalan ke pantai SEKARANG JUGA!'"

    menu:
        "Tiba-tiba temanmu menarik tanganmu. 'Ayo kita jalan-jalan ke pantai SEKARANG JUGA!'"

        "Gas! urusan nanti dipikir belakangan.":
            $ IE += 5
            $ JP += 5
            $ user_choice_text = "Gas! urusan nanti dipikir belakangan."
            $ last_answer = "Extrovert & Perceiving"
            jump show_question_q_a_11_id_A

        "Tolak karena harus cek jadwal dulu.":
            $ IE -= 5
            $ JP -= 5
            $ user_choice_text = "Tolak karena harus cek jadwal dulu."
            $ last_answer = "Introvert & Judging"
            jump show_question_q_a_11_id_B


label show_question_q_a_11_id_A:
    $ user_journey_summary.append("Di situasi Tiba-tiba temanmu menarik tanganmu. 'Ayo kita jalan-jalan ke pantai SEKARANG JUGA!', user memilih: Gas! urusan nanti dipikir belakangan., dengan poin MBTI: Extrovert & Perceiving")
    call ai_react_logic from _call_ai_react_logic_20
    return

label show_question_q_a_11_id_B:
    $ user_journey_summary.append("Di situasi Tiba-tiba temanmu menarik tanganmu. 'Ayo kita jalan-jalan ke pantai SEKARANG JUGA!', user memilih: Tolak karena harus cek jadwal dulu., dengan poin MBTI: Introvert & Judging")
    call ai_react_logic from _call_ai_react_logic_21
    return

label show_question_q_a_12_id:
    scene bg stasiun with dissolve
    $ narasi_asli = "(Tuutt! Tuut!) Kereta terakhir sudah berangkat meninggalkanmu! Kamu ketinggalan kereta yang harusnya kamu naiki untuk pulang!"
    n "(Tuutt! Tuut!)"
    n "Kereta terakhir sudah berangkat meninggalkanmu!"
    n "Kamu ketinggalan kereta yang harusnya kamu naiki untuk pulang!"

    menu:
        "(Tuutt! Tuut!) Kereta terakhir sudah berangkat meninggalkanmu! Kamu ketinggalan kereta yang harusnya kamu naiki untuk pulang!"

        "Asik! kita bisa bebas menjelajahi kota!.":
            $ IE += 5
            $ JP += 5
            $ user_choice_text = "Asik! kita bisa bebas menjelajahi kota!."
            $ last_answer = "Extrovert & Perceiving"
            jump show_question_q_a_12_id_A

        "Waduh! seharusnya aku datang lebih awal.":
            $ IE -= 5
            $ JP -= 5
            $ user_choice_text = "Waduh! seharusnya aku datang lebih awal."
            $ last_answer = "Introvert & Judging"
            jump show_question_q_a_12_id_B


label show_question_q_a_12_id_A:
    $ user_journey_summary.append("Di situasi (Tuutt! Tuut!) Kereta terakhir sudah berangkat meninggalkanmu! Kamu ketinggalan kereta yang harusnya kamu naiki untuk pulang!, user memilih: Asik! kita bisa bebas menjelajahi kota!., dengan poin MBTI: Extrovert & Perceiving")
    call ai_react_logic from _call_ai_react_logic_22
    return

label show_question_q_a_12_id_B:
    $ user_journey_summary.append("Di situasi (Tuutt! Tuut!) Kereta terakhir sudah berangkat meninggalkanmu! Kamu ketinggalan kereta yang harusnya kamu naiki untuk pulang!, user memilih: Waduh! seharusnya aku datang lebih awal., dengan poin MBTI: Introvert & Judging")
    call ai_react_logic from _call_ai_react_logic_23
    return

label show_question_q_a_13_id:
    scene bg taman with dissolve
    $ narasi_asli = "Kamu ditunjuk jadi pemimpin piknik besok. Apa rencanamu?"
    n "Kamu ditunjuk jadi pemimpin piknik besok."
    n "Apa rencanamu?"

    menu:
        "Kamu ditunjuk jadi pemimpin piknik besok. Apa rencanamu?"

        "Ajak semua teman! bebas mau bawa apa saja.":
            $ IE += 5
            $ JP += 5
            $ user_choice_text = "Ajak semua teman! bebas mau bawa apa saja."
            $ last_answer = "Extrovert & Perceiving"
            jump show_question_q_a_13_id_A

        "Coba pilih menu terbaik menurutmu dan tentukan waktu pasti.":
            $ IE -= 5
            $ JP -= 5
            $ user_choice_text = "Coba pilih menu terbaik menurutmu dan tentukan waktu pasti."
            $ last_answer = "Introvert & Judging"
            jump show_question_q_a_13_id_B


label show_question_q_a_13_id_A:
    $ user_journey_summary.append("Di situasi Kamu ditunjuk jadi pemimpin piknik besok. Apa rencanamu?, user memilih: Ajak semua teman! bebas mau bawa apa saja., dengan poin MBTI: Extrovert & Perceiving")
    call ai_react_logic from _call_ai_react_logic_24
    return

label show_question_q_a_13_id_B:
    $ user_journey_summary.append("Di situasi Kamu ditunjuk jadi pemimpin piknik besok. Apa rencanamu?, user memilih: Coba pilih menu terbaik menurutmu dan tentukan waktu pasti., dengan poin MBTI: Introvert & Judging")
    call ai_react_logic from _call_ai_react_logic_25
    return

label show_question_q_a_14_id:
    scene bg room with dissolve
    $ narasi_asli = "Kamu melihat kamarmu. Rasanya auranya sudah basi dan membosankan."
    n "Kamu melihat kamarmu."
    n "Rasanya auranya sudah basi dan membosankan."

    menu:
        "Kamu melihat kamarmu. Rasanya auranya sudah basi dan membosankan."

        "Ganti cat dan ubah barang-barang di kamar sekarang.":
            $ IE += 5
            $ JP += 5
            $ user_choice_text = "Ganti cat dan ubah barang-barang di kamar sekarang."
            $ last_answer = "Extrovert & Perceiving"
            jump show_question_q_a_14_id_A

        "Biarkan saja karena posisi ini sudah efisien.":
            $ IE -= 5
            $ JP -= 5
            $ user_choice_text = "Biarkan saja karena posisi ini sudah efisien."
            $ last_answer = "Introvert & Judging"
            jump show_question_q_a_14_id_B


label show_question_q_a_14_id_A:
    $ user_journey_summary.append("Di situasi Kamu melihat kamarmu. Rasanya auranya sudah basi dan membosankan., user memilih: Ganti cat dan ubah barang-barang di kamar sekarang., dengan poin MBTI: Extrovert & Perceiving")
    call ai_react_logic from _call_ai_react_logic_26
    return

label show_question_q_a_14_id_B:
    $ user_journey_summary.append("Di situasi Kamu melihat kamarmu. Rasanya auranya sudah basi dan membosankan., user memilih: Biarkan saja karena posisi ini sudah efisien., dengan poin MBTI: Introvert & Judging")
    call ai_react_logic from _call_ai_react_logic_27
    return

label show_question_q_a_15_id:
    scene bg stasiun with dissolve
    $ narasi_asli = "Kamu mampir di toko oleh-oleh stasiun. Banyak barang lucu dan menarik!"
    n "Kamu mampir di toko oleh-oleh stasiun."
    n "Banyak barang lucu dan menarik!"

    menu:
        "Kamu mampir di toko oleh-oleh stasiun. Banyak barang lucu dan menarik!"

        "Minta saran penjual dan beli barang yang pertama kali terlihat.":
            $ IE += 5
            $ JP += 5
            $ user_choice_text = "Minta saran penjual dan beli barang yang pertama kali terlihat."
            $ last_answer = "Extrovert & Perceiving"
            jump show_question_q_a_15_id_A

        "Coba berkeliling dan beli sesuai kebutuhan.":
            $ IE -= 5
            $ JP -= 5
            $ user_choice_text = "Coba berkeliling dan beli sesuai kebutuhan."
            $ last_answer = "Introvert & Judging"
            jump show_question_q_a_15_id_B


label show_question_q_a_15_id_A:
    $ user_journey_summary.append("Di situasi Kamu mampir di toko oleh-oleh stasiun. Banyak barang lucu dan menarik!, user memilih: Minta saran penjual dan beli barang yang pertama kali terlihat., dengan poin MBTI: Extrovert & Perceiving")
    call ai_react_logic from _call_ai_react_logic_28
    return

label show_question_q_a_15_id_B:
    $ user_journey_summary.append("Di situasi Kamu mampir di toko oleh-oleh stasiun. Banyak barang lucu dan menarik!, user memilih: Coba berkeliling dan beli sesuai kebutuhan., dengan poin MBTI: Introvert & Judging")
    call ai_react_logic from _call_ai_react_logic_29
    return

label show_question_q_a_16_id:
    scene bg kantor with dissolve
    $ narasi_asli = "Temanmu marah-marah padamu tanpa alasan yang jelas! Mukanya merah padam!"
    n "Temanmu marah-marah padamu tanpa alasan yang jelas!"
    n "Mukanya merah padam!"

    menu:
        "Temanmu marah-marah padamu tanpa alasan yang jelas! Mukanya merah padam!"

        "Redam amarahnya dan jelaskan buktinya dulu.":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "Redam amarahnya dan jelaskan buktinya dulu."
            $ last_answer = "Thinking & Judging"
            jump show_question_q_a_16_id_A

        "'Kok aku dimarahin? Apa mungkin aku ada salah?'.":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "'Kok aku dimarahin? Apa mungkin aku ada salah?'."
            $ last_answer = "Feeling & Perceiving"
            jump show_question_q_a_16_id_B


label show_question_q_a_16_id_A:
    $ user_journey_summary.append("Di situasi Temanmu marah-marah padamu tanpa alasan yang jelas! Mukanya merah padam!, user memilih: Redam amarahnya dan jelaskan buktinya dulu., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic from _call_ai_react_logic_30
    return

label show_question_q_a_16_id_B:
    $ user_journey_summary.append("Di situasi Temanmu marah-marah padamu tanpa alasan yang jelas! Mukanya merah padam!, user memilih: 'Kok aku dimarahin? Apa mungkin aku ada salah?'., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic from _call_ai_react_logic_31
    return

label show_question_q_a_17_id:
    scene bg dapur with dissolve
    $ narasi_asli = "Kalian sedang membuat kue ulang tahun, tapi hasilnya gosong dan kurang bagus."
    n "Kalian sedang membuat kue ulang tahun, tapi hasilnya gosong dan kurang bagus."

    menu:
        "Kalian sedang membuat kue ulang tahun, tapi hasilnya gosong dan kurang bagus."

        "Buang! dan coba bikin ulang lagi sesuai resep.":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "Buang! dan coba bikin ulang lagi sesuai resep."
            $ last_answer = "Thinking & Judging"
            jump show_question_q_a_17_id_A

        "Gapapa tampilannya kurang bagus, tapi dibuat dengan penuh perasaan.":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "Gapapa tampilannya kurang bagus, tapi dibuat dengan penuh perasaan."
            $ last_answer = "Feeling & Perceiving"
            jump show_question_q_a_17_id_B


label show_question_q_a_17_id_A:
    $ user_journey_summary.append("Di situasi Kalian sedang membuat kue ulang tahun, tapi hasilnya gosong dan kurang bagus., user memilih: Buang! dan coba bikin ulang lagi sesuai resep., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic from _call_ai_react_logic_32
    return

label show_question_q_a_17_id_B:
    $ user_journey_summary.append("Di situasi Kalian sedang membuat kue ulang tahun, tapi hasilnya gosong dan kurang bagus., user memilih: Gapapa tampilannya kurang bagus, tapi dibuat dengan penuh perasaan., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic from _call_ai_react_logic_33
    return

label show_question_q_a_18_id:
    scene bg abstrak with dissolve
    $ narasi_asli = "Kamu menemukan sebuah Lukisan Pemandangan Misterius. Kira-kira apa yang membuatnya bagus?"
    n "Kamu menemukan sebuah Lukisan Pemandangan Misterius."
    n "Kira-kira apa yang membuatnya bagus?"

    menu:
        "Kamu menemukan sebuah Lukisan Pemandangan Misterius. Kira-kira apa yang membuatnya bagus?"

        "Komposisi warnanya, tekniknya, semua sempurna dan rapi!.":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "Komposisi warnanya, tekniknya, semua sempurna dan rapi!."
            $ last_answer = "Thinking & Judging"
            jump show_question_q_a_18_id_A

        "Lukisan ini memiliki emosi yang dalam dan juga indah.":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "Lukisan ini memiliki emosi yang dalam dan juga indah."
            $ last_answer = "Feeling & Perceiving"
            jump show_question_q_a_18_id_B


label show_question_q_a_18_id_A:
    $ user_journey_summary.append("Di situasi Kamu menemukan sebuah Lukisan Pemandangan Misterius. Kira-kira apa yang membuatnya bagus?, user memilih: Komposisi warnanya, tekniknya, semua sempurna dan rapi!., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic from _call_ai_react_logic_34
    return

label show_question_q_a_18_id_B:
    $ user_journey_summary.append("Di situasi Kamu menemukan sebuah Lukisan Pemandangan Misterius. Kira-kira apa yang membuatnya bagus?, user memilih: Lukisan ini memiliki emosi yang dalam dan juga indah., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic from _call_ai_react_logic_35
    return

label show_question_q_a_19_id:
    scene bg abstrak with dissolve
    $ narasi_asli = "Ada satu tombol merah. Kalau ditekan, kamu dapat uang tapi satu orang asing akan sedih."
    n "Ada satu tombol merah."
    n "Kalau ditekan, kamu dapat uang tapi satu orang asing akan sedih."

    menu:
        "Ada satu tombol merah. Kalau ditekan, kamu dapat uang tapi satu orang asing akan sedih."

        "Tekan tombolnya, karena lumayan uangnya berguna.":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "Tekan tombolnya, karena lumayan uangnya berguna."
            $ last_answer = "Thinking & Judging"
            jump show_question_q_a_19_id_A

        "Jangan tekan karena gak tega sama orang asing itu.":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "Jangan tekan karena gak tega sama orang asing itu."
            $ last_answer = "Feeling & Perceiving"
            jump show_question_q_a_19_id_B


label show_question_q_a_19_id_A:
    $ user_journey_summary.append("Di situasi Ada satu tombol merah. Kalau ditekan, kamu dapat uang tapi satu orang asing akan sedih., user memilih: Tekan tombolnya, karena lumayan uangnya berguna., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic from _call_ai_react_logic_36
    return

label show_question_q_a_19_id_B:
    $ user_journey_summary.append("Di situasi Ada satu tombol merah. Kalau ditekan, kamu dapat uang tapi satu orang asing akan sedih., user memilih: Jangan tekan karena gak tega sama orang asing itu., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic from _call_ai_react_logic_37
    return

label show_question_q_a_20_id:
    scene bg kantor with dissolve
    $ narasi_asli = "Tim kamu malas-malasan hari ini. Mereka tidak memiliki semangat sama sekali."
    n "Tim kamu malas-malasan hari ini."
    n "Mereka tidak memiliki semangat sama sekali."

    menu:
        "Tim kamu malas-malasan hari ini. Mereka tidak memiliki semangat sama sekali."

        "Beri target dan janjikan pemberian bonus.":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "Beri target dan janjikan pemberian bonus."
            $ last_answer = "Thinking & Judging"
            jump show_question_q_a_20_id_A

        "Ayolah teman! kita lakukan demi kebaikan.":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "Ayolah teman! kita lakukan demi kebaikan."
            $ last_answer = "Feeling & Perceiving"
            jump show_question_q_a_20_id_B


label show_question_q_a_20_id_A:
    $ user_journey_summary.append("Di situasi Tim kamu malas-malasan hari ini. Mereka tidak memiliki semangat sama sekali., user memilih: Beri target dan janjikan pemberian bonus., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic from _call_ai_react_logic_38
    return

label show_question_q_a_20_id_B:
    $ user_journey_summary.append("Di situasi Tim kamu malas-malasan hari ini. Mereka tidak memiliki semangat sama sekali., user memilih: Ayolah teman! kita lakukan demi kebaikan., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic from _call_ai_react_logic_39
    return

label show_question_q_b_21_id:
    scene bg dapur with dissolve
    $ narasi_asli = "(Bingung!) Kamu menemukan Buku resep kuno yang bentuknya aneh. Saat itu kamu lapar sekali. Kira-kira bagaimana cara masaknya?"
    n "(Bingung!) Kamu menemukan Buku resep kuno yang bentuknya aneh."
    n "Saat itu kamu lapar sekali."
    n "Kira-kira bagaimana cara masaknya?"

    menu:
        "(Bingung!) Kamu menemukan Buku resep kuno yang bentuknya aneh. Saat itu kamu lapar sekali. Kira-kira bagaimana cara masaknya?"

        "Baca sendiri dengan tenang dan ikuti instruksi takarannya secara presisi.":
            $ IE -= 5
            $ SN -= 5
            $ user_choice_text = "Baca sendiri dengan tenang dan ikuti instruksi takarannya secara presisi."
            $ last_answer = "Introvert & Sensing"
            jump show_question_q_b_21_id_A

        "Panggil teman-teman untuk menebak dan meracik rasa baru.":
            $ IE += 5
            $ SN += 5
            $ user_choice_text = "Panggil teman-teman untuk menebak dan meracik rasa baru."
            $ last_answer = "Extrovert & Intuitive"
            jump show_question_q_b_21_id_B


label show_question_q_b_21_id_A:
    $ user_journey_summary.append("Di situasi (Bingung!) Kamu menemukan Buku resep kuno yang bentuknya aneh. Saat itu kamu lapar sekali. Kira-kira bagaimana cara masaknya?, user memilih: Baca sendiri dengan tenang dan ikuti instruksi takarannya secara presisi., dengan poin MBTI: Introvert & Sensing")
    call ai_react_logic from _call_ai_react_logic_40
    return

label show_question_q_b_21_id_B:
    $ user_journey_summary.append("Di situasi (Bingung!) Kamu menemukan Buku resep kuno yang bentuknya aneh. Saat itu kamu lapar sekali. Kira-kira bagaimana cara masaknya?, user memilih: Panggil teman-teman untuk menebak dan meracik rasa baru., dengan poin MBTI: Extrovert & Intuitive")
    call ai_react_logic from _call_ai_react_logic_41
    return

label show_question_q_b_22_id:
    scene bg kantor with dissolve
    $ narasi_asli = "(Mendadak!) Klien datang minta ide yang fresh sekarang juga! sedangkan Kamu belum menyiapkan materi apapun."
    n "(Mendadak!) Klien datang minta ide yang fresh sekarang juga!"
    n "sedangkan Kamu belum menyiapkan materi apapun."

    menu:
        "(Mendadak!) Klien datang minta ide yang fresh sekarang juga! sedangkan Kamu belum menyiapkan materi apapun."

        "Minta waktu menyendiri untuk menyusun fakta dan data yang ada.":
            $ IE -= 5
            $ SN -= 5
            $ user_choice_text = "Minta waktu menyendiri untuk menyusun fakta dan data yang ada."
            $ last_answer = "Introvert & Sensing"
            jump show_question_q_b_22_id_A

        "Ajak diskusi santai dan sampaikan idemu tentang visi masa depan.":
            $ IE += 5
            $ SN += 5
            $ user_choice_text = "Ajak diskusi santai dan sampaikan idemu tentang visi masa depan."
            $ last_answer = "Extrovert & Intuitive"
            jump show_question_q_b_22_id_B


label show_question_q_b_22_id_A:
    $ user_journey_summary.append("Di situasi (Mendadak!) Klien datang minta ide yang fresh sekarang juga! sedangkan Kamu belum menyiapkan materi apapun., user memilih: Minta waktu menyendiri untuk menyusun fakta dan data yang ada., dengan poin MBTI: Introvert & Sensing")
    call ai_react_logic from _call_ai_react_logic_42
    return

label show_question_q_b_22_id_B:
    $ user_journey_summary.append("Di situasi (Mendadak!) Klien datang minta ide yang fresh sekarang juga! sedangkan Kamu belum menyiapkan materi apapun., user memilih: Ajak diskusi santai dan sampaikan idemu tentang visi masa depan., dengan poin MBTI: Extrovert & Intuitive")
    call ai_react_logic from _call_ai_react_logic_43
    return

label show_question_q_b_23_id:
    scene bg abstrak with dissolve
    $ narasi_asli = "Kamu masuk ke perpustakaan Internasional. Buku mana yang kamu ambil duluan?"
    n "Kamu masuk ke perpustakaan Internasional."
    n "Buku mana yang kamu ambil duluan?"

    menu:
        "Kamu masuk ke perpustakaan Internasional. Buku mana yang kamu ambil duluan?"

        "'Ensiklopedia bergambar'  yang bisa dibaca bareng teman.":
            $ IE += 5
            $ SN -= 5
            $ user_choice_text = "'Ensiklopedia bergambar'  yang bisa dibaca bareng teman."
            $ last_answer = "Extrovert & Sensing"
            jump show_question_q_b_23_id_A

        "'Filosofi tebal'  yang menarik untuk dibaca di tempat sepi.":
            $ IE -= 5
            $ SN += 5
            $ user_choice_text = "'Filosofi tebal'  yang menarik untuk dibaca di tempat sepi."
            $ last_answer = "Introvert & Intuitive"
            jump show_question_q_b_23_id_B


label show_question_q_b_23_id_A:
    $ user_journey_summary.append("Di situasi Kamu masuk ke perpustakaan Internasional. Buku mana yang kamu ambil duluan?, user memilih: 'Ensiklopedia bergambar'  yang bisa dibaca bareng teman., dengan poin MBTI: Extrovert & Sensing")
    call ai_react_logic from _call_ai_react_logic_44
    return

label show_question_q_b_23_id_B:
    $ user_journey_summary.append("Di situasi Kamu masuk ke perpustakaan Internasional. Buku mana yang kamu ambil duluan?, user memilih: 'Filosofi tebal'  yang menarik untuk dibaca di tempat sepi., dengan poin MBTI: Introvert & Intuitive")
    call ai_react_logic from _call_ai_react_logic_45
    return

label show_question_q_b_24_id:
    scene bg kafe with dissolve
    $ narasi_asli = "Perutmu lapar, tapi dompetmu tipis. Sementara itu teman-temanmu mengajakmu makan diluar."
    n "Perutmu lapar, tapi dompetmu tipis."
    n "Sementara itu teman-temanmu mengajakmu makan diluar."

    menu:
        "Perutmu lapar, tapi dompetmu tipis. Sementara itu teman-temanmu mengajakmu makan diluar."

        "Ikut mereka tapi cari warung langganan yang sudah pasti murah dan enak.":
            $ IE += 5
            $ SN -= 5
            $ user_choice_text = "Ikut mereka tapi cari warung langganan yang sudah pasti murah dan enak."
            $ last_answer = "Extrovert & Sensing"
            jump show_question_q_b_24_id_A

        "Tolak dahulu, mau coba cari makanan murah dan unik yang mungkin ada disekitar tempatmu.":
            $ IE -= 5
            $ SN += 5
            $ user_choice_text = "Tolak dahulu, mau coba cari makanan murah dan unik yang mungkin ada disekitar tempatmu."
            $ last_answer = "Introvert & Intuitive"
            jump show_question_q_b_24_id_B


label show_question_q_b_24_id_A:
    $ user_journey_summary.append("Di situasi Perutmu lapar, tapi dompetmu tipis. Sementara itu teman-temanmu mengajakmu makan diluar., user memilih: Ikut mereka tapi cari warung langganan yang sudah pasti murah dan enak., dengan poin MBTI: Extrovert & Sensing")
    call ai_react_logic from _call_ai_react_logic_46
    return

label show_question_q_b_24_id_B:
    $ user_journey_summary.append("Di situasi Perutmu lapar, tapi dompetmu tipis. Sementara itu teman-temanmu mengajakmu makan diluar., user memilih: Tolak dahulu, mau coba cari makanan murah dan unik yang mungkin ada disekitar tempatmu., dengan poin MBTI: Introvert & Intuitive")
    call ai_react_logic from _call_ai_react_logic_47
    return

label show_question_q_b_25_id:
    scene bg stasiun with dissolve
    $ narasi_asli = "Ada koper mencurigakan tertinggal di stasiun sepi."
    n "Ada koper mencurigakan tertinggal di stasiun sepi."

    menu:
        "Ada koper mencurigakan tertinggal di stasiun sepi."

        "Panggil petugas untuk mengecek isinya secara aman.":
            $ IE += 5
            $ SN -= 5
            $ user_choice_text = "Panggil petugas untuk mengecek isinya secara aman."
            $ last_answer = "Extrovert & Sensing"
            jump show_question_q_b_25_id_A

        "Perhatikan dari jauh sambil membayangkan apa isi sebenarnya dari koper tersebut.":
            $ IE -= 5
            $ SN += 5
            $ user_choice_text = "Perhatikan dari jauh sambil membayangkan apa isi sebenarnya dari koper tersebut."
            $ last_answer = "Introvert & Intuitive"
            jump show_question_q_b_25_id_B


label show_question_q_b_25_id_A:
    $ user_journey_summary.append("Di situasi Ada koper mencurigakan tertinggal di stasiun sepi., user memilih: Panggil petugas untuk mengecek isinya secara aman., dengan poin MBTI: Extrovert & Sensing")
    call ai_react_logic from _call_ai_react_logic_48
    return

label show_question_q_b_25_id_B:
    $ user_journey_summary.append("Di situasi Ada koper mencurigakan tertinggal di stasiun sepi., user memilih: Perhatikan dari jauh sambil membayangkan apa isi sebenarnya dari koper tersebut., dengan poin MBTI: Introvert & Intuitive")
    call ai_react_logic from _call_ai_react_logic_49
    return

label show_question_q_b_26_id:
    scene bg kantor with dissolve
    $ narasi_asli = "Rekan timmu melakukan kesalahan fatal yang merugikan semua orang."
    n "Rekan timmu melakukan kesalahan fatal yang merugikan semua orang."

    menu:
        "Rekan timmu melakukan kesalahan fatal yang merugikan semua orang."

        "Hadapi langsung! dan minta dia jelaskan ada apa sebenarnya.":
            $ IE += 5
            $ TF -= 5
            $ user_choice_text = "Hadapi langsung! dan minta dia jelaskan ada apa sebenarnya."
            $ last_answer = "Extrovert & Thinking"
            jump show_question_q_b_26_id_A

        "Kirim dia pesan pribadi, lalu tanya apakah dia baik-baik saja.":
            $ IE -= 5
            $ TF += 5
            $ user_choice_text = "Kirim dia pesan pribadi, lalu tanya apakah dia baik-baik saja."
            $ last_answer = "Introvert & Feeling"
            jump show_question_q_b_26_id_B


label show_question_q_b_26_id_A:
    $ user_journey_summary.append("Di situasi Rekan timmu melakukan kesalahan fatal yang merugikan semua orang., user memilih: Hadapi langsung! dan minta dia jelaskan ada apa sebenarnya., dengan poin MBTI: Extrovert & Thinking")
    call ai_react_logic from _call_ai_react_logic_50
    return

label show_question_q_b_26_id_B:
    $ user_journey_summary.append("Di situasi Rekan timmu melakukan kesalahan fatal yang merugikan semua orang., user memilih: Kirim dia pesan pribadi, lalu tanya apakah dia baik-baik saja., dengan poin MBTI: Introvert & Feeling")
    call ai_react_logic from _call_ai_react_logic_51
    return

label show_question_q_b_27_id:
    scene bg kantor with dissolve
    $ narasi_asli = "Temanmu minta pendapat jujur soal karyanya yang... bisa dibilang...hancur lebur menurutmu."
    n "Temanmu minta pendapat jujur soal karyanya yang..."
    n "bisa dibilang...hancur lebur menurutmu."

    menu:
        "Temanmu minta pendapat jujur soal karyanya yang... bisa dibilang...hancur lebur menurutmu."

        "Bilang terus terang bagian mana yang salah agar bisa diperbaiki.":
            $ IE += 5
            $ TF -= 5
            $ user_choice_text = "Bilang terus terang bagian mana yang salah agar bisa diperbaiki."
            $ last_answer = "Extrovert & Thinking"
            jump show_question_q_b_27_id_A

        "Diam atau senyum saja, nggak tega menyakiti perasaannya.":
            $ IE -= 5
            $ TF += 5
            $ user_choice_text = "Diam atau senyum saja, nggak tega menyakiti perasaannya."
            $ last_answer = "Introvert & Feeling"
            jump show_question_q_b_27_id_B


label show_question_q_b_27_id_A:
    $ user_journey_summary.append("Di situasi Temanmu minta pendapat jujur soal karyanya yang... bisa dibilang...hancur lebur menurutmu., user memilih: Bilang terus terang bagian mana yang salah agar bisa diperbaiki., dengan poin MBTI: Extrovert & Thinking")
    call ai_react_logic from _call_ai_react_logic_52
    return

label show_question_q_b_27_id_B:
    $ user_journey_summary.append("Di situasi Temanmu minta pendapat jujur soal karyanya yang... bisa dibilang...hancur lebur menurutmu., user memilih: Diam atau senyum saja, nggak tega menyakiti perasaannya., dengan poin MBTI: Introvert & Feeling")
    call ai_react_logic from _call_ai_react_logic_53
    return

label show_question_q_b_28_id:
    scene bg kafe with dissolve
    $ narasi_asli = "Dua orang asing berdebat keras di meja sebelah. Mengganggu banget!"
    n "Dua orang asing berdebat keras di meja sebelah."
    n "Mengganggu banget!"

    menu:
        "Dua orang asing berdebat keras di meja sebelah. Mengganggu banget!"

        "Tegur mereka, 'Tolong tenang, argumen kalian nggak logis!'.":
            $ IE += 5
            $ TF -= 5
            $ user_choice_text = "Tegur mereka, 'Tolong tenang, argumen kalian nggak logis!'."
            $ last_answer = "Extrovert & Thinking"
            jump show_question_q_b_28_id_A

        "Pindah meja, menjauh karena energinya negatif banget.":
            $ IE -= 5
            $ TF += 5
            $ user_choice_text = "Pindah meja, menjauh karena energinya negatif banget."
            $ last_answer = "Introvert & Feeling"
            jump show_question_q_b_28_id_B


label show_question_q_b_28_id_A:
    $ user_journey_summary.append("Di situasi Dua orang asing berdebat keras di meja sebelah. Mengganggu banget!, user memilih: Tegur mereka, 'Tolong tenang, argumen kalian nggak logis!'., dengan poin MBTI: Extrovert & Thinking")
    call ai_react_logic from _call_ai_react_logic_54
    return

label show_question_q_b_28_id_B:
    $ user_journey_summary.append("Di situasi Dua orang asing berdebat keras di meja sebelah. Mengganggu banget!, user memilih: Pindah meja, menjauh karena energinya negatif banget., dengan poin MBTI: Introvert & Feeling")
    call ai_react_logic from _call_ai_react_logic_55
    return

label show_question_q_b_29_id:
    scene bg abstrak with dissolve
    $ narasi_asli = "Kamu harus memilih pemimpin untuk misi berbahaya."
    n "Kamu harus memilih pemimpin untuk misi berbahaya."

    menu:
        "Kamu harus memilih pemimpin untuk misi berbahaya."

        "Debat terbuka, pilih yang statistiknya paling kuat.":
            $ IE += 5
            $ TF -= 5
            $ user_choice_text = "Debat terbuka, pilih yang statistiknya paling kuat."
            $ last_answer = "Extrovert & Thinking"
            jump show_question_q_b_29_id_A

        "Renungkan dengan beberapa teman dekat, lalu pilih yang hatinya paling tulus.":
            $ IE -= 5
            $ TF += 5
            $ user_choice_text = "Renungkan dengan beberapa teman dekat, lalu pilih yang hatinya paling tulus."
            $ last_answer = "Introvert & Feeling"
            jump show_question_q_b_29_id_B


label show_question_q_b_29_id_A:
    $ user_journey_summary.append("Di situasi Kamu harus memilih pemimpin untuk misi berbahaya., user memilih: Debat terbuka, pilih yang statistiknya paling kuat., dengan poin MBTI: Extrovert & Thinking")
    call ai_react_logic from _call_ai_react_logic_56
    return

label show_question_q_b_29_id_B:
    $ user_journey_summary.append("Di situasi Kamu harus memilih pemimpin untuk misi berbahaya., user memilih: Renungkan dengan beberapa teman dekat, lalu pilih yang hatinya paling tulus., dengan poin MBTI: Introvert & Feeling")
    call ai_react_logic from _call_ai_react_logic_57
    return

label show_question_q_b_30_id:
    scene bg taman with dissolve
    $ narasi_asli = "Ada kerumunan orang sedang sedih karena pohon tua ditebang oleh pemerintah sekitar."
    n "Ada kerumunan orang sedang sedih karena pohon tua ditebang oleh pemerintah sekitar."

    menu:
        "Ada kerumunan orang sedang sedih karena pohon tua ditebang oleh pemerintah sekitar."

        "Kumpulkan mereka untuk buat petisi protes ke pemerintah.":
            $ IE += 5
            $ TF -= 5
            $ user_choice_text = "Kumpulkan mereka untuk buat petisi protes ke pemerintah."
            $ last_answer = "Extrovert & Thinking"
            jump show_question_q_b_30_id_A

        "Duduk diam di sana sebagai tanda solidaritas.":
            $ IE -= 5
            $ TF += 5
            $ user_choice_text = "Duduk diam di sana sebagai tanda solidaritas."
            $ last_answer = "Introvert & Feeling"
            jump show_question_q_b_30_id_B


label show_question_q_b_30_id_A:
    $ user_journey_summary.append("Di situasi Ada kerumunan orang sedang sedih karena pohon tua ditebang oleh pemerintah sekitar., user memilih: Kumpulkan mereka untuk buat petisi protes ke pemerintah., dengan poin MBTI: Extrovert & Thinking")
    call ai_react_logic from _call_ai_react_logic_58
    return

label show_question_q_b_30_id_B:
    $ user_journey_summary.append("Di situasi Ada kerumunan orang sedang sedih karena pohon tua ditebang oleh pemerintah sekitar., user memilih: Duduk diam di sana sebagai tanda solidaritas., dengan poin MBTI: Introvert & Feeling")
    call ai_react_logic from _call_ai_react_logic_59
    return

label show_question_q_b_31_id:
    scene bg stasiun with dissolve
    $ narasi_asli = "(Telat!) Kereta terakhir berangkat 1 menit lagi! Kamu masih di lobi!"
    n "(Telat!) Kereta terakhir berangkat 1 menit lagi!"
    n "Kamu masih di lobi!"

    menu:
        "(Telat!) Kereta terakhir berangkat 1 menit lagi! Kamu masih di lobi!"

        "Teriak 'Tunggu!' dan lari menerobos gerbang tanpa pikir panjang.":
            $ IE += 5
            $ JP += 5
            $ user_choice_text = "Teriak 'Tunggu!' dan lari menerobos gerbang tanpa pikir panjang."
            $ last_answer = "Extrovert & Perceiving"
            jump show_question_q_b_31_id_A

        "Pasrah. Ini salahku karena tidak cek jadwal tadi pagi.":
            $ IE -= 5
            $ JP -= 5
            $ user_choice_text = "Pasrah. Ini salahku karena tidak cek jadwal tadi pagi."
            $ last_answer = "Introvert & Judging"
            jump show_question_q_b_31_id_B


label show_question_q_b_31_id_A:
    $ user_journey_summary.append("Di situasi (Telat!) Kereta terakhir berangkat 1 menit lagi! Kamu masih di lobi!, user memilih: Teriak 'Tunggu!' dan lari menerobos gerbang tanpa pikir panjang., dengan poin MBTI: Extrovert & Perceiving")
    call ai_react_logic from _call_ai_react_logic_60
    return

label show_question_q_b_31_id_B:
    $ user_journey_summary.append("Di situasi (Telat!) Kereta terakhir berangkat 1 menit lagi! Kamu masih di lobi!, user memilih: Pasrah. Ini salahku karena tidak cek jadwal tadi pagi., dengan poin MBTI: Introvert & Judging")
    call ai_react_logic from _call_ai_react_logic_61
    return

label show_question_q_b_32_id:
    scene bg kafe with dissolve
    $ narasi_asli = "Kamu dan rombongan besar bingung mau pesan apa di Restoran. Pelayan yang menunggu mulai kesal."
    n "Kamu dan rombongan besar bingung mau pesan apa di Restoran."
    n "Pelayan yang menunggu mulai kesal."

    menu:
        "Kamu dan rombongan besar bingung mau pesan apa di Restoran. Pelayan yang menunggu mulai kesal."

        "Tanya ke yang lain!, 'Mau makanan apa? Bebas deh!'.":
            $ IE += 5
            $ JP += 5
            $ user_choice_text = "Tanya ke yang lain!, 'Mau makanan apa? Bebas deh!'."
            $ last_answer = "Extrovert & Perceiving"
            jump show_question_q_b_32_id_A

        "Ambil alih, 'Oke, aku pesankan menu paket buat semua agar lebih cepat ya'.":
            $ IE -= 5
            $ JP -= 5
            $ user_choice_text = "Ambil alih, 'Oke, aku pesankan menu paket buat semua agar lebih cepat ya'."
            $ last_answer = "Introvert & Judging"
            jump show_question_q_b_32_id_B


label show_question_q_b_32_id_A:
    $ user_journey_summary.append("Di situasi Kamu dan rombongan besar bingung mau pesan apa di Restoran. Pelayan yang menunggu mulai kesal., user memilih: Tanya ke yang lain!, 'Mau makanan apa? Bebas deh!'., dengan poin MBTI: Extrovert & Perceiving")
    call ai_react_logic from _call_ai_react_logic_62
    return

label show_question_q_b_32_id_B:
    $ user_journey_summary.append("Di situasi Kamu dan rombongan besar bingung mau pesan apa di Restoran. Pelayan yang menunggu mulai kesal., user memilih: Ambil alih, 'Oke, aku pesankan menu paket buat semua agar lebih cepat ya'., dengan poin MBTI: Introvert & Judging")
    call ai_react_logic from _call_ai_react_logic_63
    return

label show_question_q_b_33_id:
    scene bg kafe with dissolve
    $ narasi_asli = "Kamu lihat jaket yang keren banget dipajang di toko, tapi harganya mahal."
    n "Kamu lihat jaket yang keren banget dipajang di toko, tapi harganya mahal."

    menu:
        "Kamu lihat jaket yang keren banget dipajang di toko, tapi harganya mahal."

        "Tanya pendapat orang lain, kalau bagus langsung beli aja!.":
            $ IE += 5
            $ JP += 5
            $ user_choice_text = "Tanya pendapat orang lain, kalau bagus langsung beli aja!."
            $ last_answer = "Extrovert & Perceiving"
            jump show_question_q_b_33_id_A

        "Tanyakan diri sendiri, 'lagi tidak ada di budget. jangan dulu deh'.":
            $ IE -= 5
            $ JP -= 5
            $ user_choice_text = "Tanyakan diri sendiri, 'lagi tidak ada di budget. jangan dulu deh'."
            $ last_answer = "Introvert & Judging"
            jump show_question_q_b_33_id_B


label show_question_q_b_33_id_A:
    $ user_journey_summary.append("Di situasi Kamu lihat jaket yang keren banget dipajang di toko, tapi harganya mahal., user memilih: Tanya pendapat orang lain, kalau bagus langsung beli aja!., dengan poin MBTI: Extrovert & Perceiving")
    call ai_react_logic from _call_ai_react_logic_64
    return

label show_question_q_b_33_id_B:
    $ user_journey_summary.append("Di situasi Kamu lihat jaket yang keren banget dipajang di toko, tapi harganya mahal., user memilih: Tanyakan diri sendiri, 'lagi tidak ada di budget. jangan dulu deh'., dengan poin MBTI: Introvert & Judging")
    call ai_react_logic from _call_ai_react_logic_65
    return

label show_question_q_b_34_id:
    scene bg room with dissolve
    $ narasi_asli = "Temanmu bilang kamarmu membosankan. Lalu apa reaksimu?"
    n "Temanmu bilang kamarmu membosankan."
    n "Lalu apa reaksimu?"

    menu:
        "Temanmu bilang kamarmu membosankan. Lalu apa reaksimu?"

        "'Benar juga!' Mumpung ada teman, ajak dia geser-geser furnitur sekarang juga.":
            $ IE += 5
            $ JP += 5
            $ user_choice_text = "'Benar juga!' Mumpung ada teman, ajak dia geser-geser furnitur sekarang juga."
            $ last_answer = "Extrovert & Perceiving"
            jump show_question_q_b_34_id_A

        "Biarkan. 'Aku lebih suka, karena semuanya sudah ada di tempat yang seharusnya'.":
            $ IE -= 5
            $ JP -= 5
            $ user_choice_text = "Biarkan. 'Aku lebih suka, karena semuanya sudah ada di tempat yang seharusnya'."
            $ last_answer = "Introvert & Judging"
            jump show_question_q_b_34_id_B


label show_question_q_b_34_id_A:
    $ user_journey_summary.append("Di situasi Temanmu bilang kamarmu membosankan. Lalu apa reaksimu?, user memilih: 'Benar juga!' Mumpung ada teman, ajak dia geser-geser furnitur sekarang juga., dengan poin MBTI: Extrovert & Perceiving")
    call ai_react_logic from _call_ai_react_logic_66
    return

label show_question_q_b_34_id_B:
    $ user_journey_summary.append("Di situasi Temanmu bilang kamarmu membosankan. Lalu apa reaksimu?, user memilih: Biarkan. 'Aku lebih suka, karena semuanya sudah ada di tempat yang seharusnya'., dengan poin MBTI: Introvert & Judging")
    call ai_react_logic from _call_ai_react_logic_67
    return

label show_question_q_b_35_id:
    scene bg kantor with dissolve
    $ narasi_asli = "Kamu harus pidato dadakan di depan umum! bagaimana ini?!"
    n "Kamu harus pidato dadakan di depan umum!"
    n "bagaimana ini?!"

    menu:
        "Kamu harus pidato dadakan di depan umum! bagaimana ini?!"

        "Maju dengan percaya diri, ngomong mengalir, dengan lihat situasi.":
            $ IE += 5
            $ JP += 5
            $ user_choice_text = "Maju dengan percaya diri, ngomong mengalir, dengan lihat situasi."
            $ last_answer = "Extrovert & Perceiving"
            jump show_question_q_b_35_id_A

        "Mundur sebentar, minta waktu buat mencatat poin-poin penting dahulu.":
            $ IE -= 5
            $ JP -= 5
            $ user_choice_text = "Mundur sebentar, minta waktu buat mencatat poin-poin penting dahulu."
            $ last_answer = "Introvert & Judging"
            jump show_question_q_b_35_id_B


label show_question_q_b_35_id_A:
    $ user_journey_summary.append("Di situasi Kamu harus pidato dadakan di depan umum! bagaimana ini?!, user memilih: Maju dengan percaya diri, ngomong mengalir, dengan lihat situasi., dengan poin MBTI: Extrovert & Perceiving")
    call ai_react_logic from _call_ai_react_logic_68
    return

label show_question_q_b_35_id_B:
    $ user_journey_summary.append("Di situasi Kamu harus pidato dadakan di depan umum! bagaimana ini?!, user memilih: Mundur sebentar, minta waktu buat mencatat poin-poin penting dahulu., dengan poin MBTI: Introvert & Judging")
    call ai_react_logic from _call_ai_react_logic_69
    return

label show_question_q_b_36_id:
    scene bg abstrak with dissolve
    $ narasi_asli = "(Bencana!) Desa kamu diserang! Kamu yang pegang kunci gerbang pertahanan. Masih ada warga yang berlari berusaha masuk ke dalam."
    n "(Bencana!) Desa kamu diserang!"
    n "Kamu yang pegang kunci gerbang pertahanan."
    n "Masih ada warga yang berlari berusaha masuk ke dalam."

    menu:
        "(Bencana!) Desa kamu diserang! Kamu yang pegang kunci gerbang pertahanan. Masih ada warga yang berlari berusaha masuk ke dalam."

        "Segera kunci gerbang demi keselamatan mayoritas, meski ada yang tertinggal.":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "Segera kunci gerbang demi keselamatan mayoritas, meski ada yang tertinggal."
            $ last_answer = "Thinking & Judging"
            jump show_question_q_b_36_id_A

        "Biarkan terbuka sedikit lagi, kasihan yang masih lari di luar.":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "Biarkan terbuka sedikit lagi, kasihan yang masih lari di luar."
            $ last_answer = "Feeling & Perceiving"
            jump show_question_q_b_36_id_B


label show_question_q_b_36_id_A:
    $ user_journey_summary.append("Di situasi (Bencana!) Desa kamu diserang! Kamu yang pegang kunci gerbang pertahanan. Masih ada warga yang berlari berusaha masuk ke dalam., user memilih: Segera kunci gerbang demi keselamatan mayoritas, meski ada yang tertinggal., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic from _call_ai_react_logic_70
    return

label show_question_q_b_36_id_B:
    $ user_journey_summary.append("Di situasi (Bencana!) Desa kamu diserang! Kamu yang pegang kunci gerbang pertahanan. Masih ada warga yang berlari berusaha masuk ke dalam., user memilih: Biarkan terbuka sedikit lagi, kasihan yang masih lari di luar., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic from _call_ai_react_logic_71
    return

label show_question_q_b_37_id:
    scene bg kantor with dissolve
    $ narasi_asli = "Anggota timmu curhat. Dia lagi patah hati dan nggak bisa kerja. Apa yang Kamu lakukan sebagai ketua tim?"
    n "Anggota timmu curhat."
    n "Dia lagi patah hati dan nggak bisa kerja."
    n "Apa yang Kamu lakukan sebagai ketua tim?"

    menu:
        "Anggota timmu curhat. Dia lagi patah hati dan nggak bisa kerja. Apa yang Kamu lakukan sebagai ketua tim?"

        "'Kerja adalah kerja. Selesaikan tugasmu, baru urus perasaan.'":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "'Kerja adalah kerja. Selesaikan tugasmu, baru urus perasaan.'"
            $ last_answer = "Thinking & Judging"
            jump show_question_q_b_37_id_A

        "'Pulanglah. Kerjaan bisa kita atur ulang nanti.'":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "'Pulanglah. Kerjaan bisa kita atur ulang nanti.'"
            $ last_answer = "Feeling & Perceiving"
            jump show_question_q_b_37_id_B


label show_question_q_b_37_id_A:
    $ user_journey_summary.append("Di situasi Anggota timmu curhat. Dia lagi patah hati dan nggak bisa kerja. Apa yang Kamu lakukan sebagai ketua tim?, user memilih: 'Kerja adalah kerja. Selesaikan tugasmu, baru urus perasaan.', dengan poin MBTI: Thinking & Judging")
    call ai_react_logic from _call_ai_react_logic_72
    return

label show_question_q_b_37_id_B:
    $ user_journey_summary.append("Di situasi Anggota timmu curhat. Dia lagi patah hati dan nggak bisa kerja. Apa yang Kamu lakukan sebagai ketua tim?, user memilih: 'Pulanglah. Kerjaan bisa kita atur ulang nanti.', dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic from _call_ai_react_logic_73
    return

label show_question_q_b_38_id:
    scene bg dapur with dissolve
    $ narasi_asli = "Kamu menjadi juri lomba masak. Masakan temanmu gosong. Dia nangis, padahal dia sudah berusaha keras."
    n "Kamu menjadi juri lomba masak."
    n "Masakan temanmu gosong."
    n "Dia nangis, padahal dia sudah berusaha keras."

    menu:
        "Kamu menjadi juri lomba masak. Masakan temanmu gosong. Dia nangis, padahal dia sudah berusaha keras."

        "Beri nilai nol. Aturan penilaian harus objektif.":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "Beri nilai nol. Aturan penilaian harus objektif."
            $ last_answer = "Thinking & Judging"
            jump show_question_q_b_38_id_A

        "Beri nilai tambahan. Hargai proses dan usahanya.":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "Beri nilai tambahan. Hargai proses dan usahanya."
            $ last_answer = "Feeling & Perceiving"
            jump show_question_q_b_38_id_B


label show_question_q_b_38_id_A:
    $ user_journey_summary.append("Di situasi Kamu menjadi juri lomba masak. Masakan temanmu gosong. Dia nangis, padahal dia sudah berusaha keras., user memilih: Beri nilai nol. Aturan penilaian harus objektif., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic from _call_ai_react_logic_74
    return

label show_question_q_b_38_id_B:
    $ user_journey_summary.append("Di situasi Kamu menjadi juri lomba masak. Masakan temanmu gosong. Dia nangis, padahal dia sudah berusaha keras., user memilih: Beri nilai tambahan. Hargai proses dan usahanya., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic from _call_ai_react_logic_75
    return

label show_question_q_b_39_id:
    scene bg stasiun with dissolve
    $ narasi_asli = "Ada turis kebingungan, salah masuk jalur di Stasiun. Lalu dia kena denda. Kamu sebagai petugas di sana"
    n "Ada turis kebingungan, salah masuk jalur di Stasiun."
    n "Lalu dia kena denda."
    n "Kamu sebagai petugas di sana"

    menu:
        "Ada turis kebingungan, salah masuk jalur di Stasiun. Lalu dia kena denda. Kamu sebagai petugas di sana"

        "Biarkan dia bayar denda. Peraturan tetap peraturan.":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "Biarkan dia bayar denda. Peraturan tetap peraturan."
            $ last_answer = "Thinking & Judging"
            jump show_question_q_b_39_id_A

        "Bantu dia nego. Maklumi karena dia orang asing.":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "Bantu dia nego. Maklumi karena dia orang asing."
            $ last_answer = "Feeling & Perceiving"
            jump show_question_q_b_39_id_B


label show_question_q_b_39_id_A:
    $ user_journey_summary.append("Di situasi Ada turis kebingungan, salah masuk jalur di Stasiun. Lalu dia kena denda. Kamu sebagai petugas di sana, user memilih: Biarkan dia bayar denda. Peraturan tetap peraturan., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic from _call_ai_react_logic_76
    return

label show_question_q_b_39_id_B:
    $ user_journey_summary.append("Di situasi Ada turis kebingungan, salah masuk jalur di Stasiun. Lalu dia kena denda. Kamu sebagai petugas di sana, user memilih: Bantu dia nego. Maklumi karena dia orang asing., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic from _call_ai_react_logic_77
    return

label show_question_q_b_40_id:
    scene bg kantor with dissolve
    $ narasi_asli = "Kamu bikin jadwal piket baru. Namun temanmu ada yang protes karena jadwalnya bentrok."
    n "Kamu bikin jadwal piket baru."
    n "Namun temanmu ada yang protes karena jadwalnya bentrok."

    menu:
        "Kamu bikin jadwal piket baru. Namun temanmu ada yang protes karena jadwalnya bentrok."

        "'Tidak bisa! Sistem sudah dibuat efisien. Harus ikuti jadwal yang ada.'":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "'Tidak bisa! Sistem sudah dibuat efisien. Harus ikuti jadwal yang ada.'"
            $ last_answer = "Thinking & Judging"
            jump show_question_q_b_40_id_A

        "'Oke, kita bisa tukar-tukar aja. Yang penting semua senang.'":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "'Oke, kita bisa tukar-tukar aja. Yang penting semua senang.'"
            $ last_answer = "Feeling & Perceiving"
            jump show_question_q_b_40_id_B


label show_question_q_b_40_id_A:
    $ user_journey_summary.append("Di situasi Kamu bikin jadwal piket baru. Namun temanmu ada yang protes karena jadwalnya bentrok., user memilih: 'Tidak bisa! Sistem sudah dibuat efisien. Harus ikuti jadwal yang ada.', dengan poin MBTI: Thinking & Judging")
    call ai_react_logic from _call_ai_react_logic_78
    return

label show_question_q_b_40_id_B:
    $ user_journey_summary.append("Di situasi Kamu bikin jadwal piket baru. Namun temanmu ada yang protes karena jadwalnya bentrok., user memilih: 'Oke, kita bisa tukar-tukar aja. Yang penting semua senang.', dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic from _call_ai_react_logic_79
    return

label show_question_q_c_41_id:
    scene bg taman with dissolve
    $ narasi_asli = "Libur telah tiba. Teman-teman mengajakmu pergi jalan-jalan, tapi belum tahu pasti mau ke mana."
    n "Libur telah tiba."
    n "Teman-teman mengajakmu pergi jalan-jalan, tapi belum tahu pasti mau ke mana."

    menu:
        "Libur telah tiba. Teman-teman mengajakmu pergi jalan-jalan, tapi belum tahu pasti mau ke mana."

        "Pergi sendiri mengunjungi museum sejarah untuk melihat artefak bersejarah.":
            $ IE -= 5
            $ SN -= 5
            $ user_choice_text = "Pergi sendiri mengunjungi museum sejarah untuk melihat artefak bersejarah."
            $ last_answer = "Introvert & Sensing"
            jump show_question_q_c_41_id_A

        "Ikut rombongan menjelajahi hutan mitos yang penuh misteri.":
            $ IE += 5
            $ SN += 5
            $ user_choice_text = "Ikut rombongan menjelajahi hutan mitos yang penuh misteri."
            $ last_answer = "Extrovert & Intuitive"
            jump show_question_q_c_41_id_B


label show_question_q_c_41_id_A:
    $ user_journey_summary.append("Di situasi Libur telah tiba. Teman-teman mengajakmu pergi jalan-jalan, tapi belum tahu pasti mau ke mana., user memilih: Pergi sendiri mengunjungi museum sejarah untuk melihat artefak bersejarah., dengan poin MBTI: Introvert & Sensing")
    call ai_react_logic from _call_ai_react_logic_80
    return

label show_question_q_c_41_id_B:
    $ user_journey_summary.append("Di situasi Libur telah tiba. Teman-teman mengajakmu pergi jalan-jalan, tapi belum tahu pasti mau ke mana., user memilih: Ikut rombongan menjelajahi hutan mitos yang penuh misteri., dengan poin MBTI: Extrovert & Intuitive")
    call ai_react_logic from _call_ai_react_logic_81
    return

label show_question_q_c_42_id:
    scene bg kafe with dissolve
    $ narasi_asli = "Kamu menang lotre besar! Memenangkan sekantong koin emas."
    n "Kamu menang lotre besar!"
    n "Memenangkan sekantong koin emas."

    menu:
        "Kamu menang lotre besar! Memenangkan sekantong koin emas."

        "Simpan sendiri di brankas sebagai aset fisik yang aman.":
            $ IE -= 5
            $ SN -= 5
            $ user_choice_text = "Simpan sendiri di brankas sebagai aset fisik yang aman."
            $ last_answer = "Introvert & Sensing"
            jump show_question_q_c_42_id_A

        "Traktir semua orang sambil memikirkan kekayaanmu yang semakin bertambah.":
            $ IE += 5
            $ SN += 5
            $ user_choice_text = "Traktir semua orang sambil memikirkan kekayaanmu yang semakin bertambah."
            $ last_answer = "Extrovert & Intuitive"
            jump show_question_q_c_42_id_B


label show_question_q_c_42_id_A:
    $ user_journey_summary.append("Di situasi Kamu menang lotre besar! Memenangkan sekantong koin emas., user memilih: Simpan sendiri di brankas sebagai aset fisik yang aman., dengan poin MBTI: Introvert & Sensing")
    call ai_react_logic from _call_ai_react_logic_82
    return

label show_question_q_c_42_id_B:
    $ user_journey_summary.append("Di situasi Kamu menang lotre besar! Memenangkan sekantong koin emas., user memilih: Traktir semua orang sambil memikirkan kekayaanmu yang semakin bertambah., dengan poin MBTI: Extrovert & Intuitive")
    call ai_react_logic from _call_ai_react_logic_83
    return

label show_question_q_c_43_id:
    scene bg room with dissolve
    $ narasi_asli = "Kamu melihat lukisan abstrak yang 'cuma coretan beberapa garis'."
    n "Kamu melihat lukisan abstrak yang 'cuma coretan beberapa garis'."

    menu:
        "Kamu melihat lukisan abstrak yang 'cuma coretan beberapa garis'."

        "Tanya orang lain, 'Ini gambar apa sih? Maksudnya apaan?'.":
            $ IE += 5
            $ SN -= 5
            $ user_choice_text = "Tanya orang lain, 'Ini gambar apa sih? Maksudnya apaan?'."
            $ last_answer = "Extrovert & Sensing"
            jump show_question_q_c_43_id_A

        "Diam dan mencoba merasakan emosi pelukisnya.":
            $ IE -= 5
            $ SN += 5
            $ user_choice_text = "Diam dan mencoba merasakan emosi pelukisnya."
            $ last_answer = "Introvert & Intuitive"
            jump show_question_q_c_43_id_B


label show_question_q_c_43_id_A:
    $ user_journey_summary.append("Di situasi Kamu melihat lukisan abstrak yang 'cuma coretan beberapa garis'., user memilih: Tanya orang lain, 'Ini gambar apa sih? Maksudnya apaan?'., dengan poin MBTI: Extrovert & Sensing")
    call ai_react_logic from _call_ai_react_logic_84
    return

label show_question_q_c_43_id_B:
    $ user_journey_summary.append("Di situasi Kamu melihat lukisan abstrak yang 'cuma coretan beberapa garis'., user memilih: Diam dan mencoba merasakan emosi pelukisnya., dengan poin MBTI: Introvert & Intuitive")
    call ai_react_logic from _call_ai_react_logic_85
    return

label show_question_q_c_44_id:
    scene bg arcade with dissolve
    $ narasi_asli = "Temanmu minta diajari main game, yang jago banget kamu mainkan."
    n "Temanmu minta diajari main game, yang jago banget kamu mainkan."

    menu:
        "Temanmu minta diajari main game, yang jago banget kamu mainkan."

        "'Sini, tekan tombol maju, lalu lompat.' Pandu dia langsung.":
            $ IE += 5
            $ SN -= 5
            $ user_choice_text = "'Sini, tekan tombol maju, lalu lompat.' Pandu dia langsung."
            $ last_answer = "Extrovert & Sensing"
            jump show_question_q_c_44_id_A

        "'Kamu pahami dulu konsepnya.' Biarkan dia belajar sendiri.":
            $ IE -= 5
            $ SN += 5
            $ user_choice_text = "'Kamu pahami dulu konsepnya.' Biarkan dia belajar sendiri."
            $ last_answer = "Introvert & Intuitive"
            jump show_question_q_c_44_id_B


label show_question_q_c_44_id_A:
    $ user_journey_summary.append("Di situasi Temanmu minta diajari main game, yang jago banget kamu mainkan., user memilih: 'Sini, tekan tombol maju, lalu lompat.' Pandu dia langsung., dengan poin MBTI: Extrovert & Sensing")
    call ai_react_logic from _call_ai_react_logic_86
    return

label show_question_q_c_44_id_B:
    $ user_journey_summary.append("Di situasi Temanmu minta diajari main game, yang jago banget kamu mainkan., user memilih: 'Kamu pahami dulu konsepnya.' Biarkan dia belajar sendiri., dengan poin MBTI: Introvert & Intuitive")
    call ai_react_logic from _call_ai_react_logic_87
    return

label show_question_q_c_45_id:
    scene bg abstrak with dissolve
    $ narasi_asli = "Kamu punya waktu luang 1 jam hari ini. Kamu mau ngapain?"
    n "Kamu punya waktu luang 1 jam hari ini."
    n "Kamu mau ngapain?"

    menu:
        "Kamu punya waktu luang 1 jam hari ini. Kamu mau ngapain?"

        "Olahraga atau beres-beres bareng di rumah.":
            $ IE += 5
            $ SN -= 5
            $ user_choice_text = "Olahraga atau beres-beres bareng di rumah."
            $ last_answer = "Extrovert & Sensing"
            jump show_question_q_c_45_id_A

        "Melakukan hal yang kamu suka, sambil membayangkan apa yang bisa kamu lakukan di kemudian hari.":
            $ IE -= 5
            $ SN += 5
            $ user_choice_text = "Melakukan hal yang kamu suka, sambil membayangkan apa yang bisa kamu lakukan di kemudian hari."
            $ last_answer = "Introvert & Intuitive"
            jump show_question_q_c_45_id_B


label show_question_q_c_45_id_A:
    $ user_journey_summary.append("Di situasi Kamu punya waktu luang 1 jam hari ini. Kamu mau ngapain?, user memilih: Olahraga atau beres-beres bareng di rumah., dengan poin MBTI: Extrovert & Sensing")
    call ai_react_logic from _call_ai_react_logic_88
    return

label show_question_q_c_45_id_B:
    $ user_journey_summary.append("Di situasi Kamu punya waktu luang 1 jam hari ini. Kamu mau ngapain?, user memilih: Melakukan hal yang kamu suka, sambil membayangkan apa yang bisa kamu lakukan di kemudian hari., dengan poin MBTI: Introvert & Intuitive")
    call ai_react_logic from _call_ai_react_logic_89
    return

label show_question_q_c_46_id:
    scene bg room with dissolve
    $ narasi_asli = "(Hiks!) Temanmu nangis karena diputusin pacarnya"
    n "(Hiks!) Temanmu nangis karena diputusin pacarnya"

    menu:
        "(Hiks!) Temanmu nangis karena diputusin pacarnya"

        "'Sudah, jangan nangis. Nih tisu. Jika dipikir-pikir dia memang gak baik buatmu.'":
            $ SN -= 5
            $ TF -= 5
            $ user_choice_text = "'Sudah, jangan nangis. Nih tisu. Jika dipikir-pikir dia memang gak baik buatmu.'"
            $ last_answer = "Sensing & Thinking"
            jump show_question_q_c_46_id_A

        "Temani dia. lalu dengarkan ceritanya.":
            $ SN += 5
            $ TF += 5
            $ user_choice_text = "Temani dia. lalu dengarkan ceritanya."
            $ last_answer = "Intuitive & Feeling"
            jump show_question_q_c_46_id_B


label show_question_q_c_46_id_A:
    $ user_journey_summary.append("Di situasi (Hiks!) Temanmu nangis karena diputusin pacarnya, user memilih: 'Sudah, jangan nangis. Nih tisu. Jika dipikir-pikir dia memang gak baik buatmu.', dengan poin MBTI: Sensing & Thinking")
    call ai_react_logic from _call_ai_react_logic_90
    return

label show_question_q_c_46_id_B:
    $ user_journey_summary.append("Di situasi (Hiks!) Temanmu nangis karena diputusin pacarnya, user memilih: Temani dia. lalu dengarkan ceritanya., dengan poin MBTI: Intuitive & Feeling")
    call ai_react_logic from _call_ai_react_logic_91
    return

label show_question_q_c_47_id:
    scene bg room with dissolve
    $ narasi_asli = "Film yang kalian tonton ending-nya gantung dan nggak jelas!"
    n "Film yang kalian tonton ending-nya gantung dan nggak jelas!"

    menu:
        "Film yang kalian tonton ending-nya gantung dan nggak jelas!"

        "'Ah..Jelek banget! Banyak adegan yang nggak dijelaskan kaitannya!.'":
            $ SN -= 5
            $ TF -= 5
            $ user_choice_text = "'Ah..Jelek banget! Banyak adegan yang nggak dijelaskan kaitannya!.'"
            $ last_answer = "Sensing & Thinking"
            jump show_question_q_c_47_id_A

        "'Keren... Maknanya dalam banget, soal harapan yang sirna.'":
            $ SN += 5
            $ TF += 5
            $ user_choice_text = "'Keren... Maknanya dalam banget, soal harapan yang sirna.'"
            $ last_answer = "Intuitive & Feeling"
            jump show_question_q_c_47_id_B


label show_question_q_c_47_id_A:
    $ user_journey_summary.append("Di situasi Film yang kalian tonton ending-nya gantung dan nggak jelas!, user memilih: 'Ah..Jelek banget! Banyak adegan yang nggak dijelaskan kaitannya!.', dengan poin MBTI: Sensing & Thinking")
    call ai_react_logic from _call_ai_react_logic_92
    return

label show_question_q_c_47_id_B:
    $ user_journey_summary.append("Di situasi Film yang kalian tonton ending-nya gantung dan nggak jelas!, user memilih: 'Keren... Maknanya dalam banget, soal harapan yang sirna.', dengan poin MBTI: Intuitive & Feeling")
    call ai_react_logic from _call_ai_react_logic_93
    return

label show_question_q_c_48_id:
    scene bg kantor with dissolve
    $ narasi_asli = "Ada tawaran job dengan Gaji besar, tapi kamu belum tau apa kerjaannya. Orang tersebut juga cukup mencurigakan"
    n "Ada tawaran job dengan Gaji besar, tapi kamu belum tau apa kerjaannya."
    n "Orang tersebut juga cukup mencurigakan"

    menu:
        "Ada tawaran job dengan Gaji besar, tapi kamu belum tau apa kerjaannya. Orang tersebut juga cukup mencurigakan"

        "Tolak. 'Tawarannya belum jelas' tidak yakin bakal dibawa kemana.":
            $ SN += 5
            $ TF += 5
            $ user_choice_text = "Tolak. 'Tawarannya belum jelas' tidak yakin bakal dibawa kemana."
            $ last_answer = "Intuitive & Feeling"
            jump show_question_q_c_48_id_A

        "Terima aja. Secara finansial kita lagi butuh uangnya.":
            $ SN -= 5
            $ TF -= 5
            $ user_choice_text = "Terima aja. Secara finansial kita lagi butuh uangnya."
            $ last_answer = "Sensing & Thinking"
            jump show_question_q_c_48_id_B


label show_question_q_c_48_id_A:
    $ user_journey_summary.append("Di situasi Ada tawaran job dengan Gaji besar, tapi kamu belum tau apa kerjaannya. Orang tersebut juga cukup mencurigakan, user memilih: Tolak. 'Tawarannya belum jelas' tidak yakin bakal dibawa kemana., dengan poin MBTI: Intuitive & Feeling")
    call ai_react_logic from _call_ai_react_logic_94
    return

label show_question_q_c_48_id_B:
    $ user_journey_summary.append("Di situasi Ada tawaran job dengan Gaji besar, tapi kamu belum tau apa kerjaannya. Orang tersebut juga cukup mencurigakan, user memilih: Terima aja. Secara finansial kita lagi butuh uangnya., dengan poin MBTI: Sensing & Thinking")
    call ai_react_logic from _call_ai_react_logic_95
    return

label show_question_q_c_49_id:
    scene bg abstrak with dissolve
    $ narasi_asli = "Kamu harus memilih satu skill untuk dipelajari seumur hidup."
    n "Kamu harus memilih satu skill untuk dipelajari seumur hidup."

    menu:
        "Kamu harus memilih satu skill untuk dipelajari seumur hidup."

        "Skill teknis yang berguna buat cari kerja.":
            $ SN -= 5
            $ TF -= 5
            $ user_choice_text = "Skill teknis yang berguna buat cari kerja."
            $ last_answer = "Sensing & Thinking"
            jump show_question_q_c_49_id_A

        "Skill seni yang bisa menyentuh hati orang.":
            $ SN += 5
            $ TF += 5
            $ user_choice_text = "Skill seni yang bisa menyentuh hati orang."
            $ last_answer = "Intuitive & Feeling"
            jump show_question_q_c_49_id_B


label show_question_q_c_49_id_A:
    $ user_journey_summary.append("Di situasi Kamu harus memilih satu skill untuk dipelajari seumur hidup., user memilih: Skill teknis yang berguna buat cari kerja., dengan poin MBTI: Sensing & Thinking")
    call ai_react_logic from _call_ai_react_logic_96
    return

label show_question_q_c_49_id_B:
    $ user_journey_summary.append("Di situasi Kamu harus memilih satu skill untuk dipelajari seumur hidup., user memilih: Skill seni yang bisa menyentuh hati orang., dengan poin MBTI: Intuitive & Feeling")
    call ai_react_logic from _call_ai_react_logic_97
    return

label show_question_q_c_50_id:
    scene bg kafe with dissolve
    $ narasi_asli = "Temanmu debat soal fakta sains tapi datanya salah semua."
    n "Temanmu debat soal fakta sains tapi datanya salah semua."

    menu:
        "Temanmu debat soal fakta sains tapi datanya salah semua."

        "Koreksi dia. Tunjukkan data asli agar dia tidak membuat dirinya malu.":
            $ SN -= 5
            $ TF -= 5
            $ user_choice_text = "Koreksi dia. Tunjukkan data asli agar dia tidak membuat dirinya malu."
            $ last_answer = "Sensing & Thinking"
            jump show_question_q_c_50_id_A

        "Biarkan saja. Nanti dia sadar sendiri, daripada ribut di sini.":
            $ SN += 5
            $ TF += 5
            $ user_choice_text = "Biarkan saja. Nanti dia sadar sendiri, daripada ribut di sini."
            $ last_answer = "Intuitive & Feeling"
            jump show_question_q_c_50_id_B


label show_question_q_c_50_id_A:
    $ user_journey_summary.append("Di situasi Temanmu debat soal fakta sains tapi datanya salah semua., user memilih: Koreksi dia. Tunjukkan data asli agar dia tidak membuat dirinya malu., dengan poin MBTI: Sensing & Thinking")
    call ai_react_logic from _call_ai_react_logic_98
    return

label show_question_q_c_50_id_B:
    $ user_journey_summary.append("Di situasi Temanmu debat soal fakta sains tapi datanya salah semua., user memilih: Biarkan saja. Nanti dia sadar sendiri, daripada ribut di sini., dengan poin MBTI: Intuitive & Feeling")
    call ai_react_logic from _call_ai_react_logic_99
    return

label show_question_q_c_51_id:
    scene bg stasiun with dissolve
    $ narasi_asli = "(Hilang!) Tiket keretamu hilang! Kereta berangkat 5 menit lagi."
    n "(Hilang!) Tiket keretamu hilang!"
    n "Kereta berangkat 5 menit lagi."

    menu:
        "(Hilang!) Tiket keretamu hilang! Kereta berangkat 5 menit lagi."

        "Cek saku, tas, lantai secara urut. Jangan panik, coba ingat kembali.":
            $ SN -= 5
            $ JP -= 5
            $ user_choice_text = "Cek saku, tas, lantai secara urut. Jangan panik, coba ingat kembali."
            $ last_answer = "Sensing & Judging"
            jump show_question_q_c_51_id_A

        "Cari tiket di tempat yang mungkin terselip. Bisa jadi jatuh di jalan.":
            $ SN += 5
            $ JP += 5
            $ user_choice_text = "Cari tiket di tempat yang mungkin terselip. Bisa jadi jatuh di jalan."
            $ last_answer = "Intuitive & Perceiving"
            jump show_question_q_c_51_id_B


label show_question_q_c_51_id_A:
    $ user_journey_summary.append("Di situasi (Hilang!) Tiket keretamu hilang! Kereta berangkat 5 menit lagi., user memilih: Cek saku, tas, lantai secara urut. Jangan panik, coba ingat kembali., dengan poin MBTI: Sensing & Judging")
    call ai_react_logic from _call_ai_react_logic_100
    return

label show_question_q_c_51_id_B:
    $ user_journey_summary.append("Di situasi (Hilang!) Tiket keretamu hilang! Kereta berangkat 5 menit lagi., user memilih: Cari tiket di tempat yang mungkin terselip. Bisa jadi jatuh di jalan., dengan poin MBTI: Intuitive & Perceiving")
    call ai_react_logic from _call_ai_react_logic_101
    return

label show_question_q_c_52_id:
    scene bg dapur with dissolve
    $ narasi_asli = "Kamu lapar, tapi di kulkas cuma ada telur, selai, dan daging."
    n "Kamu lapar, tapi di kulkas cuma ada telur, selai, dan daging."

    menu:
        "Kamu lapar, tapi di kulkas cuma ada telur, selai, dan daging."

        "Masak telur dadar aja. Pasti enak dan sudah jelas rasanya.":
            $ SN -= 5
            $ JP -= 5
            $ user_choice_text = "Masak telur dadar aja. Pasti enak dan sudah jelas rasanya."
            $ last_answer = "Sensing & Judging"
            jump show_question_q_c_52_id_A

        "Campur semuanya! Siapa tahu jadi masterpiece baru.":
            $ SN += 5
            $ JP += 5
            $ user_choice_text = "Campur semuanya! Siapa tahu jadi masterpiece baru."
            $ last_answer = "Intuitive & Perceiving"
            jump show_question_q_c_52_id_B


label show_question_q_c_52_id_A:
    $ user_journey_summary.append("Di situasi Kamu lapar, tapi di kulkas cuma ada telur, selai, dan daging., user memilih: Masak telur dadar aja. Pasti enak dan sudah jelas rasanya., dengan poin MBTI: Sensing & Judging")
    call ai_react_logic from _call_ai_react_logic_102
    return

label show_question_q_c_52_id_B:
    $ user_journey_summary.append("Di situasi Kamu lapar, tapi di kulkas cuma ada telur, selai, dan daging., user memilih: Campur semuanya! Siapa tahu jadi masterpiece baru., dengan poin MBTI: Intuitive & Perceiving")
    call ai_react_logic from _call_ai_react_logic_103
    return

label show_question_q_c_53_id:
    scene bg room with dissolve
    $ narasi_asli = "Kamu ada ujian besok, tapi kamu baru ingat 1 hari sebelum hari-H"
    n "Kamu ada ujian besok, tapi kamu baru ingat 1 hari sebelum hari-H"

    menu:
        "Kamu ada ujian besok, tapi kamu baru ingat 1 hari sebelum hari-H"

        "Baca rangkuman bab sesuai apa yang mungkin keluar di ujian.":
            $ SN -= 5
            $ JP -= 5
            $ user_choice_text = "Baca rangkuman bab sesuai apa yang mungkin keluar di ujian."
            $ last_answer = "Sensing & Judging"
            jump show_question_q_c_53_id_A

        "Baca bagian yang paling kamu pahami saja, sisanya bisa dipikir saat ujian.":
            $ SN += 5
            $ JP += 5
            $ user_choice_text = "Baca bagian yang paling kamu pahami saja, sisanya bisa dipikir saat ujian."
            $ last_answer = "Intuitive & Perceiving"
            jump show_question_q_c_53_id_B


label show_question_q_c_53_id_A:
    $ user_journey_summary.append("Di situasi Kamu ada ujian besok, tapi kamu baru ingat 1 hari sebelum hari-H, user memilih: Baca rangkuman bab sesuai apa yang mungkin keluar di ujian., dengan poin MBTI: Sensing & Judging")
    call ai_react_logic from _call_ai_react_logic_104
    return

label show_question_q_c_53_id_B:
    $ user_journey_summary.append("Di situasi Kamu ada ujian besok, tapi kamu baru ingat 1 hari sebelum hari-H, user memilih: Baca bagian yang paling kamu pahami saja, sisanya bisa dipikir saat ujian., dengan poin MBTI: Intuitive & Perceiving")
    call ai_react_logic from _call_ai_react_logic_105
    return

label show_question_q_c_54_id:
    scene bg kantor with dissolve
    $ narasi_asli = "Bos minta kamu kerjakan proyek 'Rahasia' tanpa petunjuk jelas."
    n "Bos minta kamu kerjakan proyek 'Rahasia' tanpa petunjuk jelas."

    menu:
        "Bos minta kamu kerjakan proyek 'Rahasia' tanpa petunjuk jelas."

        "Tolak halus. 'Saya butuh detail dan deadline yang jelas.'":
            $ SN -= 5
            $ JP -= 5
            $ user_choice_text = "Tolak halus. 'Saya butuh detail dan deadline yang jelas.'"
            $ last_answer = "Sensing & Judging"
            jump show_question_q_c_54_id_A

        "Terima! 'Siap, saya akan improvisasi sambil jalan.'":
            $ SN += 5
            $ JP += 5
            $ user_choice_text = "Terima! 'Siap, saya akan improvisasi sambil jalan.'"
            $ last_answer = "Intuitive & Perceiving"
            jump show_question_q_c_54_id_B


label show_question_q_c_54_id_A:
    $ user_journey_summary.append("Di situasi Bos minta kamu kerjakan proyek 'Rahasia' tanpa petunjuk jelas., user memilih: Tolak halus. 'Saya butuh detail dan deadline yang jelas.', dengan poin MBTI: Sensing & Judging")
    call ai_react_logic from _call_ai_react_logic_106
    return

label show_question_q_c_54_id_B:
    $ user_journey_summary.append("Di situasi Bos minta kamu kerjakan proyek 'Rahasia' tanpa petunjuk jelas., user memilih: Terima! 'Siap, saya akan improvisasi sambil jalan.', dengan poin MBTI: Intuitive & Perceiving")
    call ai_react_logic from _call_ai_react_logic_107
    return

label show_question_q_c_55_id:
    scene bg stasiun with dissolve
    $ narasi_asli = "Kamu mau pindah kota, tapi barangmu kebanyakan!"
    n "Kamu mau pindah kota, tapi barangmu kebanyakan!"

    menu:
        "Kamu mau pindah kota, tapi barangmu kebanyakan!"

        "Sortir barang. Buang yang menurutmu kurang penting.":
            $ SN -= 5
            $ JP -= 5
            $ user_choice_text = "Sortir barang. Buang yang menurutmu kurang penting."
            $ last_answer = "Sensing & Judging"
            jump show_question_q_c_55_id_A

        "'Kita gak tahu, mungkin butuh barang ini di kemudian hari, jadi bawa semua!'. Nanti semua bisa diatur lagi di sana.":
            $ SN += 5
            $ JP += 5
            $ user_choice_text = "'Kita gak tahu, mungkin butuh barang ini di kemudian hari, jadi bawa semua!'. Nanti semua bisa diatur lagi di sana."
            $ last_answer = "Intuitive & Perceiving"
            jump show_question_q_c_55_id_B


label show_question_q_c_55_id_A:
    $ user_journey_summary.append("Di situasi Kamu mau pindah kota, tapi barangmu kebanyakan!, user memilih: Sortir barang. Buang yang menurutmu kurang penting., dengan poin MBTI: Sensing & Judging")
    call ai_react_logic from _call_ai_react_logic_108
    return

label show_question_q_c_55_id_B:
    $ user_journey_summary.append("Di situasi Kamu mau pindah kota, tapi barangmu kebanyakan!, user memilih: 'Kita gak tahu, mungkin butuh barang ini di kemudian hari, jadi bawa semua!'. Nanti semua bisa diatur lagi di sana., dengan poin MBTI: Intuitive & Perceiving")
    call ai_react_logic from _call_ai_react_logic_109
    return

label show_question_q_c_56_id:
    scene bg room with dissolve
    $ narasi_asli = "Adikmu memecahkan vas bunga kesayangan ibu, dia takut banget, hampir mau nangis"
    n "Adikmu memecahkan vas bunga kesayangan ibu, dia takut banget, hampir mau nangis"

    menu:
        "Adikmu memecahkan vas bunga kesayangan ibu, dia takut banget, hampir mau nangis"

        "Suruh dia ngaku. Salah ya salah, harus tanggung jawab.":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "Suruh dia ngaku. Salah ya salah, harus tanggung jawab."
            $ last_answer = "Thinking & Judging"
            jump show_question_q_c_56_id_A

        "Bantu sembunyikan pecahannya. Kasihan kalau dia dimarahi.":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "Bantu sembunyikan pecahannya. Kasihan kalau dia dimarahi."
            $ last_answer = "Feeling & Perceiving"
            jump show_question_q_c_56_id_B


label show_question_q_c_56_id_A:
    $ user_journey_summary.append("Di situasi Adikmu memecahkan vas bunga kesayangan ibu, dia takut banget, hampir mau nangis, user memilih: Suruh dia ngaku. Salah ya salah, harus tanggung jawab., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic from _call_ai_react_logic_110
    return

label show_question_q_c_56_id_B:
    $ user_journey_summary.append("Di situasi Adikmu memecahkan vas bunga kesayangan ibu, dia takut banget, hampir mau nangis, user memilih: Bantu sembunyikan pecahannya. Kasihan kalau dia dimarahi., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic from _call_ai_react_logic_111
    return

label show_question_q_c_57_id:
    scene bg kafe with dissolve
    $ narasi_asli = "Kamu punya ide bisnis aneh tapi inovatif. Kapan kamu mau mulai mewujudkannya?"
    n "Kamu punya ide bisnis aneh tapi inovatif."
    n "Kapan kamu mau mulai mewujudkannya?"

    menu:
        "Kamu punya ide bisnis aneh tapi inovatif. Kapan kamu mau mulai mewujudkannya?"

        "Nanti, setelah analisis untung-rugi selesai 100%%.":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "Nanti, setelah analisis untung-rugi selesai 100%%."
            $ last_answer = "Thinking & Judging"
            jump show_question_q_c_57_id_A

        "Sekarang! Yang penting banyak orang suka idenya.":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "Sekarang! Yang penting banyak orang suka idenya."
            $ last_answer = "Feeling & Perceiving"
            jump show_question_q_c_57_id_B


label show_question_q_c_57_id_A:
    $ user_journey_summary.append("Di situasi Kamu punya ide bisnis aneh tapi inovatif. Kapan kamu mau mulai mewujudkannya?, user memilih: Nanti, setelah analisis untung-rugi selesai 100%%., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic from _call_ai_react_logic_112
    return

label show_question_q_c_57_id_B:
    $ user_journey_summary.append("Di situasi Kamu punya ide bisnis aneh tapi inovatif. Kapan kamu mau mulai mewujudkannya?, user memilih: Sekarang! Yang penting banyak orang suka idenya., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic from _call_ai_react_logic_113
    return

label show_question_q_c_58_id:
    scene bg kantor with dissolve
    $ narasi_asli = "Tim olahragamu kalah terus. Sebagai kapten, apa yang kamu katakan?"
    n "Tim olahragamu kalah terus."
    n "Sebagai kapten, apa yang kamu katakan?"

    menu:
        "Tim olahragamu kalah terus. Sebagai kapten, apa yang kamu katakan?"

        "'Latihan ditambah! Kita harus menang, skor adalah segalanya.'":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "'Latihan ditambah! Kita harus menang, skor adalah segalanya.'"
            $ last_answer = "Thinking & Judging"
            jump show_question_q_c_58_id_A

        "'Santai guys. Yang penting kita enjoy aja main bareng.'":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "'Santai guys. Yang penting kita enjoy aja main bareng.'"
            $ last_answer = "Feeling & Perceiving"
            jump show_question_q_c_58_id_B


label show_question_q_c_58_id_A:
    $ user_journey_summary.append("Di situasi Tim olahragamu kalah terus. Sebagai kapten, apa yang kamu katakan?, user memilih: 'Latihan ditambah! Kita harus menang, skor adalah segalanya.', dengan poin MBTI: Thinking & Judging")
    call ai_react_logic from _call_ai_react_logic_114
    return

label show_question_q_c_58_id_B:
    $ user_journey_summary.append("Di situasi Tim olahragamu kalah terus. Sebagai kapten, apa yang kamu katakan?, user memilih: 'Santai guys. Yang penting kita enjoy aja main bareng.', dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic from _call_ai_react_logic_115
    return

label show_question_q_c_59_id:
    scene bg abstrak with dissolve
    $ narasi_asli = "Kamu menemukan Senjata Kuno dalam eksplorasi. Apa yang jadi perhatianmu?"
    n "Kamu menemukan Senjata Kuno dalam eksplorasi."
    n "Apa yang jadi perhatianmu?"

    menu:
        "Kamu menemukan Senjata Kuno dalam eksplorasi. Apa yang jadi perhatianmu?"

        "Kekuatannya dan kondisinya yang masih utuh.":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "Kekuatannya dan kondisinya yang masih utuh."
            $ last_answer = "Thinking & Judging"
            jump show_question_q_c_59_id_A

        "Cerita legendanya dan misteri siapa pemiliknya dulu.":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "Cerita legendanya dan misteri siapa pemiliknya dulu."
            $ last_answer = "Feeling & Perceiving"
            jump show_question_q_c_59_id_B


label show_question_q_c_59_id_A:
    $ user_journey_summary.append("Di situasi Kamu menemukan Senjata Kuno dalam eksplorasi. Apa yang jadi perhatianmu?, user memilih: Kekuatannya dan kondisinya yang masih utuh., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic from _call_ai_react_logic_116
    return

label show_question_q_c_59_id_B:
    $ user_journey_summary.append("Di situasi Kamu menemukan Senjata Kuno dalam eksplorasi. Apa yang jadi perhatianmu?, user memilih: Cerita legendanya dan misteri siapa pemiliknya dulu., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic from _call_ai_react_logic_117
    return

label show_question_q_c_60_id:
    scene bg kantor with dissolve
    $ narasi_asli = "Ada aturan kantor baru yang menyusahkan karyawan."
    n "Ada aturan kantor baru yang menyusahkan karyawan."

    menu:
        "Ada aturan kantor baru yang menyusahkan karyawan."

        "Ajukan revisi resmi. Tunjukkan poin yang tidak efisien.":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "Ajukan revisi resmi. Tunjukkan poin yang tidak efisien."
            $ last_answer = "Thinking & Judging"
            jump show_question_q_c_60_id_A

        "Bikin petisi secara emosional. Minta kelonggaran aturan.":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "Bikin petisi secara emosional. Minta kelonggaran aturan."
            $ last_answer = "Feeling & Perceiving"
            jump show_question_q_c_60_id_B


label show_question_q_c_60_id_A:
    $ user_journey_summary.append("Di situasi Ada aturan kantor baru yang menyusahkan karyawan., user memilih: Ajukan revisi resmi. Tunjukkan poin yang tidak efisien., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic from _call_ai_react_logic_118
    return

label show_question_q_c_60_id_B:
    $ user_journey_summary.append("Di situasi Ada aturan kantor baru yang menyusahkan karyawan., user memilih: Bikin petisi secara emosional. Minta kelonggaran aturan., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic from _call_ai_react_logic_119
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

        "Go home alone and eat nutritious food to recover physically.":
            $ IE -= 5
            $ SN -= 5
            $ user_choice_text = "Go home alone and eat nutritious food to recover physically."
            $ last_answer = "Introvert & Sensing"
            jump show_question_q_a_01_en_A

        "Gather with friends and talk about the idea for the next trip.":
            $ IE += 5
            $ SN += 5
            $ user_choice_text = "Gather with friends and talk about the idea for the next trip."
            $ last_answer = "Extrovert & Intuitive"
            jump show_question_q_a_01_en_B


label show_question_q_a_01_en_A:
    $ user_journey_summary.append("Di situasi (Rumble...) Oh, so tired after walking around today! Your energy is depleted and you are hungry. What does your body need?, user memilih: Go home alone and eat nutritious food to recover physically., dengan poin MBTI: Introvert & Sensing")
    call ai_react_logic from _call_ai_react_logic_120
    return

label show_question_q_a_01_en_B:
    $ user_journey_summary.append("Di situasi (Rumble...) Oh, so tired after walking around today! Your energy is depleted and you are hungry. What does your body need?, user memilih: Gather with friends and talk about the idea for the next trip., dengan poin MBTI: Extrovert & Intuitive")
    call ai_react_logic from _call_ai_react_logic_121
    return

label show_question_q_a_02_en:
    scene bg kafe with dissolve
    $ narasi_asli = "(Ring!) The cafe door opens! A cool, mysterious figure enters. What is the first thing that catches your attention?"
    n "(Ring!) The cafe door opens!"
    n "A cool, mysterious figure enters."
    n "What is the first thing that catches your attention?"

    menu:
        "(Ring!) The cafe door opens! A cool, mysterious figure enters. What is the first thing that catches your attention?"

        "Observe them from your seat, while monitoring their movements.":
            $ IE -= 5
            $ SN -= 5
            $ user_choice_text = "Observe them from your seat, while monitoring their movements."
            $ last_answer = "Introvert & Sensing"
            jump show_question_q_a_02_en_A

        "Immediately greet them, and ask where they are going with such an outfit.":
            $ IE += 5
            $ SN += 5
            $ user_choice_text = "Immediately greet them, and ask where they are going with such an outfit."
            $ last_answer = "Extrovert & Intuitive"
            jump show_question_q_a_02_en_B


label show_question_q_a_02_en_A:
    $ user_journey_summary.append("Di situasi (Ring!) The cafe door opens! A cool, mysterious figure enters. What is the first thing that catches your attention?, user memilih: Observe them from your seat, while monitoring their movements., dengan poin MBTI: Introvert & Sensing")
    call ai_react_logic from _call_ai_react_logic_122
    return

label show_question_q_a_02_en_B:
    $ user_journey_summary.append("Di situasi (Ring!) The cafe door opens! A cool, mysterious figure enters. What is the first thing that catches your attention?, user memilih: Immediately greet them, and ask where they are going with such an outfit., dengan poin MBTI: Extrovert & Intuitive")
    call ai_react_logic from _call_ai_react_logic_123
    return

label show_question_q_a_03_en:
    scene bg kantor with dissolve
    $ narasi_asli = "(Thud!) The boss gives you a mountain-high stack of jobs! Impossible to finish alone today."
    n "(Thud!) The boss gives you a mountain-high stack of jobs!"
    n "Impossible to finish alone today."

    menu:
        "(Thud!) The boss gives you a mountain-high stack of jobs! Impossible to finish alone today."

        "Call the whole team to divide the physical tasks right now.":
            $ IE += 5
            $ SN -= 5
            $ user_choice_text = "Call the whole team to divide the physical tasks right now."
            $ last_answer = "Extrovert & Sensing"
            jump show_question_q_a_03_en_A

        "Call a close colleague to try out the assistance program you just developed.":
            $ IE -= 5
            $ SN += 5
            $ user_choice_text = "Call a close colleague to try out the assistance program you just developed."
            $ last_answer = "Introvert & Intuitive"
            jump show_question_q_a_03_en_B


label show_question_q_a_03_en_A:
    $ user_journey_summary.append("Di situasi (Thud!) The boss gives you a mountain-high stack of jobs! Impossible to finish alone today., user memilih: Call the whole team to divide the physical tasks right now., dengan poin MBTI: Extrovert & Sensing")
    call ai_react_logic from _call_ai_react_logic_124
    return

label show_question_q_a_03_en_B:
    $ user_journey_summary.append("Di situasi (Thud!) The boss gives you a mountain-high stack of jobs! Impossible to finish alone today., user memilih: Call a close colleague to try out the assistance program you just developed., dengan poin MBTI: Introvert & Intuitive")
    call ai_react_logic from _call_ai_react_logic_125
    return

label show_question_q_a_04_en:
    scene bg dapur with dissolve
    $ narasi_asli = "(Oh no!) You want to cook a special meal, but one main ingredient is gone—you forgot to buy it yesterday."
    n "(Oh no!) You want to cook a special meal, but one main ingredient is gone—you forgot to buy it yesterday."

    menu:
        "(Oh no!) You want to cook a special meal, but one main ingredient is gone—you forgot to buy it yesterday."

        "Contact and ask a friend to ask for the missing raw ingredient.":
            $ IE += 5
            $ SN -= 5
            $ user_choice_text = "Contact and ask a friend to ask for the missing raw ingredient."
            $ last_answer = "Extrovert & Sensing"
            jump show_question_q_a_04_en_A

        "Stay in the kitchen and try experimenting by replacing it with another ingredient.":
            $ IE -= 5
            $ SN += 5
            $ user_choice_text = "Stay in the kitchen and try experimenting by replacing it with another ingredient."
            $ last_answer = "Introvert & Intuitive"
            jump show_question_q_a_04_en_B


label show_question_q_a_04_en_A:
    $ user_journey_summary.append("Di situasi (Oh no!) You want to cook a special meal, but one main ingredient is gone—you forgot to buy it yesterday., user memilih: Contact and ask a friend to ask for the missing raw ingredient., dengan poin MBTI: Extrovert & Sensing")
    call ai_react_logic from _call_ai_react_logic_126
    return

label show_question_q_a_04_en_B:
    $ user_journey_summary.append("Di situasi (Oh no!) You want to cook a special meal, but one main ingredient is gone—you forgot to buy it yesterday., user memilih: Stay in the kitchen and try experimenting by replacing it with another ingredient., dengan poin MBTI: Introvert & Intuitive")
    call ai_react_logic from _call_ai_react_logic_127
    return

label show_question_q_a_05_en:
    scene bg room with dissolve
    $ narasi_asli = "There is a 'Hot News!' poster that causes an uproar in the whole village! Everyone is talking about it."
    n "There is a 'Hot News!' poster that causes an uproar in the whole village!"
    n "Everyone is talking about it."

    menu:
        "There is a 'Hot News!' poster that causes an uproar in the whole village! Everyone is talking about it."

        "Join the comments with other residents and look for evidence of the incident.":
            $ IE += 5
            $ SN -= 5
            $ user_choice_text = "Join the comments with other residents and look for evidence of the incident."
            $ last_answer = "Extrovert & Sensing"
            jump show_question_q_a_05_en_A

        "Read and observe, try to imagine what really happened.":
            $ IE -= 5
            $ SN += 5
            $ user_choice_text = "Read and observe, try to imagine what really happened."
            $ last_answer = "Introvert & Intuitive"
            jump show_question_q_a_05_en_B


label show_question_q_a_05_en_A:
    $ user_journey_summary.append("Di situasi There is a 'Hot News!' poster that causes an uproar in the whole village! Everyone is talking about it., user memilih: Join the comments with other residents and look for evidence of the incident., dengan poin MBTI: Extrovert & Sensing")
    call ai_react_logic from _call_ai_react_logic_128
    return

label show_question_q_a_05_en_B:
    $ user_journey_summary.append("Di situasi There is a 'Hot News!' poster that causes an uproar in the whole village! Everyone is talking about it., user memilih: Read and observe, try to imagine what really happened., dengan poin MBTI: Introvert & Intuitive")
    call ai_react_logic from _call_ai_react_logic_129
    return

label show_question_q_a_06_en:
    scene bg kantor with dissolve
    $ narasi_asli = "(Danger!) Your teammate accidentally lost a valuable company item! They look like they are about to cry."
    n "(Danger!) Your teammate accidentally lost a valuable company item!"
    n "They look like they are about to cry."

    menu:
        "(Danger!) Your teammate accidentally lost a valuable company item! They look like they are about to cry."

        "Confront them immediately so they take responsibility.":
            $ IE += 5
            $ TF -= 5
            $ user_choice_text = "Confront them immediately so they take responsibility."
            $ last_answer = "Extrovert & Thinking"
            jump show_question_q_a_06_en_A

        "Pull them away and say 'it's okay, we'll find a solution together'.":
            $ IE -= 5
            $ TF += 5
            $ user_choice_text = "Pull them away and say 'it's okay, we'll find a solution together'."
            $ last_answer = "Introvert & Feeling"
            jump show_question_q_a_06_en_B


label show_question_q_a_06_en_A:
    $ user_journey_summary.append("Di situasi (Danger!) Your teammate accidentally lost a valuable company item! They look like they are about to cry., user memilih: Confront them immediately so they take responsibility., dengan poin MBTI: Extrovert & Thinking")
    call ai_react_logic from _call_ai_react_logic_130
    return

label show_question_q_a_06_en_B:
    $ user_journey_summary.append("Di situasi (Danger!) Your teammate accidentally lost a valuable company item! They look like they are about to cry., user memilih: Pull them away and say 'it's okay, we'll find a solution together'., dengan poin MBTI: Introvert & Feeling")
    call ai_react_logic from _call_ai_react_logic_131
    return

label show_question_q_a_07_en:
    scene bg taman with dissolve
    $ narasi_asli = "There is a new rule in the park: 'No Loud Laughter'."
    n "There is a new rule in the park: 'No Loud Laughter'."

    menu:
        "There is a new rule in the park: 'No Loud Laughter'."

        "Protest to the officer because the rule is illogical.":
            $ IE += 5
            $ TF -= 5
            $ user_choice_text = "Protest to the officer because the rule is illogical."
            $ last_answer = "Extrovert & Thinking"
            jump show_question_q_a_07_en_A

        "Remain silent, because maybe it's true, it could ruin the peaceful atmosphere.":
            $ IE -= 5
            $ TF += 5
            $ user_choice_text = "Remain silent, because maybe it's true, it could ruin the peaceful atmosphere."
            $ last_answer = "Introvert & Feeling"
            jump show_question_q_a_07_en_B


label show_question_q_a_07_en_A:
    $ user_journey_summary.append("Di situasi There is a new rule in the park: 'No Loud Laughter'., user memilih: Protest to the officer because the rule is illogical., dengan poin MBTI: Extrovert & Thinking")
    call ai_react_logic from _call_ai_react_logic_132
    return

label show_question_q_a_07_en_B:
    $ user_journey_summary.append("Di situasi There is a new rule in the park: 'No Loud Laughter'., user memilih: Remain silent, because maybe it's true, it could ruin the peaceful atmosphere., dengan poin MBTI: Introvert & Feeling")
    call ai_react_logic from _call_ai_react_logic_133
    return

label show_question_q_a_08_en:
    scene bg kafe with dissolve
    $ narasi_asli = "The visitor at the next table looks very worried and sighs deeply..."
    n "The visitor at the next table looks very worried and sighs deeply..."

    menu:
        "The visitor at the next table looks very worried and sighs deeply..."

        "Try to approach and ask directly, analyze the problem to find a solution.":
            $ IE += 5
            $ TF -= 5
            $ user_choice_text = "Try to approach and ask directly, analyze the problem to find a solution."
            $ last_answer = "Extrovert & Thinking"
            jump show_question_q_a_08_en_A

        "Quietly give them a tissue because you feel sorry for them.":
            $ IE -= 5
            $ TF += 5
            $ user_choice_text = "Quietly give them a tissue because you feel sorry for them."
            $ last_answer = "Introvert & Feeling"
            jump show_question_q_a_08_en_B


label show_question_q_a_08_en_A:
    $ user_journey_summary.append("Di situasi The visitor at the next table looks very worried and sighs deeply..., user memilih: Try to approach and ask directly, analyze the problem to find a solution., dengan poin MBTI: Extrovert & Thinking")
    call ai_react_logic from _call_ai_react_logic_134
    return

label show_question_q_a_08_en_B:
    $ user_journey_summary.append("Di situasi The visitor at the next table looks very worried and sighs deeply..., user memilih: Quietly give them a tissue because you feel sorry for them., dengan poin MBTI: Introvert & Feeling")
    call ai_react_logic from _call_ai_react_logic_135
    return

label show_question_q_a_09_en:
    scene bg kantor with dissolve
    $ narasi_asli = "The ship captain distributes the treasure, but your share is the least! Unfair!"
    n "The ship captain distributes the treasure, but your share is the least!"
    n "Unfair!"

    menu:
        "The ship captain distributes the treasure, but your share is the least! Unfair!"

        "Debate with the Captain because the calculation is wrong.":
            $ IE += 5
            $ TF -= 5
            $ user_choice_text = "Debate with the Captain because the calculation is wrong."
            $ last_answer = "Extrovert & Thinking"
            jump show_question_q_a_09_en_A

        "Just accept it because maybe the captain needs it more.":
            $ IE -= 5
            $ TF += 5
            $ user_choice_text = "Just accept it because maybe the captain needs it more."
            $ last_answer = "Introvert & Feeling"
            jump show_question_q_a_09_en_B


label show_question_q_a_09_en_A:
    $ user_journey_summary.append("Di situasi The ship captain distributes the treasure, but your share is the least! Unfair!, user memilih: Debate with the Captain because the calculation is wrong., dengan poin MBTI: Extrovert & Thinking")
    call ai_react_logic from _call_ai_react_logic_136
    return

label show_question_q_a_09_en_B:
    $ user_journey_summary.append("Di situasi The ship captain distributes the treasure, but your share is the least! Unfair!, user memilih: Just accept it because maybe the captain needs it more., dengan poin MBTI: Introvert & Feeling")
    call ai_react_logic from _call_ai_react_logic_137
    return

label show_question_q_a_10_en:
    scene bg abstrak with dissolve
    $ narasi_asli = "(Mysterious Voice) 'Choose your destiny... Left Door or Right Door?' Without any clues at all!"
    n "(Mysterious Voice) 'Choose your destiny..."
    n "Left Door or Right Door?' Without any clues at all!"

    menu:
        "(Mysterious Voice) 'Choose your destiny... Left Door or Right Door?' Without any clues at all!"

        "Ask the voice back 'approximately, which door is the safest?'":
            $ IE += 5
            $ TF -= 5
            $ user_choice_text = "Ask the voice back 'approximately, which door is the safest?'"
            $ last_answer = "Extrovert & Thinking"
            jump show_question_q_a_10_en_A

        "Close your eyes and follow your heart.":
            $ IE -= 5
            $ TF += 5
            $ user_choice_text = "Close your eyes and follow your heart."
            $ last_answer = "Introvert & Feeling"
            jump show_question_q_a_10_en_B


label show_question_q_a_10_en_A:
    $ user_journey_summary.append("Di situasi (Mysterious Voice) 'Choose your destiny... Left Door or Right Door?' Without any clues at all!, user memilih: Ask the voice back 'approximately, which door is the safest?', dengan poin MBTI: Extrovert & Thinking")
    call ai_react_logic from _call_ai_react_logic_138
    return

label show_question_q_a_10_en_B:
    $ user_journey_summary.append("Di situasi (Mysterious Voice) 'Choose your destiny... Left Door or Right Door?' Without any clues at all!, user memilih: Close your eyes and follow your heart., dengan poin MBTI: Introvert & Feeling")
    call ai_react_logic from _call_ai_react_logic_139
    return

label show_question_q_a_11_en:
    scene bg kafe with dissolve
    $ narasi_asli = "Suddenly your friend pulls your hand. 'Let's go to the beach RIGHT NOW!'"
    n "Suddenly your friend pulls your hand."
    n "'Let's go to the beach RIGHT NOW!'"

    menu:
        "Suddenly your friend pulls your hand. 'Let's go to the beach RIGHT NOW!'"

        "Go! We’ll think about the consequences later.":
            $ IE += 5
            $ JP += 5
            $ user_choice_text = "Go! We’ll think about the consequences later."
            $ last_answer = "Extrovert & Perceiving"
            jump show_question_q_a_11_en_A

        "Refuse because you have to check the schedule first.":
            $ IE -= 5
            $ JP -= 5
            $ user_choice_text = "Refuse because you have to check the schedule first."
            $ last_answer = "Introvert & Judging"
            jump show_question_q_a_11_en_B


label show_question_q_a_11_en_A:
    $ user_journey_summary.append("Di situasi Suddenly your friend pulls your hand. 'Let's go to the beach RIGHT NOW!', user memilih: Go! We’ll think about the consequences later., dengan poin MBTI: Extrovert & Perceiving")
    call ai_react_logic from _call_ai_react_logic_140
    return

label show_question_q_a_11_en_B:
    $ user_journey_summary.append("Di situasi Suddenly your friend pulls your hand. 'Let's go to the beach RIGHT NOW!', user memilih: Refuse because you have to check the schedule first., dengan poin MBTI: Introvert & Judging")
    call ai_react_logic from _call_ai_react_logic_141
    return

label show_question_q_a_12_en:
    scene bg stasiun with dissolve
    $ narasi_asli = "(Toot! Toot!) The last train has left without you! You missed the train you were supposed to take home!"
    n "(Toot!Toot!)"
    n  "The last train has left without you!"
    n "You missed the train you were supposed to take home!"

    menu:
        "(Toot! Toot!) The last train has left without you! You missed the train you were supposed to take home!"

        "Awesome! We are free to explore the city!.":
            $ IE += 5
            $ JP += 5
            $ user_choice_text = "Awesome! We are free to explore the city!."
            $ last_answer = "Extrovert & Perceiving"
            jump show_question_q_a_12_en_A

        "Oh dear! I should have arrived earlier.":
            $ IE -= 5
            $ JP -= 5
            $ user_choice_text = "Oh dear! I should have arrived earlier."
            $ last_answer = "Introvert & Judging"
            jump show_question_q_a_12_en_B


label show_question_q_a_12_en_A:
    $ user_journey_summary.append("Di situasi (Toot! Toot!) The last train has left without you! You missed the train you were supposed to take home!, user memilih: Awesome! We are free to explore the city!., dengan poin MBTI: Extrovert & Perceiving")
    call ai_react_logic from _call_ai_react_logic_142
    return

label show_question_q_a_12_en_B:
    $ user_journey_summary.append("Di situasi (Toot! Toot!) The last train has left without you! You missed the train you were supposed to take home!, user memilih: Oh dear! I should have arrived earlier., dengan poin MBTI: Introvert & Judging")
    call ai_react_logic from _call_ai_react_logic_143
    return

label show_question_q_a_13_en:
    scene bg taman with dissolve
    $ narasi_asli = "You are appointed as the picnic leader tomorrow. What is your plan?"
    n "You are appointed as the picnic leader tomorrow."
    n "What is your plan?"

    menu:
        "You are appointed as the picnic leader tomorrow. What is your plan?"

        "Invite all friends! They are free to bring whatever they want.":
            $ IE += 5
            $ JP += 5
            $ user_choice_text = "Invite all friends! They are free to bring whatever they want."
            $ last_answer = "Extrovert & Perceiving"
            jump show_question_q_a_13_en_A

        "Try to choose the best menu according to you and determine the exact time.":
            $ IE -= 5
            $ JP -= 5
            $ user_choice_text = "Try to choose the best menu according to you and determine the exact time."
            $ last_answer = "Introvert & Judging"
            jump show_question_q_a_13_en_B


label show_question_q_a_13_en_A:
    $ user_journey_summary.append("Di situasi You are appointed as the picnic leader tomorrow. What is your plan?, user memilih: Invite all friends! They are free to bring whatever they want., dengan poin MBTI: Extrovert & Perceiving")
    call ai_react_logic from _call_ai_react_logic_144
    return

label show_question_q_a_13_en_B:
    $ user_journey_summary.append("Di situasi You are appointed as the picnic leader tomorrow. What is your plan?, user memilih: Try to choose the best menu according to you and determine the exact time., dengan poin MBTI: Introvert & Judging")
    call ai_react_logic from _call_ai_react_logic_145
    return

label show_question_q_a_14_en:
    scene bg room with dissolve
    $ narasi_asli = "You look at your room. It feels dull and boring."
    n "You look at your room."
    n "It feels dull and boring."

    menu:
        "You look at your room. It feels dull and boring."

        "Change the paint and reorganize the items in the room now.":
            $ IE += 5
            $ JP += 5
            $ user_choice_text = "Change the paint and reorganize the items in the room now."
            $ last_answer = "Extrovert & Perceiving"
            jump show_question_q_a_14_en_A

        "Just let it be because this position is already efficient.":
            $ IE -= 5
            $ JP -= 5
            $ user_choice_text = "Just let it be because this position is already efficient."
            $ last_answer = "Introvert & Judging"
            jump show_question_q_a_14_en_B


label show_question_q_a_14_en_A:
    $ user_journey_summary.append("Di situasi You look at your room. It feels dull and boring., user memilih: Change the paint and reorganize the items in the room now., dengan poin MBTI: Extrovert & Perceiving")
    call ai_react_logic from _call_ai_react_logic_146
    return

label show_question_q_a_14_en_B:
    $ user_journey_summary.append("Di situasi You look at your room. It feels dull and boring., user memilih: Just let it be because this position is already efficient., dengan poin MBTI: Introvert & Judging")
    call ai_react_logic from _call_ai_react_logic_147
    return

label show_question_q_a_15_en:
    scene bg stasiun with dissolve
    $ narasi_asli = "You stop by the station souvenir shop. Many cute and interesting items!"
    n "You stop by the station souvenir shop."
    n "Many cute and interesting items!"

    menu:
        "You stop by the station souvenir shop. Many cute and interesting items!"

        "Ask the seller for advice and buy the first item you see.":
            $ IE += 5
            $ JP += 5
            $ user_choice_text = "Ask the seller for advice and buy the first item you see."
            $ last_answer = "Extrovert & Perceiving"
            jump show_question_q_a_15_en_A

        "Try to look around and buy according to your needs.":
            $ IE -= 5
            $ JP -= 5
            $ user_choice_text = "Try to look around and buy according to your needs."
            $ last_answer = "Introvert & Judging"
            jump show_question_q_a_15_en_B


label show_question_q_a_15_en_A:
    $ user_journey_summary.append("Di situasi You stop by the station souvenir shop. Many cute and interesting items!, user memilih: Ask the seller for advice and buy the first item you see., dengan poin MBTI: Extrovert & Perceiving")
    call ai_react_logic from _call_ai_react_logic_148
    return

label show_question_q_a_15_en_B:
    $ user_journey_summary.append("Di situasi You stop by the station souvenir shop. Many cute and interesting items!, user memilih: Try to look around and buy according to your needs., dengan poin MBTI: Introvert & Judging")
    call ai_react_logic from _call_ai_react_logic_149
    return

label show_question_q_a_16_en:
    scene bg kantor with dissolve
    $ narasi_asli = "Your friend is angry at you for no clear reason! Their face is red with rage!"
    n "Your friend is angry at you for no clear reason!"
    n "Their face is red with rage!"

    menu:
        "Your friend is angry at you for no clear reason! Their face is red with rage!"

        "Diffuse their anger and explain the evidence first.":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "Diffuse their anger and explain the evidence first."
            $ last_answer = "Thinking & Judging"
            jump show_question_q_a_16_en_A

        "'Why am I being yelled at? Did I do something wrong?'.":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "'Why am I being yelled at? Did I do something wrong?'."
            $ last_answer = "Feeling & Perceiving"
            jump show_question_q_a_16_en_B


label show_question_q_a_16_en_A:
    $ user_journey_summary.append("Di situasi Your friend is angry at you for no clear reason! Their face is red with rage!, user memilih: Diffuse their anger and explain the evidence first., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic from _call_ai_react_logic_150
    return

label show_question_q_a_16_en_B:
    $ user_journey_summary.append("Di situasi Your friend is angry at you for no clear reason! Their face is red with rage!, user memilih: 'Why am I being yelled at? Did I do something wrong?'., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic from _call_ai_react_logic_151
    return

label show_question_q_a_17_en:
    scene bg dapur with dissolve
    $ narasi_asli = "You are making a birthday cake, but the result is burnt and not good enough."
    n "You are making a birthday cake, but the result is burnt and not good enough."

    menu:
        "You are making a birthday cake, but the result is burnt and not good enough."

        "Throw it away! and try to make it again according to the recipe.":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "Throw it away! and try to make it again according to the recipe."
            $ last_answer = "Thinking & Judging"
            jump show_question_q_a_17_en_A

        "It's okay the appearance is not good, but it was made with full heart.":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "It's okay the appearance is not good, but it was made with full heart."
            $ last_answer = "Feeling & Perceiving"
            jump show_question_q_a_17_en_B


label show_question_q_a_17_en_A:
    $ user_journey_summary.append("Di situasi You are making a birthday cake, but the result is burnt and not good enough., user memilih: Throw it away! and try to make it again according to the recipe., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic from _call_ai_react_logic_152
    return

label show_question_q_a_17_en_B:
    $ user_journey_summary.append("Di situasi You are making a birthday cake, but the result is burnt and not good enough., user memilih: It's okay the appearance is not good, but it was made with full heart., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic from _call_ai_react_logic_153
    return

label show_question_q_a_18_en:
    scene bg abstrak with dissolve
    $ narasi_asli = "You find a Mysterious Landscape Painting. What do you think makes it good?"
    n "You find a Mysterious Landscape Painting."
    n "What do you think makes it good?"

    menu:
        "You find a Mysterious Landscape Painting. What do you think makes it good?"

        "The color composition, the technique, everything is perfect and neat!.":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "The color composition, the technique, everything is perfect and neat!."
            $ last_answer = "Thinking & Judging"
            jump show_question_q_a_18_en_A

        "This painting has deep and beautiful emotion.":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "This painting has deep and beautiful emotion."
            $ last_answer = "Feeling & Perceiving"
            jump show_question_q_a_18_en_B


label show_question_q_a_18_en_A:
    $ user_journey_summary.append("Di situasi You find a Mysterious Landscape Painting. What do you think makes it good?, user memilih: The color composition, the technique, everything is perfect and neat!., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic from _call_ai_react_logic_154
    return

label show_question_q_a_18_en_B:
    $ user_journey_summary.append("Di situasi You find a Mysterious Landscape Painting. What do you think makes it good?, user memilih: This painting has deep and beautiful emotion., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic from _call_ai_react_logic_155
    return

label show_question_q_a_19_en:
    scene bg abstrak with dissolve
    $ narasi_asli = "There is one red button. If you press it, you get money but one stranger will be sad."
    n "There is one red button."
    n "If you press it, you get money but one stranger will be sad."

    menu:
        "There is one red button. If you press it, you get money but one stranger will be sad."

        "Press the button, because the money is useful.":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "Press the button, because the money is useful."
            $ last_answer = "Thinking & Judging"
            jump show_question_q_a_19_en_A

        "Don't press it because you feel bad for the stranger.":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "Don't press it because you feel bad for the stranger."
            $ last_answer = "Feeling & Perceiving"
            jump show_question_q_a_19_en_B


label show_question_q_a_19_en_A:
    $ user_journey_summary.append("Di situasi There is one red button. If you press it, you get money but one stranger will be sad., user memilih: Press the button, because the money is useful., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic from _call_ai_react_logic_156
    return

label show_question_q_a_19_en_B:
    $ user_journey_summary.append("Di situasi There is one red button. If you press it, you get money but one stranger will be sad., user memilih: Don't press it because you feel bad for the stranger., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic from _call_ai_react_logic_157
    return

label show_question_q_a_20_en:
    scene bg kantor with dissolve
    $ narasi_asli = "Your team is lazy today. They have no spirit at all."
    n "Your team is lazy today."
    n "They have no spirit at all."

    menu:
        "Your team is lazy today. They have no spirit at all."

        "Set targets and promise a bonus.":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "Set targets and promise a bonus."
            $ last_answer = "Thinking & Judging"
            jump show_question_q_a_20_en_A

        "Come on friends! let's do it for the greater good.":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "Come on friends! let's do it for the greater good."
            $ last_answer = "Feeling & Perceiving"
            jump show_question_q_a_20_en_B


label show_question_q_a_20_en_A:
    $ user_journey_summary.append("Di situasi Your team is lazy today. They have no spirit at all., user memilih: Set targets and promise a bonus., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic from _call_ai_react_logic_158
    return

label show_question_q_a_20_en_B:
    $ user_journey_summary.append("Di situasi Your team is lazy today. They have no spirit at all., user memilih: Come on friends! let's do it for the greater good., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic from _call_ai_react_logic_159
    return

label show_question_q_b_21_en:
    scene bg dapur with dissolve
    $ narasi_asli = "(Confusion!) You found a strange-looking ancient recipe book. You are starving right now. How do you decide to cook?"
    n "(Confusion!) You found a strange-looking ancient recipe book."
    n "You are starving right now."
    n "How do you decide to cook?"

    menu:
        "(Confusion!) You found a strange-looking ancient recipe book. You are starving right now. How do you decide to cook?"

        "Read it alone calmly and follow the measurements precisely.":
            $ IE -= 5
            $ SN -= 5
            $ user_choice_text = "Read it alone calmly and follow the measurements precisely."
            $ last_answer = "Introvert & Sensing"
            jump show_question_q_b_21_en_A

        "Call friends to guess and create a new magical flavor.":
            $ IE += 5
            $ SN += 5
            $ user_choice_text = "Call friends to guess and create a new magical flavor."
            $ last_answer = "Extrovert & Intuitive"
            jump show_question_q_b_21_en_B


label show_question_q_b_21_en_A:
    $ user_journey_summary.append("Di situasi (Confusion!) You found a strange-looking ancient recipe book. You are starving right now. How do you decide to cook?, user memilih: Read it alone calmly and follow the measurements precisely., dengan poin MBTI: Introvert & Sensing")
    call ai_react_logic from _call_ai_react_logic_160
    return

label show_question_q_b_21_en_B:
    $ user_journey_summary.append("Di situasi (Confusion!) You found a strange-looking ancient recipe book. You are starving right now. How do you decide to cook?, user memilih: Call friends to guess and create a new magical flavor., dengan poin MBTI: Extrovert & Intuitive")
    call ai_react_logic from _call_ai_react_logic_161
    return

label show_question_q_b_22_en:
    scene bg kantor with dissolve
    $ narasi_asli = "(Suddenly!) A client comes asking for fresh ideas right now! You haven't prepared any material yet."
    n "(Suddenly!) A client comes asking for fresh ideas right now!"
    n "You haven't prepared any material yet."

    menu:
        "(Suddenly!) A client comes asking for fresh ideas right now! You haven't prepared any material yet."

        "Ask for time alone to compile existing facts and data.":
            $ IE -= 5
            $ SN -= 5
            $ user_choice_text = "Ask for time alone to compile existing facts and data."
            $ last_answer = "Introvert & Sensing"
            jump show_question_q_b_22_en_A

        "Have a casual discussion and convey your idea about the vision for the future.":
            $ IE += 5
            $ SN += 5
            $ user_choice_text = "Have a casual discussion and convey your idea about the vision for the future."
            $ last_answer = "Extrovert & Intuitive"
            jump show_question_q_b_22_en_B


label show_question_q_b_22_en_A:
    $ user_journey_summary.append("Di situasi (Suddenly!) A client comes asking for fresh ideas right now! You haven't prepared any material yet., user memilih: Ask for time alone to compile existing facts and data., dengan poin MBTI: Introvert & Sensing")
    call ai_react_logic from _call_ai_react_logic_162
    return

label show_question_q_b_22_en_B:
    $ user_journey_summary.append("Di situasi (Suddenly!) A client comes asking for fresh ideas right now! You haven't prepared any material yet., user memilih: Have a casual discussion and convey your idea about the vision for the future., dengan poin MBTI: Extrovert & Intuitive")
    call ai_react_logic from _call_ai_react_logic_163
    return

label show_question_q_b_23_en:
    scene bg abstrak with dissolve
    $ narasi_asli = "You enter an International library. Which book do you pick up first?"
    n "You enter an International library."
    n "Which book do you pick up first?"

    menu:
        "You enter an International library. Which book do you pick up first?"

        "'Illustrated Encyclopedia' which can be read with friends.":
            $ IE += 5
            $ SN -= 5
            $ user_choice_text = "'Illustrated Encyclopedia' which can be read with friends."
            $ last_answer = "Extrovert & Sensing"
            jump show_question_q_b_23_en_A

        "'Thick Philosophy' which is interesting to read in a quiet place.":
            $ IE -= 5
            $ SN += 5
            $ user_choice_text = "'Thick Philosophy' which is interesting to read in a quiet place."
            $ last_answer = "Introvert & Intuitive"
            jump show_question_q_b_23_en_B


label show_question_q_b_23_en_A:
    $ user_journey_summary.append("Di situasi You enter an International library. Which book do you pick up first?, user memilih: 'Illustrated Encyclopedia' which can be read with friends., dengan poin MBTI: Extrovert & Sensing")
    call ai_react_logic from _call_ai_react_logic_164
    return

label show_question_q_b_23_en_B:
    $ user_journey_summary.append("Di situasi You enter an International library. Which book do you pick up first?, user memilih: 'Thick Philosophy' which is interesting to read in a quiet place., dengan poin MBTI: Introvert & Intuitive")
    call ai_react_logic from _call_ai_react_logic_165
    return

label show_question_q_b_24_en:
    scene bg kafe with dissolve
    $ narasi_asli = "You are hungry, but your wallet is thin. Meanwhile, your friends invite you to eat out."
    n "You are hungry, but your wallet is thin."
    n "Meanwhile, your friends invite you to eat out."

    menu:
        "You are hungry, but your wallet is thin. Meanwhile, your friends invite you to eat out."

        "Join them but look for a regular stall that is definitely cheap and delicious.":
            $ IE += 5
            $ SN -= 5
            $ user_choice_text = "Join them but look for a regular stall that is definitely cheap and delicious."
            $ last_answer = "Extrovert & Sensing"
            jump show_question_q_b_24_en_A

        "Refuse first, you want to try looking for cheap and unique food that might be around your place.":
            $ IE -= 5
            $ SN += 5
            $ user_choice_text = "Refuse first, you want to try looking for cheap and unique food that might be around your place."
            $ last_answer = "Introvert & Intuitive"
            jump show_question_q_b_24_en_B


label show_question_q_b_24_en_A:
    $ user_journey_summary.append("Di situasi You are hungry, but your wallet is thin. Meanwhile, your friends invite you to eat out., user memilih: Join them but look for a regular stall that is definitely cheap and delicious., dengan poin MBTI: Extrovert & Sensing")
    call ai_react_logic from _call_ai_react_logic_166
    return

label show_question_q_b_24_en_B:
    $ user_journey_summary.append("Di situasi You are hungry, but your wallet is thin. Meanwhile, your friends invite you to eat out., user memilih: Refuse first, you want to try looking for cheap and unique food that might be around your place., dengan poin MBTI: Introvert & Intuitive")
    call ai_react_logic from _call_ai_react_logic_167
    return

label show_question_q_b_25_en:
    scene bg stasiun with dissolve
    $ narasi_asli = "There is a suspicious suitcase left behind at a quiet station."
    n "There is a suspicious suitcase left behind at a quiet station."

    menu:
        "There is a suspicious suitcase left behind at a quiet station."

        "Call an officer to safely check its contents.":
            $ IE += 5
            $ SN -= 5
            $ user_choice_text = "Call an officer to safely check its contents."
            $ last_answer = "Extrovert & Sensing"
            jump show_question_q_b_25_en_A

        "Observe from a distance while imagining what the contents of the suitcase really are.":
            $ IE -= 5
            $ SN += 5
            $ user_choice_text = "Observe from a distance while imagining what the contents of the suitcase really are."
            $ last_answer = "Introvert & Intuitive"
            jump show_question_q_b_25_en_B


label show_question_q_b_25_en_A:
    $ user_journey_summary.append("Di situasi There is a suspicious suitcase left behind at a quiet station., user memilih: Call an officer to safely check its contents., dengan poin MBTI: Extrovert & Sensing")
    call ai_react_logic from _call_ai_react_logic_168
    return

label show_question_q_b_25_en_B:
    $ user_journey_summary.append("Di situasi There is a suspicious suitcase left behind at a quiet station., user memilih: Observe from a distance while imagining what the contents of the suitcase really are., dengan poin MBTI: Introvert & Intuitive")
    call ai_react_logic from _call_ai_react_logic_169
    return

label show_question_q_b_26_en:
    scene bg kantor with dissolve
    $ narasi_asli = "Your teammate made a fatal mistake that cost everyone."
    n "Your teammate made a fatal mistake that cost everyone."

    menu:
        "Your teammate made a fatal mistake that cost everyone."

        "Confront them directly! and ask them to logically explain what happened.":
            $ IE += 5
            $ TF -= 5
            $ user_choice_text = "Confront them directly! and ask them to logically explain what happened."
            $ last_answer = "Extrovert & Thinking"
            jump show_question_q_b_26_en_A

        "Send them a private message, then ask if they are okay.":
            $ IE -= 5
            $ TF += 5
            $ user_choice_text = "Send them a private message, then ask if they are okay."
            $ last_answer = "Introvert & Feeling"
            jump show_question_q_b_26_en_B


label show_question_q_b_26_en_A:
    $ user_journey_summary.append("Di situasi Your teammate made a fatal mistake that cost everyone., user memilih: Confront them directly! and ask them to logically explain what happened., dengan poin MBTI: Extrovert & Thinking")
    call ai_react_logic from _call_ai_react_logic_170
    return

label show_question_q_b_26_en_B:
    $ user_journey_summary.append("Di situasi Your teammate made a fatal mistake that cost everyone., user memilih: Send them a private message, then ask if they are okay., dengan poin MBTI: Introvert & Feeling")
    call ai_react_logic from _call_ai_react_logic_171
    return

label show_question_q_b_27_en:
    scene bg kantor with dissolve
    $ narasi_asli = "Your friend asks for an honest opinion about their work, which you would say... is terrible."
    n "Your friend asks for an honest opinion about their work, which you would say..."
    n "is terrible."

    menu:
        "Your friend asks for an honest opinion about their work, which you would say... is terrible."

        "Tell them straight which part is wrong so they can fix it.":
            $ IE += 5
            $ TF -= 5
            $ user_choice_text = "Tell them straight which part is wrong so they can fix it."
            $ last_answer = "Extrovert & Thinking"
            jump show_question_q_b_27_en_A

        "Just keep quiet or smile, you can't bear to hurt their feelings.":
            $ IE -= 5
            $ TF += 5
            $ user_choice_text = "Just keep quiet or smile, you can't bear to hurt their feelings."
            $ last_answer = "Introvert & Feeling"
            jump show_question_q_b_27_en_B


label show_question_q_b_27_en_A:
    $ user_journey_summary.append("Di situasi Your friend asks for an honest opinion about their work, which you would say... is terrible., user memilih: Tell them straight which part is wrong so they can fix it., dengan poin MBTI: Extrovert & Thinking")
    call ai_react_logic from _call_ai_react_logic_172
    return

label show_question_q_b_27_en_B:
    $ user_journey_summary.append("Di situasi Your friend asks for an honest opinion about their work, which you would say... is terrible., user memilih: Just keep quiet or smile, you can't bear to hurt their feelings., dengan poin MBTI: Introvert & Feeling")
    call ai_react_logic from _call_ai_react_logic_173
    return

label show_question_q_b_28_en:
    scene bg kafe with dissolve
    $ narasi_asli = "Two strangers are arguing loudly at the next table. It's very annoying!"
    n "Two strangers are arguing loudly at the next table."
    n "It's very annoying!"

    menu:
        "Two strangers are arguing loudly at the next table. It's very annoying!"

        "Confront them, 'Please be quiet, your arguments are illogical!'.":
            $ IE += 5
            $ TF -= 5
            $ user_choice_text = "Confront them, 'Please be quiet, your arguments are illogical!'."
            $ last_answer = "Extrovert & Thinking"
            jump show_question_q_b_28_en_A

        "Move tables, move away because the energy is too negative.":
            $ IE -= 5
            $ TF += 5
            $ user_choice_text = "Move tables, move away because the energy is too negative."
            $ last_answer = "Introvert & Feeling"
            jump show_question_q_b_28_en_B


label show_question_q_b_28_en_A:
    $ user_journey_summary.append("Di situasi Two strangers are arguing loudly at the next table. It's very annoying!, user memilih: Confront them, 'Please be quiet, your arguments are illogical!'., dengan poin MBTI: Extrovert & Thinking")
    call ai_react_logic from _call_ai_react_logic_174
    return

label show_question_q_b_28_en_B:
    $ user_journey_summary.append("Di situasi Two strangers are arguing loudly at the next table. It's very annoying!, user memilih: Move tables, move away because the energy is too negative., dengan poin MBTI: Introvert & Feeling")
    call ai_react_logic from _call_ai_react_logic_175
    return

label show_question_q_b_29_en:
    scene bg abstrak with dissolve
    $ narasi_asli = "You must choose a leader for a dangerous mission."
    n "You must choose a leader for a dangerous mission."

    menu:
        "You must choose a leader for a dangerous mission."

        "Open debate, choose the one with the strongest statistics.":
            $ IE += 5
            $ TF -= 5
            $ user_choice_text = "Open debate, choose the one with the strongest statistics."
            $ last_answer = "Extrovert & Thinking"
            jump show_question_q_b_29_en_A

        "Reflect with a few close friends, then choose the one with the most sincere heart.":
            $ IE -= 5
            $ TF += 5
            $ user_choice_text = "Reflect with a few close friends, then choose the one with the most sincere heart."
            $ last_answer = "Introvert & Feeling"
            jump show_question_q_b_29_en_B


label show_question_q_b_29_en_A:
    $ user_journey_summary.append("Di situasi You must choose a leader for a dangerous mission., user memilih: Open debate, choose the one with the strongest statistics., dengan poin MBTI: Extrovert & Thinking")
    call ai_react_logic from _call_ai_react_logic_176
    return

label show_question_q_b_29_en_B:
    $ user_journey_summary.append("Di situasi You must choose a leader for a dangerous mission., user memilih: Reflect with a few close friends, then choose the one with the most sincere heart., dengan poin MBTI: Introvert & Feeling")
    call ai_react_logic from _call_ai_react_logic_177
    return

label show_question_q_b_30_en:
    scene bg taman with dissolve
    $ narasi_asli = "There is a crowd of people grieving because an old tree was cut down by the local government."
    n "There is a crowd of people grieving because an old tree was cut down by the local government."

    menu:
        "There is a crowd of people grieving because an old tree was cut down by the local government."

        "Gather them to create a protest petition to the government.":
            $ IE += 5
            $ TF -= 5
            $ user_choice_text = "Gather them to create a protest petition to the government."
            $ last_answer = "Extrovert & Thinking"
            jump show_question_q_b_30_en_A

        "Sit quietly there as a sign of solidarity.":
            $ IE -= 5
            $ TF += 5
            $ user_choice_text = "Sit quietly there as a sign of solidarity."
            $ last_answer = "Introvert & Feeling"
            jump show_question_q_b_30_en_B


label show_question_q_b_30_en_A:
    $ user_journey_summary.append("Di situasi There is a crowd of people grieving because an old tree was cut down by the local government., user memilih: Gather them to create a protest petition to the government., dengan poin MBTI: Extrovert & Thinking")
    call ai_react_logic from _call_ai_react_logic_178
    return

label show_question_q_b_30_en_B:
    $ user_journey_summary.append("Di situasi There is a crowd of people grieving because an old tree was cut down by the local government., user memilih: Sit quietly there as a sign of solidarity., dengan poin MBTI: Introvert & Feeling")
    call ai_react_logic from _call_ai_react_logic_179
    return

label show_question_q_b_31_en:
    scene bg stasiun with dissolve
    $ narasi_asli = "(Late!) The last train leaves in 1 minute! You are still in the lobby!"
    n "(Late!) The last train leaves in 1 minute!"
    n "You are still in the lobby!"

    menu:
        "(Late!) The last train leaves in 1 minute! You are still in the lobby!"

        "Shout 'Wait!' and run through the gate without thinking.":
            $ IE += 5
            $ JP += 5
            $ user_choice_text = "Shout 'Wait!' and run through the gate without thinking."
            $ last_answer = "Extrovert & Perceiving"
            jump show_question_q_b_31_en_A

        "Resign. 'This is my fault for not checking the schedule this morning'.":
            $ IE -= 5
            $ JP -= 5
            $ user_choice_text = "Resign. 'This is my fault for not checking the schedule this morning'."
            $ last_answer = "Introvert & Judging"
            jump show_question_q_b_31_en_B


label show_question_q_b_31_en_A:
    $ user_journey_summary.append("Di situasi (Late!) The last train leaves in 1 minute! You are still in the lobby!, user memilih: Shout 'Wait!' and run through the gate without thinking., dengan poin MBTI: Extrovert & Perceiving")
    call ai_react_logic from _call_ai_react_logic_180
    return

label show_question_q_b_31_en_B:
    $ user_journey_summary.append("Di situasi (Late!) The last train leaves in 1 minute! You are still in the lobby!, user memilih: Resign. 'This is my fault for not checking the schedule this morning'., dengan poin MBTI: Introvert & Judging")
    call ai_react_logic from _call_ai_react_logic_181
    return

label show_question_q_b_32_en:
    scene bg kafe with dissolve
    $ narasi_asli = "You and a large group are confused about what to order at the Restaurant. The waiter is getting annoyed."
    n "You and a large group are confused about what to order at the Restaurant."
    n "The waiter is getting annoyed."

    menu:
        "You and a large group are confused about what to order at the Restaurant. The waiter is getting annoyed."

        "Ask everyone!, 'What food do you want? Anything goes!'.":
            $ IE += 5
            $ JP += 5
            $ user_choice_text = "Ask everyone!, 'What food do you want? Anything goes!'."
            $ last_answer = "Extrovert & Perceiving"
            jump show_question_q_b_32_en_A

        "Take charge, 'Okay, I'll order the package menu for everyone to speed things up'.":
            $ IE -= 5
            $ JP -= 5
            $ user_choice_text = "Take charge, 'Okay, I'll order the package menu for everyone to speed things up'."
            $ last_answer = "Introvert & Judging"
            jump show_question_q_b_32_en_B


label show_question_q_b_32_en_A:
    $ user_journey_summary.append("Di situasi You and a large group are confused about what to order at the Restaurant. The waiter is getting annoyed., user memilih: Ask everyone!, 'What food do you want? Anything goes!'., dengan poin MBTI: Extrovert & Perceiving")
    call ai_react_logic from _call_ai_react_logic_182
    return

label show_question_q_b_32_en_B:
    $ user_journey_summary.append("Di situasi You and a large group are confused about what to order at the Restaurant. The waiter is getting annoyed., user memilih: Take charge, 'Okay, I'll order the package menu for everyone to speed things up'., dengan poin MBTI: Introvert & Judging")
    call ai_react_logic from _call_ai_react_logic_183
    return

label show_question_q_b_33_en:
    scene bg kafe with dissolve
    $ narasi_asli = "You see a really cool jacket displayed in the store, but it's expensive."
    n "You see a really cool jacket displayed in the store, but it's expensive."

    menu:
        "You see a really cool jacket displayed in the store, but it's expensive."

        "Ask others' opinions, if it's good, just buy it!.":
            $ IE += 5
            $ JP += 5
            $ user_choice_text = "Ask others' opinions, if it's good, just buy it!."
            $ last_answer = "Extrovert & Perceiving"
            jump show_question_q_b_33_en_A

        "Ask yourself, 'It's not in the budget. Don't do it yet'.":
            $ IE -= 5
            $ JP -= 5
            $ user_choice_text = "Ask yourself, 'It's not in the budget. Don't do it yet'."
            $ last_answer = "Introvert & Judging"
            jump show_question_q_b_33_en_B


label show_question_q_b_33_en_A:
    $ user_journey_summary.append("Di situasi You see a really cool jacket displayed in the store, but it's expensive., user memilih: Ask others' opinions, if it's good, just buy it!., dengan poin MBTI: Extrovert & Perceiving")
    call ai_react_logic from _call_ai_react_logic_184
    return

label show_question_q_b_33_en_B:
    $ user_journey_summary.append("Di situasi You see a really cool jacket displayed in the store, but it's expensive., user memilih: Ask yourself, 'It's not in the budget. Don't do it yet'., dengan poin MBTI: Introvert & Judging")
    call ai_react_logic from _call_ai_react_logic_185
    return

label show_question_q_b_34_en:
    scene bg room with dissolve
    $ narasi_asli = "Your friend says your room is boring. What is your reaction?"
    n "Your friend says your room is boring."
    n "What is your reaction?"

    menu:
        "Your friend says your room is boring. What is your reaction?"

        "'That's right!' Since a friend is here, ask them to move the furniture around right now.":
            $ IE += 5
            $ JP += 5
            $ user_choice_text = "'That's right!' Since a friend is here, ask them to move the furniture around right now."
            $ last_answer = "Extrovert & Perceiving"
            jump show_question_q_b_34_en_A

        "Leave it. 'I prefer it, because everything is already in its proper place'.":
            $ IE -= 5
            $ JP -= 5
            $ user_choice_text = "Leave it. 'I prefer it, because everything is already in its proper place'."
            $ last_answer = "Introvert & Judging"
            jump show_question_q_b_34_en_B


label show_question_q_b_34_en_A:
    $ user_journey_summary.append("Di situasi Your friend says your room is boring. What is your reaction?, user memilih: 'That's right!' Since a friend is here, ask them to move the furniture around right now., dengan poin MBTI: Extrovert & Perceiving")
    call ai_react_logic from _call_ai_react_logic_186
    return

label show_question_q_b_34_en_B:
    $ user_journey_summary.append("Di situasi Your friend says your room is boring. What is your reaction?, user memilih: Leave it. 'I prefer it, because everything is already in its proper place'., dengan poin MBTI: Introvert & Judging")
    call ai_react_logic from _call_ai_react_logic_187
    return

label show_question_q_b_35_en:
    scene bg kantor with dissolve
    $ narasi_asli = "You have to give a spontaneous public speech! What now?!"
    n "You have to give a spontaneous public speech!"
    n "What now?!"

    menu:
        "You have to give a spontaneous public speech! What now?!"

        "Step forward confidently, speak freely, watching the situation.":
            $ IE += 5
            $ JP += 5
            $ user_choice_text = "Step forward confidently, speak freely, watching the situation."
            $ last_answer = "Extrovert & Perceiving"
            jump show_question_q_b_35_en_A

        "Step back for a moment, ask for time to jot down key points first.":
            $ IE -= 5
            $ JP -= 5
            $ user_choice_text = "Step back for a moment, ask for time to jot down key points first."
            $ last_answer = "Introvert & Judging"
            jump show_question_q_b_35_en_B


label show_question_q_b_35_en_A:
    $ user_journey_summary.append("Di situasi You have to give a spontaneous public speech! What now?!, user memilih: Step forward confidently, speak freely, watching the situation., dengan poin MBTI: Extrovert & Perceiving")
    call ai_react_logic from _call_ai_react_logic_188
    return

label show_question_q_b_35_en_B:
    $ user_journey_summary.append("Di situasi You have to give a spontaneous public speech! What now?!, user memilih: Step back for a moment, ask for time to jot down key points first., dengan poin MBTI: Introvert & Judging")
    call ai_react_logic from _call_ai_react_logic_189
    return

label show_question_q_b_36_en:
    scene bg abstrak with dissolve
    $ narasi_asli = "(Disaster!) Your village is attacked! You hold the key to the defense gate. There are still citizens running trying to get inside."
    n "(Disaster!) Your village is attacked!"
    n "You hold the key to the defense gate."
    n "There are still citizens running trying to get inside."

    menu:
        "(Disaster!) Your village is attacked! You hold the key to the defense gate. There are still citizens running trying to get inside."

        "Immediately lock the gate for the safety of the majority, even if some are left behind.":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "Immediately lock the gate for the safety of the majority, even if some are left behind."
            $ last_answer = "Thinking & Judging"
            jump show_question_q_b_36_en_A

        "Leave it open a little longer, feel sorry for those still running outside.":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "Leave it open a little longer, feel sorry for those still running outside."
            $ last_answer = "Feeling & Perceiving"
            jump show_question_q_b_36_en_B


label show_question_q_b_36_en_A:
    $ user_journey_summary.append("Di situasi (Disaster!) Your village is attacked! You hold the key to the defense gate. There are still citizens running trying to get inside., user memilih: Immediately lock the gate for the safety of the majority, even if some are left behind., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic from _call_ai_react_logic_190
    return

label show_question_q_b_36_en_B:
    $ user_journey_summary.append("Di situasi (Disaster!) Your village is attacked! You hold the key to the defense gate. There are still citizens running trying to get inside., user memilih: Leave it open a little longer, feel sorry for those still running outside., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic from _call_ai_react_logic_191
    return

label show_question_q_b_37_en:
    scene bg kantor with dissolve
    $ narasi_asli = "Your teammate is heartbroken and can't work. What do you do as team leader?"
    n "Your teammate is heartbroken and can't work."
    n "What do you do as team leader?"

    menu:
        "Your teammate is heartbroken and can't work. What do you do as team leader?"

        "'Work is work. Finish your tasks, then deal with feelings.'":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "'Work is work. Finish your tasks, then deal with feelings.'"
            $ last_answer = "Thinking & Judging"
            jump show_question_q_b_37_en_A

        "'Go home. We can rearrange the work later.'":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "'Go home. We can rearrange the work later.'"
            $ last_answer = "Feeling & Perceiving"
            jump show_question_q_b_37_en_B


label show_question_q_b_37_en_A:
    $ user_journey_summary.append("Di situasi Your teammate is heartbroken and can't work. What do you do as team leader?, user memilih: 'Work is work. Finish your tasks, then deal with feelings.', dengan poin MBTI: Thinking & Judging")
    call ai_react_logic from _call_ai_react_logic_192
    return

label show_question_q_b_37_en_B:
    $ user_journey_summary.append("Di situasi Your teammate is heartbroken and can't work. What do you do as team leader?, user memilih: 'Go home. We can rearrange the work later.', dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic from _call_ai_react_logic_193
    return

label show_question_q_b_38_en:
    scene bg dapur with dissolve
    $ narasi_asli = "You are a judge in a cooking competition. Your friend's dish is burnt. They are crying, even though they tried hard."
    n "You are a judge in a cooking competition."
    n "Your friend's dish is burnt."
    n "They are crying, even though they tried hard."

    menu:
        "You are a judge in a cooking competition. Your friend's dish is burnt. They are crying, even though they tried hard."

        "Give a score of zero. The scoring rules must be objective.":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "Give a score of zero. The scoring rules must be objective."
            $ last_answer = "Thinking & Judging"
            jump show_question_q_b_38_en_A

        "Give an extra score. Appreciate the process and effort.":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "Give an extra score. Appreciate the process and effort."
            $ last_answer = "Feeling & Perceiving"
            jump show_question_q_b_38_en_B


label show_question_q_b_38_en_A:
    $ user_journey_summary.append("Di situasi You are a judge in a cooking competition. Your friend's dish is burnt. They are crying, even though they tried hard., user memilih: Give a score of zero. The scoring rules must be objective., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic from _call_ai_react_logic_194
    return

label show_question_q_b_38_en_B:
    $ user_journey_summary.append("Di situasi You are a judge in a cooking competition. Your friend's dish is burnt. They are crying, even though they tried hard., user memilih: Give an extra score. Appreciate the process and effort., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic from _call_ai_react_logic_195
    return

label show_question_q_b_39_en:
    scene bg stasiun with dissolve
    $ narasi_asli = "A confused tourist entered the wrong line at the Station. Then they were fined. You are the officer there."
    n "A confused tourist entered the wrong line at the Station."
    n "Then they were fined."
    n "You are the officer there."

    menu:
        "A confused tourist entered the wrong line at the Station. Then they were fined. You are the officer there."

        "Let them pay the fine. Rules are rules.":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "Let them pay the fine. Rules are rules."
            $ last_answer = "Thinking & Judging"
            jump show_question_q_b_39_en_A

        "Help them negotiate. Be understanding because they are a foreigner.":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "Help them negotiate. Be understanding because they are a foreigner."
            $ last_answer = "Feeling & Perceiving"
            jump show_question_q_b_39_en_B


label show_question_q_b_39_en_A:
    $ user_journey_summary.append("Di situasi A confused tourist entered the wrong line at the Station. Then they were fined. You are the officer there., user memilih: Let them pay the fine. Rules are rules., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic from _call_ai_react_logic_196
    return

label show_question_q_b_39_en_B:
    $ user_journey_summary.append("Di situasi A confused tourist entered the wrong line at the Station. Then they were fined. You are the officer there., user memilih: Help them negotiate. Be understanding because they are a foreigner., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic from _call_ai_react_logic_197
    return

label show_question_q_b_40_en:
    scene bg kantor with dissolve
    $ narasi_asli = "You create a new duty schedule. But one of your friends protests because the schedule clashes."
    n "You create a new duty schedule."
    n "But one of your friends protests because the schedule clashes."

    menu:
        "You create a new duty schedule. But one of your friends protests because the schedule clashes."

        "'No way! The system is already made efficient. You must follow the existing schedule.'":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "'No way! The system is already made efficient. You must follow the existing schedule.'"
            $ last_answer = "Thinking & Judging"
            jump show_question_q_b_40_en_A

        "'Okay, we can switch around. The important thing is that everyone is happy.'":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "'Okay, we can switch around. The important thing is that everyone is happy.'"
            $ last_answer = "Feeling & Perceiving"
            jump show_question_q_b_40_en_B


label show_question_q_b_40_en_A:
    $ user_journey_summary.append("Di situasi You create a new duty schedule. But one of your friends protests because the schedule clashes., user memilih: 'No way! The system is already made efficient. You must follow the existing schedule.', dengan poin MBTI: Thinking & Judging")
    call ai_react_logic from _call_ai_react_logic_198
    return

label show_question_q_b_40_en_B:
    $ user_journey_summary.append("Di situasi You create a new duty schedule. But one of your friends protests because the schedule clashes., user memilih: 'Okay, we can switch around. The important thing is that everyone is happy.', dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic from _call_ai_react_logic_199
    return

label show_question_q_c_41_en:
    scene bg taman with dissolve
    $ narasi_asli = "Holidays have arrived. Friends invite you to go traveling, but don't know exactly where to go yet."
    n "Holidays have arrived."
    n "Friends invite you to go traveling, but don't know exactly where to go yet."

    menu:
        "Holidays have arrived. Friends invite you to go traveling, but don't know exactly where to go yet."

        "Go solo to visit a history museum to see historical artifacts.":
            $ IE -= 5
            $ SN -= 5
            $ user_choice_text = "Go solo to visit a history museum to see historical artifacts."
            $ last_answer = "Introvert & Sensing"
            jump show_question_q_c_41_en_A

        "Join the group to explore a mythical forest full of mysteries.":
            $ IE += 5
            $ SN += 5
            $ user_choice_text = "Join the group to explore a mythical forest full of mysteries."
            $ last_answer = "Extrovert & Intuitive"
            jump show_question_q_c_41_en_B


label show_question_q_c_41_en_A:
    $ user_journey_summary.append("Di situasi Holidays have arrived. Friends invite you to go traveling, but don't know exactly where to go yet., user memilih: Go solo to visit a history museum to see historical artifacts., dengan poin MBTI: Introvert & Sensing")
    call ai_react_logic from _call_ai_react_logic_200
    return

label show_question_q_c_41_en_B:
    $ user_journey_summary.append("Di situasi Holidays have arrived. Friends invite you to go traveling, but don't know exactly where to go yet., user memilih: Join the group to explore a mythical forest full of mysteries., dengan poin MBTI: Extrovert & Intuitive")
    call ai_react_logic from _call_ai_react_logic_201
    return

label show_question_q_c_42_en:
    scene bg kafe with dissolve
    $ narasi_asli = "You won a huge lottery! Winning a bag of gold coins."
    n "You won a huge lottery!"
    n "Winning a bag of gold coins."

    menu:
        "You won a huge lottery! Winning a bag of gold coins."

        "Keep it in a safe as a secure physical asset.":
            $ IE -= 5
            $ SN -= 5
            $ user_choice_text = "Keep it in a safe as a secure physical asset."
            $ last_answer = "Introvert & Sensing"
            jump show_question_q_c_42_en_A

        "Treat everyone while thinking about your increasing wealth.":
            $ IE += 5
            $ SN += 5
            $ user_choice_text = "Treat everyone while thinking about your increasing wealth."
            $ last_answer = "Extrovert & Intuitive"
            jump show_question_q_c_42_en_B


label show_question_q_c_42_en_A:
    $ user_journey_summary.append("Di situasi You won a huge lottery! Winning a bag of gold coins., user memilih: Keep it in a safe as a secure physical asset., dengan poin MBTI: Introvert & Sensing")
    call ai_react_logic from _call_ai_react_logic_202
    return

label show_question_q_c_42_en_B:
    $ user_journey_summary.append("Di situasi You won a huge lottery! Winning a bag of gold coins., user memilih: Treat everyone while thinking about your increasing wealth., dengan poin MBTI: Extrovert & Intuitive")
    call ai_react_logic from _call_ai_react_logic_203
    return

label show_question_q_c_43_en:
    scene bg room with dissolve
    $ narasi_asli = "You see an abstract painting that is 'just a few line scribbles'."
    n "You see an abstract painting that is 'just a few line scribbles'."

    menu:
        "You see an abstract painting that is 'just a few line scribbles'."

        "Ask others, 'What is this picture? What does it mean?'.":
            $ IE += 5
            $ SN -= 5
            $ user_choice_text = "Ask others, 'What is this picture? What does it mean?'."
            $ last_answer = "Extrovert & Sensing"
            jump show_question_q_c_43_en_A

        "Stay silent and try to feel the painter's emotion.":
            $ IE -= 5
            $ SN += 5
            $ user_choice_text = "Stay silent and try to feel the painter's emotion."
            $ last_answer = "Introvert & Intuitive"
            jump show_question_q_c_43_en_B


label show_question_q_c_43_en_A:
    $ user_journey_summary.append("Di situasi You see an abstract painting that is 'just a few line scribbles'., user memilih: Ask others, 'What is this picture? What does it mean?'., dengan poin MBTI: Extrovert & Sensing")
    call ai_react_logic from _call_ai_react_logic_204
    return

label show_question_q_c_43_en_B:
    $ user_journey_summary.append("Di situasi You see an abstract painting that is 'just a few line scribbles'., user memilih: Stay silent and try to feel the painter's emotion., dengan poin MBTI: Introvert & Intuitive")
    call ai_react_logic from _call_ai_react_logic_205
    return

label show_question_q_c_44_en:
    scene bg arcade with dissolve
    $ narasi_asli = "Your friend asks you to teach them a game that you are really good at playing."
    n "Your friend asks you to teach them a game that you are really good at playing."

    menu:
        "Your friend asks you to teach them a game that you are really good at playing."

        "'Here, press the forward button, then jump.' Guide them directly.":
            $ IE += 5
            $ SN -= 5
            $ user_choice_text = "'Here, press the forward button, then jump.' Guide them directly."
            $ last_answer = "Extrovert & Sensing"
            jump show_question_q_c_44_en_A

        "'Understand the concept first.' Let them learn on their own.":
            $ IE -= 5
            $ SN += 5
            $ user_choice_text = "'Understand the concept first.' Let them learn on their own."
            $ last_answer = "Introvert & Intuitive"
            jump show_question_q_c_44_en_B


label show_question_q_c_44_en_A:
    $ user_journey_summary.append("Di situasi Your friend asks you to teach them a game that you are really good at playing., user memilih: 'Here, press the forward button, then jump.' Guide them directly., dengan poin MBTI: Extrovert & Sensing")
    call ai_react_logic from _call_ai_react_logic_206
    return

label show_question_q_c_44_en_B:
    $ user_journey_summary.append("Di situasi Your friend asks you to teach them a game that you are really good at playing., user memilih: 'Understand the concept first.' Let them learn on their own., dengan poin MBTI: Introvert & Intuitive")
    call ai_react_logic from _call_ai_react_logic_207
    return

label show_question_q_c_45_en:
    scene bg abstrak with dissolve
    $ narasi_asli = "You have 1 hour of free time today. What do you want to do?"
    n "You have 1 hour of free time today."
    n "What do you want to do?"

    menu:
        "You have 1 hour of free time today. What do you want to do?"

        "Exercise or clean up together at home.":
            $ IE += 5
            $ SN -= 5
            $ user_choice_text = "Exercise or clean up together at home."
            $ last_answer = "Extrovert & Sensing"
            jump show_question_q_c_45_en_A

        "Do something you like, while imagining what you can do in the future.":
            $ IE -= 5
            $ SN += 5
            $ user_choice_text = "Do something you like, while imagining what you can do in the future."
            $ last_answer = "Introvert & Intuitive"
            jump show_question_q_c_45_en_B


label show_question_q_c_45_en_A:
    $ user_journey_summary.append("Di situasi You have 1 hour of free time today. What do you want to do?, user memilih: Exercise or clean up together at home., dengan poin MBTI: Extrovert & Sensing")
    call ai_react_logic from _call_ai_react_logic_208
    return

label show_question_q_c_45_en_B:
    $ user_journey_summary.append("Di situasi You have 1 hour of free time today. What do you want to do?, user memilih: Do something you like, while imagining what you can do in the future., dengan poin MBTI: Introvert & Intuitive")
    call ai_react_logic from _call_ai_react_logic_209
    return

label show_question_q_c_46_en:
    scene bg room with dissolve
    $ narasi_asli = "(Sob!) Your friend is crying because they were broken up with by their partner."
    n "(Sob!) Your friend is crying because they were broken up with by their partner."

    menu:
        "(Sob!) Your friend is crying because they were broken up with by their partner."

        "'Stop crying. Here's a tissue. If you think about it, they weren't good for you anyway.'":
            $ SN -= 5
            $ TF -= 5
            $ user_choice_text = "'Stop crying. Here's a tissue. If you think about it, they weren't good for you anyway.'"
            $ last_answer = "Sensing & Thinking"
            jump show_question_q_c_46_en_A

        "Accompany them. then listen to their story.":
            $ SN += 5
            $ TF += 5
            $ user_choice_text = "Accompany them. then listen to their story."
            $ last_answer = "Intuitive & Feeling"
            jump show_question_q_c_46_en_B


label show_question_q_c_46_en_A:
    $ user_journey_summary.append("Di situasi (Sob!) Your friend is crying because they were broken up with by their partner., user memilih: 'Stop crying. Here's a tissue. If you think about it, they weren't good for you anyway.', dengan poin MBTI: Sensing & Thinking")
    call ai_react_logic from _call_ai_react_logic_210
    return

label show_question_q_c_46_en_B:
    $ user_journey_summary.append("Di situasi (Sob!) Your friend is crying because they were broken up with by their partner., user memilih: Accompany them. then listen to their story., dengan poin MBTI: Intuitive & Feeling")
    call ai_react_logic from _call_ai_react_logic_211
    return

label show_question_q_c_47_en:
    scene bg room with dissolve
    $ narasi_asli = "The movie you watched has a vague and unclear ending!"
    n "The movie you watched has a vague and unclear ending!"

    menu:
        "The movie you watched has a vague and unclear ending!"

        "'Ugh... It's terrible! Many scenes weren't logically explained!.'":
            $ SN -= 5
            $ TF -= 5
            $ user_choice_text = "'Ugh... It's terrible! Many scenes weren't logically explained!.'"
            $ last_answer = "Sensing & Thinking"
            jump show_question_q_c_47_en_A

        "'Cool... The meaning is so deep, about hope that is lost.'":
            $ SN += 5
            $ TF += 5
            $ user_choice_text = "'Cool... The meaning is so deep, about hope that is lost.'"
            $ last_answer = "Intuitive & Feeling"
            jump show_question_q_c_47_en_B


label show_question_q_c_47_en_A:
    $ user_journey_summary.append("Di situasi The movie you watched has a vague and unclear ending!, user memilih: 'Ugh... It's terrible! Many scenes weren't logically explained!.', dengan poin MBTI: Sensing & Thinking")
    call ai_react_logic from _call_ai_react_logic_212
    return

label show_question_q_c_47_en_B:
    $ user_journey_summary.append("Di situasi The movie you watched has a vague and unclear ending!, user memilih: 'Cool... The meaning is so deep, about hope that is lost.', dengan poin MBTI: Intuitive & Feeling")
    call ai_react_logic from _call_ai_react_logic_213
    return

label show_question_q_c_48_en:
    scene bg kantor with dissolve
    $ narasi_asli = "There is a job offer with a large salary, but you don't know what the job is. The person looks quite promising.."
    n "There is a job offer with a large salary, but you don't know what the job is."
    n "The person looks quite promising.."

    menu:
        "There is a job offer with a large salary, but you don't know what the job is. The person looks quite promising.."

        "Refuse. 'The offer is vague' and you are not sure where it will lead.":
            $ SN += 5
            $ TF += 5
            $ user_choice_text = "Refuse. 'The offer is vague' and you are not sure where it will lead."
            $ last_answer = "Intuitive & Feeling"
            jump show_question_q_c_48_en_A

        "Just accept it. Financially you need the money.":
            $ SN -= 5
            $ TF -= 5
            $ user_choice_text = "Just accept it. Financially you need the money."
            $ last_answer = "Sensing & Thinking"
            jump show_question_q_c_48_en_B


label show_question_q_c_48_en_A:
    $ user_journey_summary.append("Di situasi There is a job offer with a large salary, but you don't know what the job is. The person looks quite promising.., user memilih: Refuse. 'The offer is vague' and you are not sure where it will lead., dengan poin MBTI: Intuitive & Feeling")
    call ai_react_logic from _call_ai_react_logic_214
    return

label show_question_q_c_48_en_B:
    $ user_journey_summary.append("Di situasi There is a job offer with a large salary, but you don't know what the job is. The person looks quite promising.., user memilih: Just accept it. Financially you need the money., dengan poin MBTI: Sensing & Thinking")
    call ai_react_logic from _call_ai_react_logic_215
    return

label show_question_q_c_49_en:
    scene bg abstrak with dissolve
    $ narasi_asli = "You must choose one skill to learn for life."
    n "You must choose one skill to learn for life."

    menu:
        "You must choose one skill to learn for life."

        "Technical skill that is useful for finding work.":
            $ SN -= 5
            $ TF -= 5
            $ user_choice_text = "Technical skill that is useful for finding work."
            $ last_answer = "Sensing & Thinking"
            jump show_question_q_c_49_en_A

        "Art skill that can touch people's hearts.":
            $ SN += 5
            $ TF += 5
            $ user_choice_text = "Art skill that can touch people's hearts."
            $ last_answer = "Intuitive & Feeling"
            jump show_question_q_c_49_en_B


label show_question_q_c_49_en_A:
    $ user_journey_summary.append("Di situasi You must choose one skill to learn for life., user memilih: Technical skill that is useful for finding work., dengan poin MBTI: Sensing & Thinking")
    call ai_react_logic from _call_ai_react_logic_216
    return

label show_question_q_c_49_en_B:
    $ user_journey_summary.append("Di situasi You must choose one skill to learn for life., user memilih: Art skill that can touch people's hearts., dengan poin MBTI: Intuitive & Feeling")
    call ai_react_logic from _call_ai_react_logic_217
    return

label show_question_q_c_50_en:
    scene bg kafe with dissolve
    $ narasi_asli = "Your friend is debating a science fact but all their data is wrong."
    n "Your friend is debating a science fact but all their data is wrong."

    menu:
        "Your friend is debating a science fact but all their data is wrong."

        "Correct them. Show the original data so they don't embarrass themselves.":
            $ SN -= 5
            $ TF -= 5
            $ user_choice_text = "Correct them. Show the original data so they don't embarrass themselves."
            $ last_answer = "Sensing & Thinking"
            jump show_question_q_c_50_en_A

        "Just let it be. They will realize it themselves, rather than fighting here.":
            $ SN += 5
            $ TF += 5
            $ user_choice_text = "Just let it be. They will realize it themselves, rather than fighting here."
            $ last_answer = "Intuitive & Feeling"
            jump show_question_q_c_50_en_B


label show_question_q_c_50_en_A:
    $ user_journey_summary.append("Di situasi Your friend is debating a science fact but all their data is wrong., user memilih: Correct them. Show the original data so they don't embarrass themselves., dengan poin MBTI: Sensing & Thinking")
    call ai_react_logic from _call_ai_react_logic_218
    return

label show_question_q_c_50_en_B:
    $ user_journey_summary.append("Di situasi Your friend is debating a science fact but all their data is wrong., user memilih: Just let it be. They will realize it themselves, rather than fighting here., dengan poin MBTI: Intuitive & Feeling")
    call ai_react_logic from _call_ai_react_logic_219
    return

label show_question_q_c_51_en:
    scene bg stasiun with dissolve
    $ narasi_asli = "(Lost!) Your train ticket is missing! The train leaves in 5 minutes."
    n "(Lost!) Your train ticket is missing!"
    n "The train leaves in 5 minutes."

    menu:
        "(Lost!) Your train ticket is missing! The train leaves in 5 minutes."

        "Check pockets, bags, floor sequentially. Don't panic, try to recall.":
            $ SN -= 5
            $ JP -= 5
            $ user_choice_text = "Check pockets, bags, floor sequentially. Don't panic, try to recall."
            $ last_answer = "Sensing & Judging"
            jump show_question_q_c_51_en_A

        "Look for the ticket where it might be tucked away. It might have fallen on the street.":
            $ SN += 5
            $ JP += 5
            $ user_choice_text = "Look for the ticket where it might be tucked away. It might have fallen on the street."
            $ last_answer = "Intuitive & Perceiving"
            jump show_question_q_c_51_en_B


label show_question_q_c_51_en_A:
    $ user_journey_summary.append("Di situasi (Lost!) Your train ticket is missing! The train leaves in 5 minutes., user memilih: Check pockets, bags, floor sequentially. Don't panic, try to recall., dengan poin MBTI: Sensing & Judging")
    call ai_react_logic from _call_ai_react_logic_220
    return

label show_question_q_c_51_en_B:
    $ user_journey_summary.append("Di situasi (Lost!) Your train ticket is missing! The train leaves in 5 minutes., user memilih: Look for the ticket where it might be tucked away. It might have fallen on the street., dengan poin MBTI: Intuitive & Perceiving")
    call ai_react_logic from _call_ai_react_logic_221
    return

label show_question_q_c_52_en:
    scene bg dapur with dissolve
    $ narasi_asli = "You are hungry, but the fridge only has eggs, jam, and meat."
    n "You are hungry, but the fridge only has eggs, jam, and meat."

    menu:
        "You are hungry, but the fridge only has eggs, jam, and meat."

        "Just cook a scrambled egg. It's definitely delicious and the taste is clear.":
            $ SN -= 5
            $ JP -= 5
            $ user_choice_text = "Just cook a scrambled egg. It's definitely delicious and the taste is clear."
            $ last_answer = "Sensing & Judging"
            jump show_question_q_c_52_en_A

        "Mix everything! Who knows, it might become a new masterpiece.":
            $ SN += 5
            $ JP += 5
            $ user_choice_text = "Mix everything! Who knows, it might become a new masterpiece."
            $ last_answer = "Intuitive & Perceiving"
            jump show_question_q_c_52_en_B


label show_question_q_c_52_en_A:
    $ user_journey_summary.append("Di situasi You are hungry, but the fridge only has eggs, jam, and meat., user memilih: Just cook a scrambled egg. It's definitely delicious and the taste is clear., dengan poin MBTI: Sensing & Judging")
    call ai_react_logic from _call_ai_react_logic_222
    return

label show_question_q_c_52_en_B:
    $ user_journey_summary.append("Di situasi You are hungry, but the fridge only has eggs, jam, and meat., user memilih: Mix everything! Who knows, it might become a new masterpiece., dengan poin MBTI: Intuitive & Perceiving")
    call ai_react_logic from _call_ai_react_logic_223
    return

label show_question_q_c_53_en:
    scene bg room with dissolve
    $ narasi_asli = "You have an exam tomorrow, but you only remembered 1 day before the date."
    n "You have an exam tomorrow, but you only remembered 1 day before the date."

    menu:
        "You have an exam tomorrow, but you only remembered 1 day before the date."

        "Read the summary of chapters according to what is likely to appear on the exam.":
            $ SN -= 5
            $ JP -= 5
            $ user_choice_text = "Read the summary of chapters according to what is likely to appear on the exam."
            $ last_answer = "Sensing & Judging"
            jump show_question_q_c_53_en_A

        "Read only the parts you understand best, the rest can be figured out during the exam.":
            $ SN += 5
            $ JP += 5
            $ user_choice_text = "Read only the parts you understand best, the rest can be figured out during the exam."
            $ last_answer = "Intuitive & Perceiving"
            jump show_question_q_c_53_en_B


label show_question_q_c_53_en_A:
    $ user_journey_summary.append("Di situasi You have an exam tomorrow, but you only remembered 1 day before the date., user memilih: Read the summary of chapters according to what is likely to appear on the exam., dengan poin MBTI: Sensing & Judging")
    call ai_react_logic from _call_ai_react_logic_224
    return

label show_question_q_c_53_en_B:
    $ user_journey_summary.append("Di situasi You have an exam tomorrow, but you only remembered 1 day before the date., user memilih: Read only the parts you understand best, the rest can be figured out during the exam., dengan poin MBTI: Intuitive & Perceiving")
    call ai_react_logic from _call_ai_react_logic_225
    return

label show_question_q_c_54_en:
    scene bg kantor with dissolve
    $ narasi_asli = "The boss asks you to work on a 'Secret' project without clear instructions."
    n "The boss asks you to work on a 'Secret' project without clear instructions."

    menu:
        "The boss asks you to work on a 'Secret' project without clear instructions."

        "Gently refuse. 'I need clear details and a deadline.'":
            $ SN -= 5
            $ JP -= 5
            $ user_choice_text = "Gently refuse. 'I need clear details and a deadline.'"
            $ last_answer = "Sensing & Judging"
            jump show_question_q_c_54_en_A

        "Accept! 'Ready, I will improvise as I go.'":
            $ SN += 5
            $ JP += 5
            $ user_choice_text = "Accept! 'Ready, I will improvise as I go.'"
            $ last_answer = "Intuitive & Perceiving"
            jump show_question_q_c_54_en_B


label show_question_q_c_54_en_A:
    $ user_journey_summary.append("Di situasi The boss asks you to work on a 'Secret' project without clear instructions., user memilih: Gently refuse. 'I need clear details and a deadline.', dengan poin MBTI: Sensing & Judging")
    call ai_react_logic from _call_ai_react_logic_226
    return

label show_question_q_c_54_en_B:
    $ user_journey_summary.append("Di situasi The boss asks you to work on a 'Secret' project without clear instructions., user memilih: Accept! 'Ready, I will improvise as I go.', dengan poin MBTI: Intuitive & Perceiving")
    call ai_react_logic from _call_ai_react_logic_227
    return

label show_question_q_c_55_en:
    scene bg stasiun with dissolve
    $ narasi_asli = "You want to move cities, but you have too many items!"
    n "You want to move cities, but you have too many items!"

    menu:
        "You want to move cities, but you have too many items!"

        "Sort the items. Throw away what you think is less important.":
            $ SN -= 5
            $ JP -= 5
            $ user_choice_text = "Sort the items. Throw away what you think is less important."
            $ last_answer = "Sensing & Judging"
            jump show_question_q_c_55_en_A

        "'We don't know, we might need this item later, so bring everything!'. Everything can be arranged again there.":
            $ SN += 5
            $ JP += 5
            $ user_choice_text = "'We don't know, we might need this item later, so bring everything!'. Everything can be arranged again there."
            $ last_answer = "Intuitive & Perceiving"
            jump show_question_q_c_55_en_B


label show_question_q_c_55_en_A:
    $ user_journey_summary.append("Di situasi You want to move cities, but you have too many items!, user memilih: Sort the items. Throw away what you think is less important., dengan poin MBTI: Sensing & Judging")
    call ai_react_logic from _call_ai_react_logic_228
    return

label show_question_q_c_55_en_B:
    $ user_journey_summary.append("Di situasi You want to move cities, but you have too many items!, user memilih: 'We don't know, we might need this item later, so bring everything!'. Everything can be arranged again there., dengan poin MBTI: Intuitive & Perceiving")
    call ai_react_logic from _call_ai_react_logic_229
    return

label show_question_q_c_56_en:
    scene bg room with dissolve
    $ narasi_asli = "Your little sibling broke your mother's favorite vase, they are so scared, almost crying."
    n "Your little sibling broke your mother's favorite vase, they are so scared, almost crying."

    menu:
        "Your little sibling broke your mother's favorite vase, they are so scared, almost crying."

        "Tell them to confess. Wrong is wrong, they must take responsibility.":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "Tell them to confess. Wrong is wrong, they must take responsibility."
            $ last_answer = "Thinking & Judging"
            jump show_question_q_c_56_en_A

        "Help hide the pieces. It's a pity if they get scolded.":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "Help hide the pieces. It's a pity if they get scolded."
            $ last_answer = "Feeling & Perceiving"
            jump show_question_q_c_56_en_B


label show_question_q_c_56_en_A:
    $ user_journey_summary.append("Di situasi Your little sibling broke your mother's favorite vase, they are so scared, almost crying., user memilih: Tell them to confess. Wrong is wrong, they must take responsibility., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic from _call_ai_react_logic_230
    return

label show_question_q_c_56_en_B:
    $ user_journey_summary.append("Di situasi Your little sibling broke your mother's favorite vase, they are so scared, almost crying., user memilih: Help hide the pieces. It's a pity if they get scolded., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic from _call_ai_react_logic_231
    return

label show_question_q_c_57_en:
    scene bg kafe with dissolve
    $ narasi_asli = "You have a strange but innovative business idea. When do you want to start making it happen?"
    n "You have a strange but innovative business idea."
    n "When do you want to start making it happen?"

    menu:
        "You have a strange but innovative business idea. When do you want to start making it happen?"

        "Later, after the profit-loss analysis is 100%% complete.":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "Later, after the profit-loss analysis is 100%% complete."
            $ last_answer = "Thinking & Judging"
            jump show_question_q_c_57_en_A

        "Now! The important thing is that many people like the idea.":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "Now! The important thing is that many people like the idea."
            $ last_answer = "Feeling & Perceiving"
            jump show_question_q_c_57_en_B


label show_question_q_c_57_en_A:
    $ user_journey_summary.append("Di situasi You have a strange but innovative business idea. When do you want to start making it happen?, user memilih: Later, after the profit-loss analysis is 100%% complete., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic from _call_ai_react_logic_232
    return

label show_question_q_c_57_en_B:
    $ user_journey_summary.append("Di situasi You have a strange but innovative business idea. When do you want to start making it happen?, user memilih: Now! The important thing is that many people like the idea., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic from _call_ai_react_logic_233
    return

label show_question_q_c_58_en:
    scene bg kantor with dissolve
    $ narasi_asli = "Your sports team keeps losing. As captain, what do you say?"
    n "Your sports team keeps losing."
    n "As captain, what do you say?"

    menu:
        "Your sports team keeps losing. As captain, what do you say?"

        "'Add more practice! We must win, score is everything.'":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "'Add more practice! We must win, score is everything.'"
            $ last_answer = "Thinking & Judging"
            jump show_question_q_c_58_en_A

        "'Relax guys. The important thing is that we enjoy playing together.'":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "'Relax guys. The important thing is that we enjoy playing together.'"
            $ last_answer = "Feeling & Perceiving"
            jump show_question_q_c_58_en_B


label show_question_q_c_58_en_A:
    $ user_journey_summary.append("Di situasi Your sports team keeps losing. As captain, what do you say?, user memilih: 'Add more practice! We must win, score is everything.', dengan poin MBTI: Thinking & Judging")
    call ai_react_logic from _call_ai_react_logic_234
    return

label show_question_q_c_58_en_B:
    $ user_journey_summary.append("Di situasi Your sports team keeps losing. As captain, what do you say?, user memilih: 'Relax guys. The important thing is that we enjoy playing together.', dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic from _call_ai_react_logic_235
    return

label show_question_q_c_59_en:
    scene bg abstrak with dissolve
    $ narasi_asli = "You find an Ancient Weapon during an exploration. What is your focus?"
    n "You find an Ancient Weapon during an exploration."
    n "What is your focus?"

    menu:
        "You find an Ancient Weapon during an exploration. What is your focus?"

        "Its power and its intact condition.":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "Its power and its intact condition."
            $ last_answer = "Thinking & Judging"
            jump show_question_q_c_59_en_A

        "Its legendary story and the mystery of who its former owner was.":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "Its legendary story and the mystery of who its former owner was."
            $ last_answer = "Feeling & Perceiving"
            jump show_question_q_c_59_en_B


label show_question_q_c_59_en_A:
    $ user_journey_summary.append("Di situasi You find an Ancient Weapon during an exploration. What is your focus?, user memilih: Its power and its intact condition., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic from _call_ai_react_logic_236
    return

label show_question_q_c_59_en_B:
    $ user_journey_summary.append("Di situasi You find an Ancient Weapon during an exploration. What is your focus?, user memilih: Its legendary story and the mystery of who its former owner was., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic from _call_ai_react_logic_237
    return

label show_question_q_c_60_en:
    scene bg kantor with dissolve
    $ narasi_asli = "There is a new office rule that is inconvenient for employees."
    n "There is a new office rule that is inconvenient for employees."

    menu:
        "There is a new office rule that is inconvenient for employees."

        "Propose an official revision. Show the points that are inefficient.":
            $ TF -= 5
            $ JP -= 5
            $ user_choice_text = "Propose an official revision. Show the points that are inefficient."
            $ last_answer = "Thinking & Judging"
            jump show_question_q_c_60_en_A

        "Create an emotional petition. Ask for leniency on the rules.":
            $ TF += 5
            $ JP += 5
            $ user_choice_text = "Create an emotional petition. Ask for leniency on the rules."
            $ last_answer = "Feeling & Perceiving"
            jump show_question_q_c_60_en_B


label show_question_q_c_60_en_A:
    $ user_journey_summary.append("Di situasi There is a new office rule that is inconvenient for employees., user memilih: Propose an official revision. Show the points that are inefficient., dengan poin MBTI: Thinking & Judging")
    call ai_react_logic from _call_ai_react_logic_238
    return

label show_question_q_c_60_en_B:
    $ user_journey_summary.append("Di situasi There is a new office rule that is inconvenient for employees., user memilih: Create an emotional petition. Ask for leniency on the rules., dengan poin MBTI: Feeling & Perceiving")
    call ai_react_logic from _call_ai_react_logic_239
    return
