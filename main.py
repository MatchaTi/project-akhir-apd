from services import clear_screen, enter_continue, check_role
from auth import register, login
from admin import main_admin
from user import main_user


def main():
    while True:
        clear_screen()
        print("Selamat Datang di Aplikasi Screening Kesehatan")
        print("Menu:")
        print("[1] Register")
        print("[2] Login")
        print("[3] Keluar")

        pilihan = input("Pilih menu\t: ")
        if pilihan == "1":
            register()
        elif pilihan == "2":
            user = login()

            if not user:
                print("Akun tidak ditemukan, silahkan registrasi!")
                enter_continue()
            else:
                admin = check_role(user["role"])

                if admin:
                    main_admin()
                else:
                    main_user()

        elif pilihan == "3":
            return
        else:
            print(f"Pilihan [{pilihan}] tidak tersedia!")
            enter_continue()


if __name__ == "__main__":
    main()
    clear_screen()
    print("Program Selesai!")
