# mengambil fungsi yang ada di file services
from services import enter_continue

# mengambil fungsi, variable yang ada di file crud
from crud import data_users, create_data


# fungsi register untuk registrasi user
def register():
    print("Register")
    # input untuk username user
    username = input("Masukkan nama anda\t: ")
    # input untuk password user
    password = input("Masukkan password anda\t: ")
    # inisialisasi variable gender
    gender = ""
    # perulangan untuk validasi gender
    while True:
        print("Jenis Kelamin:")
        print("[1] Laki-Laki")
        print("[2] Perempuan")
        # input untuk gender user
        gender = input("Masukkan jenis kelamin anda\t: ")

        # jika inputan user tidak sama dengan 1 dan 2, maka tampilkan output
        if gender != "1" and gender != "2":
            print("Maaf, di dunia ini hanya memiliki 2 jenis kelamin!")
        # selain itu jika inputan user sudah valid, akhiri perulangan
        else:
            break

    # disini kita menggunakan operator ternary
    # ternary adalah percabangan satu baris
    # jika dari input user gender itu "1" maka, assign nilai "Laki-Laki" ke variable gender
    # selain itu yaitu "2", assign nilai "Perempuan" ke variable gender
    gender = "Laki-Laki" if gender == "1" else "Perempuan"
    # kode di atas sama seperti kode comment di bawah ini
    # if gender == '1':
    #     gender = 'Laki-Laki'
    # else:
    #     gender = 'Perempuan'

    # lakukan perulangan pada variable data_users yang ada di file crud
    # data merupakan representasi dari setiap data yang ada di dalam variable data_users
    # variable data_users merupakan list yang di dalam nya terdapat sekumpulan dictionary data user
    for data in data_users:
        # lakukan pengecekan terhadap variable data
        # jika nilai data dengan key "nama" sama dengan inputan user username dan nilai data dengan key "password" sama dengan inputan user password maka,
        if data["nama"] == username and data["password"] == password:
            # tampilkan output
            print("Akun sudah terdaftar, silahkan login atau register!")
            # memanggil fungsi enter_continue
            enter_continue()
            # mengakhiri fungsi register sehingga kode di bawah return tidak akan dieksekusi
            return

    # membuat variable untuk menampung data user yang baru
    new_user = {
        "nama": username,
        "password": password,
        "gender": gender,
        "verif": False,
        "role": "user",
        "riwayat": [],
    }

    # memanggil fungsi create_data dan menaruh variable new_user sebagai argumen pada fungsi tersebut
    # agar data new_user di simpan ke dalam database yaitu file users.json
    create_data(new_user)
    # cetak pesan ke terminal
    print("Akun berhasil didaftarkan, Mohon tunggu data diverifikasi!")
    # memanggil fungsi enter_continue
    enter_continue()


# fungsi login untuk user melakukan login
def login():
    print("Login")
    # input untuk username user
    username = input("Masukkan nama anda\t: ")
    # input untuk password user
    password = input("Masukkan password anda\t: ")

    # lakukan perulangan pada variable data_users yang ada di file crud
    # data merupakan representasi dari setiap data yang ada di dalam variable data_users
    # variable data_users merupakan list yang di dalam nya terdapat sekumpulan dictionary data user
    for data in data_users:
        # lakukan pengecekan terhadap variable data
        # jika nilai data dengan key "nama" sama dengan inputan user username dan nilai data dengan key "password" sama dengan inputan user password maka,
        if data["nama"] == username and data["password"] == password:
            # kembalikan nilai data yang isinya data user, dan kode di bawah return tidak akan dieksekusi
            return data

    # jika kondisi di perkondisian dalam looping di atas tidak terpenuhi maka, kembalikan nilai False
    # karena akun tidak ditemukan
    return False
