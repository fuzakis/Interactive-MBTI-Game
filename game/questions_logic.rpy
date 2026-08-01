# --- HELPER FUNCTIONS ---
init python:
    import time
    import re

    # Batas aman panjang satu balon teks (karakter).
    # Respons normal AI dibatasi 270-540 karakter lewat prompt, tapi kalau AI
    # "kebablasan" (misal user minta kode program), teks tanpa tanda baca bisa
    # jadi satu blok raksasa yang meluber keluar textbox.
    MAX_SAY_CHARS = 300

    # Karakter yang TIDAK BOLEH ada di nama profil.
    # Alasannya dua, keduanya bikin game crash:
    #   1. '[' dan '{' -> Ren'Py memproses nama sebagai interpolasi/text tag
    #      saat ditampilkan di layar profil.
    #   2. \ / : * ? " < > | -> nama profil dipakai sebagai NAMA FILE memori AI
    #      (<nama>_<companion>.json), dan karakter ini ilegal di Windows.
    # Catatan: ini hanya mencegah nama BARU. Nama lama yang terlanjur nakal
    # tetap aman ditampilkan berkat safe_display_text().
    INVALID_NAME_CHARS = "{}[]\\/:*?\"<>|"

    def safe_display_text(value):
        """
        Escape teks BUATAN PEMAIN (nama profil, data dari file JSON save)
        sebelum ditampilkan lewat displayable Text di screen.

        Ren'Py menjalankan interpolasi pada string yang diberikan ke `text`,
        jadi nama profil "[test]" bikin layar profil CRASH
        (NameError: name 'test' is not defined), dan "Ani[" juga crash.

        PAKAI: text safe_display_text(p["name"])
        JANGAN: text "[nama_variabel]"  <- itu interpolasi literal, nilainya
        disisipkan SETELAH substitusi sehingga sudah aman dan tidak boleh
        di-escape (nanti '[[' malah terlihat mentah oleh pemain).
        """
        if not value:
            return ""
        return str(value).replace("[", "[[").replace("{", "{{")

    def sanitize_ai_text(text):
        """
        Benteng terakhir sebelum teks AI masuk ke renpy.say().

        Ren'Py memperlakukan '[' sebagai interpolasi variabel dan '{' sebagai
        text tag. Kalau teks AI mengandung kode program, keduanya membuat game
        CRASH atau teks termakan diam-diam. Contoh nyata (sudah diuji):
            "arr[i] = 5"  -> NameError: name 'i' is not defined  (CRASH)
            "arr[i"       -> Exception: ends with an open format (CRASH)
            "[]"          -> ValueError: expected expression      (CRASH)
            "data[0]"     -> tampil jadi "data0"   (teks hilang diam-diam)
            "if x {"      -> Exception: open text tag             (CRASH)
        Menggandakan jadi '[[' dan '{{' membuat Ren'Py menampilkannya sebagai
        karakter biasa.

        CATATAN: JANGAN pakai fungsi ini untuk teks yang ditampilkan lewat
        interpolasi screen (contoh: text "[detailed_mbti_explanation]"),
        karena di sana nilainya disisipkan SETELAH proses substitusi sehingga
        '[[' akan terlihat mentah oleh pemain.
        """
        if not text:
            return ""
        return text.replace("[", "[[").replace("{", "{{")

    def chunk_long_text(text, limit=MAX_SAY_CHARS):
        """Pecah teks kepanjangan di batas kata agar tidak meluber dari textbox."""
        text = text.strip()
        if len(text) <= limit:
            return [text] if text else []

        chunks = []
        sisa = text
        while len(sisa) > limit:
            potong = sisa.rfind(" ", 0, limit)
            if potong <= 0:  # satu kata super panjang (misal baris kode)
                potong = limit
            chunks.append(sisa[:potong].strip())
            sisa = sisa[potong:].strip()
        if sisa:
            chunks.append(sisa)
        return [c for c in chunks if c]

    def say_ai_safe(text):
        """Satu-satunya pintu menampilkan teks AI: disanitasi + dipenggal aman."""
        for potongan in chunk_long_text(sanitize_ai_text(text)):
            renpy.say(store.ai, potongan)


    # Fungsi memecah teks AI menjadi list kalimat
    def breakdown_ai_text(text):
        if not text: return []
        # AI sering mengirim beberapa paragraf, masing-masing dibungkus tanda
        # kutip ("..."). Kalau langsung di-split, kutip pembuka paragraf
        # berikutnya ikut menempel di kalimat sebelumnya (bug: muncul tanda "
        # yatim dan baris kosong panjang di textbox/history).
        # Solusi: proses per baris dulu, buang kutip pembungkusnya.
        sentences = []
        for line in text.splitlines():
            line = line.strip().strip('"').strip()
            if not line:
                continue
            # Regex ini memecah teks setiap ketemu Titik, Seru, atau Tanya
            # (boleh diikuti tanda kutip penutup), namun tetap mempertahankan
            # tanda bacanya. Juga memecah sebelum tag [EMOSI].
            # Elipsis (...) TIDAK memecah kalimat, karena AI memakainya
            # sebagai jeda dramatis di tengah kalimat.
            parts = re.split(r'(?<=[.!?])(?<!\.\.\.)"?\s+|(?=\[)', line)
            for p in parts:
                p = p.strip().strip('"').strip()
                if p:
                    sentences.append(p)
        return sentences

# --- Label PENGACAKAN ---
label start_test_session:
    #play music "audio/sus.mp3" fadein 1.0
    show screen quest_shuffle with dissolve

    # Show a transparent black box with white text for the continue prompt
    if persistent.cur_lang == "en":
        show screen continue_prompt("Click anywhere to continue")
    else:
        show screen continue_prompt("Klik di mana saja untuk melanjutkan")
            
    hide screen quest_shuffle with dissolve
    
    if persistent.cur_lang == "en":
        n "System is selecting a random question packet..."
    else:
        n "Sistem sedang memilih paket soal secara acak..."

    hide screen continue_prompt with dissolve

    # 1. Pilih paket (acak, hindari yang sudah pernah dikerjakan)
    python:
        import time
        start_time = time.time() # Stopwatch Ditekan!
        
        # Inisialisasi persistent.used_packet_titles jika belum ada
        if not hasattr(persistent, 'used_packet_titles') or persistent.used_packet_titles is None:
            persistent.used_packet_titles = []

        # Buat list index paket yang belum pernah dikerjakan
        available_indexes = [i for i, title in enumerate(all_packet_titles) if title not in persistent.used_packet_titles]
        debug_log("Available packet indexes", str(available_indexes))
        debug_log("Used packet titles before", str(persistent.used_packet_titles))
        if not available_indexes:
            # Jika semua sudah pernah dikerjakan, simpan judul terakhir lalu reset used_packet_titles
            debug_log("All packets used, resetting used_packet_titles", "RESET")
            if hasattr(persistent, 'last_packet_title') and persistent.last_packet_title:
                last_title = persistent.last_packet_title
            elif persistent.used_packet_titles:
                last_title = persistent.used_packet_titles[-1]
            else:
                last_title = None
            persistent.used_packet_titles = []
            available_indexes = list(range(len(all_packet_titles)))
            # Jika ada judul terakhir, exclude dari available_indexes untuk satu kali pengacakan
            if last_title and last_title in all_packet_titles:
                last_idx = all_packet_titles.index(last_title)
                available_indexes = [i for i in available_indexes if i != last_idx]
                debug_log("Excluding last packet title from first pick after reset", str(last_title))

        # Pilih index paket secara acak
        selected_index = renpy.random.choice(available_indexes)
        selected_packet = all_packets[selected_index]
        selected_title = all_packet_titles[selected_index]
        debug_log("Selected packet title", str(selected_title))

        # Simpan judul paket yang dipilih ke persistent.used_packet_titles
        persistent.used_packet_titles.append(selected_title)
        
        # Simpan judul paket terakhir ke persistent.last_packet_title
        persistent.last_packet_title = selected_title
        debug_log("Used packet titles after", str(persistent.used_packet_titles))
        debug_log("Last packet title", str(persistent.last_packet_title))
    
    # 2. Salin & Acak
    python:
        current_question_list = selected_packet[:]
        t = int(time.time() * 1000)
        for i in range(len(current_question_list)-1, 0, -1):
            t = (t * 9301 + 49297) % 233280  # simple LCGS
            
            j = t % (i + 1)
            current_question_list[i], current_question_list[j] = current_question_list[j], current_question_list[i]
        debug_log("Shuffled question order", str(current_question_list))
    
    # RESET PROGRESS
    $ question_progress = 0
    
    # TAMPILKAN INDICATOR SCREEN
    
    show screen progress_indicator

    jump ask_next_question

# --- LABEL LOOP UTAMA (Harus Bersih) ---
label ask_next_question:
    # 1. Cek sisa soal
    if not current_question_list:
        hide screen progress_indicator
        jump scene_hasil_tes

    # 2. Update Progress
    $ question_progress += 1
    $ (current_question_id, dimension) = current_question_list.pop()

    # 3. Panggil Soal
    # Di dalam label inilah (hasil generate) pemanggilan 'ai_react_logic' terjadi
    call expression "show_question_" + current_question_id + "_" + persistent.cur_lang from _call_expression

    # 4. Loop kembali
    # PERHATIKAN: TIDAK ADA LAGI KODE PYTHON AI DISINI
    jump ask_next_question


# --- LABEL HELPER (Tempat Logika AI Disimpan) ---
label ai_react_logic:
    # Indikator Loading
    window hide
    show screen ai_loading with dissolve
    
    python:
        update_companion_name_string()
        
        # --- NEW: MBTI SCORING DEBUG LOGGER ---
        # This will print the running total of the MBTI scores to your console
        debug_log("MBTI SCORE TRACKER", f"Current Total -> IE (Intro/Extro): {IE} | SN (Sens/Intui): {SN} | TF (Think/Feel): {TF} | JP (Judge/Perc): {JP}")
        # --------------------------------------
        if persistent.cur_lang == "en":
            ctx = f"""
            SITUATION: {narasi_asli}
            PAST Situation Recap: {', '.join(user_journey_summary[-5:])} (only the last 5 for context)
            
            PLAYER ACTION:
            Player chose option: "{user_choice_text}"
            (MBTI Analysis of this choice: {last_answer})
            The player did NOT choose this other option: "{unchosen_choice_text}"
            (MBTI Analysis of the rejected option: {unchosen_answer})

            INSTRUCTION:
            Give your reaction to the PLAYER ACTION above.
            Does the action "{user_choice_text}" make sense according to your personality ({companion_personality})?
            You may briefly weigh it against the option they rejected: from YOUR OWN character's instincts and values, which one would you have leaned toward, and why?
            Neither option is objectively right or wrong (both are valid), so judge only by your persona's taste, never as morality or a correct answer. Keep it light, do not lecture.
            Do not focus too much on the MBTI label, but comment on the content of the action itself.
            Try to keep the continuation of the conversation from the previous situation,
            so it feels like a natural conversation flow, and not just separate questions and answers.

            RULES:
            - Insert [EMOTION] tag at every tone change. Only use the provided emotions tags!
            - Correct Example: "Wow I agree! [HAPPY] But be careful.. [FEAR]"
            - Wrong Example: "Wow i really looking forward to it! (EXCITED) But there is something that we need to think it properly.. (ANXIOUS)"
            - Available emotions tags: [HAPPY], [SAD], [ANGRY], [FEAR], [SURPRISE], [DISGUST], [NEUTRAL].
            - DO NOT put animal sounds inside the brackets [ ], for example: [WOOF], [MEOW], and other sounds.
            - Make sure to not include ("role":"character name","content":...) in your response, just give the raw text with emotion tags.
            - Max 270 characters.
            """
        else:
            # --- VERSI INDONESIA ---
            ctx = f"""
            SITUASI: {narasi_asli}
            Rekap Situasi Masa Lalu: {', '.join(user_journey_summary[-5:])} (hanya 5 terakhir untuk konteks)
            
            TINDAKAN PEMAIN:
            Pemain memilih opsi: "{user_choice_text}"
            (Analisis MBTI dari pilihan ini: {last_answer})
            Pemain TIDAK memilih opsi yang satunya: "{unchosen_choice_text}"
            (Analisis MBTI dari opsi yang ditolak: {unchosen_answer})

            INSTRUKSI:
            Berikan reaksimu terhadap TINDAKAN PEMAIN di atas.
            Apakah tindakan "{user_choice_text}" itu masuk akal menurut kepribadianmu ({companion_personality})?
            Kamu boleh membandingkannya sedikit dengan opsi yang ditolak: menurut naluri dan nilai KARAKTERMU sendiri, mana yang lebih kamu condongi, dan kenapa?
            Tidak ada opsi yang benar atau salah secara objektif (keduanya sah), jadi nilai hanya dari selera personamu, bukan sebagai moralitas atau jawaban yang benar. Santai saja, jangan menggurui.
            Jangan terlalu terpaku pada label MBTI-nya, tapi komentari isi tindakannya.
            Cobalah untuk menjaga kelanjutan percakapan dari situasi sebelumnya, sehingga terasa seperti alur percakapan yang alami, dan bukan hanya soal dan jawaban yang terpisah.

            ATURAN:
            - Sisipkan tag [EMOSI] di setiap perubahan nada bicara. Hanya gunakan tag emosi yang sudah disediakan!
            - Contoh Benar: "Wah aku setuju! [HAPPY] Tapi hati-hati ya.. [FEAR]"
            - Contoh Salah: "Wah aku sangat menantikan hal itu! (EXCITED) Tapi ada sesuatu yang perlu kita pikirkan dengan baik.. (ANXIOUS)"
            - Tag emosi yang tersedia: [HAPPY], [SAD], [ANGRY], [FEAR], [SURPRISE], [DISGUST], [NEUTRAL].
            - JANGAN masukkan suara hewan ke dalam kurung [ ], contohnya seperti: [GUK], [MEONG], dan suara lainnya.
            - Pastikan untuk tidak menyertakan ("role":"nama karakter","content":...) dalam responsmu, cukup berikan teks mentah dengan tag emosi saja.
            - Maksimal 270 karakter.
            """

        import time
        start_time = time.time() # ⏱️ Mulai hitung waktu

        # 2. PANGGIL AI
        ai_full = get_ai_feedback(ctx, companion_personality, lang=persistent.cur_lang)

        end_time = time.time() # ⏱️ Hentikan waktu
        latency_duration = end_time - start_time # Hitung selisihnya

        # Cetak ke konsol untuk dicatat di laporan
        debug_log("API LATENCY", f"Karakter: {companion_personality} | Waktu Respon: {latency_duration:.2f} detik")
        debug_log("AI RAW RESPONSE", ai_full)

    # 3. TAMPILKAN
    hide screen ai_loading with dissolve
    window show
    
    # Set Emosi Awal (Safety Net: Neutral dulu)
    $ current_emo = "neutral"
    show expression "companion " + companion_personality + " neutral" at companion_std
    
    # Loop untuk menampilkan kalimat satu per satu
    python:
        # Pecah teks AI menjadi list kalimat
        sentence_list = breakdown_ai_text(ai_full)

        import re
        pattern = r"\[(.*?)\]"

        for sentence in sentence_list:
            match = re.search(pattern, sentence, re.IGNORECASE)
            
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
                    new_emo = "happy"
                elif raw_tag in ["anger", "angry", "mad", "furious"]: 
                    new_emo = "anger"
                else: 
                    new_emo = "neutral"
                
                # B. UPDATE GAMBAR (Hanya jika emosi berubah)
                if new_emo != current_emo:
                    current_emo = new_emo
                    # Fungsi renpy.show via python
                    renpy.show("companion " + companion_personality + " " + current_emo, at_list=[companion_std])
                
                # C. Bersihkan tag dari teks agar tidak terbaca user
                clean_sentence = re.sub(pattern, "", sentence).strip()
            else:
                # Jika tidak ada tag, gunakan emosi terakhir (tidak berubah)
                clean_sentence = sentence.strip()

            # D. Tampilkan Teks Bersih
            if clean_sentence: # Cek biar gak nampilin balon kosong
                say_ai_safe(clean_sentence)
            match = None  # Reset match untuk iterasi berikutnya
    
    return