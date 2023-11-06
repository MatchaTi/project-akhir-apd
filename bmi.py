def bmi():
    while True:
        try:
            BB = float(input("Berat Badan(KG)  :"))
            TB = float(input("Tinggi Badan(CM) :"))
            BMI = BB / ((TB / 100) * (TB / 100))

            if BB < 0 or TB < 0:
                raise Exception("Berat atau tinggi badan tidak boleh minus!")

            break
        except ValueError:
            print("Input harus berupa angka!")
        except Exception as e:
            print(e)

    result = {"status": "", "note": "", "skor": 0}
    BMI = round(BMI, 2)

    if BMI >= 27:
        result["status"] = "Obesitas"
        result["note"] = "Kelebihan berat badan tingkat berat"
        result["skor"] = BMI
    elif BMI >= 25.1 and BMI <= 26.9:
        result["status"] = "Obesitas"
        result["note"] = "Kelebihan berat badan tingkat ringan"
        result["skor"] = BMI
    elif BMI >= 18.5 and BMI <= 25:
        result["status"] = "Normal"
        result["note"] = "Berat badan ideal"
        result["skor"] = BMI
    elif BMI >= 17 and BMI <= 18.4:
        result["status"] = "Kurus"
        result["note"] = "Kekurangan Berat badan ringan"
        result["skor"] = BMI
    else:
        result["status"] = "Kurus"
        result["note"] = "Kekurangan Berat badan berat"
        result["skor"] = BMI

    return result
