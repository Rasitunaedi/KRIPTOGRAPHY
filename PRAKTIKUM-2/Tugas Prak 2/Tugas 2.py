# Program Kalkulator Hybrid
# Tugas Praktikum 2

def kalkulator_hybrid():
    print("=== KALKULATOR HYBRID ===")
    ekspresi = input("Masukkan ekspresi (contoh: 4+4-3 atau 5 - 3 * 4): ")

    try:
        # Menghapus spasi agar ekspresi bisa diproses dengan atau tanpa spasi
        ekspresi_bersih = ekspresi.replace(" ", "")

        # Memproses hasil ekspresi matematika
        hasil = eval(ekspresi_bersih)

        # Menampilkan hasil
        print(f"Ekspresi  : {ekspresi}")
        print(f"Hasil     : {hasil}")
    except Exception as e:
        print("Terjadi kesalahan dalam perhitungan!")
        print(f"Detail error: {e}")


# Jalankan program
kalkulator_hybrid()
