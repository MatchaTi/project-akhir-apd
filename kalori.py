def kalori(gender):
    while True:
        try:
            BB = int(input("Berat Badan(KG)  :"))
            TB = int(input("Tinggi Badan(CM) :"))
            U = int(input("Usia(Tahun)      :"))

            if BB < 1 or TB < 1 or U < 0:
                raise Exception("Input tidak boleh minus!")

            break
        except ValueError:
            print("Input harus berupa angka!")
        except Exception as e:
            print(e)

    if gender == "Laki-Laki":
        BMR = 88.4 + (13.4 * BB) + (4.8 * TB) - (5.68 * U)
    else:
        BMR = 447.6 + (9.25 * BB) + (3.1 * TB) - (4.33 * U)

    result = {
        "program": "kalori",
        "bmr": BMR,
        "note": "Jumlah kalori yang dibutuhkan per hari adalah: ",
    }

    return result
