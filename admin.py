from services import clear_screen, enter_continue
from crud import show_data


def menu_admin():
    print("Menu Admin:")
    print("[1] Tampilkan Daftar User")
    print("[2] Verifikasi Data User")
    print("[3] Hapus User")
    print("[4] Tampilkan Riwayat User")
    print("[5] Logout")


def main_admin():
    while True:
        clear_screen()
        menu_admin()
        pilihan = input("Pilih menu\t: ")

        if pilihan == "1":
            clear_screen()
            print("Tampilkan Daftar User")
            show_data()
            enter_continue()
        elif pilihan == "2":
            print("Verifikasi Data User")
        elif pilihan == "3":
            print("Tampilkan Riwayat User")
        elif pilihan == "4":
            print("Hapus User")
        elif pilihan == "5":
            return
        else:
            print(f"Pilihan [{pilihan}] tidak tersedia!")
