# === Class untuk logika Vigenere Cipher ===
class VigenereCipher:
    @staticmethod
    def encrypt(plaintext, key):
        plaintext = plaintext.upper().replace(" ", "")
        key = key.upper()
        ciphertext = ""
        detail = []
        full_key = (key * (len(plaintext) // len(key) + 1))[:len(plaintext)]

        for p, k in zip(plaintext, full_key):
            shift_p = ord(p) - 65
            shift_k = ord(k) - 65
            enc = (shift_p + shift_k) % 26
            c = chr(enc + 65)
            ciphertext += c
            detail.append(f"{p}({shift_p}) + {k}({shift_k}) = {enc} → {c}")
        return ciphertext, "\n".join(detail)

    @staticmethod
    def decrypt(ciphertext, key):
        ciphertext = ciphertext.upper().replace(" ", "")
        key = key.upper()
        plaintext = ""
        detail = []
        full_key = (key * (len(ciphertext) // len(key) + 1))[:len(ciphertext)]

        for c, k in zip(ciphertext, full_key):
            shift_c = ord(c) - 65
            shift_k = ord(k) - 65
            dec = (shift_c - shift_k + 26) % 26
            p = chr(dec + 65)
            plaintext += p
            detail.append(f"{c}({shift_c}) - {k}({shift_k}) = {dec} → {p}")
        return plaintext, "\n".join(detail)


# === Class Aplikasi berbasis console ===
class VigenereApp:
    def __init__(self):
        self.cipher = VigenereCipher()

    def run(self):
        print("=== 🔐 Vigenère Cipher Console App ===")
        while True:
            print("\nPilih menu:")
            print("1. Enkripsi")
            print("2. Deskripsi")
            print("3. Keluar")
            choice = input("Masukkan pilihan (1/2/3): ")

            if choice == "1":
                self.encrypt_action()
            elif choice == "2":
                self.decrypt_action()
            elif choice == "3":
                print("Terima kasih! Program selesai.")
                break
            else:
                print("Pilihan tidak valid, coba lagi!")

    def encrypt_action(self):
        text = input("\nMasukkan plaintext: ").strip()
        key = input("Masukkan key: ").strip()
        if not text or not key:
            print("⚠️  Plaintext dan key wajib diisi!")
            return
        cipher, detail = self.cipher.encrypt(text, key)
        print(f"\n🔒 Ciphertext: {cipher}")
        print("\n=== Detail Proses Enkripsi ===")
        print(detail)

    def decrypt_action(self):
        text = input("\nMasukkan ciphertext: ").strip()
        key = input("Masukkan key: ").strip()
        if not text or not key:
            print("⚠️  Ciphertext dan key wajib diisi!")
            return
        plain, detail = self.cipher.decrypt(text, key)
        print(f"\n🔓 Plaintext: {plain}")
        print("\n=== Detail Proses Deskripsi ===")
        print(detail)


# === Main Program ===
if __name__ == "__main__":
    app = VigenereApp()
    app.run()
