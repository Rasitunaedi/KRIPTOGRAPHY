import math
import itertools
import tkinter as tk
from tkinter import messagebox

# === BAGIAN 1: Permutasi Menyeluruh ===
def hitung_menyeluruh():
    try:
        n = int(entry_n1.get())
        hasil = math.factorial(n)
        langkah = f"Rumus: P = n!\nPerhitungan: {n}! = "
        for i in range(n, 0, -1):
            langkah += str(i)
            if i > 1:
                langkah += " × "
        langkah += f" = {hasil}"

        text_hasil1.config(state='normal')
        text_hasil1.delete(1.0, tk.END)
        text_hasil1.insert(tk.END, f"Permutasi Menyeluruh (n!)\n\n{langkah}")
        text_hasil1.config(state='disabled')
    except:
        messagebox.showerror("Error", "Masukkan nilai n yang valid!")


# === BAGIAN 2: Permutasi Sebagian ===
def hitung_sebagian():
    try:
        n = int(entry_n2.get())
        r = int(entry_r2.get())
        if r > n or r < 0:
            raise ValueError
        hasil = math.factorial(n) // math.factorial(n - r)
        langkah = f"Rumus: P(n, r) = n! / (n - r)!\nPerhitungan:\n" \
                  f"{n}! / ({n}-{r})! = {n}! / {n - r}! = " \
                  f"{math.factorial(n)} / {math.factorial(n - r)} = {hasil}"

        text_hasil2.config(state='normal')
        text_hasil2.delete(1.0, tk.END)
        text_hasil2.insert(tk.END, f"Permutasi Sebagian P({n},{r})\n\n{langkah}")
        text_hasil2.config(state='disabled')
    except:
        messagebox.showerror("Error", "Masukkan nilai n dan r yang valid!\nSyarat: 0 ≤ r ≤ n")


# === BAGIAN 3: Permutasi Keliling ===
def hitung_keliling():
    try:
        n = int(entry_n3.get())
        hasil = math.factorial(n - 1) if n > 1 else 1
        langkah = f"Rumus: P_keliling = (n - 1)!\nPerhitungan: ({n} - 1)! = {n - 1}! = "
        for i in range(n - 1, 0, -1):
            langkah += str(i)
            if i > 1:
                langkah += " × "
        langkah += f" = {hasil}"

        text_hasil3.config(state='normal')
        text_hasil3.delete(1.0, tk.END)
        text_hasil3.insert(tk.END, f"Permutasi Keliling ((n-1)!)\n\n{langkah}")
        text_hasil3.config(state='disabled')
    except:
        messagebox.showerror("Error", "Masukkan nilai n yang valid!")


# === BAGIAN 4: Permutasi Data Berkelompok ===
def hitung_berkelompok():
    try:
        data_input = entry_data4.get().replace(" ", "")
        if not data_input:
            raise ValueError
        data = list(data_input)
        n = len(data)
        hasil_total = math.factorial(n)
        frek = {}
        for item in data:
            frek[item] = frek.get(item, 0) + 1

        langkah = f"Rumus: P = n! / (k1! × k2! × ...)\n"
        langkah += f"Data: {data}\nFrekuensi: {frek}\n\n"
        langkah += f"Perhitungan:\nP = {n}! / "
        penyebut = []
        penyebut_nilai = []
        penyebut_nilai_math = 1
        for k, v in frek.items():
            if v > 1:
                penyebut.append(f"{v}! ({k})")
                penyebut_nilai.append(f"{math.factorial(v)}")
                penyebut_nilai_math *= math.factorial(v)
            else:
                penyebut.append("1")
                penyebut_nilai.append("1")

        hasil_akhir = hasil_total // penyebut_nilai_math
        langkah += " × ".join(penyebut)
        langkah += f"\n= {math.factorial(n)} / (" + " × ".join(penyebut_nilai) + ")"
        langkah += f"\n= {math.factorial(n)} / {penyebut_nilai_math}"
        langkah += f"\n\n➡️ Jumlah Permutasi Berbeda = {hasil_akhir:,}"

        text_hasil4.config(state='normal')
        text_hasil4.delete(1.0, tk.END)
        text_hasil4.insert(tk.END, f"Permutasi Data Berkelompok\n\n{langkah}")
        text_hasil4.config(state='disabled')
    except:
        messagebox.showerror("Error", "Masukkan data huruf/angka dengan benar!")


# === BAGIAN 5: Permutasi Buku di Rak ===
def hitung_buku_rak():
    try:
        n = int(entry_n5.get())
        r = int(entry_r5.get())
        if n <= 0 or r <= 0:
            raise ValueError

        total = r ** n
        langkah = f"Rumus: Jumlah cara = rⁿ\nPerhitungan: {r}^{n} = {total}\n\n"
        langkah += f"Terdapat {total} cara menempatkan {n} buku di {r} rak.\n\n"

        # tampilkan kombinasi hanya jika jumlah kecil
        if n <= 3 and r <= 3:
            buku = [f"B{i+1}" for i in range(n)]
            rak = [f"R{j+1}" for j in range(r)]
            semua = list(itertools.product(rak, repeat=n))
            langkah += "Daftar semua cara:\n"
            for i, susunan in enumerate(semua, start=1):
                pasangan = [f"{buku[k]}→{susunan[k]}" for k in range(n)]
                langkah += f"{i}. " + ", ".join(pasangan) + "\n"

        text_hasil5.config(state='normal')
        text_hasil5.delete(1.0, tk.END)
        text_hasil5.insert(tk.END, f"Permutasi Buku di Rak\n\n{langkah}")
        text_hasil5.config(state='disabled')
    except:
        messagebox.showerror("Error", "Masukkan nilai n dan r yang valid! (harus > 0)")


# === GUI UTAMA ===
root = tk.Tk()
root.title("🧮 KALKULATOR PERMUTASI PYTHON")
root.geometry("800x850")
root.configure(bg="#f5f5f5")

# POSISI DI TENGAH LAYAR
root.update_idletasks()
lebar, tinggi = 800, 850
x = (root.winfo_screenwidth() // 2) - (lebar // 2)
y = (root.winfo_screenheight() // 2) - (tinggi // 2)
root.geometry(f"{lebar}x{tinggi}+{x}+{y}")

# SCROLL AREA
canvas = tk.Canvas(root, bg="#f5f5f5", highlightthickness=0)
scroll_y = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scroll_y.set)
scroll_y.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

main_frame = tk.Frame(canvas, bg="#f5f5f5")
canvas.create_window((0, 0), window=main_frame, anchor="n", width=780)

def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))
main_frame.bind("<Configure>", on_frame_configure)

judul = tk.Label(main_frame, text="🧮 KALKULATOR PERMUTASI PYTHON", 
                 font=("Arial", 18, "bold"), bg="#f5f5f5", fg="#333")
judul.pack(pady=15)


# === FRAME 1 ===
frame1 = tk.LabelFrame(main_frame, text="1️ Permutasi Menyeluruh", font=("Arial", 12, "bold"), 
                       bg="#e8f0fe", padx=10, pady=10)
frame1.pack(padx=15, pady=10)
tk.Label(frame1, text="Masukkan n:", font=("Arial", 11), bg="#e8f0fe").grid(row=0, column=0, padx=5, pady=5)
entry_n1 = tk.Entry(frame1, width=10)
entry_n1.grid(row=0, column=1, padx=5, pady=5)
tk.Button(frame1, text="Hitung", bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), command=hitung_menyeluruh).grid(row=0, column=2, padx=10)
text_hasil1 = tk.Text(frame1, height=5, width=80, font=("Consolas", 10))
text_hasil1.grid(row=1, column=0, columnspan=3, pady=5)
text_hasil1.config(state='disabled')


# === FRAME 2 ===
frame2 = tk.LabelFrame(main_frame, text="2️ Permutasi Sebagian", font=("Arial", 12, "bold"), 
                       bg="#fff3cd", padx=10, pady=10)
frame2.pack(padx=15, pady=10)
tk.Label(frame2, text="Masukkan n:", font=("Arial", 11), bg="#fff3cd").grid(row=0, column=0, padx=5, pady=5)
entry_n2 = tk.Entry(frame2, width=10)
entry_n2.grid(row=0, column=1, padx=5, pady=5)
tk.Label(frame2, text="Masukkan r:", font=("Arial", 11), bg="#fff3cd").grid(row=0, column=2, padx=5, pady=5)
entry_r2 = tk.Entry(frame2, width=10)
entry_r2.grid(row=0, column=3, padx=5, pady=5)
tk.Button(frame2, text="Hitung", bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), command=hitung_sebagian).grid(row=0, column=4, padx=10)
text_hasil2 = tk.Text(frame2, height=5, width=80, font=("Consolas", 10))
text_hasil2.grid(row=1, column=0, columnspan=5, pady=5)
text_hasil2.config(state='disabled')


# === FRAME 3 ===
frame3 = tk.LabelFrame(main_frame, text="3️ Permutasi Keliling", font=("Arial", 12, "bold"), 
                       bg="#e2f7e1", padx=10, pady=10)
frame3.pack(padx=15, pady=10)
tk.Label(frame3, text="Masukkan n:", font=("Arial", 11), bg="#e2f7e1").grid(row=0, column=0, padx=5, pady=5)
entry_n3 = tk.Entry(frame3, width=10)
entry_n3.grid(row=0, column=1, padx=5, pady=5)
tk.Button(frame3, text="Hitung", bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), command=hitung_keliling).grid(row=0, column=2, padx=10)
text_hasil3 = tk.Text(frame3, height=5, width=80, font=("Consolas", 10))
text_hasil3.grid(row=1, column=0, columnspan=3, pady=5)
text_hasil3.config(state='disabled')


# === FRAME 4 ===
frame4 = tk.LabelFrame(main_frame, text="4️ Permutasi Data Berkelompok", font=("Arial", 12, "bold"), 
                       bg="#f8d7da", padx=10, pady=10)
frame4.pack(padx=15, pady=10)
tk.Label(frame4, text="Masukkan Data (contoh: AABBC):", font=("Arial", 11), bg="#f8d7da").grid(row=0, column=0, padx=5, pady=5)
entry_data4 = tk.Entry(frame4, width=20)
entry_data4.grid(row=0, column=1, padx=5, pady=5)
tk.Button(frame4, text="Hitung", bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), command=hitung_berkelompok).grid(row=0, column=2, padx=10)
text_hasil4 = tk.Text(frame4, height=8, width=80, font=("Consolas", 10))
text_hasil4.grid(row=1, column=0, columnspan=3, pady=5)
text_hasil4.config(state='disabled')


# === FRAME 5 ===
frame5 = tk.LabelFrame(main_frame, text="5️ Permutasi Buku di Rak", font=("Arial", 12, "bold"), 
                       bg="#d1ecf1", padx=10, pady=10)
frame5.pack(padx=15, pady=10)
tk.Label(frame5, text="Masukkan jumlah buku (n):", font=("Arial", 11), bg="#d1ecf1").grid(row=0, column=0, padx=5, pady=5)
entry_n5 = tk.Entry(frame5, width=10)
entry_n5.grid(row=0, column=1, padx=5, pady=5)
tk.Label(frame5, text="Masukkan jumlah rak (r):", font=("Arial", 11), bg="#d1ecf1").grid(row=0, column=2, padx=5, pady=5)
entry_r5 = tk.Entry(frame5, width=10)
entry_r5.grid(row=0, column=3, padx=5, pady=5)
tk.Button(frame5, text="Hitung", bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), command=hitung_buku_rak).grid(row=0, column=4, padx=10)
text_hasil5 = tk.Text(frame5, height=8, width=90, font=("Consolas", 10))
text_hasil5.grid(row=1, column=0, columnspan=5, pady=5)
text_hasil5.config(state='disabled')

root.mainloop()
