# mengambil fungsi dari file service
from services import clear_screen, enter_continue
# mengambil fungsi dari file hidrasi
from hidrasi import hidrasi
# mengambil fungsi dari file crud
from crud import user_screening, table_riwayat
# mengambil fungsi dari file kebahagiaan
from kebahagiaan import kebahagiaan
# mengambil fungsi dari file kalori
from kalori import kalori
# mengambil fungsi dari file bmi
from bmi import bmi

# fungsi untuk menampilkan menu user
def menu_user(name): 
    print(f"Profile = {name}")
    print("Pilih Layanan:")
    print("[1] Kalkulator BMI")
    print("[2] Kalkulator Kalori")
    print("[3] Kalkulator Hidrasi")
    print("[4] Kalkulator Kebahagiaan")
    print("[5] Logout")

# fungsi untuk menjalankan menu user
def main_user(user):
    while True:
        clear_screen()
        # 
        menu_user(user["nama"])

        # input pilihan menu user
        pilihan = input("Pilih layanan: ")

        # Jika user memilih pilihan 1 maka,
        if pilihan == "1":
            # memanggil fungsi bmi dan memasukkan ke variabel result
            result = bmi()
            # menambah riwayat user ke json
            user_screening(user["nama"], user["password"], result)
            # header untuk tabel riwayat
            table_fields = ["skor", "status", "note"]
            # menampilkan riwayat ke terminal sebagai tabel
            clear_screen()
            print("[-] Hasil Screening")
            table_riwayat([result], table_fields)
            enter_continue()
        # jika user memilih pilihan 2 maka,
        elif pilihan == "2":
            # memanggil fungsi kalori dan memasukkan ke variabel result
            result = kalori(user["gender"])
            # menambah riwayat user ke json
            user_screening(user["nama"], user["password"], result)
            # header untuk tabel riwayat
            table_fields = ["tinggi badan", "berat badan", "bmr"]
            # menampilkan riwayat ke terminal sebagai tabel
            clear_screen()
            print("[-] Hasil Screening")
            table_riwayat([result], table_fields)
            enter_continue()
        # Jika user memilih pilihan 3 maka,
        elif pilihan == "3":
            # memanggil fungsi hidrasi dan memasukkan ke variabel result
            result = hidrasi()
            # menambah riwayat user ke json
            user_screening(user["nama"], user["password"], result)
            # header untuk tabel riwayat
            table_fields = ["note"]
            # menampilkan riwayat ke terminal sebagai tabel
            clear_screen()
            print("[-] Hasil Screening")
            table_riwayat([result], table_fields)
            enter_continue()
        # Jika user memilih pilihan 4 maka,
        elif pilihan == "4":
            # memanggil fungsi kebahagiaan dan memasukkan ke variabel result
            result = kebahagiaan()
            # menambah riwayat user ke json
            user_screening(user["nama"], user["password"], result)
            # header untuk tabel riwayat
            table_fields = ["skor", "parameter"]
            # menampilkan riwayat ke terminal sebagai tabel
            clear_screen()
            print("[-] Hasil Screening")
            table_riwayat([result], table_fields)
            # menampilkan note 
            print(result["note"])
            enter_continue()
        # Jika user memilih pilihan 5 maka,
        elif pilihan == "5":
            # kembali ke menu awal
            return
        # Jika user memilih pilihan yang bukan berupa angka 1-5 maka,
        else:
            # menampilkan bahwa input user tidak tersedia
            print(f"Pilihan [{pilihan}] tidak tersedia!")
            enter_continue()
