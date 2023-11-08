# fungsi fitur Kalori yang memakai argumen variabel gender
def kalori(gender):
    while True:
        try:
            # input berat badan user
            BB = int(input("Berat Badan(KG)  :"))
            # input tinggi badan user
            TB = int(input("Tinggi Badan(CM) :"))
            # input usia user
            U = int(input("Usia(Tahun)      :"))
            # error handling jika input berat badan atau tinggi badan kurang dari 1 atau umur kurang dari 0
            if BB < 1 or TB < 1 or U < 0:
                # membuat pesan error sendiri dengan output kesalahan input
                raise Exception("Input tidak boleh minus!")
            # keluar dari loop
            break
        # error handling jika input bukan berupa angka
        except ValueError:
            # output kesalahan input
            print("Input harus berupa angka!")
        # menangkap pesan error yang telah dibuat tadi
        except Exception as e:
            print(e)
    # kondisi rumus hitung kalori jika jenis kelamin user adalah laki-laki
    if gender == "Laki-Laki":
        BMR = 88.4 + (13.4 * BB) + (4.8 * TB) - (5.68 * U)
    # kondisi rumus hitung kalori jika jenis kelamin user adalah perempuan
    else:
        BMR = 447.6 + (9.25 * BB) + (3.1 * TB) - (4.33 * U)
    # hasil
    result = {
        "program": "kalori",
        "berat badan": BB,
        "tinggi badan": TB,
        "bmr": round(BMR, 2),
    }
    # mengembalikan hasil
    return result
