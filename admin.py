# mengambil fungsi dari file service
from services import clear_screen, enter_continue, get_len_data

# mengambil fungsi dari file crud
from crud import show_data, update_status, delete_user, show_user_riwayat


# fungsi menampilkan menu
def menu_admin():
    print("Menu Admin:")
    print("[1] Tampilkan Daftar User")
    print("[2] Verifikasi Data User")
    print("[3] Tampilkan Riwayat User")
    print("[4] Hapus User")
    print("[5] Logout")


# fungsi pilih menu
def main_admin():
    while True:
        # memanggil fitur membersihkan terminal
        clear_screen()
        # memanggil menu
        menu_admin()
        # input user untuk memilih menu
        pilihan = input("Pilih menu\t: ")

        # kondisi jika admin ingin menampilkan data list user
        # jika admin memilih menu "1" maka,
        if pilihan == "1":
            clear_screen()
            print("Daftar User")
            # memanggil fungsi show_data dari file crud yang berfungsi untuk menampilkan list user/pasien
            show_data()
            # lakukan pengecekan terhadap data dengan memanggil fungsi get_len_data dari file service
            # get_len_data digunakan untuk menghitung seberapa banyak user yang ada
            # jika banyak user sama dengan 0 maka,
            if get_len_data() == 0:
                # tampilkan pesan ke terminal
                print("Belum ada data!")
            enter_continue()
        # kondisi jika admin ingin meng-update status verif user
        # jika admin memilih menu "2" maka,
        elif pilihan == "2":
            clear_screen()
            print("Daftar User")
            # memanggil fungsi show_data dari file crud yang berfungsi untuk menampilkan list user/pasien
            show_data()
            # lakukan pengecekan terhadap data dengan memanggil fungsi get_len_data dari file service
            # get_len_data digunakan untuk menghitung seberapa banyak user yang ada
            # jika banyak user sama dengan 0 maka,
            if get_len_data() == 0:
                # tampilkan pesan ke terminal
                print("Belum ada data!")
                enter_continue()
            # selain itu, jalankan kode program untuk memverifikasi data user
            else:
                # lakukan perulangan untuk memvalidasi inputan admin
                while True:
                    # semua kode program untuk memverifikasi data user kita taruh di dalam block try dan except untuk error handling
                    # block try digunakan untuk menjalankan kode program
                    # dan block except digunakan untuk menangkap error yang terjadi di block try
                    try:
                        clear_screen()
                        print("Daftar User")
                        # memanggil fungsi show_data dari file crud yang berfungsi untuk menampilkan list user/pasien
                        show_data()
                        # input index dari user
                        index = int(
                            input(
                                "Masukkan index user yang ingin diverifikasi (0 untuk keluar): "
                            )
                        )
                        # lakukan pengecekan terhadap input index
                        # jika index lebih dari sama dengan 1 dan index kurang dari sama dengan nilai kembalian dari
                        # fungsi get_len_data maka,
                        if index >= 1 and index <= get_len_data():
                            # input konfirmasi yakin
                            # dan hasil input tersebut ditransformasi menjadi lowercase menggunakan method lower
                            # sehingga jika input berupa "Y" akan berubah menjadi "y"
                            yakin = input(
                                "Yakin ingin memverifikasi data? (y/n): "
                            ).lower()
                            # lakukan pengecekan terhadap variable yakin
                            # jika input admin di variable yakin sama dengan "y" maka,
                            if yakin == "y":
                                # update status verif user menjadi true dari user yang memiliki index yang sama dengan input index
                                update_status(index)
                                clear_screen()
                                print("Daftar User")
                                # tampilkan daftar user
                                show_data()
                                # tampilkan pesan ke terminal
                                print("Data user berhasil diverifikasi!")
                                enter_continue()
                                # hentikan perulangan
                                break
                            # jika inputan yakin bukan "y" maka,
                            else:
                                # tampilkan pesan ke terminal
                                print("Gagal verifikasi data!")
                                enter_continue()
                                # akhiri perulangan
                                break
                        # kondisi dimana input index sama dengan 0 untuk admin kembali ke menu admin
                        elif index == 0:
                            # tampilkan pesan ke terminal
                            print("Tidak ada data yang diverifikasi!")
                            enter_continue()
                            # akhiri perulangan
                            break
                        # kondisi input index kurang dari 1 dan index lebih dari nilai kembalian dari fungsi get_len_data maka,
                        else:
                            # raise Exceptiion("...") digunakan untuk membuat pesan error sendiri yang pesan tersebut
                            # nantinya akan ditangkap pada block except dengan jenis error Exception
                            raise Exception("Data tidak ditemukan!")
                    # block ini digunakan untuk menangkap ValueError yang ada pada block try
                    # error seperti input index, yang di mana kita spesifik nilai index adalah integer
                    # kemudian kita tidak sengaja meng-inputkan huruf ke index, sehingga program menjadi error dan berhenti
                    # sehingga block except ValueError ini diperlukan untuk meng-handle contoh error yang di atas yang terjadi pada block try
                    except ValueError:
                        # tampilkan pesan error ke terminal
                        print("Input tidak valid!")
                        enter_continue()
                    # block ini digunakan untuk menangkap pesan error yang kita buat sendiri pada block try
                    # kemudian pesan tersebut kita alias ke sebagai variable e
                    except Exception as e:
                        # tampilkan pesan error ke terminal
                        print(e)
                        enter_continue()
        # kondisi jika admin ingin menampilkan data riwayat user
        # jika admin memilih menu "3" maka,
        elif pilihan == "3":
            clear_screen()
            print("Daftar User")
            # memanggil fungsi show_data dari file crud yang berfungsi untuk menampilkan list user/pasien
            show_data()
            # lakukan pengecekan terhadap data dengan memanggil fungsi get_len_data dari file service
            # get_len_data digunakan untuk menghitung seberapa banyak user yang ada
            # jika banyak user sama dengan 0 maka,
            if get_len_data() == 0:
                # tampilkan pesan ke terminal
                print("Belum ada data!")
                enter_continue()
            # selain itu, jalankan kode program untuk menampilkan data riwayat user
            else:
                # lakukan perulangan untuk memvalidasi inputan admin
                while True:
                    # semua kode program untuk menampilkan data riwayat user kita taruh di dalam block try dan except untuk error handling
                    # block try digunakan untuk menjalankan kode program
                    # dan block except digunakan untuk menangkap error yang terjadi di block try
                    try:
                        clear_screen()
                        print("Daftar User")
                        # menampilkan data user
                        show_data()
                        # input index dari user
                        index = int(input("Masukkan index user (0 untuk keluar): "))
                        # lakukan pengecekan terhadap input index
                        # jika index lebih dari sama dengan 1 dan index kurang dari sama dengan nilai kembalian dari
                        # fungsi get_len_data maka,
                        if index >= 1 and index <= get_len_data():
                            # memanggil fungsi show_user_riwayat dari file crud yang berfungsi untuk menampilkan tabel riwayat dari user
                            show_user_riwayat(index)
                            enter_continue()
                            clear_screen()
                            # akhiri perulangan
                            break
                        # kondisi dimana input index sama dengan 0 untuk admin kembali ke menu admin
                        elif index == 0:
                            # akhiri perulangan
                            break
                        # kondisi input index kurang dari 1 dan index lebih dari nilai kembalian dari fungsi get_len_data maka,
                        else:
                            # raise Exceptiion("...") digunakan untuk membuat pesan error sendiri yang pesan tersebut
                            # nantinya akan ditangkap pada block except dengan jenis error Exception
                            raise Exception("Data tidak ditemukan!")
                    # block ini digunakan untuk menangkap ValueError yang ada pada block try
                    # error seperti input index, yang di mana kita spesifik nilai index adalah integer
                    # kemudian kita tidak sengaja meng-inputkan huruf ke index, sehingga program menjadi error dan berhenti
                    # sehingga block except ValueError ini diperlukan untuk meng-handle contoh error yang di atas yang terjadi pada block try
                    except ValueError:
                        # tampilkan pesan error ke terminal
                        print("Input tidak valid!")
                        enter_continue()
                    # block ini digunakan untuk menangkap pesan error yang kita buat sendiri pada block try
                    # kemudian pesan tersebut kita alias ke sebagai variable e
                    except Exception as e:
                        # tampilkan pesan error ke terminal
                        print(e)
                        enter_continue()
        # kondisi jika admin ingin menghapus data user
        # jika admin memilih menu "4" maka,
        elif pilihan == "4":
            clear_screen()
            print("Daftar User")
            # memanggil fungsi show_data dari file crud yang berfungsi untuk menampilkan list user/pasien
            show_data()
            # lakukan pengecekan terhadap data dengan memanggil fungsi get_len_data dari file service
            # get_len_data digunakan untuk menghitung seberapa banyak user yang ada
            # jika banyak user sama dengan 0 maka,
            if get_len_data() == 0:
                # tampilkan pesan ke terminal
                print("Belum ada data!")
                enter_continue()
            # selain itu, jalankan kode program untuk menghapus data user
            else:
                # lakukan perulangan untuk memvalidasi inputan admin
                while True:
                    # semua kode program untuk menampilkan data riwayat user kita taruh di dalam block try dan except untuk error handling
                    # block try digunakan untuk menjalankan kode program
                    # dan block except digunakan untuk menangkap error yang terjadi di block try
                    try:
                        clear_screen()
                        print("Daftar User")
                        # menampilkan list user
                        show_data()
                        # input index dari user
                        index = int(
                            input(
                                "Masukkan index user yang ingin dihapus (0 untuk keluar): "
                            )
                        )
                        # lakukan pengecekan terhadap input index
                        # jika index lebih dari sama dengan 1 dan index kurang dari sama dengan nilai kembalian dari
                        # fungsi get_len_data maka,
                        if index >= 1 and index <= get_len_data():
                            # input konfirmasi yakin
                            # dan hasil input tersebut ditransformasi menjadi lowercase menggunakan method lower
                            # sehingga jika input berupa "Y" akan berubah menjadi "y"
                            yakin = input("Yakin ingin menghapus data? (y/n): ").lower()
                            # lakukan pengecekan terhadap variable yakin
                            # jika input admin di variable yakin sama dengan "y" maka,
                            if yakin == "y":
                                # hapus user berdasarkan input index
                                delete_user(index)
                                clear_screen()
                                print("Daftar User")
                                # tampilkan data list user
                                show_data()
                                print("Data user berhasil dihapus!")
                                enter_continue()
                                # akhiri perulangan
                                break
                            # jika inputan yakin bukan "y" maka,
                            else:
                                # tampilkan pesan ke terminal
                                print("Gagal menghapus data!")
                                enter_continue()
                                # akhiri perulangan
                                break
                        # kondisi dimana input index sama dengan 0 untuk admin kembali ke menu admin
                        elif index == 0:
                            # tampilkan pesan ke terminal
                            print("Tidak ada data yang terhapus!")
                            enter_continue()
                            # akhiri perulangan
                            break
                        # kondisi input index kurang dari 1 dan index lebih dari nilai kembalian dari fungsi get_len_data maka,
                        else:
                            # raise Exceptiion("...") digunakan untuk membuat pesan error sendiri yang pesan tersebut
                            # nantinya akan ditangkap pada block except dengan jenis error Exception
                            raise Exception("Data tidak ditemukan!")
                    # block ini digunakan untuk menangkap ValueError yang ada pada block try
                    # error seperti input index, yang di mana kita spesifik nilai index adalah integer
                    # kemudian kita tidak sengaja meng-inputkan huruf ke index, sehingga program menjadi error dan berhenti
                    # sehingga block except ValueError ini diperlukan untuk meng-handle contoh error yang di atas yang terjadi pada block try
                    except ValueError:
                        # tampilkan pesan error ke terminal
                        print("Input tidak valid!")
                        enter_continue()
                    # block ini digunakan untuk menangkap pesan error yang kita buat sendiri pada block try
                    # kemudian pesan tersebut kita alias ke sebagai variable e
                    except Exception as e:
                        # tampilkan pesan error ke terminal
                        print(e)
                        enter_continue()
        # kondisi jika inputan sama dengan "5" apabila ingin logout dan kembali ke menu utama
        elif pilihan == "5":
            # akhiri perulangan
            return
        # untuk meng-handle jika inputan pilihan tidak memenuhi perkondisian di atas
        else:
            # tampilkan pesan ke terminal
            print(f"Pilihan [{pilihan}] tidak tersedia!")
            enter_continue()
