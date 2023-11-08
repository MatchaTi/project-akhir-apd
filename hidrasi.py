def hidrasi():#fungsi fitur hidrasi
    while True:
        try:
            Berat = float(input("Berat badan: "))#input berat badan

            if Berat < 0:#error handling jika input dibawah 0
                raise Exception("Input tidak boleh minus!")#membuat pesan error sendiri dengan output kesalahan input

            break #Keluar dari loop
        except ValueError:#error handling jika input bukan angka
            print("Input harus berupa angka!")#output kesalahan input
        except Exception as e: # menangkap pesan error yang dibuat tadi
            print(e)

    Liter = (Berat * 30) / 1000 #hitung berapa liter air yang harus diminum
    Gelas = round((Berat * 30) / 220) #hitung berapa gelas air yang harus diminum

    result = {
        "program": "hidrasi",
        "note": f"Jumlah air yang harus diminum: {Liter} liter/hari atau setara dengan {Gelas} gelas",
    }#hasil 

    return result #mengembalikan hasil 
