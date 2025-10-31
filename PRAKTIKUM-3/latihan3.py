import tkinter as tk
from tkinter import messagebox
import itertools

# === Fungsi Faktorial ===
def faktorial(x):
    if x == 0 or x == 1:
        return 1
    hasil = 1
    for i in range(2, x + 1):
        hasil *= i
    return hasil

# === Fungsi Kombinasi ===
def kombinasi(n, r):
    if r > n:
        return 0
    faktorial_n = faktorial(n)
    faktorial_r = faktorial(r)
    faktorial_n_r = faktorial(n - r)
    hasil = faktorial_n // (faktorial_r * faktorial_n_r)
    return hasil, faktorial_n, faktorial_r, faktorial_n_r

# === Fungsi untuk membangkitkan kombinasi huruf ===
def kombinasi_huruf(n, r):
    huruf = [chr(65 + i) for i in range(n)]  # ['A', 'B', 'C', ...]
    semua = list(itertools.combinations(huruf, r))
    hasil_str = [", ".join(k) for k in semua]
    return hasil_str

# === Fungsi Proses Tombol ===
def hitung_kombinasi():
    try:
        n = int(entry_n.get())
        r = int(entry_r.get())

        if n < 0 or r < 0:
            messagebox.showerror("Error", "n dan r harus bilangan positif!")
            return
        if n > 26:
            messagebox.showerror("Error", "Maksimal n = 26 (A-Z)!")
            return

        hasil, fakt_n, fakt_r, fakt_n_r = kombinasi(n, r)
        kombinasi_list = kombinasi_huruf(n, r)

        langkah = (
            f"Rumus kombinasi:\n"
            f"C(n, r) = n! / (r! × (n - r)!)\n\n"
            f"Substitusi:\n"
            f"C({n}, {r}) = {n}! / ({r}! × ({n} - {r})!)\n\n"
            f"Perhitungan:\n"
            f"{n}! = {fakt_n}\n"
            f"{r}! = {fakt_r}\n"
            f"({n}-{r})! = {fakt_n_r}\n\n"
            f"C({n}, {r}) = {fakt_n} / ({fakt_r} × {fakt_n_r})\n"
            f"C({n}, {r}) = {hasil}\n\n"
            f"Artinya:\n"
            f"Terdapat {hasil} cara untuk memilih {r} objek dari total {n} objek.\n\n"
            f"== Daftar Kombinasi Huruf ==\n"
        )

        for i, kombinasi_item in enumerate(kombinasi_list, start=1):
            langkah += f"{i}. {kombinasi_item}\n"

        text_hasil.config(state='normal')
        text_hasil.delete(1.0, tk.END)
        text_hasil.insert(tk.END, langkah)
        text_hasil.config(state='disabled')

        # Tampilkan hasil ringkas di bawah tombol
        label_hasil_langsung.config(
            text=f"Hasil Kombinasi C({n}, {r}) = {hasil}",
            fg="darkblue"
        )

    except ValueError:
        messagebox.showerror("Error", "Masukkan hanya angka!")

# === Membuat Jendela Utama ===
root = tk.Tk()
root.title("Program Kombinasi (C(n, r)) dengan Inisial Huruf")
root.geometry("700x550")
root.configure(bg="#e8f0fe")

# Pusatkan jendela di layar
root.update_idletasks()
width = 700
height = 550
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry(f"{width}x{height}+{x}+{y}")

# === Judul ===
label_judul = tk.Label(
    root,
    text="💡 Program Kombinasi (C(n, r)) + Inisial Huruf",
    font=("Arial", 16, "bold"),
    bg="#e8f0fe",
    fg="#1a237e"
)
label_judul.pack(pady=10)

# === Frame Input ===
frame_input = tk.Frame(root, bg="#e8f0fe")
frame_input.pack(pady=10)

label_n = tk.Label(frame_input, text="Masukkan n (jumlah huruf):", font=("Arial", 12), bg="#e8f0fe")
label_n.grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_n = tk.Entry(frame_input, font=("Arial", 12), width=10)
entry_n.grid(row=0, column=1, padx=5, pady=5)

label_r = tk.Label(frame_input, text="Masukkan r (dipilih):", font=("Arial", 12), bg="#e8f0fe")
label_r.grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_r = tk.Entry(frame_input, font=("Arial", 12), width=10)
entry_r.grid(row=1, column=1, padx=5, pady=5)

# === Tombol Hitung ===
btn_hitung = tk.Button(
    root,
    text="Hitung Kombinasi",
    command=hitung_kombinasi,
    bg="#3949ab",
    fg="white",
    font=("Arial", 12, "bold"),
    relief="raised"
)
btn_hitung.pack(pady=10)

# === Label Hasil Langsung ===
label_hasil_langsung = tk.Label(
    root,
    text="",
    font=("Arial", 13, "bold"),
    bg="#e8f0fe"
)
label_hasil_langsung.pack(pady=5)

# === Kotak Teks Hasil Detail ===
label_hasil = tk.Label(
    root,
    text="Langkah Perhitungan dan Daftar Kombinasi:",
    font=("Arial", 12, "bold"),
    bg="#e8f0fe",
    fg="#0d47a1"
)
label_hasil.pack()

text_hasil = tk.Text(
    root,
    font=("Consolas", 11),
    height=18,
    width=80,
    wrap="word",
    state='disabled'
)
text_hasil.pack(padx=10, pady=5)

# === Jalankan Aplikasi ===
root.mainloop()
