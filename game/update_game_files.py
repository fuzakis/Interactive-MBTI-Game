import csv
import os
import re

folder_csv = ""

# --- KONFIGURASI ---
csv_files_map = {
    'id': 'soal_mbti_id.csv',
    'en': 'soal_mbti_en.csv' 
}
output_logic_file = 'questions_logic_generated.rpy'
output_data_file = 'questions_data.rpy'

# Mengatur Path Otomatis
script_dir = os.path.dirname(os.path.abspath(__file__))
# Path lengkap ke folder CSV
csv_base_path = os.path.join(script_dir, folder_csv)
logic_path = os.path.join(script_dir, output_logic_file)
data_path = os.path.join(script_dir, output_data_file)

# --- DEBUG: CEK LOKASI ---
print(f"Script berjalan di: {script_dir}")
print(f"Mencari CSV di: {csv_base_path}")
print("-" * 30)

# MAPPING BACKGROUND (Sesuaikan dengan nama file gambar di folder images)
bg_map_dict = {
    "Taman Kota": "bg taman",
    "Kafe": "bg kafe",
    "Ruang Kerja": "bg kantor",
    "Dapur": "bg dapur",
    "Jalan": "bg jalan",
    "Ruang Abstrak": "bg abstrak",
    "Stasiun": "bg stasiun",
    "Rumah": "bg room",

    #versi Inggris
    "City Park": "bg taman",
    "Cafe": "bg kafe",
    "Workspace": "bg kantor",
    "Kitchen": "bg dapur",
    "Abstract Space": "bg abstrak",
    "Public": "bg jalan",
    "Station": "bg stasiun",
    "Home": "bg room",
    "Arcade": "bg arcade"

    # Tambahkan mapping lain jika ada
}

def get_score_updates(option_text):
    """Mendeteksi tanda (E), (I), dll untuk update skor."""
    updates = []
    summary = []
    if "(E)" in option_text: updates.append("$ IE += 5"); summary.append("Extrovert")
    if "(I)" in option_text: updates.append("$ IE -= 5"); summary.append("Introvert")
    if "(N)" in option_text: updates.append("$ SN += 5"); summary.append("Intuitive")
    if "(S)" in option_text: updates.append("$ SN -= 5"); summary.append("Sensing")
    if "(F)" in option_text: updates.append("$ TF += 5"); summary.append("Feeling")
    if "(T)" in option_text: updates.append("$ TF -= 5"); summary.append("Thinking")
    if "(P)" in option_text: updates.append("$ JP += 5"); summary.append("Perceiving")
    if "(J)" in option_text: updates.append("$ JP -= 5"); summary.append("Judging")
    return updates, " & ".join(summary)

# Fungsi Sanitasi Teks
# PENTING: menetralkan karakter yang membuat Ren'Py ERROR saat teks ditampilkan:
#   {  }  -> tanda text-tag Ren'Py (mis. {b}, {size=..}) -> diganti ( )
#   [  ]  -> tanda interpolasi variabel Ren'Py (mis. [nama]) -> diganti ( )
#   %     -> format operator -> digandakan jadi %%
#   "     -> escape agar tidak menutup string di file .rpy
# Marker skor memakai ( ) yang aman, jadi penggantian di atas tidak menyentuhnya.
def sanitize_text(text):
    if not text: return ""
    text = text.replace('"', '\\"')
    text = text.replace("%", "%%")
    text = text.replace("[", "(").replace("]", ")")
    text = text.replace("{", "(").replace("}", ")")
    text = text.replace("\n", " ").replace("\r", "")
    return text.strip()

# Fungsi untuk memecah teks panjang menjadi list kalimat
# Memecah berdasarkan titik (.), tanda seru (!), atau tanda tanya (?)
def split_into_sentences(text):
    if not text: return []
    
    # Regex ini mencari tanda baca penutup kalimat, lalu memisahnya
    # Hasilnya adalah list kalimat-kalimat pendek
    # Contoh: "Halo. Apa kabar?" -> ["Halo.", "Apa kabar?"]
    sentences = re.split(r'(?<=[.!?])\s+', text)
    
    # Hapus string kosong jika ada
    return [s.strip() for s in sentences if s.strip()]

def generate_all_files():
    print(f"--- MULAI MEMPROSES ---")
    
    logic_lines = [] 
    master_packets_data = {} #data ambil dari ID
    total_soal_terproses = 0

    # LOOP UNTUK SETIAP BAHASA (ID dulu, lalu EN)
    for lang_code, filename in csv_files_map.items():
        csv_full_path = os.path.join(csv_base_path, filename)
        print(f"[{lang_code.upper()}] Membaca: {filename}")

        if not os.path.exists(csv_full_path):
            print(f"  WARNING: File {filename} tidak ditemukan! Lewati.")
            continue

        try:
            with open(csv_full_path, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                rows = list(reader)
        except Exception as e:
            print(f"  ERROR membaca file: {e}")
            continue

        # Header komentar di file logic
        logic_lines.append(f"\n# ================= BAHASA: {lang_code.upper()} =================\n")    
        
        current_packet = None

        for row in rows:
            if not row or len(row) < 2: continue

            val_col_1 = str(row[1]).strip()
            
            # 1. DETEKSI PAKET
            if "Paket" in val_col_1 and len(val_col_1) < 20:
                packet_letter = val_col_1.replace("Paket", "").strip().lower()
                
                # Kita hanya catat struktur paket saat memproses bahasa 'id'
                if lang_code == 'id' and packet_letter in ['a', 'b', 'c']:
                    current_packet = packet_letter
                    master_packets_data[current_packet] = []
                elif packet_letter in ['a', 'b', 'c']:
                    current_packet = packet_letter
                continue

            if current_packet is None or not val_col_1.isdigit() or len(row) < 6:
                continue

            # --- PARSING DATA ---
            no = val_col_1.zfill(2)
            dimensi = row[2].strip()
            raw_latar = str(row[3]).strip()
            bg_image = bg_map_dict.get(raw_latar, "bg default")
            narasi = sanitize_text(row[4])
            opt_a_text = sanitize_text(row[5].replace("A: ", ""))
            opt_b_text = sanitize_text(row[6].replace("B: ", "") if len(row) > 6 else "")
            
            # ID SOAL BASIC (Tanpa suffix bahasa)
            qid_base = f"q_{current_packet}_{no}"
            
            # Jika ini bahasa ID, simpan ke master data list
            if lang_code == 'id':
                master_packets_data[current_packet].append( (qid_base, dimensi) )
                total_soal_terproses += 1

            # --- GENERATE LABEL DENGAN SUFFIX BAHASA ---
            # Contoh: label show_question_q_a_01_id
            label_name = f"show_question_{qid_base}_{lang_code}"
            
            logic_lines.append(f"\nlabel {label_name}:\n")
            logic_lines.append(f"    scene {bg_image} with dissolve\n")
            logic_lines.append(f"    $ narasi_asli = \"{narasi}\"\n")
            
            # Fitur Pecah Kalimat
            pecahan_narasi = split_into_sentences(narasi)
            for kalimat in pecahan_narasi:
                logic_lines.append(f"    n \"{kalimat}\"\n")

            # Menu Pilihan
            logic_lines.append("\n    menu:\n")
            logic_lines.append(f"        \"{narasi}\"\n\n")

            # Opsi A
            updates_a, sum_a = get_score_updates(opt_a_text)
            logic_lines.append(f"        \"{opt_a_text}\":\n")
            for up in updates_a: logic_lines.append(f"            {up}\n")
            logic_lines.append(f"            $ user_choice_text = \"{opt_a_text}\"\n")
            logic_lines.append(f"            $ last_answer = \"{sum_a}\"\n")
            logic_lines.append(f"            jump {label_name}_A\n") # Jump ke label outcome bahasa yg sama

            # Opsi B
            updates_b, sum_b = get_score_updates(opt_b_text)
            logic_lines.append(f"\n        \"{opt_b_text}\":\n")
            for up in updates_b: logic_lines.append(f"            {up}\n")
            logic_lines.append(f"            $ user_choice_text = \"{opt_b_text}\"\n")
            logic_lines.append(f"            $ last_answer = \"{sum_b}\"\n")
            logic_lines.append(f"            jump {label_name}_B\n")
            
            logic_lines.append("\n")

            # --- OUTCOME LABELS ---
            # Label A
            logic_lines.append(f"\nlabel {label_name}_A:\n")
            logic_lines.append(f"    $ user_journey_summary.append(\"Di situasi {narasi}, user memilih: {opt_a_text}, dengan poin MBTI: {sum_a}\")\n")
            logic_lines.append(f"    call ai_react_logic\n") 
            logic_lines.append("    return\n")

            # Label B
            logic_lines.append(f"\nlabel {label_name}_B:\n")
            logic_lines.append(f"    $ user_journey_summary.append(\"Di situasi {narasi}, user memilih: {opt_b_text}, dengan poin MBTI: {sum_b}\")\n")
            logic_lines.append(f"    call ai_react_logic\n")
            logic_lines.append("    return\n")


    # --- PENULISAN FILE ---
    
    # 1. Tulis Logic (Berisi label ID dan EN)
    with open(logic_path, 'w', encoding='utf-8') as f:
        f.writelines(logic_lines)
    
    # 2. Tulis Data (Hanya sekali, pakai master data ID)
    if master_packets_data:
        with open(data_path, 'w', encoding='utf-8') as f:
            f.write("# FILE INI DIGENERATE OTOMATIS\n\n")
            packet_var_names = []
            
            for pkt in ['a', 'b', 'c']:
                if pkt in master_packets_data:
                    var_name = f"paket_{pkt}"
                    packet_var_names.append(var_name)
                    f.write(f"define {var_name} = [\n")
                    for q in master_packets_data[pkt]:
                        # q[0] adalah qid_base (q_a_01), tanpa suffix bahasa
                        f.write(f"    (\"{q[0]}\", \"{q[1]}\"),\n")
                    f.write("]\n\n")
            
            all_pkts_str = ", ".join(packet_var_names)
            f.write(f"define all_packets = [{all_pkts_str}]\n")
            
        print(f"\nSUKSES! Total soal unik (ID) diproses: {total_soal_terproses}")
        print(f"File terupdate:\n1. {output_logic_file}\n2. {output_data_file}")
    else:
        print("\nGAGAL: Tidak ada data paket yang valid.")

if __name__ == "__main__":
    generate_all_files()