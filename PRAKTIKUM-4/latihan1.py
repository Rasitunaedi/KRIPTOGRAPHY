def substitusi_cipher(plaintext, aturan):
    """Fungsi untuk melakukan enkripsi substitusi cipher"""
    ciphertext = ''
    for char in plaintext.upper():
        if char in aturan:
            ciphertext += aturan[char]
        else:
            ciphertext += char
    return ciphertext


def buat_aturan(input_aturan):
    """Mengubah input teks aturan (misalnya 'A=K,B=N') menjadi dictionary"""
    aturan_dict = {}
    pasangan = input_aturan.split(',')
    for p in pasangan:
        if '=' in p:
            k, v = p.strip().split('=')
            aturan_dict[k.upper()] = v.upper()
    return aturan_dict


# === Input dari pengguna ===
print("=== PROGRAM SUBSTITUSI CIPHER ===")
plaintext = input("Masukkan plaintext: ")

input_aturan = input("Masukkan aturan substitusi (contoh: A=K,B=N,I=Z): ")
aturan_substitusi = buat_aturan(input_aturan)

# Tampilkan aturan hasil parsing
print("\nAturan substitusi yang digunakan:")
for k, v in aturan_substitusi.items():
    print(f"{k} → {v}")

# === Proses enkripsi ===
ciphertext = substitusi_cipher(plaintext, aturan_substitusi)

# === Hasil ===
print("\n=== HASIL ENKRIPSI ===")
print(f"Plaintext : {plaintext.upper()}")
print(f"Ciphertext: {ciphertext}")
