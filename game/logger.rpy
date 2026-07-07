init python:
    import os
    import time
    import csv
    import json

    # 1. Logger untuk setiap Chat (API Usage)
    def log_api_chat(karakter, model, latency, in_tok, out_tok, tot_tok, user_input, ai_response):
        # MENGGUNAKAN GAMEDIR AGAR MASUK KE FOLDER GAME
        log_path = os.path.join(renpy.config.gamedir, "PA_Log_API_Chat.csv")
        file_exists = os.path.exists(log_path)
        
        with open(log_path, mode="a", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["Waktu", "Karakter", "Model", "Latency (Detik)", "In_Token", "Out_Token", "Total_Token", "Prompt_User", "Respons_AI"])
            
            waktu = time.strftime("%Y-%m-%d %H:%M:%S")
            writer.writerow([waktu, karakter, model, f"{latency:.2f}", in_tok, out_tok, tot_tok, user_input, ai_response])

    # 2. Logger untuk Hasil MBTI & Memori AI di Akhir Game
    def log_mbti_result(nama_player, mbti_hasil, spirit_animal, skor_mentah, memori_ai):
        log_path = os.path.join(renpy.config.gamedir, "PA_Log_MBTI_Akhir.csv")
        file_exists = os.path.exists(log_path)
        
        with open(log_path, mode="a", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["Waktu", "Nama_Player", "Hasil_MBTI", "Spirit_Animal", "Skor_Mentah (IE,SN,TF,JP)", "Memori_Akhir"])
            
            waktu = time.strftime("%Y-%m-%d %H:%M:%S")
            writer.writerow([waktu, nama_player, mbti_hasil, spirit_animal, skor_mentah, json.dumps(memori_ai, ensure_ascii=False)])

    # 3. Logger Rekapitulasi 1x Main Penuh
    def log_rekap_permainan(karakter, total_chat, in_tok, out_tok, tot_tok):
        log_path = os.path.join(renpy.config.gamedir, "PA_Rekap_10_Permainan.csv")
        file_exists = os.path.exists(log_path)
        
        with open(log_path, mode="a", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["Percobaan", "Waktu_Selesai", "Karakter", "Total_Interaksi", "Total_Input_Tokens", "Total_Output_Tokens", "Grand_Total_Tokens"])
            
            # Hitung ini percobaan ke berapa
            percobaan_ke = 1
            if file_exists:
                with open(log_path, "r", encoding="utf-8") as f_read:
                    percobaan_ke = sum(1 for row in f_read) # Menghitung jumlah baris termasuk header
            
            waktu = time.strftime("%Y-%m-%d %H:%M:%S")
            writer.writerow([percobaan_ke, waktu, karakter, total_chat, in_tok, out_tok, tot_tok])