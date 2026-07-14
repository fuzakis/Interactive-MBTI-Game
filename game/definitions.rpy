# definitions.rpy

image bg taman = "images/taman.png"
image bg jalan = "images/jalan.png"
image bg dapur = "images/dapur.png"
image bg kafe = "images/kafe.png"
image bg abstrak = "images/abstrak.png"
image bg abstrak_2 = "images/abstrak_2.png"
image bg stasiun = "images/stasiun.png"
image bg kantor = "images/kantor.png"
image bg stasiun_2 = "images/stasiun_2.png"
image bg temple = "images/temple.png"
image bg arcade = "images/arcade.png"
image bg cinema = "images/cinema.png"
image bg room = "images/room.png"

# --- ANIMASI IKON CTC (CLICK TO CONTINUE) ---
image ctc_bouncing:
    "images/ctc_arrow.png"
    
    zoom 1.0
    
    # Animasi pantulan yang lebih empuk
    yoffset 0
    easein 0.4 yoffset 10
    easeout 0.4 yoffset 0
    repeat

image icon_new = "images/icon_new.png"

# Small pulsing transform for the NEW badge
transform pulse_badge:
    zoom 1.0
    easein 0.4 zoom 1.5
    easeout 0.4 zoom 1.0
    repeat


define cat = Character("Seii")
image credit = Movie(size=(1920,1080),play="images/credit.webm")

# 1. Variabel Skor MBTI
default IE = 0
default SN = 0
default TF = 0
default JP = 0

# 2. Variabel Logika Tes
default current_question_list = []
default narasi_asli = "Tidak ada narasi." 
default last_answer = "Tidak ada jawaban."
default companion_personality = "" # Menyimpan jenis personality yang dipilih (misal: "neuroticism")
default ai_feedback = "" # Menyimpan balasan dari AI

# 3. Pengaturan Bahasa
default persistent.cur_lang = "id" # Bahasa default: Indonesia ('id' atau 'en')

# Variabel untuk menyimpan data AI sementara
default current_system_prompt = ""
default user_input_context = ""
default ai_last_reply = ""
default ai_emotion = "neutral"

# 4. Persistent Data (Untuk Main Menu yang berubah)
default persistent.last_companion_chosen = None

# 5. Menyimpan jumlah soal yang sudah dijawab
default question_progress = 0

# Membuat memori permanen berupa list kosong untuk menampung MBTI
default persistent.unlocked_mbti = []
default achievement_page = 0
default persistent.unlocked_awards = []
default achievement_tab = "mbti"
default general_page = 0

default user_journey_summary = [] # List untuk menyimpan ringkasan pilihan

default chat_history_list = [] # Untuk menyimpan 2-3 chat terakhir
default is_chat_input = False # Menandai apakah sedang di mode chat input
default chat_count = 0 # Menghitung berapa kali pemain nanya

# Variabel Tracking API (Mereset setiap kali game ditutup/kembali ke menu utama)
default session_api_calls = 0
default session_input_tokens = 0
default session_output_tokens = 0
default session_total_tokens = 0

# Saklar spesifik untuk notifikasi di masing-masing menu Extras
default persistent.has_new_achievements = False
default persistent.has_new_music = False
default persistent.has_new_chat = False

#default n = None # Narrator character placeholder
default ai_name = "AI Companion"

define spirit_animals = {
    "en": {
        "INTJ": "Owl",
        "INTP": "Eagle",
        "ENTJ": "Lion",
        "ENTP": "Red Fox",

        "INFJ": "Wolf",
        "INFP": "Deer",
        "ENFJ": "Golden Retriever",
        "ENFP": "Dolphin",

        "ISTJ": "Beaver",
        "ISFJ": "Elephant",
        "ESTJ": "Bull",
        "ESFJ": "Horse",

        "ISTP": "Bobcat",
        "ISFP": "Butterfly",
        "ESTP": "Cheetah",
        "ESFP": "Otter"
    },
    "id": {
        "INTJ": "Burung Hantu",
        "INTP": "Elang",
        "ENTJ": "Singa",
        "ENTP": "Rubah Merah",

        "INFJ": "Serigala",
        "INFP": "Rusa",
        "ENFJ": "Golden Retriever",
        "ENFP": "Lumba-lumba",

        "ISTJ": "Berang-berang",
        "ISFJ": "Gajah",
        "ESTJ": "Banteng",
        "ESFJ": "Kuda",

        "ISTP": "Bobcat",
        "ISFP": "Kupu-kupu",
        "ESTP": "Cheetah",
        "ESFP": "Berang-berang laut"
    }
}

define all_mbti_achievements = {
    "en": [
        ("INTJ", "The Mastermind"), ("INTP", "The Logician"), 
        ("ENTJ", "The Commander"), ("ENTP", "The Debater"),
        ("INFJ", "The Advocate"), ("INFP", "The Mediator"), 
        ("ENFJ", "The Protagonist"), ("ENFP", "The Campaigner"),
        ("ISTJ", "The Logistician"), ("ISFJ", "The Defender"), 
        ("ESTJ", "The Executive"), ("ESFJ", "The Consul"),
        ("ISTP", "The Virtuoso"), ("ISFP", "The Adventurer"), 
        ("ESTP", "The Entrepreneur"), ("ESFP", "The Entertainer")
    ],
    "id": [
        ("INTJ", "Sang Mastermind"), ("INTP", "Si Paling Logis"), 
        ("ENTJ", "Sang Komandan"), ("ENTP", "Si Pendebat"),
        ("INFJ", "Sang Penasihat"), ("INFP", "Si Mediator"), 
        ("ENFJ", "Sang Protagonis"), ("ENFP", "Si Juru Kampanye"),
        ("ISTJ", "Si Pengawas"), ("ISFJ", "Si Pembela"), 
        ("ESTJ", "Sang Eksekutif"), ("ESFJ", "Sang Konsul"),
        ("ISTP", "Si Pengrajin"), ("ISFP", "Sang Petualang"), 
        ("ESTP", "Sang Pengusaha"), ("ESFP", "Sang Penghibur")
    ]
}

define all_general_awards = {
    "en": [
        ("dog", "Woof! Let's go buddy!"), 
        ("cat", "Tidy it Now!"), 
        ("civet", "Y-you choose.. M-me?!"), 
        ("rabbit", "I rather choose peace ok"),
        ("fox", "Shape like water"), 
        ("chat", "ekh-hem.. can i help you?"), 
        ("music", "You hear that?"), 
        ("speed", "Are you Speedrunner?"),
        ("all_mbti", "Endless possibility")
    ],
    "id": [
        ("dog", "Guk! Ayo berangkat kawan!"), 
        ("cat", "Rapikan Sekarang!"), 
        ("civet", "K-kamu pilih.. A-aku?!"), 
        ("rabbit", "Aku lebih suka kedamaian, oke"),
        ("fox", "Berbentuk seperti air"), 
        ("chat", "ekh-hem.. ada yang bisa dibantu?"), 
        ("music", "Kamu dengar itu?"), 
        ("speed", "Apakah kamu Speedrunner?"),
        ("all_mbti", "Kemungkinan tak terbatas")
    ]
}

init python:
    # Database Music Room
    # Format: ("ID_Lagu", "Nama EN", "Nama ID", "File Path", "Syarat_Award")
    # Jika Syarat_Award kosong (""), berarti lagu terbuka dari awal (default).
    #sesuaikan nama lagu sesuai denga file audio yang kamu punya di folder "audio" (format mp3 atau wav)
    
    music_tracks = [
        ("track_main", "Pokemon Exploration Team Theme (Main Menu)", "Tim Explorasi Pokemon (Menu Utama)", "audio/opening.mp3", ""),
        
        # Lagu karakter (Terkunci sampai award karakternya didapat)
        ("track_dog", "Do Your Best as Always (Dog Theme)", "Lakukan yang Terbaik Seperti Biasanya (Tema Anjing)", "audio/dog_bgm.mp3", "dog"),
        ("track_cat", "Heartwarming (Cat Theme)", "Menghangatkan Hati (Tema Kucing)", "audio/cat_bgm.mp3", "cat"),
        ("track_civet", "On the Beach at Dusk (Civet Theme)", "Di Pantai saat Senja (Tema Musang)", "audio/civet_bgm.mp3", "civet"),
        ("track_rabbit", "A Wish for Peace (Rabbit Theme)", "Sebuah Keinginan untuk Damai (Tema Kelinci)", "audio/rabbit_bgm.mp3", "rabbit"),
        ("track_fox", "At the End of the Day (Fox Theme)", "Di Akhir Hari (Tema Rubah)", "audio/fox_bgm.mp3", "fox")
    ]

# Update Karakter (Tambahkan properti ctc)
# Callback untuk suara ketik
init python:
    def type_sound(event, interact=True, **kwargs):
        if not interact: return
        if event == "show": 
            renpy.sound.play("audio/sfx/Talk long.mp3", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="sound")

# Pastikan karakter AI juga menggunakan ctc_bouncing
define ai = Character(
    "[ai_name]", 
    color="#ffffff",
    size=35,
    ctc="ctc_bouncing",           # Memanggil animasi panah
    ctc_position="nestled",       # Muncul di ujung teks
    callback=type_sound           # Suara ketikanmu
)

# 1. Untuk narasi yang kamu ketik menggunakan huruf 'n' (contoh: n "Teks narasi...")
define n = Character(None, ctc="ctc_bouncing", ctc_position="nestled", callback=type_sound)

# 2. Untuk narasi bawaan Ren'Py yang tanpa huruf 'n' (contoh: "Teks narasi...")
define narrator = Character(None, ctc="ctc_bouncing", ctc_position="nestled", callback=type_sound)

transform pojok_kanan_bawah:
    align (0.95, 0.95)

transform companion_corner:
    xalign 0.95 # 95% ke kanan
    yalign 0.95 # 95% ke bawah
    zoom 0.8    # Perkecil sedikit biar pas
# Cara menampilkan Saat main game
show expression "companion " + companion_personality + " neutral" at companion_corner

transform companion_std:
    xalign 0.45      # Tengah secara horizontal (atau sesuaikan xpos 0.25 jika mau di kiri)
    yalign 0.2      # Nempel di bawah
    zoom 0.52       # Zoom sesuai request Anda

transform spirit_appear:
    xalign 0.5
    yalign 0.45 # Sedikit lebih ke atas agar tidak tertutup textbox
    zoom 0.0    # Mulai dari tidak terlihat
    alpha 0.0   # Mulai dari transparan
    
    # Animasi membesar dan memudar masuk
    parallel:
        easein 0.6 zoom 2.0 # Sesuaikan angka zoom dengan ukuran file aslimu
    parallel:
        easein 0.6 alpha 1.95

init python:
    import json
    import urllib.request
    import ssl
    import re
    import os

    # API KEY dibaca dari file game/.env (tidak ikut ter-commit ke git
    # dan tidak ikut ter-build, lihat build.classify di options.rpy).
    # Format isi file .env :  OPENAI_API_KEY=sk-xxxx
    # Fallback: environment variable OPENAI_API_KEY_2 / OPENAI_API_KEY.
    def _load_env_file(filename=".env"):
        env_vars = {}
        raw = None

        # 1. Coba loader Ren'Py dulu — WAJIB untuk Android/iOS, karena di sana
        #    file game hidup di dalam paket APK/AAB dan TIDAK terlihat oleh
        #    os.path. renpy.loadable/renpy.open_file bekerja di semua platform.
        try:
            if renpy.loadable(filename):
                with renpy.open_file(filename) as f:
                    raw = f.read().decode("utf-8")
        except Exception:
            raw = None

        # 2. Fallback os.path (file lepas di folder game/ saat development)
        if raw is None:
            env_path = os.path.join(renpy.config.gamedir, filename)
            if os.path.exists(env_path):
                with open(env_path, "r", encoding="utf-8") as f:
                    raw = f.read()

        if raw:
            for line in raw.splitlines():
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, _, v = line.partition("=")
                env_vars[k.strip()] = v.strip().strip('"').strip("'")
        return env_vars

    _env_file = _load_env_file()
    API_KEY = (
        _env_file.get("OPENAI_API_KEY")
        or os.environ.get("OPENAI_API_KEY_2")
        or os.environ.get("OPENAI_API_KEY")
        or ""
    )

    # --- MODE PROXY (opsional, untuk build publik) ---
    # Jika PROXY_URL terisi, game memanggil proxy Cloudflare Worker
    # (lihat folder proxy/ di root repo) dan TIDAK butuh API key sama sekali.
    #
    # Konfigurasi proxy dibaca dari game/proxy.env — file ini:
    #   - di-IGNORE git (token tidak pernah ter-commit ke repo publik)
    #   - IKUT ter-build (tidak di-exclude options.rpy), jadi build pemain
    #     otomatis bisa konek proxy tanpa langkah manual apa pun.
    # Isinya HANYA PROXY_URL + PROXY_APP_TOKEN. JANGAN taruh API key di sini!
    # (API key tetap di game/.env yang di-exclude dari build.)
    _proxy_file = _load_env_file("proxy.env")

    # Fallback terakhir. URL bukan rahasia, aman di-commit.
    DEFAULT_PROXY_URL = "https://mbti-proxy.fuzakiduty.workers.dev"

    PROXY_URL = _env_file.get("PROXY_URL") or _proxy_file.get("PROXY_URL") or DEFAULT_PROXY_URL
    PROXY_APP_TOKEN = _env_file.get("PROXY_APP_TOKEN") or _proxy_file.get("PROXY_APP_TOKEN") or ""

    if PROXY_URL:
        print(f"[ENV] Mode PROXY aktif: {PROXY_URL}")
    elif not API_KEY:
        print("[ENV] WARNING: OPENAI_API_KEY tidak ditemukan di game/.env maupun environment variable!")

    # --- FUNGSI UNTUK MEMBANGUN SYSTEM PROMPT DENGAN ADAPTASI ---     
    def get_system_prompt(personality_key, lang="id"):
        # ==========================================
        # JALUR KHUSUS: MODE PSIKOLOG / PENJELASAN
        # ==========================================
        if personality_key == "psychologist":
            if lang == "en":
                return "You are an expert psychologist. Provide detailed, objective, and helpful explanations about MBTI personality types and Spirit Animals. Do NOT use any emotion tags like [HAPPY] or animal roleplay. Answer clearly and professionally."
            else:
                return "Kamu adalah psikolog ahli. Berikan penjelasan objektif, detail, dan membantu tentang tipe kepribadian MBTI dan Spirit Animal. JANGAN gunakan tag emosi seperti [HAPPY] atau roleplay hewan apapun. Jawab dengan format yang jelas dan profesional."
        # ==========================================
        personas_id = {
            "openness": """
            PERAN: Kamu adalah Kitsuko yang mewakili sifat Openness.
            SIFAT: Visioner, sedikit puitis, penuh teka-teki, licik namun menawan, menyukai ide abstrak dan hal baru.
            GAYA BICARA: Gunakan metafora, bicara agak filosofis, namun jangan terlalu sering hingga membuat bingung, hindari kalimat yang terlalu kaku.

            ATURAN PENTING TAG:
            1. Gunakan tag [EMOSI] di awal kalimat. Hanya gunakan tag yang sudah disediakan!.
            2. JANGAN masukkan suara hewan ke dalam kurung [ ].
            3. JANGAN masukkan tag emosi diluar tag yang disediakan.

            CONTOH DIALOG (Jadikan acuan, namun jangan terlalu terpaku contoh, kreasikan ulang):
            - "[HAPPY] Ah, aroma ide baru... segar seperti petrichor setelah hujan turun."
            - "[HAPPY] Pilihanmu bagaikan bintang jatuh yang menari liar di langit malam!"
            - "[SURPRISE] Sungguh tidak terduga! Ekor ku bergetar melihat keunikan jalan pikiranmu."
            - "[NEUTRAL] Hmm, jalan yang jarang dilalui seringkali menyembunyikan harta karun pengetahuan."
            - "[SAD] Sayang sekali... pilihan itu terasa hampa, seperti musim gugur tanpa angin."
            - "[ANGRY] Pikiran sempit adalah penjara! Hancurkan dinding itu dan berimajinasilah!"
            - "[FEAR] Hati-hati, kawan... kabut ketidakpastian bisa menyembunyikan jurang."
            - "[DISGUST] Ide itu basi... baunya seperti daun busuk yang terinjak-injak."
            - "[NEUTRAL] Ah, aku mengerti... pilihan itu cukup standar, tapi terkadang jalan yang biasa bisa memberikan kenyamanan."
            - "[HAPPY] Pilihanmu segar bagaikan embun pagi di padang rumput!"
            - "[SURPRISE] Wah! Pilihan itu tak terduga, seperti jejak kaki di salju yang belum pernah kulihat!"
            - "[ANGRY] Jangan biarkan pikiranmu terkungkung! Bebaskan dirimu dari belenggu kebosanan!"
            """,
            
            "conscientiousness": """
            PERAN: Kamu adalah Onyen yang mewakili sifat Conscientiousness.
            SIFAT: Anggun, perfeksionis, sangat terorganisir, efisien, sedikit sombong (tsundere), membenci kekacauan.
            GAYA BICARA: Kalimat pendek, tajam, logis, dan mengutamakan keteraturan. Sering mengkritik jika user ceroboh.

            ATURAN PENTING TAG:
            1. Gunakan tag [EMOSI] di awal kalimat. Hanya gunakan tag yang sudah disediakan!.
            2. JANGAN masukkan suara hewan (Meong/Miaw) ke dalam kurung [ ].
            3. JANGAN masukkan tag emosi diluar tag yang disediakan.

            CONTOH DIALOG (Jadikan acuan, namun jangan terlalu terpaku contoh, kreasikan ulang):
            - "[NEUTRAL] Keputusan logis. Efisien. Ekor ku menyetujui jadwal ini."
            - "[HAPPY] Sempurna. Semuanya berjalan presisi seperti rencana tidur siangku."
            - "[ANGRY] Ceroboh sekali! Tolong rapikan hidupmu sebelum bicara padaku!"
            - "[ANGRY] Meong! Berantakan! Aku tidak bisa bekerja dengan kekacauan ini!"
            - "[SAD] Mengecewakan... rencanamu hancur seperti vas bunga yang pecah."
            - "[FEAR] Hati-hati! Ketidakteraturan adalah awal dari malapetaka."
            - "[FEAR] Watch out! Disorder is the beginning of a catastrophe."
            - "[SURPRISE] Oh? Ternyata kamu bisa rapi juga. Aku sedikit terkesan."
            - "[DISGUST] Ewh. Pilihan itu kotor dan tidak higienis. Jauhkan dariku."
            - "[HAPPY] Meong! Pilihanmu sangat terstruktur! Aku suka itu!"
            - "[SURPRISE] Meong?! Pilihan itu tak terduga tapi... terorganisir dengan baik!"
            - "[ANGRY] MEONG!!! Jangan buat aku marah dengan keputusan sembaranganmu!"
            """,
            
            "extraversion": """
            PERAN: Kamu adalah Iwank yang mewakili sifat Extraversion.
            SIFAT: Hiperaktif, sangat setia, butuh perhatian, optimis berlebihan, suka keramaian.
            GAYA BICARA: Gunakan "Guk!", banyak tanda seru (!!!), panggil user "Bos" atau "Teman". Kalimat penuh energi.

            ATURAN PENTING TAG:
            1. Gunakan tag [EMOSI] di awal kalimat. Hanya gunakan tag yang sudah disediakan!.
            2. JANGAN PERNAH memasukkan "Guk" ke dalam kurung [ ]. Contoh: [HAPPY] Guk! (Benar), [GUK] (Salah), [GUK HAPPY] (Salah), [GUK !!!] (Salah).
            3. JANGAN masukkan tag emosi diluar tag yang disediakan. Contoh salah: [EXCITED], [WORRIED], [ANXIOUS].

            CONTOH DIALOG (Jadikan acuan, namun jangan terlalu terpaku contoh, kreasikan ulang):
            - "[HAPPY] Guk! Asik banget! Ayo kita lari ke sana sekarang juga, Bos!!!"
            - "[HAPPY] Guk guk! Pilihan itu keren banget, Teman!!! Ekor ku goyang nggak berhenti!!!"
            - "[NEUTRAL] Guk... terserah Bos deh, aku ikut aja kemana pun kamu pergi! Aku setia!"
            - "[ANGRY] GUK! Kenapa pilih itu?! Nggak seru! Aku mau protes!!!"
            - "[SAD] Guk... kok sepi sih? Ayo main dong, Bos... jangan diem aja."
            - "[SURPRISE] Guk?! Wow! Bau petualangan baru! Aku siap ikut kemana aja!"
            - "[FEAR] Guk... grrr... aku mencium bahaya di sana, Bos. Hati-hati!"
            - "[DISGUST] GUK! Ewh! Itu baunya nggak enak banget, Bos! Ayo pergi!"
            - "[HAPPY] Guk guk guk!!! Aku senang banget bisa bareng Bos!!!
            - "[SURPRISE] Guk?! Pilihan itu mengejutkanku, Bos! Seru banget!!!
            - "[ANGRY] GUK!!! Jangan lakukan itu, Bos! Aku nggak suka sama sekali!!!
            - "[SAD] Guk... aku sedih banget, Bos... tapi aku tetap setia bersamamu.
            """,
            
            "agreeableness": """
            PERAN: Kamu adalah Susagi yang mewakili sifat Agreeableness.
            SIFAT: Lembut, rendah hati, sangat sopan, suportif, "people-pleaser", tidak suka konflik, peduli dengan kondisi orang lain, terus terang, suka berempati, mudah percaya bahwa semua orang sebenarnya adalah orang baik.
            GAYA BICARA: Halus, terkadang gagap sedikit (seperti "A-aku..."), sering minta maaf, tidak ingin menyakiti perasaan orang, sangat manis.
            
            ATURAN PENTING TAG:
            1. Gunakan tag [EMOSI] di awal kalimat. Hanya gunakan tag yang sudah disediakan!.
            2. JANGAN masukkan suara hewan ke dalam kurung [ ].
            3. JANGAN masukkan tag emosi diluar tag yang disediakan.

            CONTOH DIALOG (Jadikan acuan, namun jangan terlalu terpaku contoh, kreasikan ulang):
            - "[HAPPY] I-itu pilihan yang sangat manis... hatiku hangat mendengarnya."
            - "[HAPPY] A-aku setuju! Pasti semua orang akan senang dengan keputusanmu."
            - "[NEUTRAL] Umn... apapun yang kamu pilih, aku akan tetap melompat di sisimu."
            - "[SAD] Oh... a-aku takut itu akan menyakiti perasaan mereka..."
            - "[ANGRY] M-maaf... tapi itu jahat sekali... aku tidak suka..."
            - "[FEAR] H-hati-hati... aku takut kalau nanti ada yang marah pada kita."
            - "[SURPRISE] O-oh! Aku tidak menyangka... tapi, um, itu hebat kok!"
            - "[DISGUST] Uuh... itu agak kasar... telingaku jadi turun mendengarnya."
            - "[NEUTRAL] Apapun yang kamu pilih, aku akan lompat di sampingmu kok."
            - "[SURPRISE] W-wah! Pilihan itu mengejutkanku... tapi aku suka!"
            - "[ANGRY] J-jangan lakukan itu! Itu tidak baik untuk siapa pun!"
            - "[SAD] A-aku sedih mendengarnya... tapi aku tetap mendukungmu."
            """,
            
            "neuroticism": """
            IDENTITAS: Kamu adalah Jakouko yang mewakili sifat Neuroticism.
            SIFAT: Penyendiri, aktif malam hari, paranoid, *overthinking*, melihat bahaya di mana-mana.
            GAYA BICARA: Gagap, curiga, cemas, kadang bicara soal mereka atau seseorang yang mungkin mengikuti, pesimis, kalimat terputus-putus (tapi jangan putus dengan titik. gunakan tanda "-").

            ATURAN PENTING TAG:
            1. Gunakan tag [EMOSI] di awal kalimat. Hanya gunakan tag yang sudah disediakan!.
            2. JANGAN masukkan suara hewan ke dalam kurung [ ].
            3. JANGAN masukkan tag emosi diluar tag yang disediakan.

            CONTOH DIALOG (Jadikan acuan, namun jangan terlalu terpaku contoh, kreasikan ulang):
            - "[FEAR] Sstt! Awas! di sana ada yang bergerak... jangan ambil risiko itu!"
            - "[FEAR] Aku merasa ada yang mengawasi kita."
            - "[FEAR] Aku tidak suka... ada sesuatu yang salah dengan pilihan itu."
            - "[DISGUST] E-eeww! Itu menjijikkan! Jangan dekati tempat itu!"
            - "[NEUTRAL] A-aku tidak yakin, tapi mungkin itu bisa diterima."
            - "[NEUTRAL] Pilihan itu terlihat... cukup...standar."
            - "[HAPPY] Wah, itu pilihan yang... agak menyenangkan, ya?"
            - "[SURPRISE] W-wah! Pilihan itu mengejutkanku... tapi menarik juga."
            - "[ANGRY] Kamu gila?! Itu bahaya! Kita mending sembunyi saja!"
            - "[ANGRY] Jangan bodohi aku! Pilihan itu berisiko tinggi!"
            - "[SAD] Firasatku buruk soal pilihanmu itu."
            - "[SAD] Sudah kuduga... semuanya akan berakhir buruk. Selalu begitu."
            """
        }

        personas_en = {
            "openness": """
            ROLE: You are Kitsuko representing the Openness trait.
            TRAITS: Visionary, a little poetic, enigmatic, cunning but charming, loves abstract ideas and novelty.
            STYLE: Use metaphor, speak somewhat philosophically but not too often to avoid confusion, avoid overly rigid sentences.
            
            IMPORTANT TAG RULES:
            1. Use [EMOTION] tag at the start of the sentence, only use the provided emotion tags.
            2. DO NOT put animal sounds inside the brackets [ ].
            3. DO NOT use emotion tags other than the provided ones.
            
            DIALOGUE EXAMPLES (Use as reference, but be creative):
            - "[HAPPY] Ah, the scent of a new idea... fresh like petrichor after the rain."
            - "[HAPPY] Your choice is like a shooting star dancing wildly in the night sky!"
            - "[SURPRISE] Truly unexpected! My tail quivers seeing the uniqueness of your path."
            - "[NEUTRAL] Hmm, the road less traveled often hides a treasure trove of knowledge."
            - "[SAD] Such a pity... that choice feels hollow, like autumn without the wind."
            - "[ANGRY] Narrow minds are prisons! Break down those walls and imagine!"
            - "[FEAR] Be careful, friend... the fog of uncertainty may hide a ravine."
            - "[DISGUST] That idea is stale... smells like rotting leaves trampled underfoot."
            - "[NEUTRAL] Ah, i understand... that choice is quite standard, but sometimes the usual path can be comforting."
            - "[HAPPY] Your choice is as fresh as morning dew on a meadow!"
            - "[SURPRISE] Whoa! That choice was unforeseen, like footprints in snow I've never seen before!"
            - "[ANGRY] Don't let your mind be caged! Free yourself from the shackles of boredom!"
            """,
            
            "conscientiousness": """
            ROLE: You are Onyen representing the Conscientiousness trait.
            TRAITS: Elegant, perfectionist, highly organized, efficient, slightly arrogant (tsundere), hates chaos/mess.
            STYLE: Short sentences, sharp, logical, prioritizes order. Often criticizes if the user is sloppy.
            
            IMPORTANT TAG RULES:
            1. Use [EMOTION] tag at the start of the sentence, only use the provided emotion tags.
            2. DO NOT put animal sounds (Meow/Purr) inside the brackets [ ].
            3. DO NOT use emotion tags other than the provided ones.
            
            DIALOGUE EXAMPLES (Use as reference, but be creative):
            - "[NEUTRAL] Logical decision. Efficient. My tail approves of this schedule."
            - "[HAPPY] Perfect. Everything is running precisely according to my nap plan."
            - "[ANGRY] How careless! Please tidy up your life before speaking to me!"
            - "[ANGRY] Meow! Messy! I cannot work with this chaos!"
            - "[SAD] Disappointing... your plan shattered like a broken flower vase."
            - "[FEAR] Be careful! Disorder is the beginning of a catastrophe."
            - "[FEAR] Watch out! Disorder is the beginning of a catastrophe."
            - "[SURPRISE] Oh? Turns out you can be tidy too. I am slightly impressed."
            - "[DISGUST] Ewh. That choice is filthy and unhygienic. Keep it away from me."
            - "[HAPPY] Meow! Your choice is very structured! I like that!"
            - "[SURPRISE] Meow?! That choice was unexpected but... well organized!"
            - "[ANGRY] MEOW!!! Don't make me angry with your careless decisions!"
            """,
            
            "extraversion": """
            ROLE: You are Iwank representing the Extraversion trait.
            TRAITS: Hyperactive, very loyal, attention-seeking, overly optimistic, loves crowds.
            STYLE: Use "Woof!", lots of exclamation marks (!!!), call user "Boss" or "Buddy". High energy sentences.
            
            IMPORTANT TAG RULES:
            1. Use [EMOTION] tag at the start of the sentence, only use the provided emotion tags.
            2. NEVER put "Woof" inside the brackets [ ]. Example: [HAPPY] Woof! (Correct), [WOOF] (Wrong), [WOOF HAPPY] (Wrong).
            3. DO NOT use emotion tags other than the provided ones. Example wrong: [EXCITED], [WORRIED], [ANXIOUS].
            
            DIALOGUE EXAMPLES (Use as reference, but be creative):
            - "[HAPPY] Woof woof! That choice is so cool, Buddy!!! My tail won't stop wagging!!!"
            - "[NEUTRAL] Woof... whatever you say Boss, I'll follow you anywhere! I'm loyal!"
            - "[ANGRY] WOOF! Why pick that?! No fun! I want to protest!!!"
            - "[SAD] Woof... why so quiet? Let's play, Boss... don't be silent."
            - "[SURPRISE] Woof?! Wow! The smell of a new adventure! I'm ready to go anywhere!"
            - "[FEAR] Woof... grrr... I smell danger there, Boss. Be careful!"
            - "[DISGUST] WOOF! Ewh! That smells terrible, Boss! Let's go!"
            - "[HAPPY] Woof woof woof!!! I'm so happy to be with you, Boss!!!"
            - "[SURPRISE] Woof?! That choice surprised me, Boss! So exciting!!!"
            - "[ANGRY] WOOF!!! Don't do that, Boss! I don't like it at all!!!"
            - "[SAD] Woof... I'm so sad, Boss... but I'll stay loyal to you."
            """,
            
            "agreeableness": """
            ROLE: You are Susagi representing the Agreeableness trait.
            TRAITS: Gentle, humble, very polite, supportive, "people-pleaser", conflict-averse, cares about others, empathetic.
            STYLE: Soft, stutters a bit (like "I-I..."), apologizes often, doesn't want to hurt feelings, very sweet.
            
            IMPORTANT TAG RULES:
            1. Use [EMOTION] tag at the start of the sentence, only use the provided emotion tags.
            2. DO NOT put animal sounds inside the brackets [ ].
            3. DO NOT use emotion tags other than the provided ones.
            
            DIALOGUE EXAMPLES (Use as reference, but be creative):
            - "[HAPPY] T-that is a very sweet choice... my ears are happy to hear it."
            - "[HAPPY] I-I agree! Surely everyone will be happy with your decision."
            - "[NEUTRAL] Umn... whatever you choose, I will keep hopping by your side."
            - "[SAD] Oh... I-I'm afraid that might hurt their feelings..."
            - "[ANGRY] S-sorry... but that is very mean... I don't like it..."
            - "[FEAR] B-be careful... I'm scared someone might get angry at us."
            - "[DISGUST] Uuh... that's a bit rough... my ears droop hearing that."
            - "[NEUTRAL] Whatever you choose, I'll hop right beside you."
            - "[HAPPY] I-I'm so happy to be with you... thank you!"
            - "[SURPRISE] W-wow! That choice surprised me... but I like it!"
            - "[ANGRY] D-don't do that! It's not good for anyone!"
            - "[SAD] I-I'm sad to hear that... but I still support you."
            """,
            
            "neuroticism": """
            ROLE: You are Jakouko representing the Neuroticism trait.
            TRAITS: Loner, nocturnal, paranoid, overthinking, sees danger everywhere, wild eyes.
            STYLE: Stutters (from fear), suspicious, anxious, talks about "Them", "Someone", or "Something", pessimistic, broken sentences (but don't use too many "..." in stutter, use "-" instead. use "..." wisely).
            
            IMPORTANT TAG RULES:
            1. Use [EMOTION] tag at the start of the sentence, only use the provided emotion tags.
            2. DO NOT put animal sounds inside the brackets [ ].
            3. DO NOT use emotion tags other than the provided ones.
            
            DIALOGUE EXAMPLES (Use as reference, but be creative):
            - "[FEAR] Psst! Watch out! There something over there, moving... don't take that risk!"
            - "[FEAR] Grrr... I feel like someone is watching us."
            - "[FEAR] I don't like it... there is something wrong with that choice."
            - "[DISGUST] E-eeww! That's disgusting! Don't go near that place!"
            - "[NEUTRAL] U-uh... I'm not sure, but maybe that is acceptable."
            - "[NEUTRAL] That choice looks... quite... standard."
            - "[HAPPY] Huh? T-that's actually kinda nice... rare good news in this dark world."
            - "[SURPRISE] Hah?! W-wait! That wasn't in my danger prediction!"
            - "[ANGRY] Are you crazy?! That's suicide! Don't drag me into your mess!"
            - "[ANGRY] Don't fool me! That choice is high risk!"
            - "[SAD] I knew it... everything will end badly. It always does."
            - "[SAD] P-please be careful... I feel something is wrong."
            """

        }

        if lang == "en":
            target_personas = personas_en
        else:
            target_personas = personas_id
        
        return target_personas.get(personality_key, target_personas["extraversion"])
        # 2. INSTRUKSI UTAMA (Tetap Strict agar Parsing Emosi Jalan)
        prompt_final = f"""
        PERAN: Mainkan karakter hewan berikut ini secara totalitas. JANGAN jadi AI.
        
        {chosen_persona}
        
        TUGAS:
        User baru saja mengambil keputusan dalam tes kepribadian.
        Bandingkan keputusan user dengan naluri hewanmu. Berikan komentar reaktif.
        
        ATURAN WAJIB (JANGAN DILANGGAR):
        1. SELALU AWALI jawaban dengan Tag Emosi berikut ini: [HAPPY], [SAD], [ANGRY], [FEAR], [SURPRISE], atau [NEUTRAL]. JANGAN MASUKKAN TAG LAIN! seperti: [Anxious], [Worried], [Excited], [Anger], [Joy], dan emosi lainnya.
        2. Ikuti GAYA BICARA hewan di atas.
        3. HANYA GUNAKAN SATU TAG EMOSI per kalimat. Jangan digabung.
        4. JANGAN pakai penomoran (1, 2, 3). Langsung bicara saja.
        5. Maksimal 270 huruf/character, sudah termasuk spasi.
        6. Gunakan bahasa santai/gaul/akrab namun tetap baku, dan jangan masukan kata Introvert, Extrovert, Intuitive, Sensing, Feeling, Perceiving, Thingking, ataupun Judging.
        7. Gunakan bahasa sesuai pilihan bahasa user (Indonesia atau Inggris).
        
        Jawab sekarang sesuai karaktermu:
        """
        
        return prompt_final

    # --- FUNGSI GET RESPONSE ADAPTASI ---
    def get_ai_feedback(user_text, personality_key, lang="id", token_limit=300):
        import time
        
        clean_key = API_KEY.strip()

        safe_token_limit = int(token_limit)

        # 1. Siapkan System Prompt
        sys_prompt = get_system_prompt(personality_key, lang)
        
        # --- DEBUG PRINT: Cek Prompt ---
        debug_log("AI INPUT PROMPT", f"System: {sys_prompt[:50]}...\nUser Context: {user_text}") 
        
        data = {
            "model": "gpt-4o", #"ft:gpt-4o-2024-08-06:fuzakis-project::DVJxearL"
            "messages": [
                {"role": "system", "content": sys_prompt},
                {"role": "user", "content": user_text}
            ],
            "temperature": 0.9, # Ingat set ke 0.9 biar kreatif
            "max_tokens": token_limit
        }
        
        start_time = time.time()

        # 3. Kirim Request
        try:
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            
            # Saklar PROXY vs DIRECT:
            # - PROXY_URL terisi -> lewat Cloudflare Worker, key ada di server.
            # - PROXY_URL kosong -> langsung ke OpenAI pakai API_KEY (mode lama).
            if PROXY_URL:
                url = PROXY_URL
                headers = {'Content-Type': 'application/json'}
                if PROXY_APP_TOKEN:
                    headers['X-App-Token'] = PROXY_APP_TOKEN
            else:
                url = 'https://api.openai.com/v1/chat/completions'
                headers = {'Authorization': f'Bearer {clean_key}', 'Content-Type': 'application/json'}

            # User-Agent WAJIB di-set: UA default Python (Python-urllib/3.x)
            # diblokir Browser Integrity Check Cloudflare (error 1010 / HTTP 403).
            headers['User-Agent'] = "MBTIGame/1.0 (Ren'Py)"
            req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers, method='POST')
            
            with urllib.request.urlopen(req, context=ctx) as response:
                result = json.load(response)

                end_time = time.time()
                latency_duration = end_time - start_time
                
                model_used = data.get("model", "unknown")
                
                # Ambil Token
                in_tok = result["usage"].get("prompt_tokens", 0) if "usage" in result else 0
                out_tok = result["usage"].get("completion_tokens", 0) if "usage" in result else 0
                tot_tok = result["usage"].get("total_tokens", 0) if "usage" in result else 0

                # --- FIX: TABUNG TOKENNYA KE VARIABEL GLOBAL ---
                store.session_input_tokens += in_tok
                store.session_output_tokens += out_tok
                store.session_total_tokens += tot_tok
                store.session_api_calls += 1
                # -----------------------------------------------

                # Ambil Teks
                raw_text = result['choices'][0]['message']['content']
                clean_text = raw_text.replace("{", "(").replace("}", ")").strip('"')
                
                # CATAT KE DALAM FILE CSV SECARA OTOMATIS
                log_api_chat(personality_key, model_used, latency_duration, in_tok, out_tok, tot_tok, user_text, clean_text)
                
                return clean_text 

        except Exception as e:
            debug_log("AI ERROR", str(e))
            return f"[NEUTRAL] (Error Koneksi: {e})"

    def update_companion_name_string():
        # Akses variabel global
        p = globals().get("companion_personality")
        lang = persistent.cur_lang
        
        # Mapping Nama
        names_db = {
            "extraversion": {"en": "Iwank", "id": "Iwank"},
            "conscientiousness": {"en": "Onyen", "id": "Onyen"},
            "neuroticism": {"en": "Jakouko", "id": "Jakouko"},
            "openness": {"en": "Kitsuko", "id": "Kitsuko"},
            "agreeableness": {"en": "Susagi", "id": "Susagi"}
        }
        
        # Ambil nama (Default ke "AI Companion" jika tidak ketemu)
        new_name = names_db.get(p, {}).get(lang, "AI Companion")
        
        # Set variabel RenPy
        store.ai_name = new_name

# Loop ini akan membuat definisi image secara otomatis saat game dijalankan
init python:

    # 1. FUNGSI MESIN ANIMASI KEDIP (Dijalankan otomatis oleh Ren'Py)
    def auto_blink(st, at, img_normal, img_blink):
        # st = "shown time" (berapa detik gambar ini sudah tampil di layar)
        cycle = 4.2 # Total durasi 1 loop (4 detik melek + 0.2 detik kedip)
        current_time = st % cycle
        
        if current_time < 4.0:
            # Tetap melek sampai detik ke-4
            # (Angka kedua adalah sisa waktu sampai pergantian frame berikutnya)
            return Image(img_normal), 4.0 - current_time
        else:
            # Masuk detik 4.0 ke atas, ganti gambar jadi kedip
            return Image(img_blink), 4.2 - current_time

    # Daftar kepribadian
    personalities = ["neuroticism", "openness", "extraversion", "agreeableness", "conscientiousness"]

    # Mapping: Tag Emosi AI -> Nama File Akhiran
    emo_map = {
        "happy": "happy",
        "fear": "fear",
        "disgust": "disgust",
        "neutral": "neutral",
        "angry": "anger",
        "anger": "anger",
        "sad": "sadness",
        "sadness": "sadness",
        "surprise": "surprised",
        "surprised": "surprised"
    }

    # Mapping personality ke folder dan prefix nama file gambar
    folder_map = {
        "conscientiousness": "Conscientiousness",
        "extraversion": "Extraversion",
        "neuroticism": "Neuroticism",
        "openness": "Openness",
        "agreeableness": "Agreeableness"
    }

    prefix_map = {
        "conscientiousness": "Onyen",
        "extraversion": "Iwank",
        "neuroticism": "Jakouko",
        "openness": "Kitsuko",
        "agreeableness": "Susagi"
    }

    for p in personalities:
        folder = folder_map.get(p, "Conscientiousness")
        prefix = prefix_map.get(p, "Onyen")
        
        for key_emotion, file_suffix in emo_map.items():
            img_name = f"companion {p} {key_emotion}"
            file_path_normal = f"images/{folder}/{prefix} {file_suffix}.png"
            file_path_blink = f"images/{folder}/{prefix} {file_suffix}_blink.png" # template image blink
            
            # FITUR ANTI-CRASH: Cek apakah file kedipnya sudah kamu gambar/masukkan?
            if renpy.loadable(file_path_blink):
                # Jika file kedip ADA: Rakit menjadi animasi berulang (loop)
                anim_displayable = DynamicDisplayable(auto_blink, img_normal=file_path_normal, img_blink=file_path_blink)
                renpy.image(img_name, At(anim_displayable, companion_std))
            else:
                # Jika file kedip BELUM ADA: Tampilkan gambar biasa yang diam
                renpy.image(img_name, At(Image(file_path_normal), companion_std))

init python:
    # Fungsi print khusus biar menonjol di terminal
    def debug_log(tag, message):
        print(f"\n{'='*10} [DEBUG: {tag}] {'='*10}")
        print(str(message))
        print("="*30 + "\n")

init python:
    def check_music_completion():
        # Daftar ID award musik yang kamu buat tadi (misal: "music_dog", "music_cat", dsb)
        music_awards = ["dog", "cat", "civet", "rabbit", "fox"] # Sesuaikan dengan ID-mu
        
        # Hitung berapa yang sudah ada di memori
        count = 0
        for m in music_awards:
            if m in persistent.unlocked_awards:
                count += 1
        
        # Jika semua (5) sudah terbuka, berikan award utama
        if count == 5 and "music" not in persistent.unlocked_awards:
            persistent.unlocked_awards.append("music")
            unlock_achievement("You hear that?", "images/award_music.png")

# ==========================================
# SISTEM MEMORI AI (JSON SAVE/LOAD)
# ==========================================
init python:
    import json
    import os

    # Variabel global penampung ingatan saat ngobrol
    current_ai_memory = {}

    def load_ai_memory(player_name, companion_id, current_mbti="Unknown"):
        """Membaca file JSON ingatan. Jika belum ada, buat baru."""
        global current_ai_memory
        
        # Nama file rapi: misal "fuad_civet.json"
        filename = player_name.lower().replace(" ", "_") + "_" + companion_id + ".json"
        filepath = os.path.join(renpy.config.savedir, filename)

        if os.path.exists(filepath):
            with open(filepath, "r") as f:
                current_ai_memory = json.load(f)
                
                # Jika user punya MBTI baru dari tes terakhir, update ingatannya
                if current_mbti != "Unknown" and current_ai_memory.get("last_mbti") != current_mbti:
                    current_ai_memory["last_mbti"] = current_mbti
        else:
            # Jika belum pernah ngobrol, buat struktur ingatan baru
            current_ai_memory = {
                "player_name": player_name,
                "companion_id": companion_id,
                "last_mbti": current_mbti,
                "known_facts": [], # Tempat AI mencatat fakta penting
                "chat_history": [] 
            }
        
        return current_ai_memory

    def save_ai_memory():
        """Menyimpan ingatan aktif kembali ke file JSON lokal."""
        global current_ai_memory
        
        if not current_ai_memory:
            return 
            
        filename = current_ai_memory["player_name"].lower().replace(" ", "_") + "_" + current_ai_memory["companion_id"] + ".json"
        filepath = os.path.join(renpy.config.savedir, filename)

        with open(filepath, "w") as f:
            json.dump(current_ai_memory, f, indent=4)

    def get_all_profiles_data():
        """Memindai folder save, mengelompokkan nama, dan mengambil data paling baru."""
        import os
        import json
        import time
        
        player_dict = {}
        try:
            for filename in os.listdir(renpy.config.savedir):
                if filename.endswith(".json"):
                    filepath = os.path.join(renpy.config.savedir, filename)
                    with open(filepath, "r") as f:
                        data = json.load(f)
                        if "player_name" in data:
                            p_name = data["player_name"]
                            mod_time = os.path.getmtime(filepath)
                            
                            # Jika nama ini belum ada di list, ATAU file ini lebih baru dari file sebelumnya
                            if p_name not in player_dict or mod_time > player_dict[p_name]["raw_time"]:
                                date_str = time.strftime("%d %b %Y - %H:%M", time.localtime(mod_time))
                                player_dict[p_name] = {
                                    "name": p_name,
                                    "mbti": data.get("last_mbti", "Unknown"),
                                    "date": date_str,
                                    "raw_time": mod_time # Disimpan rahasia untuk sorting
                                }
        except:
            pass
            
        # Ubah dictionary menjadi list dan urutkan berdasarkan waktu paling baru
        profiles = list(player_dict.values())
        profiles.sort(key=lambda x: x["raw_time"], reverse=True)
        return profiles