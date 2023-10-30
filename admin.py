from services import clear_screen, enter_continue, get_len_data
from crud import show_data, update_status, delete_user


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
            print("Daftar User")
            show_data()
            if get_len_data() == 0:
                print("Belum ada data!")
            enter_continue()
        elif pilihan == "2":
            clear_screen()
            print("Daftar User")
            show_data()

            if get_len_data() == 0:
                print("Belum ada data!")
                enter_continue()
            else:
                while True:
                    try:
                        clear_screen()
                        print("Daftar User")
                        show_data()
                        index = int(
                            input("Masukkan index user yang ingin diverifikasi: ")
                        )
                        if index > 0 and index <= get_len_data():
                            update_status(index)
                            break
                        else:
                            raise Exception("Data tidak ditemukan!")
                    except ValueError:
                        print("Input tidak valid!")
                        enter_continue()
                    except Exception as e:
                        print(e)
                        enter_continue()

                clear_screen()
                print("Daftar User")
                show_data()
                print("Data user berhasil diverifikasi!")
                enter_continue()
        elif pilihan == "3":
            print("Tampilkan Riwayat User")
        elif pilihan == "4":
            clear_screen()
            print("Daftar User")
            show_data()

            if get_len_data() == 0:
                print("Belum ada data!")
                enter_continue()
            else:
                while True:
                    try:
                        clear_screen()
                        print("Daftar User")
                        show_data()
                        index = int(input("Masukkan index user yang ingin dihapus: "))
                        if index > 0 and index <= get_len_data():
                            delete_user(index)
                            break
                        else:
                            raise Exception("Data tidak ditemukan!")
                    except ValueError:
                        print("Input tidak valid!")
                        enter_continue()
                    except Exception as e:
                        print(e)
                        enter_continue()

                clear_screen()
                print("Daftar User")
                show_data()
                print("Data user berhasil dihapus!")
                enter_continue()
        elif pilihan == "5":
            return
        else:
            print(f"Pilihan [{pilihan}] tidak tersedia!")
            enter_continue()
