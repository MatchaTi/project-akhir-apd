# mengambil fungsi dari file services
from services import clear_screen, enter_continue, check_role, install_dependencies

# mengambil fungsi dari file auth
from auth import register, login

# mengambil fungsi dari file admin
from admin import main_admin

# mengambil fungsi dari file user
from user import main_user


# fungsi utama Screening kesehatan
def main():
    while True:
        # memanggil fungsi untuk membersihkan terminal
        clear_screen()
        # Print menu utama
        print("Selamat Datang di Aplikasi Screening Kesehatan\n")
        print("Menu:")
        print("[1] Register")
        print("[2] Login")
        print("[3] Keluar")
        # input pilihan menu
        pilihan = input("\nPilih menu\t: ")
        # jika user memilih/input 1 maka....
        if pilihan == "1":
            # fungsi register dipanggil
            register()
        # jika user memilih 2 maka..
        elif pilihan == "2":
            # menyimpan nilai login ke variabel user
            user = login()
            # jika akun tidak ditemukan
            if not user:
                # output jika user tidak ditemukan
                print("Akun tidak ditemukan, silahkan registrasi!")
                # memanggil fungsi enter_continue
                enter_continue()
                # jika akun user ditemukan
            else:
                # mengecek apakah role user adalah admin atau user
                is_admin = check_role(user["role"])
                # jika role user adalah admin
                if is_admin:
                    # memanggil fungsi main/utama untuk admin
                    main_admin()
                # jika role user adalah user
                else:
                    # Jika user sudah di verifikasi maka
                    if user["verif"]:
                        # memanggil fungsi main/utama untuk pengguna biasa
                        main_user(user)
                    # jika user belum diverifikasi
                    else:
                        # output info belum diverifikasi
                        print("Akun anda belum terverifikasi, silahkan tunggu...")
                        # memanggil fungsi enter_continue
                        enter_continue()
        # jika user memilih/input 3 maka....
        elif pilihan == "3":
            # keluar dari loop
            return
        # error handling jika input bukan berupa (1/2/3)
        else:
            print(f"Pilihan [{pilihan}] tidak tersedia!")
            # memanggil fungsi enter_continue
            enter_continue()


# sebuah kondisi yang memeriksa apakah skrip Python ini sedang dijalankan sebagai program utama (main program)
# atau diimpor sebagai modul oleh program lain. Jika skrip ini adalah program utama yang dijalankan, maka blok kode di
# bawahnya akan dieksekusi.
if __name__ == "__main__":
    # memanggil fungsi yang digunakan untuk menginstall library yang dibutuhkan
    install_dependencies()
    # memanggil fungsi utama
    main()
    # memanggil fungsi untuk membersihkan terminal
    clear_screen()
    # output setelah program selesai dijalankan
    print("Program Selesai!")
