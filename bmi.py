def bmi():#fungsi fitur BMI
    while True:
        try:
            BB = float(input("Berat Badan(KG)  :"))#input berat badan user
            TB = float(input("Tinggi Badan(CM) :"))#input tinggi badan user
            BMI = BB / ((TB / 100) * (TB / 100))#menghitung BMI

            if BB < 0 or TB < 0:#error handling jika input berat badan atau tinggi badan dibawah 0
                raise Exception("Berat atau tinggi badan tidak boleh minus!")#membuat pesan error sendiri dengan output kesalahan input

            break #keluar loop
        except ValueError:#error handling jika input bukan angka
            print("Input harus berupa angka!")#output kesalahan input
        except Exception as e: # menangkap pesan error yang telah dibuat tadi
            print(e)

    result = {"program": "bmi", "status": "", "note": "", "skor": 0}#Hasil
    BMI = round(BMI, 2)#Pembulatan hasil BMI

    if BMI >= 27: #Kondisi jika hasil BMI lebih dari atau sama dengan 27
        result["status"] = "Obesitas"
        result["note"] = "Kelebihan berat badan tingkat berat"
        result["skor"] = BMI
    elif BMI >= 25.1 and BMI <= 26.9: #Kondisi jika hasil BMI lebih dari atau sama dengan 25.1 dan kurang dari atau sama dengan 26.9
        result["status"] = "Obesitas"
        result["note"] = "Kelebihan berat badan tingkat ringan"
        result["skor"] = BMI
    elif BMI >= 18.5 and BMI <= 25:#Kondisi jika hasil BMI lebih dari atau sama dengan 18.5 dan kurang dari atau sama dengan 25
        result["status"] = "Normal"
        result["note"] = "Berat badan ideal"
        result["skor"] = BMI
    elif BMI >= 17 and BMI <= 18.4:#Kondisi jika hasil BMI lebih dari atau sama dengan 17 dan kurang dari atau sama dengan 18.4
        result["status"] = "Kurus"
        result["note"] = "Kekurangan Berat badan ringan"
        result["skor"] = BMI
    else:#Kondisi jika hasil BMI kurang dari atau sama dengan 16.9
        result["status"] = "Kurus"
        result["note"] = "Kekurangan Berat badan berat"
        result["skor"] = BMI

    return result #mengembalikan hasil
