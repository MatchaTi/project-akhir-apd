def hidrasi():
    while True:
        try:
            Berat = float(input("Berat badan: "))

            if Berat < 0:
                raise Exception("Input tidak boleh minus!")

            break
        except ValueError:
            print("Input harus berupa angka!")
        except Exception as e:
            print(e)

    Liter = (Berat * 30) / 1000
    Gelas = round((Berat * 30) / 220)

    result = {
        "program": "hidrasi",
        "note": f"Jumlah air yang harus diminum: {Liter} liter/hari atau setara dengan {Gelas} gelas",
    }

    return result
