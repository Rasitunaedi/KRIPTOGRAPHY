import random
from math import gcd

# -------------------------------
# Cek bilangan prima
# -------------------------------
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# -------------------------------
# Generate bilangan prima
# -------------------------------
def generate_prime():
    while True:
        p = random.randint(300, 500)
        if is_prime(p):
            return p

# -------------------------------
# Generate kunci ElGamal
# -------------------------------
def generate_keys():
    p = generate_prime()
    g = random.randint(2, p - 2)
    x = random.randint(1, p - 2)   # private key
    y = pow(g, x, p)               # public key
    return p, g, y, x

# -------------------------------
# Enkripsi satu karakter
# -------------------------------
def encrypt_char(m, p, g, y):
    k = random.randint(1, p - 2)
    while gcd(k, p - 1) != 1:
        k = random.randint(1, p - 2)

    a = pow(g, k, p)
    b = (pow(y, k, p) * m) % p
    return a, b, k

# -------------------------------
# Dekripsi satu karakter
# -------------------------------
def decrypt_char(a, b, x, p):
    s = pow(a, x, p)
    s_inv = pow(s, -1, p)
    m = (b * s_inv) % p
    return m, s, s_inv

# -------------------------------
# Program Utama
# -------------------------------
print("=== PROGRAM ELGAMAL (PLAINTEXT HURUF) ===")

p, g, y, x = generate_keys()

print("\n[1] PEMBENTUKAN KUNCI")
print("p (prima)        =", p)
print("g (generator)    =", g)
print("x (private key)  =", x)
print("y = g^x mod p    =", y)

plaintext = input("\nMasukkan plaintext (huruf): ")

ciphertext = []

# -------------------------------
# PROSES ENKRIPSI
# -------------------------------
print("\n[2] PROSES ENKRIPSI PER KARAKTER")
for i, char in enumerate(plaintext, start=1):
    m = ord(char)
    a, b, k = encrypt_char(m, p, g, y)
    ciphertext.append((a, b))

    print(f"\nKarakter ke-{i}")
    print("Huruf        =", char)
    print("ASCII (m)    =", m)
    print("k acak       =", k)
    print("a = g^k mod p=", a)
    print("b = y^k*m mod p =", b)

# -------------------------------
# TABEL HASIL
# -------------------------------
print("\n[3] HASIL ELGAMAL DALAM BENTUK TABEL")
print("-" * 100)
print("| No | Huruf | ASCII |    a    |    b    | s=a^x mod p | ASCII Dec | Hasil |")
print("-" * 100)

for i, ((a, b), ch) in enumerate(zip(ciphertext, plaintext), start=1):
    dec, s, _ = decrypt_char(a, b, x, p)
    print(f"| {i:<2} |  {ch:^5} | {ord(ch):^5} | {a:^7} | {b:^7} | {s:^11} | {dec:^9} |  {chr(dec)}   |")

print("-" * 100)

# -------------------------------
# PROSES DEKRIPSI
# -------------------------------
print("\n[4] PROSES DEKRIPSI")
hasil = ""
for i, (a, b) in enumerate(ciphertext, start=1):
    m, s, s_inv = decrypt_char(a, b, x, p)
    hasil += chr(m)

    print(f"\nCipher ke-{i}")
    print("a =", a)
    print("b =", b)
    print("s = a^x mod p =", s)
    print("s⁻¹ mod p    =", s_inv)
    print("m = b*s⁻¹ mod p =", m, "→", chr(m))

print("\n[5] HASIL AKHIR")
print("Ciphertext :", ciphertext)
print("Plaintext  :", hasil)

# -------------------------------
# TABEL HASIL AKHIR
# -------------------------------
print("\n[6] TABEL HASIL AKHIR ELGAMAL")
print("-" * 110)
print("| No | Plaintext | ASCII | Ciphertext (a, b)       | ASCII Dekripsi | Hasil Akhir |")
print("-" * 110)

for i, ((a, b), ch) in enumerate(zip(ciphertext, plaintext), start=1):
    ascii_plain = ord(ch)
    ascii_dec, _, _ = decrypt_char(a, b, x, p)
    hasil_char = chr(ascii_dec)

    print(f"| {i:<2} |    {ch:^7} | {ascii_plain:^5} | ({a:^5},{b:^5})          | {ascii_dec:^14} |     {hasil_char:^7} |")

print("-" * 110)

print("\nKESIMPULAN:")
print("Plaintext Asli     :", plaintext)
print("Ciphertext ElGamal :", ciphertext)
print("Plaintext Dekripsi :", hasil)
