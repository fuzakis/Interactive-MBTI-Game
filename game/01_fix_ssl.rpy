init -999 python:
    import os
    import certifi

    # 1. Tentukan path manual ke file cacert.pem di dalam folder game
    # Ini mencari: game/python-packages/certifi/cacert.pem
    pem_path = os.path.join(renpy.config.gamedir, "python-packages", "certifi", "cacert.pem")

    # 2. Buat fungsi pengganti (Dummy Function)
    # Fungsi ini tugasnya cuma satu: Langsung kasih path-nya, jangan mikir aneh-aneh!
    def bypass_where():
        return pem_path

    # 3. Lakukan MONKEYPATCH (Pembajakan)
    # Kita timpa fungsi asli 'certifi.where' yang error dengan fungsi 'bypass_where' kita.
    # Sekarang, kalau ada library (requests/openai) yang panggil certifi.where(),
    # mereka akan menjalankan fungsi kita, bukan fungsi asli yang rusak.
    certifi.where = bypass_where

    # 4. Set Environment Variable sebagai cadangan (Safety Net)
    if os.path.exists(pem_path):
        os.environ["REQUESTS_CA_BUNDLE"] = pem_path
        os.environ["SSL_CERT_FILE"] = pem_path
        print(f"[SSL FIX] Berhasil membajak certifi. Path: {pem_path}")
    else:
        print(f"[SSL FIX] WARNING: File pem tidak ditemukan di {pem_path}")