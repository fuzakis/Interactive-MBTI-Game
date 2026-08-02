# ---------------------------------------------------------
# SPLASH SCREEN (Intro sebelum Main Menu)
# ---------------------------------------------------------

label before_main_menu:
    python:
        # Reset perhitungan untuk percobaan baru
        session_api_calls = 0
        session_input_tokens = 0
        session_output_tokens = 0
        session_total_tokens = 0
        
    play music "opening.mp3"
    # Cetak tanda ke terminal (Cek debug console nanti)
    $ print("--- SPLASH SCREEN DIMULAI ---")

    # Layar Hitam
    scene black 
    with dissolve

    # Teks Intro (Gunakan parameter hard=True agar tidak bisa di-skip)
    show text "{color=#ffffff}{size=60}FUZAKIS PROJECT{/size}{/color}" at truecenter with dissolve
    
    # PAUSE KERAS (Tidak bisa diklik skip)
    $ renpy.pause(3.0)

    hide text with dissolve
    $ renpy.transition(dissolve)
    $ print("--- SPLASH SCREEN SELESAI ---")

    return

label start:
    $quick_menu = False
    scene bg temple with dissolve
    hide screen quick_menu
    play music "menu.mp3" fadein 1.0

    # --- PANGGIL PROFILE MANAGER ---
    # is_start=True membuat layar tidak bisa di-cancel/close tanpa memilih
    call screen profile_manager_screen(is_start=True)

    # Validasi jaga-jaga kalau pemain mengosongkan nama lalu klik lanjut
    if not persistent.player_name or persistent.player_name.strip() == "":
        $ persistent.player_name = "Player"
    # -------------------------------

    $ print("--- DISCLAIMER SCREEN DIMULAI ---")

    # Layar Hitam
    scene black 
    with dissolve

    # Teks Intro (Gunakan parameter hard=True agar tidak bisa di-skip)
    if persistent.cur_lang == "en":
        show text "{color=#ffffff}{size=60}DISCLAIMER!{/size}\n {size=45}This is a simple personality test. Heavily inspired by the Myers-Briggs Type Indicator (MBTI). The results wont determine your actual personality.{/size}{/color}" at truecenter with dissolve
    else:
        show text "{color=#ffffff}{size=60}DISCLAIMER!{/size}\n {size=45}Ini adalah tes kepribadian sederhana. Terinspirasi oleh Myers-Briggs Type Indicator (MBTI). Hasilnya tidak akan menentukan kepribadian Anda sebenarnya.{/size}{/color}" at truecenter with dissolve

    # PAUSE KERAS (Tidak bisa diklik skip)
    $ renpy.pause(5.0, hard=True)

    # Teks Intro (Gunakan parameter hard=True agar tidak bisa di-skip)
    if persistent.cur_lang == "en":
        show text "{color=#ffffff}{size=60}HOW TO PLAY{/size}\n {size=45}Click anywhere to advance throughout the game. If there are multiple choices, select the one that best represents you.{/size}{/color}" at truecenter with dissolve
    else:
        show text "{color=#ffffff}{size=60}CARA BERMAIN{/size}\n {size=45}Klik di mana saja untuk melanjutkan sepanjang permainan. Jika ada beberapa pilihan, pilih yang paling mewakili Anda.{/size}{/color}" at truecenter with dissolve

    # PAUSE KERAS (Tidak bisa diklik skip)
    $ renpy.pause(5.0, hard=True)

    hide text with dissolve
    $ renpy.transition(dissolve)
    $ print("--- DISCLAIMER SELESAI ---")
    jump startgame

# 2. Start Game
label startgame:
    $ quick_menu = True
    show screen quick_menu
    $ renpy.transition(dissolve)
    scene bg abstrak
    play music "audio/companion.mp3"
    # Reset nilai dulu
    $ IE = 0
    $ SN = 0
    $ TF = 0
    $ JP = 0

    # STEP 1: PILIH COMPANION (Looping sampai yakin)
    call screen companion_selection_screen # (Asumsi Anda pakai screen gambar)
    
    # Setelah screen me-return 'companion_personality', masuk ke konfirmasi
    
label konfirmasi_companion:
    scene bg stasiun_2
    
    # Update nama AI sesuai pilihan hewan & bahasa saat ini
    $ update_companion_name_string()

    # Tampilkan Karakter
    show expression "companion " + companion_personality + " neutral" at companion_std with dissolve
    
    # Penjelasan Karakter (Bisa hardcode atau ambil dari definitions)
    if companion_personality == "extraversion":
        stop music fadeout 1.0
        play music "audio/dog_bgm.mp3"
        if persistent.cur_lang == "en":
            n "This is Iwank the DOG (Extraversion). Very energetic, social, and lively. Perfect for those who love crowds."
        else:
            n "Ini adalah Iwank Si ANJING (Extraversion). Dia sangat energik, sosial, dan heboh. Cocok untuk kamu yang suka keramaian."
    elif companion_personality == "neuroticism":
        stop music fadeout 1.0
        play music "audio/civet_bgm.mp3"
        if persistent.cur_lang == "en":
            n "This is Jakouko the CIVET (Neuroticism). Very alert, thoughtful, and cautious. Perfect for those who are considerate."
        else:
            n "Ini adalah Jakouko Si LUWAK (Neuroticism). Dia sangat waspada, pemikir, dan hati-hati. Cocok untuk kamu yang penuh pertimbangan."
    elif companion_personality == "openness":
        stop music fadeout 1.0
        play music "audio/fox_bgm.mp3"
        if persistent.cur_lang == "en":
            n "This is Kitsuko the FOX (Openness). Very creative, adventurous, and imaginative. Perfect for those who love new things."
        else:
            n "Ini adalah Kitsuko Si RUBAH (Openness). Dia sangat kreatif, suka petualangan, dan imajinatif. Cocok untuk kamu yang suka hal-hal baru."
    elif companion_personality == "agreeableness":
        stop music fadeout 1.0
        play music "audio/rabbit_bgm.mp3"
        if persistent.cur_lang == "en":
            n "This is Susagi the RABBIT (Agreeableness). Very friendly, caring, and understanding. Perfect for those who value peace."
        else:
            n "Ini adalah Susagi Si KELINCI (Agreeableness). Dia sangat ramah, penyayang, dan pengertian. Cocok untuk kamu yang menghargai kedamaian."
    elif companion_personality == "conscientiousness":
        stop music fadeout 1.0
        play music "audio/cat_bgm.mp3"
        if persistent.cur_lang == "en":
            n "This is Onyen the CAT (Conscientiousness). Very meticulous, disciplined, and responsible. Perfect for those who love order."  
        else:
            n "Ini adalah Onyen Si KUCING (Conscientiousness). Dia sangat teliti, disiplin, dan bertanggung jawab. Cocok untuk kamu yang suka keteraturan."

    if persistent.cur_lang == "en":
        menu:
            "Are you sure you want to choose this travel companion?"
            "Yes, I'm sure":
                jump sesi_tutorial_ai
            "No, change character":
                hide companion_std with dissolve
                call screen companion_selection_screen
                jump konfirmasi_companion
    else:
        menu:
            "Apakah kamu yakin memilih teman perjalanan ini?"
            "Ya, saya yakin":
                jump sesi_tutorial_ai
            "Tidak, ganti karakter":
                hide companion_std with dissolve
                call screen companion_selection_screen
                jump konfirmasi_companion               

        # Loop balik ke label konfirmasi akan dihandle oleh screen return

label sesi_tutorial_ai:
    # STEP 2: TUTORIAL OLEH AI

    python:
        # Buat file profil kosong dengan identitas yang sudah dipilih
        load_ai_memory(persistent.player_name, companion_personality, "Unknown")
        save_ai_memory()

    if persistent.cur_lang == "en":
        n "Alright! Your new companion will explain how to play."
    else:
        n "Baiklah! Teman barumu akan menjelaskan cara mainnya."

    # 1. Loading indikator
    show screen ai_loading with dissolve
    window hide

    # 2. PROSES GENERATE (Berat di sini)
    python:
        if persistent.cur_lang == "en":
        # Bahasa Inggris
            tutorial_prompt = f"""
            TASK: Explain interactively how to play this MBTI test game to the user.
            CONTEXT: You are {companion_personality} (Use your animal persona!).
            
            KEY POINTS TO EXPLAIN (adjust the speech style to match your personality, dont just read it like a manual):
            1. Explain that there will be 20 story questions. that will be shuffled from 3 different packets of questions.
            2. There are no right or wrong answers. Just be honest.
            3. I (your animal persona) will accompany and comment on your choices.
            4. Don't forget to tell the user that this test can be used as self-reflection, so try to choose the most honest answer that aligns with your personality!
            5. Also give a disclaimer to the user that the AI's reactions are generated based on the companion's personality, so they may not always be accurate or make sense, but they will try to provide reactions according to their personality traits.
            6. Finally, tell the user that whatever the result is, it will not define who you are as a person, so have fun, whatever the result you can take it as a lesson!
            7. Lastly, tell the user to continue the test, they just need to click the screen to continue, then choose one of the options that will be given after the tutorial, and the test will start immediately after they choose.
            - Insert [EMOTION] tags at every change in tone of voice.
            - Start the conversation with "[emotion] Alright, I'm (character name) with {companion_personality} personality and I'll explain how to play." Explain with speech style matching your personality.
            - Example: "Wow I agree! [HAPPY] But be careful.. [WORRIED]"
            - Available emotions: [HAPPY], [SAD], [ANGRY], [FEAR], [SURPRISE], [DISGUST], [NEUTRAL]. Don't include anything else in the tags.
            - DO NOT include animal sounds inside brackets [ ].
            - Maximum 270 characters per point (e.g., point 1, point 2, point 3, etc.).
            - Don't just say "point 1", "point 2", etc. Make it natural, like a conversation.
            """
        else:
            tutorial_prompt = f"""
            TUGAS: Jelaskan secara interaktif cara bermain game tes MBTI ini kepada user.
            KONTEKS: Kamu adalah {companion_personality} (Gunakan persona hewanmu!).
            
            POIN YANG HARUS DIJELASKAN (atur gaya bicara agar sesuai dengan kepribadianmu, jangan hanya membacakannya seperti manual):
            1. jelaskan jika akan ada 20 soal cerita. 
            2. Tidak ada jawaban benar atau salah. Jujur saja.
            3. Aku (persona hewanmu) akan menemani dan mengomentari pilihanmu.
            4. Jangan lupa beri tahu user bahwa tes ini bisa dijadikan sebagai refleksi diri, jadi coba pilih jawaban yang paling jujurlah dan selaras dengan kepribadianmu!
            5. Beri juga disclaimer kepada user bahwa reaksi AI dihasilkan berdasarkan kepribadian dari companion, jadi mungkin tidak selalu akurat atau masuk akal, tapi mereka akan berusaha memberikan reaksi sesuai dengan trait kepribadian mereka.
            6. Terakhir, katakan kepada user bahwa apapun hasilnya, itu tidak akan mendefinisikan siapa kamu sebagai pribadi, jadi bersenang-senanglah, apapun hasilnya kamu bisa mengambilnya sebagai pelajaran!
            7. Penutup, beri tahu user untuk melanjutkan tes, mereka hanya perlu mengklik layar untuk melanjutkan, lalu memilih salah satu opsi yang akan diberikan setelah tutorial, dan tes akan dimulai segera setelah mereka memilih.

            ATURAN:
            - Sisipkan tag [EMOSI] di setiap perubahan nada suara.
            - Awali percakapan dengan "[emosi] baiklah, aku si "nama karakter" dengan personality {companion_personality} akan menjelaskan bagaimana cara bermainnya." jelaskan dengan gaya bicara yang sesuai personality hewanmu.      
            - Contoh: "Wah aku setuju! [HAPPY] Tapi hati-hati ya.. [WORRIED]"
            - Emosi yang tersedia: [HAPPY], [SAD], [ANGRY], [FEAR], [SURPRISE], [DISGUST], [NEUTRAL]. selain itu, jangan masukkan hal lain kedalam tag.
            - JANGAN masukkan suara hewan ke dalam kurung [ ].
            - Maksimal 270 karakter per poin (contoh no.1, no.2, no.3, dst).
            - Jangan hanya mengatakan "poin 1", "poin 2", dll. Buatlah natural, seperti percakapan biasa.
            """
        
        import time
        start_time = time.time() # ⏱️ Mulai hitung waktu

        ai_intro_text = get_ai_feedback(tutorial_prompt, companion_personality, lang=persistent.cur_lang, token_limit=500)
        
        end_time = time.time() # ⏱️ Hentikan waktu
        latency_duration = end_time - start_time # Hitung selisihnya

        # Cetak ke konsol untuk dicatat di laporan
        debug_log("API LATENCY", f"Karakter: {companion_personality} | Waktu Respon: {latency_duration:.2f} detik")
        # Debug untuk memastikan kurung sudah berubah
        debug_log("AI TUTORIAL SANITIZED", ai_intro_text)
    
    # 3. SEMBUNYIKAN LOADING (FIX OVERLAP)
    # Kita paksa hide dulu sebelum menampilkan karakter
    hide screen ai_loading with dissolve

    
    # 4. TAMPILKAN KARAKTER AWAL (FIX ERROR NAME 'ai_emo')
    # Gunakan 'neutral' sebagai default agar tidak error NameError
    window show
    show expression "companion " + companion_personality + " neutral" at companion_std with dissolve

    # 5. LOOP BICARA & EMOSI DINAMIS
    python:
        
        tut_sentences = breakdown_ai_text(ai_intro_text)

        # Regex Pattern
        import re
        pattern = r"\[(.*?)\]"

        # Set Emosi Awal (Safety Net)
        current_emo = "neutral"
        renpy.show("companion " + companion_personality + " " + current_emo, at_list=[companion_std])

        for s in tut_sentences:
            # Ambil isi kurung (misal: "EXCITED" atau "HAPPY")
            match = re.search(pattern, s, re.IGNORECASE)
            if match:
                raw_tag = match.group(1).lower()
                raw_tag = re.sub(r'[^a-z]', '', raw_tag)
                
                # --- PERUBAHAN 2: MAPPING EMOSI LIAR --
                # Kita petakan emosi "ilegal" ke emosi yang kita punya
                if raw_tag in ["sad", "cry", "gloom", "sadness"]: 
                    new_emo = "sadness"
                elif raw_tag in ["surprise", "shock", "wow"]: 
                    new_emo = "surprised"
                elif raw_tag in ["fear", "worried", "anxious", "terror", "scared"]: 
                    new_emo = "fear"
                elif raw_tag in ["disgust", "eww"]: 
                    new_emo = "disgust"
                elif raw_tag in ["happy", "excited", "joy", "laugh", "excited", "supportive"]: 
                    new_emo = "happy" # EXCITED dilarikan ke HAPPY
                elif raw_tag in ["anger", "angry", "mad", "furious"]: 
                    new_emo = "anger"
                else: 
                    # Jika tag tidak dikenali sama sekali (misal [GUK]), anggap neutral
                    new_emo = "neutral"
                
                # Update Sprite
                if new_emo != current_emo:
                    current_emo = new_emo
                    renpy.show("companion " + companion_personality + " " + current_emo, at_list=[companion_std])
                
                # Bersihkan tag
                clean_s = re.sub(pattern, "", s).strip()
            else:
                clean_s = s.strip()
            
            # B. Tampilkan Teks
            if clean_s:
                say_ai_safe(clean_s)
            match = None  # Reset match untuk iterasi berikutnya

    # Akhiri Tutorial
    
    if persistent.cur_lang == "en":
        n "Now, let's start the test session."
    else:
        n "Sekarang, mari kita mulai sesi tesnya."
    
    # Masuk ke Tes
    jump start_test_session

# Taruh fungsi kalkulasi di luar label agar aman
init python:
    def calc_dominance(score):
        return 50 + (abs(score) / 2.0)

label scene_hasil_tes:
    python:
        end_time = time.time()
        play_duration = end_time - start_time # Menghitung selisih detik
        
        # 600 detik = 10 menit
        if play_duration < 600 and "speed" not in persistent.unlocked_awards:
            persistent.unlocked_awards.append("speed")
            unlock_achievement("Achievement Unlocked: Are you Speedrunner? ⚡" if persistent.cur_lang == "en" else "Award Unlocked: Apakah kamu Speedrunner? ⚡", "images/award_speed.png")

    $ quick_menu = False
    hide screen quick_menu
    scene bg abstrak_2 with dissolve
    stop music fadeout 1.0
    play music "audio/memories.mp3"
    
    if persistent.cur_lang == "en":
        n "Great! You've completed the test. Now, let me evaluate your personality based on your choices."
    else:
        n "Bagus! Kamu telah menyelesaikan tesnya. Sekarang, aku akan mengevaluasi kepribadianmu berdasarkan pilihanmu."

    # --- 1. KALKULASI SKOR ---
    python:
        if IE >= 0: res_ie="E"; txt_ie="Extrovert"; val_ie=calc_dominance(IE)
        else:       res_ie="I"; txt_ie="Introvert"; val_ie=calc_dominance(IE)

        if SN >= 0: res_sn="N"; txt_sn="Intuitive"; val_sn=calc_dominance(SN)
        else:       res_sn="S"; txt_sn="Sensing";   val_sn=calc_dominance(SN)

        if TF >= 0: res_tf="F"; txt_tf="Feeling";   val_tf=calc_dominance(TF)
        else:       res_tf="T"; txt_tf="Thinking";  val_tf=calc_dominance(TF)

        if JP >= 0: res_jp="P"; txt_jp="Perceiving"; val_jp=calc_dominance(JP)
        else:       res_jp="J"; txt_jp="Judging";    val_jp=calc_dominance(JP)

        my_mbti_type = res_ie + res_sn + res_tf + res_jp

        fallback_text = "Mysterious Creature" if persistent.cur_lang == "en" else "Makhluk Misterius"
        my_spirit = spirit_animals[persistent.cur_lang].get(my_mbti_type, fallback_text)

        load_ai_memory(persistent.player_name, companion_personality, my_mbti_type)
        save_ai_memory()

    # --- 2. EVALUASI AI (RANGKUMAN) ---
    
    # Sembunyikan gambar lama
    hide ai_sprite 
    show screen ai_loading with dissolve
    window hide

    python:
        # Cek apakah list history ada isinya
        if user_journey_summary:
            # Ambil 5 data terakhir
            journey_text = " ".join(user_journey_summary) 
        else:
            # DATA PALSU (Fallback) jika history kosong
            journey_text = "User bermain dengan sangat misterius. Tidak banyak jejak yang ditinggalkan, namun hasil akhirnya menunjukkan kepribadian yang kuat."

        # Catatan perubahan hasil MBTI (dulu -> sekarang), kosong kalau tidak ada
        mbti_change_note = format_mbti_change(current_ai_memory, persistent.cur_lang)

        if persistent.cur_lang == "en":

            # --- PROMPT INGGRIS ---
            ctx_eval = f"""
            TASK: Final evaluation for user ({my_mbti_type} - {my_spirit}).
            DATA: {journey_text}
            {mbti_change_note}

            SPECIAL INSTRUCTIONS:
            Provide evaluation in 3 SEPARATE PARTS.
            YOU MUST separate each part with "###".

            Part 1: Summarize user's playstyle (max 270 chars). If a MEMORY OF CHANGE note is present above, open by warmly remarking how their result shifted from before to now.
            Part 2: Comment on personality compatibility with you (max 270 chars).
            part 3: Must Insert the [SPIRIT] tag exactly once at the beginning of the sentence. State the user's Spirit Animal, {my_spirit}, starting with "you have the spirit animal {my_spirit}", and explain why the Spirit Animal {my_spirit} fits the user, also give your opinion on that compatibility (2 sentences or max 270 chars).
            
            TAG RULES:
            - Insert [EMOTION] tag IF tone changes.
            - DO NOT put "part 1", "part 2", etc in the response. Just separate with "###".
            - DO NOT put animal sounds inside tags. Correct example: [HAPPY] Woof!
            - Available emotions: [HAPPY], [SAD], [ANGRY], [FEAR], [SURPRISE], [DISGUST], [NEUTRAL].
            """
        else:


            # --- PROMPT INDONESIA ---
            ctx_eval = f"""
            TUGAS: Evaluasi akhir user ({my_mbti_type} - {my_spirit}).
            DATA: {journey_text}
            {mbti_change_note}

            INSTRUKSI KHUSUS:
            Berikan evaluasi dalam 3 BAGIAN TERPISAH.
            Wajib pisahkan setiap bagian dengan tanda "###".

            Isi 1: Rangkum gaya bermain pemain (maksimal 270 karakter/huruf termasuk spasi). Jika ada catatan INGATAN PERUBAHAN di atas, buka dengan komentar hangat tentang bagaimana hasilnya berubah dari dulu ke sekarang.
            Isi 2: Komentar kecocokan kepribadian user denganmu, intinya per bagian maksimal 270 karakter/huruf termasuk spasi).
            Isi 3: Wajib sisipkan tag [SPIRIT] tepat satu kali di awal kalimat. Sebutkan Spirit Animal pemain, {my_spirit}, dengan dimulai kalimat "kamu memiliki spirit animal {my_spirit}", kemudian jelaskan kenapa Spirit Animal {my_spirit} cocok dengan pemain, juga berikan pendapatmu tentang kecocokan tersebut (2 kalimat atau maksimal 270 karakter/huruf termasuk spasi).
            
            ATURAN:
            - Sisipkan tag [EMOSI] di setiap perubahan nada bicara.
            - JANGAN masukkan "isi 1", "isi 2", dll dalam respons. Cukup pisahkan dengan "###".
            - Contoh: "Wah aku setuju! [HAPPY] Tapi hati-hati ya.. [WORRIED]"
            - Emosi yang tersedia: [HAPPY], [SAD], [ANGRY], [FEAR], [SURPRISE], [DISGUST], [NEUTRAL]. 
            """
        
        import time
        start_time = time.time() # ⏱️ Mulai hitung waktu

        eval_response = get_ai_feedback(ctx_eval, companion_personality, lang=persistent.cur_lang, token_limit=1500)

        end_time = time.time() # ⏱️ Hentikan waktu
        latency_duration = end_time - start_time # Hitung selisihnya

        # Cetak ke konsol untuk dicatat di laporan
        debug_log("API LATENCY", f"Karakter: {companion_personality} | Waktu Respon: {latency_duration:.2f} detik")

        # Pecah berdasarkan topik ### (Kita tidak parsing emosi global lagi di sini)
        eval_parts = eval_response.split("###")
        
    hide screen ai_loading with dissolve
    window show

    # Tampilkan Karakter Evaluasi
    show expression "companion " + companion_personality + " neutral" at companion_std with dissolve

    # Loop Teks (Klik per bagian)
    python:
        import re
        pattern = r"\[(.*?)\]"
        current_emo = "neutral"

        for part in eval_parts:
            
            if part.strip():
                # Pecah topik ini menjadi kalimat-kalimat kecil
                sub_sentences = breakdown_ai_text(part.strip())
                
                for s in sub_sentences:

                    # --- INTERCEPTOR TAG [SPIRIT] ---
                    if "[SPIRIT]" in s.upper():
                        # Menggabungkan prefix "achieve_" dengan tipe MBTI (huruf kecil)
                        # Contoh: "achieve_" + "infp" -> "achieve_infp"
                        image_name = "achieve_" + my_mbti_type.lower()
                        
                        # Transisi: Sembunyikan karakter pendamping, tampilkan gambar Spirit Animal
                        renpy.hide("companion")
                        
                        # Validasi apakah gambar tersedia di folder images
                        if renpy.has_image(image_name):
                            # Memanggil gambar dengan transform kustom kita
                            renpy.show(image_name, at_list=[spirit_appear])
                        else:
                            renpy.show("achieve_locked", at_list=[spirit_appear])
                            
                        renpy.with_statement(dissolve)
                        
                        # Bersihkan tag dan tampilkan teks dialog
                        clean_s = s.replace("[SPIRIT]", "").replace("[spirit]", "").strip()
                        if clean_s:
                            say_ai_safe(clean_s)
                        
                        # Kembalikan ke karakter pendamping setelah teks dibaca
                        renpy.hide(image_name)
                        renpy.show("companion " + companion_personality + " " + current_emo, at_list=[companion_std])
                        renpy.with_statement(dissolve)
                        
                        # Lanjut ke kalimat berikutnya
                        continue
                    # ---------------------------------------------------------    

                    # A. Cek Emosi Lokal
                    match = re.search(pattern, s, re.IGNORECASE)
                    if match:
                        # AMBIL DULU datanya
                        raw_tag = match.group(1).lower()
                        raw_tag = re.sub(r'[^a-z]', '', raw_tag)
                        
                        # MAPPING EMOSI (Handle Excited dll)
                        if raw_tag in ["sad", "cry", "gloom", "sadness"]: 
                            new_emo = "sadness"
                        elif raw_tag in ["surprise", "shock", "wow"]: 
                            new_emo = "surprised"
                        elif raw_tag in ["fear", "worried", "anxious", "terror", "scared"]: 
                            new_emo = "fear"
                        elif raw_tag in ["disgust", "eww"]: 
                            new_emo = "disgust"
                        elif raw_tag in ["happy", "excited", "joy", "laugh", "excited", "supportive"]: 
                            new_emo = "happy" # EXCITED dilarikan ke HAPPY
                        elif raw_tag in ["anger", "angry", "mad", "furious"]: 
                            new_emo = "anger"
                        else: 
                            # Jika tag tidak dikenali sama sekali (misal [GUK]), anggap neutral
                            new_emo = "neutral"
                        
                        # Update Sprite
                        if new_emo != current_emo:
                            current_emo = new_emo
                            renpy.show("companion " + companion_personality + " " + current_emo, at_list=[companion_std])
                        
                        clean_s = re.sub(pattern, "", s).strip()
                    else:
                        clean_s = s.strip()

                    # B. Tampilkan
                    if clean_s:
                        say_ai_safe(clean_s)
                    match = None  # Reset match untuk iterasi berikutnya

    # SENSOR ACHIEVEMENT: Cek apakah MBTI ini sudah ada di memori?
    if my_mbti_type not in persistent.unlocked_mbti:
        # Jika belum ada, masukkan ke memori!
        $ persistent.unlocked_mbti.append(my_mbti_type)
        
        # Munculkan notifikasi kecil di pojok layar
        $ unlock_achievement("New Spirit Animal Unlocked: " + my_mbti_type + "!" if persistent.cur_lang == "en" else "Hewan Spiritual Baru Terbuka: " + my_mbti_type + "!", "images/achieve_" + my_mbti_type.lower() + ".png")
    
    # --- SENSOR COMPANION ---
    
    # 1. Anjing (Extraversion)
    if companion_personality == "extraversion" and "dog" not in persistent.unlocked_awards:
        $ persistent.unlocked_awards.append("dog")
        $ unlock_achievement("Woof! Let's go buddy! 🐶" if persistent.cur_lang == "en" else "Award Unlocked: Guk! Ayo kita pergi! 🐶", "images/award_dog.png")

    # 2. Kucing (Conscientiousness)
    elif companion_personality == "conscientiousness" and "cat" not in persistent.unlocked_awards:
        $ persistent.unlocked_awards.append("cat")
        $ unlock_achievement("Award Unlocked: Tidy it Now! 🐱" if persistent.cur_lang == "en" else "Award Unlocked: Kita harus rapikan sekarang! 🐱", "images/award_cat.png")

    # 3. Musang/Civet (Neuroticism)
    elif companion_personality == "neuroticism" and "civet" not in persistent.unlocked_awards:
        $ persistent.unlocked_awards.append("civet")
        $ unlock_achievement("Award Unlocked: Y-you choose.. M-me?! 🐾" if persistent.cur_lang == "en" else "Award Unlocked: Kau memilih... Aku?! 🐾", "images/award_civet.png")

    # 4. Kelinci (Agreeableness)
    elif companion_personality == "agreeableness" and "rabbit" not in persistent.unlocked_awards:
        $ persistent.unlocked_awards.append("rabbit")
        $ unlock_achievement("Award Unlocked: I rather choose peace ok 🐰" if persistent.cur_lang == "en" else "Award Unlocked: Aku lebih memilih perdamaian 🐰", "images/award_rabbit.png")

    # 5. Rubah (Openness)
    elif companion_personality == "openness" and "fox" not in persistent.unlocked_awards:
        $ persistent.unlocked_awards.append("fox")
        $ unlock_achievement("Award Unlocked: Shape like water 🦊" if persistent.cur_lang == "en" else "Award Unlocked: Bentuk seperti air 🦊", "images/award_fox.png")

    # --- SENSOR MASTER MBTI (16/16) ---
    # Cek apakah panjang list MBTI di memori sudah mencapai 16
    if len(persistent.unlocked_mbti) == 16 and "all_mbti" not in persistent.unlocked_awards:
        $ persistent.unlocked_awards.append("all_mbti")
        $ unlock_achievement("Ultimate Award Unlocked: Endless possibility! 🌟" if persistent.cur_lang == "en" else "Award Unlocked: Kemungkinan Tak Terbatas! 🌟", "images/award_all.png")

    show screen ai_loading with dissolve
    python:
        if persistent.cur_lang == "en":
            # --- PROMPT INGGRIS ---
            detail_prompt = f"""
            You: Psychologist with{companion_personality} 
            Just answer normally without inserting emotion or personality tags, because this is just a detailed explanation, not a chat response!
            
            Provide a detailed explanation for the personality result {my_mbti_type} with spirit animal {my_spirit}. 
            Format it into 3 paragraphs (max 100 words per paragraph) with the following structure:
            1. An in-depth explanation of the {my_mbti_type} persona based on the test
            2. Career path/suggestions that would suit the user's playstyle and MBTI traits.
            3. Love/relationship advice that would suit this personality type (e.g., compatible MBTI types, or compatible traits).
            4. An analysis of why this persona is very similar to the spirit animal {my_spirit} and what the benefits are.
            5. At the end, add a brief disclaimer that this is just a game and does not necessarily determine real-life personality.
            6. In this part, no [EMOTION] and also [PERSONALITY] tags are needed.
            """
        else:
            # Gunakan variabel my_mbti_type dan my_spirit yang sudah ada
            detail_prompt = f"""
            Kamu: Psikolog dengan sifat {companion_personality}
            Jawab saja secara normal tanpa menyisipkan tag emosi atau kepribadian, karena ini hanya penjelasan detail, bukan respons chat!
            
            Buatlah penjelasan detail untuk hasil kepribadian {my_mbti_type} dengan spirit animal {my_spirit}. 
            Format ke dalam 3 paragraf (maksimal 100 kata per paragraf) dengan struktur berikut:
            1. Penjelasan mendalam tentang persona {my_mbti_type} berdasarkan hasil tes.
            2. Saran jalur karir/pekerjaan yang cocok berdasarkan cara bermain dan sifat MBTI tersebut.
            3. Saran percintaan yang cocok untuk tipe kepribadian ini (misal: cocok dengan tipe MBTI apa, atau cocok dengan sifat seperti apa).
            4. Analisis mengapa persona ini sangat mirip dengan spirit animal {my_spirit} dan apa benefitnya.
            5. Di akhir, tambahkan disclaimer singkat bahwa ini hanya game dan tidak serta merta menentukan kepribadian di dunia nyata.
            6. Pada bagian ini tidak diperlukan tag [EMOTION] dan juga [PERSONALITY]
            """
        
        import time
        start_time = time.time() # ⏱️ Mulai hitung waktu

        # 3. Panggil API AI (Gunakan fungsi pemanggil AI milikmu, misal get_ai_feedback)
        # Token limit dibesarkan karena butuh jawaban panjang
        detailed_mbti_explanation = get_ai_feedback(detail_prompt, "psychologist", lang=persistent.cur_lang, token_limit=2000)

        end_time = time.time() # ⏱️ Hentikan waktu
        latency_duration = end_time - start_time # Hitung selisihnya

        # Cetak ke konsol untuk dicatat di laporan
        debug_log("API LATENCY", f"Karakter: {companion_personality} | Waktu Respon: {latency_duration:.2f} detik")

        # --- SIMPAN HASIL TEST LENGKAP (untuk buka ulang & dev jump, tanpa AI) ---
        save_test_result(
            my_mbti_type,
            my_spirit,
            {"IE": IE, "SN": SN, "TF": TF, "JP": JP},
            eval_parts,
            detailed_mbti_explanation,
        )

    # --- 3. DIAGRAM & MENU ---
    hide screen ai_loading with dissolve
    window hide

    call screen mbti_result_diagram
    window show
    if persistent.cur_lang == "en":
        menu:
            "Would you like to chat more with me about your results?"
            "Yes, chat with AI":
                jump sesi_chat_bebas
            "No, exit directly":
                jump ending_scene
    else:
        menu:
            "Apakah kamu ingin mengobrol tentang hasil ini?"
            "Ya, ngobrol dengan AI":
                jump sesi_chat_bebas
            "Tidak, langsung keluar":
                jump ending_scene

label sesi_chat_bebas:
    scene bg temple # Ganti latar yang lebih santai
    
    # Ganti Prompt AI ke Mode "Konselor"
    $ current_mode = "counselor" 
    # (Nanti kita update definitions.rpy agar support mode ini)
    
    show expression "companion " + companion_personality + " neutral" at companion_std
    
    if persistent.cur_lang == "en":
        ai "Sure, feel free to ask anything about your results, or just vent if you like. Type 'exit' when you're done."
    else:
        ai "Silakan, tanyakan apa saja tentang hasilmu, atau curhat juga boleh. Ketik 'keluar' jika sudah selesai."

    label chat_loop:
        # 1. Input Pemain
        # 1. NYALAKAN MODE CHAT (Agar input pindah ke tengah)
        $ is_chat_input = True 
        
        # Panggil Input
        $ user_input = renpy.input("Ketik pesanmu..." if persistent.cur_lang == "id" else "Type your message...", length=270).strip()
        
        # 2. MATIKAN MODE CHAT (Kembalikan ke normal untuk jaga-jaga)
        $ is_chat_input = False

        if user_input.lower() in ["keluar", "exit", "sudah", "bye", "selesai", "quit", "__quit__", "cukup", "end", "done", "stop", "berhenti", "dadah", "da-dah", "see you", "sampai jumpa"]:
            # Manual set ekspresi bahagia sebelum pamit
            show expression "companion " + companion_personality + " happy" at companion_std
            if persistent.cur_lang == "en":
                ai "Goodbye! It was great chatting with you!"
            else:
                ai "Dadah! Senang bisa ngobrol sama kamu!"
            jump ending_scene

        # Indikator ketik
        show screen ai_loading with dissolve
        window hide
        show expression "companion " + companion_personality + " neutral" at companion_std

        if user_input:
            # --- SENSOR CHAT 5X ---
            $ chat_count += 1 # Tambah 1 setiap nanya
            
            if chat_count == 6 and "chat" not in persistent.unlocked_awards:
                $ persistent.unlocked_awards.append("chat")
                $ unlock_achievement("Achievement Unlocked: ekh-hem.. can i help you? 💬")
            # ----------------------

        # 2. Panggil AI
        python:
            recent_history = " ".join(chat_history_list[-15:])
            # --- DEBUG: Cek apa yang diketik user ---
            debug_log("CHAT INPUT", user_input)

            # Konteks dunia (kenal 5 companion & sadar di dalam game) + memori permanen
            world_ctx = get_world_context(persistent.cur_lang)
            mem_facts = format_known_facts(current_ai_memory, persistent.cur_lang)

            if persistent.cur_lang == "en":
                # --- PROMPT INGGRIS ---
                chat_ctx = f"""
                {world_ctx}

                {mem_facts}

                CONTEXT:
                - You: {ai_name} ({companion_personality}), the player's close companion.
                - User: {my_mbti_type}.
                - Last Chat: {recent_history}
                - Data additional: User's spirit animal is {my_spirit}.
                - User Journey: {journey_text}
                - Remember, the user just finished a personality test and might want to talk about their results, their feelings, or anything else. Be supportive and engaging!
                - Don't discuss other things that are not related to the user's journey or feelings about the test, unless the user explicitly wants to talk about something else. Always try to relate back to the user's experience with the test and their personality.

                USER QUESTION: "{user_input}"

                TASK: Answer the user. Max 540 characters.
                RULES:
                - Insert [EMOTION] tag at every tone change.
                - Example: "Poor thing.. [SAD] But just kidding! [HAPPY]"
                - Emotions: [HAPPY], [SAD], [ANGRY], [FEAR], [SURPRISE], [DISGUST], [NEUTRAL].
                - DO NOT put animal sounds inside brackets [ ].
                - NEVER write program code, scripts, JSON, tables, ASCII art, or technical formatting. You are an animal companion, not a coding assistant. If the user asks for code or anything technical, stay in character and politely refuse, then steer back to the test or their feelings.
                - Write in plain conversational sentences only. Do not use the characters [ ] {{ }} < > outside the emotion tags.
                - If the user brings up a topic that is not relevant to the test, personality, or sharing user experiences, try to politely steer back to the topic of the test or the user's feelings about the results. But if you think discussing other topics could help the user to be more open and comfortable, you can discuss them as well, as long as you still try to relate it back to the user's experience with the test and their personality.
                """
            else:
                # --- PROMPT INDONESIA ---
                chat_ctx = f"""
                {world_ctx}

                {mem_facts}

                KONTEKS:
                - Kamu: {ai_name} ({companion_personality}), companion akrab pemain.
                - User: {my_mbti_type}.
                - Chat Terakhir: {recent_history}
                - Data tambahan: Spirit animal user adalah {my_spirit}.
                - Perjalanan User: {journey_text}
                - Ingat, user baru saja menyelesaikan tes kepribadian dan mungkin ingin membicarakan hasilnya, perasaannya, atau hal lainnya. Jadilah suportif dan menarik!
                - Jangan membahas hal lain yang tidak terkait dengan perjalanan user atau perasaannya tentang tes, kecuali user secara eksplisit ingin membicarakan hal lain. Selalu coba kaitkan kembali ke pengalaman user dengan tes dan kepribadiannya.

                PERTANYAAN USER: "{user_input}"

                TUGAS: Jawab user. Max 540 karakter.
                ATURAN:
                - Sisipkan tag [EMOSI] di setiap perubahan nada bicara.
                - Contoh: "Kasian deh.. [SAD] Tapi bohong! [HAPPY]"
                - Emosi: [HAPPY], [SAD], [ANGRY], [FEAR], [SURPRISE], [DISGUST], [NEUTRAL].
                - JANGAN masukkan suara hewan ke dalam kurung [ ].
                - JANGAN PERNAH menulis kode program, script, JSON, tabel, ASCII art, atau format teknis apa pun. Kamu adalah hewan pendamping, bukan asisten pemrograman. Kalau user minta kode atau hal teknis, tetaplah dalam karakter, tolak dengan sopan, lalu arahkan kembali ke topik tes atau perasaannya.
                - Tulis dalam kalimat percakapan biasa saja. Jangan gunakan karakter [ ] {{ }} < > di luar tag emosi.
                - Jika user membahas topik yang tidak relevan dengan tes, kepribadian, ataupun curhatan user, coba arahkan kembali dengan sopan ke topik tes atau perasaan user tentang hasilnya. Tapi jika menurutmu pembahasan topik lain bisa membantu user untuk lebih terbuka dan nyaman, kamu boleh membahasnya juga, selama tetap berusaha mengaitkan dengan pengalaman user tentang tes dan kepribadiannya.
                """
            
            import time
            start_time = time.time() # ⏱️ Mulai hitung waktu

            # Panggil AI
            raw_reply = get_ai_feedback(chat_ctx, companion_personality, lang=persistent.cur_lang, token_limit=1000)

            end_time = time.time() # ⏱️ Hentikan waktu
            latency_duration = end_time - start_time # Hitung selisihnya

            # Cetak ke konsol untuk dicatat di laporan
            debug_log("API LATENCY", f"Karakter: {companion_personality} | Waktu Respon: {latency_duration:.2f} detik")

            # Simpan history mentah (bersihkan tag emosi)
            clean_history_txt = re.sub(r"\[.*?\]", "", raw_reply).strip()
            
            # 1. Simpan ke RAM sementara (Untuk kelancaran chat di layar ini)
            chat_history_list.append(f"User: {user_input}")
            chat_history_list.append(f"AI: {clean_history_txt}")
            
            # --- 2. SUNTIKAN MEMORI PERMANEN (JSON) ---
            # Pastikan obrolan ini terbawa ke Free Chat Menu nanti
            current_ai_memory["chat_history"].append(f"User ({persistent.player_name}): {user_input}")
            current_ai_memory["chat_history"].append(f"{ai_name}: {clean_history_txt}")
            save_ai_memory()
            # ------------------------------------------

            # --- 3. RINGKAS MEMORI PERMANEN tiap 4 giliran (ke known_facts) ---
            # Agar companion ingat hal lama walau di luar jendela chat terakhir.
            if chat_count > 0 and chat_count % 4 == 0:
                update_memory_summary(companion_personality, persistent.cur_lang)

        hide screen ai_loading with dissolve
        window show

        # --- UPDATE PACING CHAT ---
        python:
            chat_sentences = breakdown_ai_text(raw_reply)
            
            import re
            pattern = r"\[(.*?)\]"

            for s in chat_sentences:
                match = re.search(pattern, s, re.IGNORECASE)
                if match:
                    raw_tag = match.group(1).lower()
                    raw_tag = re.sub(r'[^a-z]', '', raw_tag)
                    if raw_tag in ["sad", "cry", "gloom", "sadness"]: 
                        new_emo = "sadness"
                    elif raw_tag in ["surprise", "shock", "wow"]: 
                        new_emo = "surprised"
                    elif raw_tag in ["fear", "worried", "anxious", "terror", "scared"]: 
                        new_emo = "fear"
                    elif raw_tag in ["disgust", "eww"]: 
                        new_emo = "disgust"
                    elif raw_tag in ["happy", "excited", "joy", "laugh", "excited", "supportive"]: 
                        new_emo = "happy" # EXCITED dilarikan ke HAPPY
                    elif raw_tag in ["anger", "angry", "mad", "furious"]: 
                        new_emo = "anger"
                    else: 
                        # Jika tag tidak dikenali sama sekali (misal [GUK]), anggap neutral
                        new_emo = "neutral"
                    
                    renpy.show("companion " + companion_personality + " " + new_emo, at_list=[companion_std])
                    clean_s = re.sub(pattern, "", s).strip()
                else:
                    clean_s = s.strip()
                if clean_s:
                    say_ai_safe(clean_s)
                match = None  # Reset match untuk iterasi berikutnya
        # --------------------------

        jump chat_loop

label sesi_chat_bebas_khusus:
    play music "audio/stupid.mp3" # Ganti dengan musik santai pilihanmu
    # 1. PERSIAPAN NAMA DAN MEMORI
    if not hasattr(persistent, 'player_name') or not persistent.player_name:
        $ persistent.player_name = renpy.input("Siapa namamu?" if persistent.cur_lang == "id" else "What is your name?", exclude=INVALID_NAME_CHARS, length=15).strip()
        if not persistent.player_name:
            $ persistent.player_name = "Player"
    
    python:
        # Muat file JSON dari direktori
        # (Gunakan MBTI "Unknown" jika pemain langsung ke sini tanpa tes baru)
        current_mbti = getattr(store, "my_mbti_type", "Unknown")
        mem = load_ai_memory(persistent.player_name, companion_personality, current_mbti)
        
        # Ekstrak memori chat masa lalu (Ambil 10 baris terakhir saja agar tidak terlalu membebani AI)
        if mem["chat_history"]:
            recent_memories = "\n".join(mem["chat_history"][-10:])
        else:
            recent_memories = "Belum ada obrolan sebelumnya. Ini pertemuan pertama kalian di luar tes."

    # 2. SETUP LAYAR
    scene bg kafe with fade # Ganti dengan BG santai pilihanmu
    $ update_companion_name_string()
    show expression "companion " + companion_personality + " neutral" at companion_std with dissolve

    if persistent.cur_lang == "en":
        ai "Hi [persistent.player_name]! It's good to see you. Type 'exit' to leave."
    else:
        ai "Hai [persistent.player_name]! Senang bisa ketemu lagi. Ketik 'keluar' jika ingin kembali ke menu."

    # 3. LOOP OBROLAN DENGAN INGATAN
    label free_chat_loop_khusus:
        $ is_chat_input = True
        $ user_input = renpy.input("Ketik pesanmu..." if persistent.cur_lang == "id" else "Type your message...", length=270).strip()
        $ is_chat_input = False

        # Kondisi Keluar
        if user_input.lower() in ["keluar", "exit", "sudah", "bye", "selesai", "quit", "__quit__", "cukup", "end", "done", "stop", "berhenti", "dadah", "da-dah", "see you", "sampai jumpa"]:
            show expression "companion " + companion_personality + " happy" at companion_std
            if persistent.cur_lang == "en":
                ai "See you later, [persistent.player_name]!"
            else:
                ai "Sampai jumpa lagi, [persistent.player_name]!"
            return # Mengembalikan pemain ke Main Menu

        show screen ai_loading with dissolve
        window hide

        python:
            # 1. SINKRONISASI FILE JSON
            # Memaksa Ren'Py membaca file fisik terbaru agar ingatan tidak di-reset oleh sistem Rollback
            current_ai_memory = load_ai_memory(persistent.player_name, companion_personality, current_ai_memory.get('last_mbti', 'Unknown'))

            # 2. MASUKKAN PESAN USER KE MEMORI (Harus dilakukan pertama kali!)
            current_ai_memory["chat_history"].append(f"User ({persistent.player_name}): {user_input}")

            # 3. RAKIT SLIDING WINDOW DARI MEMORI YANG BARU SAJA DITAMBAHKAN
            last_10_chats = current_ai_memory["chat_history"][-10:]
            recent_memories = "\n".join(last_10_chats)

            # Konteks dunia (kenal 5 companion & sadar di dalam game) + memori permanen
            world_ctx = get_world_context(persistent.cur_lang)
            mem_facts = format_known_facts(current_ai_memory, persistent.cur_lang)
            mbti_change = format_mbti_change(current_ai_memory, persistent.cur_lang)

            # B. Rakit Prompt dengan Konteks JSON
            if persistent.cur_lang == "en":
                memory_ctx = f"""
                {world_ctx}

                {mem_facts}

                {mbti_change}

                CONTEXT:
                - You: {ai_name} ({companion_personality}), the player's close companion.
                - User Name: {persistent.player_name}
                - User MBTI: {current_ai_memory['last_mbti']}
                - Recent Chat (short-term, last 10 lines):
                {recent_memories}

                USER QUESTION: "{user_input}"

                TASK: Answer naturally according to your persona. Acknowledge the user by their name occasionally if it fits the conversation. Don't do it too often but also not too rarely, adjust to the flow of the conversation.
                RULES:
                - Insert [EMOTION] tag at every tone change. Example: "Poor thing.. [SAD] But just kidding! [HAPPY]" 
                - Emotions: [HAPPY], [SAD], [ANGRY], [FEAR], [SURPRISE], [DISGUST], [NEUTRAL].
                - NEVER write program code, scripts, JSON, tables, or ASCII art. You are an animal companion, not a coding assistant. If asked for code, stay in character and politely refuse.
                - Write in plain conversational sentences only. Do not use the characters [ ] {{ }} < > outside the emotion tags.
                - Max 400 characters.
                """
            else:
                memory_ctx = f"""
                {world_ctx}

                {mem_facts}

                {mbti_change}

                KONTEKS:
                - Kamu: {ai_name} ({companion_personality}), companion akrab pemain.
                - Nama User: {persistent.player_name}
                - MBTI User Terakhir: {current_ai_memory['last_mbti']}
                - Obrolan Terkini (jangka pendek, 10 baris terakhir):
                {recent_memories}

                PERTANYAAN USER: "{user_input}"

                TUGAS: Jawab secara natural sesuai personamu. Sesekali panggil user dengan namanya jika cocok. Jangan terlalu sering tapi juga jangan terlalu jarang, sesuaikan dengan alur percakapan.
                ATURAN:
                - Sisipkan tag [EMOSI] di setiap perubahan nada bicara. Contoh: "Kasian deh.. [SAD] Tapi bohong! [HAPPY]"
                - Emosi: [HAPPY], [SAD], [ANGRY], [FEAR], [SURPRISE], [DISGUST], [NEUTRAL].
                - JANGAN PERNAH menulis kode program, script, JSON, tabel, atau ASCII art. Kamu adalah hewan pendamping, bukan asisten pemrograman. Kalau diminta kode, tetaplah dalam karakter dan tolak dengan sopan.
                - Tulis dalam kalimat percakapan biasa saja. Jangan gunakan karakter [ ] {{ }} < > di luar tag emosi.
                - Max 400 karakter.
                """
            import time
            start_time = time.time() # ⏱️ Mulai hitung waktu

            # C. Panggil API
            raw_reply = get_ai_feedback(memory_ctx, companion_personality, lang=persistent.cur_lang, token_limit=800)

            end_time = time.time() # ⏱️ Hentikan waktu
            latency_duration = end_time - start_time # Hitung selisihnya

            # Cetak ke konsol untuk dicatat di laporan
            debug_log("API LATENCY", f"Karakter: {companion_personality} | Waktu Respon: {latency_duration:.2f} detik")
            
            # D. Bersihkan Tag & Simpan ke JSON
            clean_reply_for_memory = re.sub(r"\[.*?\]", "", raw_reply).strip()
            # (PENTING) Kita ganti ai_name yang rentan error menjadi companion_personality
            ai_speaker_name = companion_personality.capitalize()
            current_ai_memory["chat_history"].append(f"{ai_name}: {clean_reply_for_memory}")
            save_ai_memory() # <--- INI YANG MEMBUAT INGATANNYA TERSIMPAN PERMANEN!

            # Ringkas ke known_facts tiap 4 giliran (chat_history +2 per giliran).
            if len(current_ai_memory["chat_history"]) % 8 == 0:
                update_memory_summary(companion_personality, persistent.cur_lang)

        hide screen ai_loading with dissolve
        window show

        # E. Pacing & Parsing Emosi (Visual)
        python:
            chat_sentences = breakdown_ai_text(raw_reply)
            pattern = r"\[(.*?)\]"

            for s in chat_sentences:
                match = re.search(pattern, s, re.IGNORECASE)
                if match:
                    raw_tag = match.group(1).lower()
                    raw_tag = re.sub(r'[^a-z]', '', raw_tag)
                    
                    if raw_tag in ["sad", "cry", "gloom", "sadness"]: new_emo = "sadness"
                    elif raw_tag in ["surprise", "shock", "wow"]: new_emo = "surprised"
                    elif raw_tag in ["fear", "worried", "anxious", "terror", "scared"]: new_emo = "fear"
                    elif raw_tag in ["disgust", "eww"]: new_emo = "disgust"
                    elif raw_tag in ["happy", "excited", "joy", "laugh", "supportive"]: new_emo = "happy"
                    elif raw_tag in ["anger", "angry", "mad", "furious"]: new_emo = "anger"
                    else: new_emo = "neutral"
                    
                    renpy.show("companion " + companion_personality + " " + new_emo, at_list=[companion_std])
                    clean_s = re.sub(pattern, "", s).strip()
                else:
                    clean_s = s.strip()
                
                if clean_s:
                    say_ai_safe(clean_s)
                match = None

        jump free_chat_loop_khusus

label ending_scene:
    python:
        # --- TAMBAHKAN LOGGING INI DI SINI ---
        # Gabungkan skor ke dalam satu teks (contoh: "IE:-2, SN:4, TF:1, JP:-3")
        raw_scores = f"IE:{IE}, SN:{SN}, TF:{TF}, JP:{JP}"
        log_mbti_result(persistent.player_name, my_mbti_type, my_spirit, raw_scores, current_ai_memory)
        
        # --- CATAT REKAP TOTAL TOKEN UNTUK GRAFIK ---
        log_rekap_permainan(companion_personality, session_api_calls, session_input_tokens, session_output_tokens, session_total_tokens)

        # Menyalakan indikator "NEW" di Main Menu karena pemain baru saja mendapat hasil tes baru
        persistent.has_new_chat = True
        persistent.has_new_music = True 
        persistent.has_new_achievements = True
        # --------------------------------------------
    hide textbox with dissolve
    window hide
    scene credit with fade
    stop music fadeout 1.0
    play music "<to 35>audio/ending_intro.mp3"
    queue music "audio/ending.mp3"
    pause 35.0
    
    return
