
def biner_ke_desimal_heksa():
    biner = input("Masukkan bilangan biner: ")
    try:
        desimal = int(biner, 2)
        heksa = hex(desimal).upper().replace("0X", "")
        print(f"\nHasil Konversi:")
        print(f"Desimal     : {desimal}")
        print(f"Hexadesimal : {heksa}\n")
    except ValueError:
        print("Input bukan bilangan biner yang valid!\n")

def oktal_ke_desimal_biner_heksa():
    oktal = input("Masukkan bilangan oktal: ")
    try:
        desimal = int(oktal, 8)
        biner = bin(desimal).replace("0b", "")
        heksa = hex(desimal).upper().replace("0X", "")
        print(f"\nHasil Konversi:")
        print(f"Desimal     : {desimal}")
        print(f"Biner       : {biner}")
        print(f"Hexadesimal : {heksa}\n")
    except ValueError:
        print("Input bukan bilangan oktal yang valid!\n")

def heksa_ke_desimal_biner_oktal():
    heksa = input("Masukkan bilangan hexadesimal: ")
    try:
        desimal = int(heksa, 16)
        biner = bin(desimal).replace("0b", "")
        oktal = oct(desimal).replace("0o", "")
        print(f"\nHasil Konversi:")
        print(f"Desimal : {desimal}")
        print(f"Biner   : {biner}")
        print(f"Oktal   : {oktal}\n")
    except ValueError:
        print("Input bukan bilangan hexadesimal yang valid!\n")

def menu():
    while True:
        print("=== PROGRAM KONVERSI BILANGAN ===")
        print("1. Biner ke Desimal dan Hexadesimal")
        print("2. Oktal ke Desimal, Biner, dan Hexadesimal")
        print("3. Hexadesimal ke Desimal, Biner, dan Oktal")
        print("4. Keluar")
        pilihan = input("Pilih menu (1/2/3/4): ")

        if pilihan == '1':
            biner_ke_desimal_heksa()
        elif pilihan == '2':
            oktal_ke_desimal_biner_heksa()
        elif pilihan == '3':
            heksa_ke_desimal_biner_oktal()
        elif pilihan == '4':
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid!\n")

if __name__ == "__main__":
    menu()
