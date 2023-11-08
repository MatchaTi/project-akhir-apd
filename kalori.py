def kalori(gender):#fungsi fitur Kalori yang memakai argumen variabel gender
    while True:
        try:
            BB = int(input("Berat Badan(KG)  :"))#input berat badan user
            TB = int(input("Tinggi Badan(CM) :"))#input tinggi badan user
            U = int(input("Usia(Tahun)      :"))#input usia user

            if BB < 1 or TB < 1 or U < 0:#error handling jika input berat badan atau tinggi badan kurang dari 1 atau umur kurang dari 0
                raise Exception("Input tidak boleh minus!")#membuat pesan error sendiri dengan output kesalahan input

            break#keluar dari loop
        except ValueError:#error handling jika input bukan berupa angka
            print("Input harus berupa angka!")#output kesalahan input
        except Exception as e: # menangkap pesan error yang telah dibuat tadi
            print(e)

    if gender == "Laki-Laki":#kondisi rumus hitung kalori jika jenis kelamin user adalah laki-laki
        BMR = 88.4 + (13.4 * BB) + (4.8 * TB) - (5.68 * U)
    else: #kondisi rumus hitung kalori jika jenis kelamin user adalah perempuan
        BMR = 447.6 + (9.25 * BB) + (3.1 * TB) - (4.33 * U)

    result = {
        "program": "kalori",
        "bmr": BMR,
        "note": "Jumlah kalori yang dibutuhkan per hari adalah: ",
    }#hasil

    return result#mengembalikan hasil
