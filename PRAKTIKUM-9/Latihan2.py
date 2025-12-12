import random
import math
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

# Daftar bilangan prima
primes = [53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
          109, 113, 127, 131, 137, 139, 149, 151, 157, 163,
          167, 173, 179, 181, 191, 193, 197, 199]

# ======================================================
# FUNGSI RSA
# ======================================================

def generate_keys():
    global p, q, n, phi, e, d

    debug = ""

    p = random.choice(primes)
    q = random.choice(primes)
    while p == q:
        q = random.choice(primes)

    debug += f"p terpilih: {p}\nq terpilih: {q}\n\n"
    n = p * q
    debug += f"n = {p} * {q} = {n}\n\n"

    phi = (p - 1) * (q - 1)
    debug += f"phi(n) = {phi}\n\n"

    e = random.randint(2, phi - 1)
    while math.gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    debug += f"e terpilih: {e}\n"
    debug += f"Public Key: (e={e}, n={n})\n\n"

    d = pow(e, -1, phi)
    debug += f"d = {d}\nPrivate Key: (d={d}, n={n})\n"

    output_debug.delete(1.0, tk.END)
    output_debug.insert(tk.END, debug)

    entry_n.config(state="normal")
    entry_e.config(state="normal")
    entry_d.config(state="normal")

    entry_n.delete(0, tk.END)
    entry_e.delete(0, tk.END)
    entry_d.delete(0, tk.END)

    entry_n.insert(0, str(n))
    entry_e.insert(0, str(e))
    entry_d.insert(0, str(d))

    entry_n.config(state="readonly")
    entry_e.config(state="readonly")
    entry_d.config(state="readonly")

    messagebox.showinfo("Sukses", "Kunci RSA berhasil dibuat!")


def proses_enkripsi():
    if 'n' not in globals() or 'e' not in globals():
        messagebox.showerror("Error", "Silakan generate kunci RSA terlebih dahulu.")
        return

    plaintext_text = entry_plain.get()
    if plaintext_text == "":
        messagebox.showerror("Error", "Masukkan plaintext terlebih dahulu!")
        return

    plaintext_bytes = plaintext_text.encode('utf-8')
    max_bytes = (n.bit_length() - 1) // 8

    chunks = [plaintext_bytes[i:i+max_bytes] for i in range(0, len(plaintext_bytes), max_bytes)]

    ciphertext_list = []
    debug_lines = []

    for i, ch in enumerate(chunks):
        m = int.from_bytes(ch, 'big')
        c = pow(m, e, n)
        ciphertext_list.append(c)
        debug_lines.append(f"blok {i}: m={m} -> c={c}")

    ciphertext_str = f"{len(plaintext_bytes)}|{','.join(str(c) for c in ciphertext_list)}"
    entry_cipher.delete(0, tk.END)
    entry_cipher.insert(0, ciphertext_str)

    output_debug.insert(tk.END,
        "\n=== ENKRIPSI TEKS ===\n" + "\n".join(debug_lines) + "\n"
    )

    messagebox.showinfo("Enkripsi", "Enkripsi teks berhasil!")


def proses_dekripsi():
    if 'n' not in globals() or 'd' not in globals():
        messagebox.showerror("Error", "Silakan generate kunci RSA terlebih dahulu.")
        return

    cipher_input = entry_cipher.get().strip()
    if cipher_input == "":
        messagebox.showerror("Error", "Masukkan ciphertext terlebih dahulu!")
        return

    orig_len_str, c_list_str = cipher_input.split("|", 1)
    orig_len = int(orig_len_str)
    ciphertext_ints = [int(x) for x in c_list_str.split(",")]

    max_bytes = (n.bit_length() - 1) // 8
    decrypted_parts = []

    debug_lines = []

    for i, c in enumerate(ciphertext_ints):
        m = pow(c, d, n)
        part = m.to_bytes(max_bytes, 'big').lstrip(b'\x00')
        decrypted_parts.append(part)
        debug_lines.append(f"blok {i}: c={c} -> m={m}")

    restored_bytes = b"".join(decrypted_parts)[:orig_len]
    restored_text = restored_bytes.decode('utf-8')

    entry_decrypt.delete(0, tk.END)
    entry_decrypt.insert(0, restored_text)

    output_debug.insert(tk.END,
        "\n=== DEKRIPSI TEKS ===\n" + "\n".join(debug_lines) + "\n"
    )

    messagebox.showinfo("Dekripsi", "Dekripsi berhasil!")

# ======================================================
# GUI DENGAN WARNA
# ======================================================

root = tk.Tk()
root.title("Program RSA - Dengan Form (Colored GUI)")
root.geometry("900x750")

# =========== WARNA LATAR UTAMA ===========
root.configure(bg="#B3E5FC")     # biru muda

# =========== GAYA TTK ===========
style = ttk.Style()
style.theme_use("clam")

style.configure("TFrame", background="white")
style.configure("TLabel", background="white", font=("Segoe UI", 10))
style.configure("TEntry", padding=3)
style.configure("TButton",
                background="#0277BD",
                foreground="white",
                padding=6)
style.map("TButton",
          background=[("active", "#01579B")])

# FRAME PUTIH (CARD)
frame = ttk.Frame(root, padding=20)
frame.pack(pady=20, padx=20, fill="both", expand=True)

# ================= WIDGET =================
btn_key = ttk.Button(frame, text="Generate Key RSA Acak", command=generate_keys)
btn_key.grid(row=0, column=0, pady=5, sticky="w")

ttk.Label(frame, text="n:").grid(row=1, column=0, sticky="w")
entry_n = ttk.Entry(frame, width=60)
entry_n.grid(row=1, column=1, columnspan=1)

ttk.Label(frame, text="e (public):").grid(row=2, column=0, sticky="w")
entry_e = ttk.Entry(frame, width=60)
entry_e.grid(row=2, column=1, columnspan=1)

ttk.Label(frame, text="d (private):").grid(row=3, column=0, sticky="w")
entry_d = ttk.Entry(frame, width=60)
entry_d.grid(row=3, column=1, columnspan=1)

ttk.Label(frame, text="Plaintext (Teks):").grid(row=4, column=0, sticky="w")
entry_plain = ttk.Entry(frame, width=60)
entry_plain.grid(row=4, column=1)

btn_encrypt = ttk.Button(frame, text="Enkripsi →", command=proses_enkripsi)
btn_encrypt.grid(row=4, column=2, padx=5)

ttk.Label(frame, text="Ciphertext:").grid(row=5, column=0, sticky="w")
entry_cipher = ttk.Entry(frame, width=60)
entry_cipher.grid(row=5, column=1)

btn_decrypt = ttk.Button(frame, text="Dekripsi →", command=proses_dekripsi)
btn_decrypt.grid(row=5, column=2, padx=5)

ttk.Label(frame, text="Hasil Dekripsi:").grid(row=6, column=0, sticky="w")
entry_decrypt = ttk.Entry(frame, width=60)
entry_decrypt.grid(row=6, column=1)

ttk.Label(frame, text="Output Debug:").grid(row=7, column=0, sticky="nw", pady=10)

# AREA DEBUG DENGAN WARNA GELAP
output_debug = scrolledtext.ScrolledText(frame,
                                         width=100,
                                         height=25,
                                         bg="#080808",
                                         fg="#E0E0E0",
                                         insertbackground="white")
output_debug.grid(row=8, column=0, columnspan=4)

root.mainloop()
