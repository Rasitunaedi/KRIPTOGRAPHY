# Program Enkripsi dan Dekripsi RSA
# Nilai tetap: p=17, q=11, e=7

p = 17
q = 11
e = 7

# Hitung n dan phi(n)
n = p * q
phi = (p - 1) * (q - 1)

# Hitung kunci privat d (inverse modular dari e modulo phi)
d = pow(e, -1, phi)  # Menggunakan fungsi built-in Python untuk modular inverse

# Output kunci
print("=== Parameter RSA ===")
print(f"p          = {p}")
print(f"q          = {q}")
print(f"n (modulus)= {n}")
print(f"phi(n)     = {phi}")
print(f"e (public) = {e}")
print(f"d (private)= {d}")
print()
print("Kunci Publik : (e, n) =", e, ",", n)
print("Kunci Privat : (d, n) =", d, ",", n)
print()

# Fungsi enkripsi: c = m^e mod n
def encrypt_rsa(plaintext, e, n):
    return pow(plaintext, e, n)

# Fungsi dekripsi: m = c^d mod n
def decrypt_rsa(ciphertext, d, n):
    return pow(ciphertext, d, n)

# Contoh penggunaan
plaintext = 65  # Contoh pesan (harus < n, misalnya angka yang mewakili huruf 'A' = 65)

print("=== Contoh Enkripsi & Dekripsi ===")
ciphertext = encrypt_rsa(plaintext, e, n)
decrypted  = decrypt_rsa(ciphertext, d, n)

print(f"Plaintext  : {plaintext}")
print(f"Ciphertext : {ciphertext}")
print(f"Decrypted  : {decrypted}")

# Verifikasi
if decrypted == plaintext:
    print("Dekripsi berhasil! Pesan kembali ke asal.")
else:
    print("Dekripsi gagal.")