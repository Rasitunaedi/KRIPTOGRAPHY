def substitusi_cipher(plaintext, aturan):
    """Tahap 1: Substitusi Cipher"""
    ciphertext = ''
    for char in plaintext.upper():
        if char in aturan:
            ciphertext += aturan[char]
        else:
            ciphertext += char
    return ciphertext


def transposisi_cipher(ciphertext, blok):
    """Tahap 2: Transposisi Cipher dengan jumlah kolom tertentu"""
    ciphertext = ciphertext.replace(" ", "")  # hilangkan spasi
    hasil = [''] * blok

    # Bagi setiap karakter ke dalam kolom sesuai indeks
    for i in range(len(ciphertext)):
        kolom = i % blok
        hasil[kolom] += ciphertext[i]

    # Gabungkan hasil per kolom
    return ''.join(hasil)


# === ATURAN SUBSTITUSI ===
aturan_substitusi = {
    'U': 'K',
    'N': 'N',
    'I': 'I',
    'K': 'K',
    'A': 'B',
    'S': 'X',
    'T': 'Z',
    'O': 'Y',
    'H': 'P',
    'M': 'C'
}

# === INPUT DATA ===
print("=== PROGRAM GABUNGAN SUBSTITUSI + TRANSPOSISI CIPHER ===")
plaintext = input("Masukkan plaintext: ").upper()

# === PROSES SUBSTITUSI ===
cipher_substitusi = substitusi_cipher(plaintext, aturan_substitusi)

# === PROSES TRANSPOSISI (4 blok) ===
cipher_transposisi = transposisi_cipher(cipher_substitusi, 4)

# === HASIL ===
print("\n=== HASIL ENKRIPSI ===")
print(f"Plaintext                         : {plaintext}")
print(f"Ciphertext (Substitusi)            : {cipher_substitusi}")
print(f"Ciphertext (Substitusi + Transposisi 4 blok) : {cipher_transposisi}")
