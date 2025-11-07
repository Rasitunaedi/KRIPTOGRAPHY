import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

# === Fungsi Enkripsi ===
def vigenere_encrypt(plaintext, key):
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

# === Fungsi Deskripsi ===
def vigenere_decrypt(ciphertext, key):
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

# === Fungsi Tombol ===
def encrypt_action():
    text = entry_plain.get()
    key = entry_key.get()
    if not text or not key:
        messagebox.showwarning("Peringatan", "Isi plaintext dan key terlebih dahulu!")
        return
    cipher, detail = vigenere_encrypt(text, key)
    entry_result.delete(0, tk.END)
    entry_result.insert(0, cipher)
    txt_detail.delete(1.0, tk.END)
    txt_detail.insert(tk.END, "🔒 === PROSES ENKRIPSI VIGENERE ===\n\n" + detail)

def decrypt_action():
    text = entry_plain.get()
    key = entry_key.get()
    if not text or not key:
        messagebox.showwarning("Peringatan", "Isi ciphertext dan key terlebih dahulu!")
        return
    plain, detail = vigenere_decrypt(text, key)
    entry_result.delete(0, tk.END)
    entry_result.insert(0, plain)
    txt_detail.delete(1.0, tk.END)
    txt_detail.insert(tk.END, "🔓 === PROSES DESKRIPSI VIGENERE ===\n\n" + detail)

def clear_all():
    entry_plain.delete(0, tk.END)
    entry_key.delete(0, tk.END)
    entry_result.delete(0, tk.END)
    txt_detail.delete(1.0, tk.END)

# === Desain GUI ===
root = tk.Tk()
root.title("🎨 Vigenère Cipher (Enkripsi & Deskripsi)")
root.geometry("800x650")
root.config(bg="#E6F0FA")  # biru lembut

# === Frame utama ===
frame = tk.Frame(root, bg="#FFFFFF", bd=3, relief="ridge")
frame.place(relx=0.5, rely=0.5, anchor="center", width=760, height=580)

# === Judul ===
lbl_title = tk.Label(
    frame,
    text="🔐 VIGENÈRE CIPHER",
    font=("Segoe UI", 16, "bold"),
    bg="#2196F3",
    fg="white",
    pady=10
)
lbl_title.pack(fill="x")

# === Frame input ===
frm_input = tk.Frame(frame, bg="#FFFFFF", pady=15)
frm_input.pack(fill="x", padx=30)

tk.Label(frm_input, text="Plaintext / Ciphertext:", font=("Segoe UI", 11), bg="#FFFFFF").grid(row=0, column=0, sticky="w")
entry_plain = ttk.Entry(frm_input, width=60, font=("Consolas", 11))
entry_plain.grid(row=0, column=1, padx=10, pady=8)

tk.Label(frm_input, text="Key:", font=("Segoe UI", 11), bg="#FFFFFF").grid(row=1, column=0, sticky="w")
entry_key = ttk.Entry(frm_input, width=30, font=("Consolas", 11))
entry_key.grid(row=1, column=1, padx=10, pady=8, sticky="w")

# === Tombol aksi ===
frm_btn = tk.Frame(frame, bg="#FFFFFF")
frm_btn.pack(pady=10)

def hover_in(btn, color):
    btn.config(bg=color)

def hover_out(btn, color):
    btn.config(bg=color)

btn_encrypt = tk.Button(frm_btn, text="🔒 Enkripsi", bg="#2196F3", fg="white", font=("Segoe UI", 10, "bold"),
                        activebackground="#1976D2", activeforeground="white", relief="flat",
                        padx=15, pady=5, command=encrypt_action)
btn_encrypt.grid(row=0, column=0, padx=10)
btn_encrypt.bind("<Enter>", lambda e: hover_in(btn_encrypt, "#1976D2"))
btn_encrypt.bind("<Leave>", lambda e: hover_out(btn_encrypt, "#2196F3"))

btn_decrypt = tk.Button(frm_btn, text="🔓 Deskripsi", bg="#4CAF50", fg="white", font=("Segoe UI", 10, "bold"),
                        activebackground="#388E3C", activeforeground="white", relief="flat",
                        padx=15, pady=5, command=decrypt_action)
btn_decrypt.grid(row=0, column=1, padx=10)
btn_decrypt.bind("<Enter>", lambda e: hover_in(btn_decrypt, "#388E3C"))
btn_decrypt.bind("<Leave>", lambda e: hover_out(btn_decrypt, "#4CAF50"))

btn_clear = tk.Button(frm_btn, text="🧹 Clear", bg="#FF9800", fg="white", font=("Segoe UI", 10, "bold"),
                      activebackground="#F57C00", relief="flat", padx=15, pady=5, command=clear_all)
btn_clear.grid(row=0, column=2, padx=10)
btn_clear.bind("<Enter>", lambda e: hover_in(btn_clear, "#F57C00"))
btn_clear.bind("<Leave>", lambda e: hover_out(btn_clear, "#FF9800"))

# === Output hasil ===
frm_output = tk.Frame(frame, bg="#FFFFFF", pady=10)
frm_output.pack(fill="x", padx=30)

tk.Label(frm_output, text="Hasil (Ciphertext / Plaintext):", font=("Segoe UI", 11, "bold"), bg="#FFFFFF").grid(row=0, column=0, sticky="w")
entry_result = ttk.Entry(frm_output, width=60, font=("Consolas", 11))
entry_result.grid(row=0, column=1, padx=10, pady=5)

# === Detail Proses ===
tk.Label(frame, text="🧩 Detail Proses:", font=("Segoe UI", 11, "bold"), bg="#FFFFFF").pack(anchor="w", padx=30)
txt_detail = scrolledtext.ScrolledText(frame, width=90, height=18, wrap=tk.WORD, font=("Consolas", 10), bg="#F7FAFC", relief="groove", bd=2)
txt_detail.pack(padx=30, pady=5)

# === Footer ===
tk.Label(frame, text="© 2025 Nadyaberkah | Vigenère Cipher GUI", bg="#E3F2FD", font=("Segoe UI", 9, "italic"), fg="#333").pack(fill="x", side="bottom")

root.mainloop()
