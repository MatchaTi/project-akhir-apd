# fungsi fitur BMI
def bmi():
    while True:
        try:
            # input berat badan user
            BB = float(input("Berat Badan(KG)  :"))
            # input tinggi badan user
            TB = float(input("Tinggi Badan(CM) :"))
            # menghitung BMI
            BMI = BB / ((TB / 100) * (TB / 100))

            # error handling jika input berat badan atau tinggi badan dibawah 0
            if BB < 0 or TB < 0:
                # membuat pesan error sendiri dengan output kesalahan input
                raise Exception("Berat atau tinggi badan tidak boleh minus!")
            # keluar loop
            break
        # error handling jika input bukan angka
        except ValueError:
            # output kesalahan input
            print("Input harus berupa angka!")
        # menangkap pesan error yang telah dibuat tadi
        except Exception as e:
            print(e)
    # Hasil
    result = {"program": "bmi", "status": "", "note": "", "skor": 0}
    # Pembulatan hasil BMI
    BMI = round(BMI, 2)
    # Kondisi jika hasil BMI lebih dari atau sama dengan 27
    if BMI >= 27:
        result["status"] = "Obesitas"
        result["note"] = "Kelebihan berat badan tingkat berat"
        result["skor"] = BMI
    # Kondisi jika hasil BMI lebih dari atau sama dengan 25.1 dan kurang dari atau sama dengan 26.9
    elif BMI >= 25.1 and BMI <= 26.9:
        result["status"] = "Obesitas"
        result["note"] = "Kelebihan berat badan tingkat ringan"
        result["skor"] = BMI
    # Kondisi jika hasil BMI lebih dari atau sama dengan 18.5 dan kurang dari atau sama dengan 25
    elif BMI >= 18.5 and BMI <= 25:
        result["status"] = "Normal"
        result["note"] = "Berat badan ideal"
        result["skor"] = BMI
    # Kondisi jika hasil BMI lebih dari atau sama dengan 17 dan kurang dari atau sama dengan 18.4
    elif BMI >= 17 and BMI <= 18.4:
        result["status"] = "Kurus"
        result["note"] = "Kekurangan Berat badan ringan"
        result["skor"] = BMI
    # Kondisi jika hasil BMI kurang dari atau sama dengan 16.9
    else:
        result["status"] = "Kurus"
        result["note"] = "Kekurangan Berat badan berat"
        result["skor"] = BMI

    # mengembalikan hasil
    return result
