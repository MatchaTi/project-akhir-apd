# fungsi fitur hidrasi
def hidrasi():
    while True:
        try:  # input berat badan
            Berat = float(input("Berat badan: "))
            # error handling jika input dibawah 0
            if Berat < 0:
                # membuat pesan error sendiri dengan output kesalahan input
                raise Exception("Input tidak boleh minus!")
            # keluar dari loop
            break
        # output kesalahan input
        except ValueError:
            print("Input harus berupa angka!")
        # menangkap pesan error yang dibuat tadi
        except Exception as e:
            print(e)
    # hitung berapa liter air yang harus diminum
    Liter = (Berat * 30) / 1000
    # hitung berapa gelas air yang harus diminum
    Gelas = round((Berat * 30) / 220)
    # hasil
    result = {
        "program": "hidrasi",
        "note": f"Jumlah air yang harus diminum: {Liter} liter/hari atau setara dengan {Gelas} gelas",
    }
    # mengembalikan hasil
    return result
