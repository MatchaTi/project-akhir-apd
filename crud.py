# meng-import module/library
# module os digunakan untuk menuliskan perintah ke dalam terminal secara terprogram
import os

# module json digunakan untuk memanipulasi data yang ada di dalam file users.json
import json

# module PrettyTable merupakan library eksternal yang di download melalui PIP
# yang digunakan untuk membuat table
from prettytable import PrettyTable


# variabel untuk tujuan file yang berisi nama file data users
file_path = "users.json"

# memeriksa apakah file dengan path yang diberikan (file_path) sudah ada
if not os.path.isfile(file_path):  #
    # jika file tidak ada, maka buat file baru dan buka dalam mode penulisan/write ("w")
    # blok with ini digunakan untuk mengatur sumber daya tertentu, seperti file
    # fungsi open() digunakan untuk membuka file dengan path yang diberikan (file_path).
    # Parameter kedua, yaitu "w", adalah mode penulisan yang digunakan untuk membuka file. Mode "w" (write)
    # digunakan untuk menulis data ke dalam file, dan jika file sudah ada, maka kontennya akan terhapus dan diganti
    # dengan konten baru.
    # dan as json_file adalah alias yang diberikan kepada file yang dibuka.
    with open(file_path, "w") as json_file:
        # buat data admin dalam bentuk dictionary
        admin = {"nama": "admin", "password": "admin", "role": "admin"}
        # Menulis data admin ke dalam file JSON dengan format yang lebih terbaca (indent=4)
        json.dump([admin], json_file, indent=4)


# fungsi untuk membaca data JSON
def load_data():
    # Membuka file yang berada di 'file_path' dalam mode default (baca) menggunakan 'with'.
    with open(file_path) as json_file:
        # Menggunakan modul 'json.load()' untuk membaca data JSON dari file yang dibuka.
        # data tersebut dikonversi menjadi list yang isi terdapat sekumpulan dictionary
        # Kemudian, data tersebut akan dikembalikan (return) sebagai hasil dari fungsi.
        return json.load(json_file)


# menyimpan nilai kembalian dari fungsi load_data ke variable data_users
data_users = load_data()


# fungsi menyimpan/menimpa data lama dengan data baru ke JSON
def save_data(json_data):
    with open(file_path, "w") as json_file:
        json.dump(json_data, json_file, indent=4)


# fungsi menambah data user baru yang digunakan pada menu registrasi
def create_data(json_data):
    # karena tipe data variable data_users ini adalah list sehingga, kita bisa menggunakan
    # method yang ada pada list untuk memanipulasi list
    data_users.append(json_data)
    # memanggil fungsi save_data untuk menimpa data lama dengan data baru untuk disimpan ke dalam file JSON(users.json)
    save_data(data_users)


# fungsi untuk menampilkan data dalam bentuk tabel
def show_data():
    # Menentukan kolom atau atribut yang akan ditampilkan dalam tabel
    table_fields = ["nama", "password", "gender", "verif", "role"]
    # inisiasi table menggunakan module PrettyTable
    table = PrettyTable()
    # Mengatur lebar padding (jarak antara isi kolom dan tepi) dalam tabel
    table.padding_width = 5
    # Menentukan judul (nama kolom) tabel dan kolom-kolom yang akan ditampilkan.
    table.field_names = ["N0."] + table_fields

    # Iterasi melalui data_users dan menambahkannya ke tabel.
    for i, row in enumerate(data_users[1:], start=1):
        # Menggabungkan nomor indeks (i) dengan data dari kolom yang dipilih (table_fields).
        row_to_display = [i] + [row[col] for col in table_fields]
        # Menambahkan baris data ke tabel.
        table.add_row(row_to_display)

    # Mencetak tabel yang telah dibuat.
    print(table)


# fungsi untuk mengubah status verif user yang digunakan pada menu admin
def update_status(index):
    # akses index data_users berdasarkan parameter fungsi ini kemudian akses dictionary dengan key "verif"
    # kemudian ubah nilainya menjadi true
    data_users[index]["verif"] = True
    # memanggil fungsi save_data untuk menimpa data lama dengan data baru untuk disimpan ke dalam file JSON(users.json)
    save_data(data_users)


# fungsi untuk menghapus data user yang digunakan pada menu admin
def delete_user(index):
    # gunakan method del untuk menghapus data user dengan mengakses index dari data_users berdasarkan parameter fungsi ini
    del data_users[index]
    # memanggil fungsi save_data untuk menimpa data lama dengan data baru untuk disimpan ke dalam file JSON(users.json)
    save_data(data_users)


# fungsi untuk menambahkan riwayat screening user
def user_screening(username, password, data):
    # assign nilai dari parameter data ke variable new_data
    new_data = data
    # lakukan perulangan dari variable data_users dimulai dari index 1, yang dimana index 1 dan seterusnya merupakan akun dengan role user
    # sedangkan index 0 merupakan akun dengan role admin
    # data merupakan representasi dari masing-masing data yang ada di dalam variable data_users
    for data in data_users[1:]:
        # lakukan pengecekan apabila nilai dari data dengan key "nama" sama dengan parameter "username" dan
        # nilai dari data dengan key "password" sama dengan parameter "password" maka,
        if data["nama"] == username and data["password"] == password:
            # tambahkan new_data ke dalam nilai data dengan key "riwayat"
            # nilai data dengan key "riwayat" bertipe data list
            # sehingga kita bisa menggunakan method-method list untuk memanipulasi nya, seperti method append
            data["riwayat"].append(new_data)
            # memanggil fungsi save_data untuk menimpa data lama dengan data baru untuk disimpan ke dalam file JSON(users.json)
            save_data(data_users)
            # akhiri perulangan
            break


# fungsi untuk menampilkan data riwayat user dalam bentuk tabel
def table_riwayat(data_riwayat, fields):
    # Menentukan kolom atau atribut yang akan ditampilkan dalam tabel berdasarkan parameter fields
    table_fields = fields
    # inisiasi table menggunakan module PrettyTable
    table = PrettyTable()
    # Mengatur lebar padding (jarak antara isi kolom dan tepi) dalam tabel
    table.padding_width = 5
    # Menentukan judul (nama kolom) tabel dan kolom-kolom yang akan ditampilkan.
    table.field_names = ["NO"] + table_fields

    # Iterasi melalui parameter data_riwayat dan menambahkannya ke tabel.
    for i, row in enumerate(data_riwayat, start=1):
        # Menggabungkan nomor indeks (i) dengan data dari kolom yang dipilih (table_fields).
        row_to_display = [i] + [row[col] for col in table_fields]
        # menambahkan baris data ke tabel
        table.add_row(row_to_display)

    # Mencetak tabel yang telah dibuat.
    print(table)


# fungsi untuk menampilkan riwayat user
def show_user_riwayat(index):
    # menampilkan menu fitur
    print("\nPilih Layanan:")
    print("[1] Kalkulator BMI")
    print("[2] Kalkulator Kalori")
    print("[3] Kalkulator Hidrasi")
    print("[4] Kalkulator Kebahagiaan")

    # inisialisasi variabel table_fields
    table_fields = []
    # inisialisasi variabel program
    program = ""
    while True:
        # input pilihan menu fitur yang ingin dilihat riwayatnya
        pilihan = input("\nPilih index program: ")
        # jika admin memilih 1 maka,
        if pilihan == "1":
            # header tabel riwayat
            table_fields = ["skor", "status", "note"]
            # nama program yang akan ditampilkan riwayatnya
            program = "bmi"
            # keluar dari looping
            break
        # jika admin memilih 2 maka,
        elif pilihan == "2":
            # header tabel riwayat
            table_fields = ["tinggi badan", "berat badan", "bmr"]
            # nama program yang akan ditampilkan riwayatnya
            program = "kalori"
            # keluar dari looping
            break
        # jika admin memilih 3 maka,
        elif pilihan == "3":
            # header tabel riwayat
            table_fields = ["note"]
            # nama program yang akan ditampilkan riwayatnya
            program = "hidrasi"
            # keluar dari looping
            break
        # jika admin memilih 4 maka,
        elif pilihan == "4":
            # header tabel riwayat
            table_fields = ["skor", "parameter"]
            # nama program yang akan ditampilkan riwayatnya
            program = "kebahagiaan"
            # keluar dari looping
            break
        # jika admin memilih pilihan yang bukan berupa angka 1-4 maka,
        else:
            # menampilkan bahwa pilihan tidak tersedia
            print("Pilihan tidak tersedia")
    # untuk mengakses/memfilterg riwayat program yang dipilih lalu memasukkannya ke variabel riwayat
    riwayat = [
        data for data in data_users[index]["riwayat"] if data["program"] == program
    ]

    # membersihkan terminal
    os.system("cls" if os.name == "nt" else "clear")
    # menampilkan tabel riwayat program yang dipilih
    print(f"List Riwayat: {program}")
    table_riwayat(riwayat, table_fields)

    # jika jumlah riwayat adalah o maka,
    if len(riwayat) == 0:
        # tampilkan info bahwa Belum ada data
        print("\nBelum ada data!")
