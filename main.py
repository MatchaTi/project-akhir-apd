from services import clear_screen, enter_continue, check_role, install_dependencies #mengambil fungsi dari file services
from auth import register, login #mengambil fungsi dari file auth
from admin import main_admin #mengambil fungsi dari file admin
from user import main_user #mengambil fungsi dari file user


def main(): #fungsi utama Screening kesehatan 
    while True:
        clear_screen()#memanggil fungsi untuk membersihkan terminal
        print("Selamat Datang di Aplikasi Screening Kesehatan") #Print menu utama
        print("Menu:")
        print("[1] Register")
        print("[2] Login")
        print("[3] Keluar")

        pilihan = input("Pilih menu\t: ")#input pilihan menu
        if pilihan == "1":#jika user memilih/input 1 maka....
            register() #fungsi register dipanggil
        elif pilihan == "2": #jika user memilih 2 maka...
            user = login() #(Tanya adi)

            if not user :#jika akun tidak ditemukan
                print("Akun tidak ditemukan, silahkan registrasi!")#output jika user tidak ditemukan
                enter_continue()#memanggil fungsi enter_continue
            else :#jika akun user ditemukan 
                is_admin = check_role(user["role"])#mengecek apakah akun user adalah akun admin

                if is_admin:#jika akun user adalah akun admin
                    main_admin()#memanggil fungsi main/utama untuk admin
                else:#jika akun user adalah akun biasa
                    if user["verif"]:#jika user sudah diverifikasi
                        main_user(user)#memanggil fungsi main/utama untuk pengguna biasa
                    else:#jika user belum diverifikasi
                        print("Akun anda belum terverifikasi, silahkan tunggu...")#output info belum diverifikasi
                        enter_continue()#memanggil fungsi enter_continue

        elif pilihan == "3":#jika user memilih/input 3 maka....
            return #keluar dari loop
        else:#error handling jika input bukan berupa (1/2/3)
            print(f"Pilihan [{pilihan}] tidak tersedia!")
            enter_continue()#memanggil fungsi enter_continue



if __name__ == "__main__":
    install_dependencies()
    main()
    clear_screen()
    print("Program Selesai!")
