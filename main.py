import os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    while True:
        clear_screen()
        print("Selamat Datang di Aplikasi Screening Kesehatan")
        print("Menu:")
        print("[1] Register")
        print("[2] Login")
        print("[3] Keluar")

        pilihan = input("Pilih menu\t:")
        if pilihan == "1":
            print("Register")
        elif pilihan == "2":
            print("Login")
        elif pilihan == "3":
            return


if __name__ == "__main__":
    main()
    clear_screen()
    print("Program Selesai!")
