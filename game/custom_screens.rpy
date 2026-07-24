init python:
    import time
    import os
    import json

    # --- KAMUS NAMA KARAKTER ---
    # Ubah bagian kanan dengan nama karakter yang sesuai dengan game-mu
    companion_names = {
        "extraversion": "Iwank (Anjing)",
        "openness": "Kitsuko (Rubah)",
        "neuroticism": "Jakouko (Luwak)",
        "conscientiousness": "Onyen (Kucing)",
        "agreeableness": "Susagi (Kelinci)"
    }
    
    # List untuk menyimpan notifikasi yang sedang aktif
    active_achievements = []

    def unlock_achievement(title, icon_path="images/award_locked.png"):
        # Tambahkan ke daftar dengan waktu kadaluarsa (Tampil selama 5 detik)
        expire_time = time.time() + 5.0
        active_achievements.append({"title": title, "icon": icon_path, "expire": expire_time})
        
        # Panggil layarnya
        renpy.show_screen("steam_achievement_overlay")
        renpy.restart_interaction()

    # Fungsi untuk membersihkan notifikasi yang sudah lewat 5 detik
    def clean_achievements():
        global active_achievements
        current_time = time.time()
        
        # Saring hanya yang belum kadaluarsa
        new_list = [a for a in active_achievements if current_time < a["expire"]]
        
        if len(new_list) != len(active_achievements):
            active_achievements = new_list
            renpy.restart_interaction()
            
        if not active_achievements:
            renpy.hide_screen("steam_achievement_overlay")

    def get_companions_for_player(target_name):
        comp_list = []
        try:
            for filename in os.listdir(renpy.config.savedir):
                if filename.endswith(".json"):
                    filepath = os.path.join(renpy.config.savedir, filename)
                    with open(filepath, "r") as f:
                        data = json.load(f)
                    
                    if data.get("player_name") == target_name:
                        # 1. Coba ambil dari variabel yang benar (companion_personality)
                        # Pakai fallback "companion_type" atau "companion" jaga-jaga kalau namanya beda
                        raw_comp = data.get("companion_id")
                        
                        # 2. Terjemahkan trait menjadi nama karakter
                        if raw_comp:
                            raw_comp_lower = str(raw_comp).lower()
                            # Cocokkan dengan kamus
                            display_name = companion_names.get(raw_comp_lower, raw_comp.capitalize()) 
                        else:
                            display_name = "Karakter Misterius"
                            
                        comp_list.append({"file": filepath, "animal": display_name})
        except Exception as e:
            print("Error membaca file json:", e)
            pass
            
        return comp_list

    # Fungsi eksekutor hapus spesifik
    def delete_specific_file(filepath):
        if os.path.exists(filepath):
            os.remove(filepath)
        renpy.restart_interaction()

    # Fungsi eksekutor hapus semua (Sapu Bersih)
    def delete_all_for_player(target_name):
        try:
            for filename in os.listdir(renpy.config.savedir):
                if filename.endswith(".json"):
                    filepath = os.path.join(renpy.config.savedir, filename)
                    with open(filepath, "r") as f:
                        data = json.load(f)
                    if data.get("player_name") == target_name:
                        os.remove(filepath)
        except:
            pass
        renpy.restart_interaction()

screen mbti_result_diagram():
    modal True
    
    # Frame Utama (Kotak Tengah)
    frame:
        xalign 0.5
        yalign 0.5
        xsize 800
        ysize 725
        padding (40, 40)
        
        vbox:
            spacing 20
            xfill True # Isi lebar penuh
            
            # HEADER: Tipe Kepribadian
            vbox:
                xalign 0.5
                spacing 50
                text ("Your personality Type:" if persistent.cur_lang == "en" else "Jenis Kepribadianmu:"):
                    size 30 xalign 0.5 color "#aaa"
                text "[my_mbti_type]" size 80 xalign 0.5 bold True color "#fff" outlines [(2, "#000", 0, 0)]
                null height 20
            
            # BAGIAN DIAGRAM (4 Baris)
            # Baris 1: IE
            hbox:
                xalign 0.5
                spacing 20
                text "[txt_ie] ([res_ie])" min_width 200 xalign 1.0 yalign 0.5 size 24
                # Bar Score (Range 0 sampai 100)
                bar value val_ie range 100 xsize 300 ysize 30 yalign 0.5 left_bar "#4CAF50" right_bar "#555"
                text "{:.0f}%".format(val_ie) min_width 50 yalign 0.5 size 20 color "#ccc"

            # Baris 2: SN
            hbox:
                xalign 0.5
                spacing 20
                text "[txt_sn] ([res_sn])" min_width 200 xalign 1.0 yalign 0.5 size 24
                bar value val_sn range 100 xsize 300 ysize 30 yalign 0.5 left_bar "#2196F3" right_bar "#555"
                text "{:.0f}%".format(val_sn) min_width 50 yalign 0.5 size 20 color "#ccc"

            # Baris 3: TF
            hbox:
                xalign 0.5
                spacing 20
                text "[txt_tf] ([res_tf])" min_width 200 xalign 1.0 yalign 0.5 size 24
                bar value val_tf range 100 xsize 300 ysize 30 yalign 0.5 left_bar "#FF9800" right_bar "#555"
                text "{:.0f}%".format(val_tf) min_width 50 yalign 0.5 size 20 color "#ccc"

            # Baris 4: JP
            hbox:
                xalign 0.5
                spacing 20
                text "[txt_jp] ([res_jp])" min_width 200 xalign 1.0 yalign 0.5 size 24
                bar value val_jp range 100 xsize 300 ysize 30 yalign 0.5 left_bar "#9C27B0" right_bar "#555"
                text "{:.0f}%".format(val_jp) min_width 50 yalign 0.5 size 20 color "#ccc"
            
            null height 25
            
            textbutton ("🔍 Lihat Lebih Detil" if persistent.cur_lang == "id" else "🔍 View Details"):
                action Show("mbti_detail_popup") # Show tidak akan menutup layar utama
                xalign 0.5
                text_size 25
                text_color "#484270"
                text_hover_color "#a4ff9c"

            # TOMBOL LANJUT
            textbutton ("Continue" if persistent.cur_lang == "en" else "Lanjut"):
                action Return() xalign 0.5 padding (20, 10) text_size 30 background "#333" hover_background "#555"

screen progress_indicator():
    zorder 100 # Agar selalu di atas
    frame:
        xalign 0.05 # Pojok kiri atas
        yalign 0.05
        background "#00000088" # Hitam transparan
        padding (10, 5)

        text ("Questions: [question_progress] / 20" if persistent.cur_lang == "en" else "Soal: [question_progress] / 20") size 24 color "#fff"

screen companion_hud():
    # Agar tidak menutupi game, tapi tetap bisa diklik
    zorder 50 
    
    # Wadah di pojok kanan bawah
    frame:
        background None # Transparan
        xalign 0.95
        yalign 0.95
        
        # Tombol berupa Gambar Karakter
        imagebutton:
            # Idle = Gambar diam
            idle At("companion " + companion_personality + " neutral", Transform(zoom=0.2)) 
            # Hover = Gambar saat mouse di atasnya (bisa ganti ekspresi happy)
            hover At("companion " + companion_personality + " happy", Transform(zoom=0.22))
            
            # Aksi saat diklik (Misal muncul bantuan)
            action Call("ai_bantuan_logic")
            
            # Tooltip saat di-hover
            tooltip ("Need Help?" if persistent.cur_lang == "en" else "Butuh bantuan?")
            
    # Menampilkan Tooltip (Balon Kata)
    $ tooltip = GetTooltip()
    if tooltip:
        frame:
            background "images/speech_bubble.png" # Siapkan gambar balon kata
            xalign 0.85 yalign 0.85 # Muncul di dekat karakter
            text "[tooltip]" color "#000"

screen companion_selection_screen():
    modal True # Mencegah interaksi dengan background
    
    # Background khusus screen (Opsional, bisa pakai solid color atau gambar)
    add "#000000AA" # Hitam transparan 

    # Variabel untuk melacak tombol mana yang sedang di-hover
    default hovered_btn = ""
    
    vbox:
        align (0.5, 0.5)
        spacing 30
        
        # 1. JUDUL DINAMIS (Pakai logika langsung di dalam teks)
        text ("Choose Your Travel Companion" if persistent.cur_lang == "en" else "Pilih Teman Perjalananmu"):
            size 50 color "#fff" xalign 0.5 bold True outlines [(2, "#000", 0, 0)]

        hbox:
            spacing 20
            xalign 0.5
            yalign 0.5
            
            # --- PILIHAN 4: OPENNESS (RUBAH) ---
            button:
                action [SetVariable("companion_personality", "openness"), Return()]
                hovered SetScreenVariable("hovered_btn", "openness")
                unhovered SetScreenVariable("hovered_btn", "")
                
                vbox:
                    spacing 10
                    $ exp_state = "happy" if hovered_btn == "openness" else "neutral"
                    $ z_level = 0.22 if hovered_btn == "openness" else 0.21
                    
                    fixed:
                        xsize 330 
                        ysize 400 # Sudah disesuaikan pas dengan ukuran 4000 * 0.22
                        xalign 0.5
                        
                        add "companion openness [exp_state]":
                            align (0.5, 1.0) 
                            zoom z_level
                    
                    # Posisi teks sekarang di LUAR fixed, jadi akan rapi di bawah gambar
                    text ("Kitsuko\n(Openness)" if persistent.cur_lang == "en" else "Kitsuko\n(Openness)"):
                        size 24 color ("#a4ff9c" if hovered_btn == "openness" else "#ffffff") xalign 0.65 text_align 0.5

            # --- PILIHAN 2: CONSCIENTIOUSNESS (KUCING) ---
            button:
                action [SetVariable("companion_personality", "conscientiousness"), Return()]
                hovered SetScreenVariable("hovered_btn", "conscientiousness")
                unhovered SetScreenVariable("hovered_btn", "")
                
                vbox:
                    spacing 10
                    $ exp_state = "happy" if hovered_btn == "conscientiousness" else "neutral"
                    $ z_level = 0.22 if hovered_btn == "conscientiousness" else 0.21

                    fixed:
                        xsize 330 
                        ysize 400 
                        xalign 0.5
                        
                        add "companion conscientiousness [exp_state]":
                            align (0.5, 1.0) 
                            zoom z_level
                        
                    text ("Onyen\n(Conscientiousness)" if persistent.cur_lang == "en" else "Onyen\n(Conscientiousness)"):
                        size 24 color ("#a4ff9c" if hovered_btn == "conscientiousness" else "#ffffff") xalign 0.8 text_align 0.5
                    
            # --- PILIHAN 1: EXTRAVERSION (ANJING) ---
            button:
                action [SetVariable("companion_personality", "extraversion"), Return()]
                hovered SetScreenVariable("hovered_btn", "extraversion")
                unhovered SetScreenVariable("hovered_btn", "")
                
                vbox:
                    spacing 10
                    $ exp_state = "happy" if hovered_btn == "extraversion" else "neutral"
                    $ z_level = 0.22 if hovered_btn == "extraversion" else 0.21
                    
                    fixed:
                        xsize 330 
                        ysize 400 
                        xalign 0.5
                        
                        add "companion extraversion [exp_state]":
                            align (0.5, 1.0) 
                            zoom z_level
                            
                    text ("Iwank\n(Extraversion)" if persistent.cur_lang == "en" else "Iwank\n(Extraversion)"):
                        size 24 color ("#a4ff9c" if hovered_btn == "extraversion" else "#ffffff") xalign 0.72 text_align 0.5
                        
            # --- PILIHAN 5: AGREEABLENESS (KELINCI) ---
            button:
                action [SetVariable("companion_personality", "agreeableness"), Return()]
                hovered SetScreenVariable("hovered_btn", "agreeableness")
                unhovered SetScreenVariable("hovered_btn", "")
                
                vbox:
                    spacing 10
                    $ exp_state = "happy" if hovered_btn == "agreeableness" else "neutral"
                    $ z_level = 0.22 if hovered_btn == "agreeableness" else 0.21
                    
                    fixed:
                        xsize 330 
                        ysize 400 
                        xalign 0.5
                        
                        add "companion agreeableness [exp_state]":
                            align (0.5, 1.0) 
                            zoom z_level
                            
                    text ("Susagi\n(Agreeableness)" if persistent.cur_lang == "en" else "Susagi\n(Agreeableness)"):
                        size 24 color ("#a4ff9c" if hovered_btn == "agreeableness" else "#ffffff") xalign 0.71 text_align 0.5

            # --- PILIHAN 3: NEUROTICISM (LUWAK) ---
            button:
                action [SetVariable("companion_personality", "neuroticism"), Return()]
                hovered SetScreenVariable("hovered_btn", "neuroticism")
                unhovered SetScreenVariable("hovered_btn", "")
                
                vbox:
                    spacing 10
                    $ exp_state = "fear" if hovered_btn == "neuroticism" else "neutral"
                    $ z_level = 0.22 if hovered_btn == "neuroticism" else 0.21
                    
                    # Jakouko sekarang sudah masuk kotak fixed!
                    fixed:
                        xsize 330 
                        ysize 400 
                        xalign 0.5
                        
                        add "companion neuroticism [exp_state]":
                            align (0.5, 1.0) 
                            zoom z_level
                            
                    text ("Jakouko\n(Neuroticism)" if persistent.cur_lang == "en" else "Jakouko\n(Neuroticism)"):
                        size 24 color("#a4ff9c" if hovered_btn == "neuroticism" else "#ffffff") xalign 0.7 text_align 0.5

    text ("Click on a companion to select them!" if persistent.cur_lang == "en" else "Klik pada teman untuk memilih!") size 20 color "#aaa" xalign 0.5 yalign 0.8

screen ai_loading():
    modal True
    zorder 200 # Pastikan di atas semua screen lainnya
    
    # Background transparan
    add "#00000088"
    
    vbox:
        align (0.5, 0.5)
        spacing 20
        
        # Indikator Loading (Bisa diganti dengan animasi GIF atau image lain)
        text ("AI is thinking..." if persistent.cur_lang == "en" else "AI sedang berpikir..."):
            size 30 color "#fff" xalign 0.5 bold True outlines [(2, "#000", 0, 0)]
        
        # Bisa tambahkan animasi loading di sini jika ada
        # Contoh: add "images/loading_spinner.gif" xalign 0.5

screen quest_shuffle():
    modal True
    zorder 200 # Pastikan di atas semua screen lainnya
    
    # Background transparan
    add "#00000088"
    
    vbox:
        align (0.5, 0.5)
        spacing 20
        
        # Indikator Loading (Bisa diganti dengan animasi GIF atau image lain)
        text ("Shuffling questions..." if persistent.cur_lang == "en" else "Mengacak soal..."):
            size 30 color "#fff" xalign 0.5 bold True outlines [(2, "#000", 0, 0)]
        
        # Bisa tambahkan animasi loading di sini jika ada
        # Contoh: add "images/loading_spinner.gif" xalign 0.5

# --- SCREEN FOR CONTINUE PROMPT ---
screen continue_prompt(message):
    frame background Frame(Solid("#00000080"), 10, 10):
        align (0.5, 0.5)
        text "[message]" color "#FFFFFF" size 20

screen achievements_screen():
    tag menu
    python:
        persistent.has_new_achievements = False # Reset notifikasi saat membuka screen ini

    use game_menu(_("Achievements" if persistent.cur_lang == "en" else "Pencapaian"), scroll=None): 
        
        vbox:
            spacing 20
            xalign 0.5
            ypos 10
            
            text (_("Achievement Gallery") if persistent.cur_lang == "en" else _("Galeri Pencapaian")) size 45 color "#484270" bold True xalign 0.5
            
            # --- TAB NAVIGASI ---
            hbox:
                xalign 0.5
                spacing 50
                
                # Tab 1: MBTI
                textbutton _("Spirit Animals (MBTI)" if persistent.cur_lang == "en" else "Hewan Spiritual (MBTI)"):
                    action SetVariable("achievement_tab", "mbti")
                    text_size 25
                    # Warna berubah jika sedang aktif
                    text_color ("#484270" if achievement_tab == "mbti" else "#aaaaaa")
                    
                # Tab 2: General Awards
                textbutton _("General Awards" if persistent.cur_lang == "en" else "Penghargaan Umum"):
                    action SetVariable("achievement_tab", "awards")
                    text_size 25
                    text_color ("#484270" if achievement_tab == "awards" else "#aaaaaa")

            null height 10

            # ==========================================
            # KONDISI 1: JIKA TAB MBTI YANG DIPILIH
            # ==========================================
            if achievement_tab == "mbti":
                # (Taruh logika matematika halaman start_idx dan vpgrid 3x2 MBTI kamu di sini persis seperti yang kemarin!)
                
                $ start_idx = achievement_page * 6
                $ end_idx = start_idx + 6
                $ current_items = all_mbti_achievements[persistent.cur_lang][start_idx:end_idx]

                grid 3 2:
                    spacing 100
                    xalign 0.5
                    for mbti_id, mbti_title in current_items:
                        vbox:
                            spacing 5
                            xalign 0.5
                            if mbti_id in persistent.unlocked_mbti:
                                add "images/achieve_" + mbti_id.lower() + ".png" zoom 0.5 xalign 0.5
                                text "[mbti_title]\n([mbti_id])" size 20 color "#484270" xalign 0.5 text_align 0.5 bold True
                            else:
                                add "images/achieve_locked.png" zoom 0.25 xalign 0.5
                                text (_("???\n(Locked)") if persistent.cur_lang == "en" else _("???\n(Terkunci)")) size 20 color "#aaaaaa" xalign 0.5 text_align 0.5

                    for i in range(6 - len(current_items)):
                        null width 200 height 180

                null height 10
                
                # Navigasi Halaman MBTI (< 1/3 >)
                hbox:
                    xalign 0.5
                    spacing 80
                    textbutton "<":
                        action SetVariable("achievement_page", max(0, achievement_page - 1))
                        text_size 50
                        text_color ("#484270" if achievement_page > 0 else "#cccccc")
                    text (_("Page [achievement_page + 1] / 3") if persistent.cur_lang == "en" else _("Halaman [achievement_page + 1] / 3")) size 30 color "#484270" yalign 0.5
                    textbutton ">":
                        action SetVariable("achievement_page", min(2, achievement_page + 1))
                        text_size 50
                        text_color ("#484270" if achievement_page < 2 else "#cccccc")

            # ==========================================
            # KONDISI 2: JIKA TAB GENERAL AWARDS DIPILIH
            # ==========================================
            else:
                # Karena total ada 9 Awards, kita buat 2 halaman (Hal 1: 6, Hal 2: 3)
                $ start_idx_gen = general_page * 6
                $ end_idx_gen = start_idx_gen + 6
                $ current_gen_items = all_general_awards[persistent.cur_lang][start_idx_gen:end_idx_gen]

                grid 3 2:
                    spacing 60
                    xalign 0.5
                    for award_id, award_title in current_gen_items:
                        vbox:
                            spacing 5
                            xalign 0.5
                            if award_id in persistent.unlocked_awards:
                                # Jika dapat, panggil gambar misal: images/award_dog.png
                                add "images/award_" + award_id + ".png" zoom 1 xalign 0.5
                                text "[award_title]" size 20 color "#484270" xalign 0.5 text_align 0.5 bold True
                            else:
                                add "images/award_locked.png" zoom 0.25 xalign 0.5
                                text (_("???\n(Locked)") if persistent.cur_lang == "en" else _("???\n(Terkunci)")) size 20 color "#aaaaaa" xalign 0.5 text_align 0.5

                    for i in range(6 - len(current_gen_items)):
                        null width 200 height 200

                null height 20
                
                # Navigasi Halaman General (< 1/2 >)
                hbox:
                    xalign 0.5
                    spacing 80
                    textbutton "<":
                        action SetVariable("general_page", max(0, general_page - 1))
                        text_size 50
                        text_color ("#484270" if general_page > 0 else "#cccccc")
                    text (_("Page [general_page + 1] / 2") if persistent.cur_lang == "en" else _("Halaman [general_page + 1] / 2")) size 30 color "#484270" yalign 0.5
                    textbutton ">":
                        action SetVariable("general_page", min(1, general_page + 1))
                        text_size 50
                        text_color ("#484270" if general_page < 1 else "#cccccc")

screen music_room_screen():
    tag menu
    python:
        persistent.has_new_music = False # Reset notifikasi saat membuka screen ini
    
    # Memakai template game_menu agar background dan tata letaknya seragam
    use game_menu(_("Music Room" if persistent.cur_lang == "en" else "Ruang Musik")):
        
        vbox:
            spacing 30
            xalign 0.5
            ypos 20
            
            text (_("BGM Gallery") if persistent.cur_lang == "en" else _("Galeri BGM")) size 45 color "#484270" bold True xalign 0.5
            
            # Tombol untuk mematikan musik
            textbutton (_("⏹ Stop Music") if persistent.cur_lang == "en" else _("⏹ Hentikan Musik")):
                action Stop("music")
                xalign 0.5
                text_size 25
                text_color "#ff6b6b" # Warna merah pastel
                text_hover_color "#ffaaaa"

            null height 20

            # --- DAFTAR LAGU ---
            vbox:
                spacing 25
                xalign 0.5
                
                # Looping membaca database lagu
                for track_id, name_en, name_id, file_path, req_award in music_tracks:
                    
                    # 1. Cek Bahasa
                    $ track_name = name_en if persistent.cur_lang == "en" else name_id
                    
                    # 2. Cek apakah lagu terbuka (Jika syarat kosong ATAU syarat ada di memory award)
                    $ is_unlocked = (req_award == "") or (req_award in persistent.unlocked_awards)
                    
                    if is_unlocked:
                        # Jika Terbuka: Tampilkan tombol Play
                        hbox:
                            spacing 15
                            xalign 0.0 # Rata Kiri
                            
                            textbutton "▶ [track_name]":
                                action Play("music", file_path)
                                text_size 30
                                text_color "#484270"
                                text_hover_color "#a4ff9c" # Hijau terang saat di-hover
                    else:
                        # Jika Terkunci: Tampilkan teks abu-abu
                        hbox:
                            spacing 15
                            xalign 0.0
                            
                            text (_("🔒 ??? (Locked)") if persistent.cur_lang == "en" else _("🔒 ??? (Terkunci)")) size 30 color "#aaaaaa"

screen free_chat_hub():
    tag menu
    python:
        persistent.has_new_chat = False # Reset notifikasi saat membuka screen ini
    use game_menu(_("Free Chat") if persistent.cur_lang == "en" else "Obrolan Bebas", scroll=None):
        
        vbox:
            spacing 50
            ypos 10
            xpos 5
            #xalign 0.5

            # --- INFO PEMAIN SAAT INI & TOMBOL GANTI ---
            hbox:
                xalign 0.5
                spacing 30

                fixed:
                    xysize (500, 80)  # Ukuran tetap agar tidak terdorong ke bawah
                    yalign 0.5
                    
                    # Asumsi persistent.player_name sudah ada (ditangani oleh script fallback)
                    $ current_player = getattr(persistent, "player_name", "Player")
                    
                    text ("Current Player: [current_player]" if persistent.cur_lang == "en" else "Pemain Saat Ini: [current_player]") size 30 color "#484270" yalign 0.5 xpos 5
                    
                    imagebutton:
                        # Bungkus path gambar ke dalam Transform() agar zoom-nya bekerja
                        idle Transform("images/profile_icon.png", zoom=0.4)
                        hover Transform("images/profile_icon_hover.png", zoom=0.45)
                        # PANGGIL SCREEN BARU
                        action Show("profile_manager_screen", is_start=False)
                        xalign 0.9
                        yalign 0.5
            # ------------------------------------------
            
            text ("Who do you want to chat with?" if persistent.cur_lang == "en" else "Kamu mau ngobrol sama siapa?") size 45 color "#484270" bold True xalign 0.3
            
            # Grid Karakter
            vpgrid:
                cols 5
                spacing 25
                xalign 0.1
                xsize 1200
                ysize 1000
                yalign 0.5
                
                # Daftar manual karakter dan syarat award-nya
                $ companion_list = [
                    ("extraversion", "dog", "Iwank The Dog", "Iwank Si Anjing", "images/award_dog.png"),
                    ("conscientiousness", "cat", "Onyen The Cat", "Onyen Si Kucing", "images/award_cat.png"),
                    ("neuroticism", "civet", "Jakouko The Civet", "Jakouko Si Luwak", "images/award_civet.png"),
                    ("agreeableness", "rabbit", "Susagi The Rabbit", "Susagi Si Kelinci", "images/award_rabbit.png"),
                    ("openness", "fox", "Kitsuko The Fox", "Kitsuko Si Rubah", "images/award_fox.png")
                ]

                for comp_id, award_req, name_en, name_id, img_path in companion_list:
                    vbox:
                        spacing 15
                        xalign 0.5
                        yalign 0.5
                        # Cek apakah karakter ini sudah pernah dimainkan (Award terbuka)
                        if award_req in persistent.unlocked_awards:
                            # --- BUNGKUS DENGAN FIXED ---
                            fixed:
                                xysize (200, 200) # Ukuran pengunci, agar tidak menendang elemen lain
                                xalign 0.5
                                imagebutton:
                                    align (0.5, 0.5) # Gambar dipusatkan di tengah kotak
                                    idle Transform(img_path, zoom=1)
                                    hover Transform(img_path, zoom=1.05)
                                    action [SetVariable("companion_personality", comp_id), Start("sesi_chat_bebas_khusus")]

                            text (name_en if persistent.cur_lang == "en" else name_id) size 20 color "#484270" bold True xalign 0.5
                        else:
                            # --- BUNGKUS UNTUK ICON TERKUNCI ---
                            fixed:
                                xysize (200, 200)
                                xalign 0.5
                                add Transform("images/award_locked.png", zoom=0.3) align (0.5, 0.5)
                            
                            text "??? (Locked)" size 22 color "#aaaaaa" xalign 0.5

# Efek Animasi Meluncur dari kiri (Slide in)
transform achievement_slide_in:
    on show:
        xoffset -400 alpha 0.0
        easein_back 0.5 xoffset 0 alpha 1.0

# Layar Manajemen Notifikasi
screen steam_achievement_overlay():
    zorder 200 # Pastikan selalu di depan
    
    # Vbox agar menumpuk ke bawah
    vbox:
        align (0.02, 0.05) # Pojok kiri atas
        spacing 10
        
        for ach in active_achievements:
            # Desain Kartu Penghargaan (Ala Steam)
            frame:
                background Solid("#222222ee") # Warna gelap semi-transparan
                padding (15, 15)
                xsize 530
                at achievement_slide_in
                
                hbox:
                    spacing 15
                    # Gambar Icon (Jika tidak ada gambar khusus, pakai gembok/logo gamemu)
                    add ach["icon"] size (60, 60) yalign 0.5 
                    
                    vbox:
                        yalign 0.5
                        text "Achievement Unlocked!" size 16 color "#a4ff9c" # Hijau Steam
                        text ach["title"] size 20 color "#ffffff" bold True
                        
    # Timer pembersih berjalan setiap 0.5 detik
    timer 0.5 action Function(clean_achievements) repeat True

screen mbti_detail_popup():
    zorder 100 # Memastikan pop-up ada di lapisan paling depan
    modal True # Mengunci layar belakang
    
    # Background hitam transparan untuk menutupi layar belakang
    add Solid("#000000cc")
    
    # Frame Pop-up di tengah layar
    frame:
        xalign 0.5
        yalign 0.5
        xsize 1500 # Lebar frame
        ysize 800  # Tinggi frame
        padding (150, 70) # Padding dalam frame
        background Frame("gui/frame.png", 40, 20) # Sesuaikan dengan gambar frame UI-mu
        
        vbox:
            spacing 20
            
            # Judul Pop-up
            text ("MBTI Detail:" if persistent.cur_lang == "en" else "Detail MBTI:"): 
                size 40 color "#484270" bold True xalign 0.5
            
            # Garis pemisah (Opsional)
            add Solid("#484270") xsize 920 ysize 2 xalign 0.5
            
            # Kotak Scroll untuk Teks AI yang panjang
            viewport:
                scrollbars "vertical"
                mousewheel True
                draggable True
                yfill False # Membiarkan viewport menyesuaikan tinggi teks
                
                # Menampilkan jawaban dari API
                text "[detailed_mbti_explanation]" size 24 color "#333333" line_spacing 10 text_align 0.0
                
            null height 20
            
            # Tombol Tutup
            textbutton ("Close" if persistent.cur_lang == "en" else "Tutup"):
                action Hide("mbti_detail_popup")
                xalign 0.5
                text_size 30
                text_bold True

# Efek membesar saat kursor ditaruh di atas slot
transform slot_hover_effect:
    on idle:
        easein 0.15 zoom 1.0
    on hover:
        easein 0.15 zoom 1.05

screen profile_manager_screen(is_start=False):
    modal True 
    zorder 150 
    add Solid("#000000e6") 
    
    default current_view = "slots"
    default delete_mode = False # <-- Variabel Switch Hapus
    
    $ profile_data = get_all_profiles_data()
    
    frame:
        xalign 0.5 yalign 0.5
        padding (40, 40)
        background Frame("gui/frame.png", 20, 20)
        xsize 1100
        ysize 800
        
        # ==========================================
        # TAMPILAN 1: DAFTAR SLOT PROFIL
        # ==========================================
        if current_view == "slots":
            vbox:
                spacing 20
                xalign 0.5
                xfill True
                
                # --- HEADER & SAKLAR HAPUS ---
                hbox:
                    xalign 0.5
                    spacing 30
                    yalign 0.5
                    
                    text ("Select Save Profile" if persistent.cur_lang == "en" else "Pilih Profil Tersimpan") size 45 color "#484270" bold True yalign 0.5
                    
                    # Tombol Switch Hapus (On/Off)
                    textbutton ("🗑️ Mode Hapus" if persistent.cur_lang == "id" else "🗑️ Delete Mode"):
                        action ToggleScreenVariable("delete_mode", True, False)
                        text_size 25 
                        # Warna merah jika menyala, abu-abu jika mati
                        text_color ("#ff6b6b" if delete_mode else "#888888")
                        text_hover_color "#a4ff9c" text_bold True
                        yalign 0.5
                
                # --- AREA SCROLL UNTUK SLOT ---
                viewport:
                    scrollbars "vertical"
                    mousewheel True
                    xsize 950 ysize 500
                    xalign 0.5
                    
                    vbox:
                        spacing 25
                        xalign 0.5
                        xfill True
                        
                        if not profile_data:
                            text ("No saved profiles found." if persistent.cur_lang == "en" else "Belum ada profil tersimpan.") size 25 color "#aaa" xalign 0.5
                        else:
                            for p in profile_data:
                                # Gunakan HBOX agar tombol sampah ada di samping slot
                                hbox:
                                    xalign 0.5
                                    spacing 15
                                    
                                    # DESAIN SLOT (BUTTON UTAMA)
                                    button:
                                        # Jika Delete Mode ON, tombol utama dimatikan fungsinya (NullAction) agar tidak kepencet masuk game
                                        action ( [SetField(persistent, "player_name", p["name"]), Return() if is_start else Hide("profile_manager_screen")] if not delete_mode else NullAction() )
                                        
                                        # Jika ada tong sampah, slot agak mengecil agar muat di layar
                                        xsize (740 if delete_mode else 850) ysize 130 
                                        padding (40, 20)
                                        
                                        background Frame("gui/button/choice_idle_background.png", 30, 30)
                                        hover_background Frame("gui/button/choice_hover_background.png", 30, 30)
                                        at slot_hover_effect 
                                        
                                        hbox:
                                            xfill True yfill True
                                            spacing 20
                                            
                                            vbox:
                                                yalign 0.5
                                                spacing 5
                                                text safe_display_text(p["name"]) size 40 color "#484270" bold True
                                                text ("Last played: " + p["date"] if persistent.cur_lang == "en" else "Terakhir main: " + p["date"]) size 20 color "#666"
                                            
                                            vbox:
                                                xalign 1.0 yalign 0.5
                                                text "MBTI Result" size 18 color "#888" xalign 1.0
                                                text safe_display_text(p["mbti"]) size 40 color "#a4ff9c" bold True xalign 1.0 outlines [(1, "#484270", 0, 0)]
                                    
                                    # DESAIN TOMBOL TONG SAMPAH (Hanya muncul saat Delete Mode ON)
                                    # Cari kode desain tombol tong sampah yang lama, ganti action-nya:
                                    if delete_mode:
                                        button:
                                            # SEKARANG MEMANGGIL SCREEN KUSTOM
                                            action Show("delete_choice_screen", target_name=p["name"])
                                            
                                            xsize 95 ysize 130
                                            background Frame("gui/button/choice_idle_background.png", 30, 30)
                                            hover_background Solid("#ff4d4d") 
                                            text "🗑️" xalign 0.5 yalign 0.5 size 50
                                            at slot_hover_effect
                null height 10
                
                # --- TOMBOL BUAT PROFIL BARU ---
                textbutton ("+ Create New Profile" if persistent.cur_lang == "en" else "+ Buat Profil Baru"):
                    action SetScreenVariable("current_view", "new")
                    xalign 0.5
                    text_size 30 text_color "#484270" text_hover_color "#a4ff9c" text_bold True

                # --- TOMBOL KEMBALI / TUTUP (LOGIKA BARU) ---
                if is_start:
                    # Jika dipanggil dari Start, kembalikan pemain ke Main Menu secara aman
                    textbutton ("< Back to Main Menu" if persistent.cur_lang == "en" else "< Kembali ke Menu Utama"):
                        action MainMenu()
                        xalign 0.5 text_size 25 text_color "#ff6b6b" text_hover_color "#484270" text_bold True
                else:
                    textbutton ("Close" if persistent.cur_lang == "en" else "Tutup"):
                        action Hide("profile_manager_screen")
                        xalign 0.5 text_size 25 text_color "#ff6b6b" text_hover_color "#484270" text_bold True

        # ==========================================
        # TAMPILAN 2: INPUT PROFIL BARU
        # (Tetap sama seperti aslimu, tidak perlu diubah)
        # ==========================================
        elif current_view == "new":
            vbox:
                spacing 40
                xalign 0.5 yalign 0.5
                
                text ("Enter New Profile Name" if persistent.cur_lang == "en" else "Masukkan Nama Profil Baru") size 45 color "#484270" bold True xalign 0.5
                
                frame:
                    background Frame("gui/button/choice_idle_background.png", 30, 30)
                    xsize 600 ysize 100 xalign 0.5 padding (20, 25)
                    
                    input:
                        value FieldInputValue(persistent, "player_name")
                        exclude INVALID_NAME_CHARS
                        color "#484270" size 40 xalign 0.5 yalign 0.5 length 15 bold True
                        
                hbox:
                    spacing 100 xalign 0.5
                    
                    textbutton ("< Back" if persistent.cur_lang == "en" else "< Kembali"):
                        action SetScreenVariable("current_view", "slots")
                        text_size 35 text_color "#888" text_hover_color "#484270" text_bold True
                        
                    textbutton ("Start Journey" if persistent.cur_lang == "en" else "Mulai Perjalanan"):
                        action [Return() if is_start else Hide("profile_manager_screen")]
                        text_size 35 text_color "#a4ff9c" text_hover_color "#484270" text_bold True text_outlines [(1, "#484270", 0, 0)]

screen delete_choice_screen(target_name):
    modal True
    zorder 300 # Harus lebih tinggi dari layar profil utama
    add Solid("#000000cc") # Background gelap
    
    # Ambil daftar rute hewan si pemain
    $ comp_list = get_companions_for_player(target_name)
    
    frame:
        xalign 0.5 yalign 0.5
        padding (40, 40)
        background Frame("gui/frame.png", 20, 20)
        xsize 1000 ysize 800
        
        vbox:
            spacing 30
            xalign 0.5
            
            text ("Delete Data: [target_name]" if persistent.cur_lang == "en" else "Hapus Data: [target_name]") size 40 color "#ff6b6b" bold True xalign 0.5
            text ("Pilih data mana yang ingin dihapus:" if persistent.cur_lang == "en" else "Pilih data mana yang ingin dihapus:") size 25 color "#888" xalign 0.5
            
            # 1. Tombol Hapus Spesifik per Hewan
            for c in comp_list:
                textbutton ("Delete Route: " + c["animal"] if persistent.cur_lang == "en" else "Hapus Rute: " + c["animal"]):
                    action [Function(delete_specific_file, c["file"]), Hide("delete_choice_screen")]
                    xalign 0.5 text_size 30 text_color "#484270" text_hover_color "#ff6b6b"
            
            null height 10
            
            # 2. Tombol Hapus Semua (Sapu Bersih)
            textbutton ("Delete ALL Profiles" if persistent.cur_lang == "en" else "Hapus SEMUA Profil Ini"):
                action [Function(delete_all_for_player, target_name), Hide("delete_choice_screen")]
                xalign 0.5 text_size 30 text_color "#ff6b6b" text_bold True text_hover_color "#ff0000"
            
            null height 20
            
            # 3. Tombol Batal
            textbutton ("Cancel" if persistent.cur_lang == "en" else "Batal"):
                action Hide("delete_choice_screen")
                xalign 0.5 text_size 25 text_color "#888888"