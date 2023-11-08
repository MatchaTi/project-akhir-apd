def kebahagiaan():#fungsi fitur kebahagiaan
    while True:
        try:
            print("Skor 1 - 3 = Kurang Puas")#menampilkan nilai dari skor 1-7
            print("Skor 4 = Netral")
            print("Skor 5 - 7 = Puas")
            #input skor kebahagiaan dari pertanyaan 1-5
            state1 = int(
                input(
                    "Dalam sebagian besar aspek, hidup saya mendekati cita-cita saya: "
                )
            )
            state2 = int(input("Secara umum kondisi kehidupan saya baik-baik saja: "))
            state3 = int(input("Saya merasa hidup saya memuaskan: "))
            state4 = int(
                input(
                    "Sejauh ini saya telah mendapatkan hal-hal penting yang saya inginkan dalam hidup saya: "
                )
            )
            state5 = int(
                input(
                    "Jika saya dapat menjalani hidup saya lagi, saya tidak akan mengubah apapun: "
                )
            )

            if state1 < 1 or state2 < 1 or state3 < 1 or state4 < 1 or state5 < 1:#error handling jika input skor dibawah 0
                raise Exception("Angka tidak boleh minus!") #membuat pesan error sendiri dengan output kesalahan input

            break #keluar dari loop
        except ValueError: #error handling jika input bukan bilangan bulat
            print("Input harus berupa bilangan bulat!") #output kesalahan input
        except Exception as e: # menangkap pesan error yang telah dibuat tadi
            print(e)

    Skor = state1 + state2 + state3 + state4 + state5 #menghitung jumlah skor
    result = {"program": "kebahagiaan", "skor": Skor, "parameter": "", "note": ""} #Hasil

    if Skor > 30: #kondisi kebahagiaan jika skor lebih dari 30
        result["parameter"] = "Sangat Puas"#Output hasil
        result[
            "note"
        ] = "Skor ini memberi tahu Anda bahwa Anda mencintai hidup Anda dan menganggapnya menyenangkan serta segala sesuatunya berjalan sengan baik untuk Anda" #Output hasil

    elif Skor > 25 and Skor <= 30: #Kondisi kebahagiaan jika skor lebih dari 25 dan kurang atau sama dengan 30
        result["parameter"] = "Puas"#Output hasil
        result[
            "note"
        ] = "Anda menyukai hidup Anda dan menemukan bahwa sebagian besar bidang kehidupan Anda berjalan dengan sangat baik untuk Anda"#Output hasil

    elif Skor > 20 and Skor <= 25: #Kondisi kebahagiaan jika skor lebih dari 20 dan kurang atau sama dengan 25
        result["parameter"] = "Sedikit Puas"#Output hasil
        result[
            "note"
        ] = "Anda menyukai hdiup Anda dan menemukan bahwa sebagian besar bidang kehidupan Anda berjalan dengan sangat baik untuk Anda"#Output hasil

    elif Skor == 20: #Kondisi kebahagiaan jika skor sama dengan 20
        result["parameter"] = "Netral"#Output hasil
        result[
            "note"
        ] = "Ini adalah skor rata-rata\nAnda secara umum puas dengan kehidupan Anda, namun ada bebrapa area yang perlu ditingkatkan\nAnda ingin naik ke tingkat yang lebih tinggi dengan melakukan perubahan dalam hidup"#Output hasil

    elif Skor >= 15 and Skor < 20: #Kondisi kebahagiaan jika skor lebih dari atau sama dengan 15 dan kurang dari 20
        result["parameter"] = "Sedikit Tidak Puas"#Output hasil
        result[
            "note"
        ] = "Anda memililki masalah kecil namun signifikan dalam beberapa bidang kehidupan atau banyak bidang kehidupan Anda yang berjalan dengan baik, namun ada satu bidang yang memiliki masalah besar\nHarapan yang moderat dan perubahan hidup dapat membantu menyelesaikan masalah"#Output hasil

    elif Skor >= 10 and Skor < 15: #Kondisi kebahagiaan jika skor lebih dari atau sama dengan 10 dan kurang dai 15
        result["parameter"] = "Tidak Puas"#Output hasil
        result[
            "note"
        ] = "Anda sangat tidak puas\nAda banyak area dalam hidup Anda yang bermasalah atau satu atau dua area dalam hidup Anda yang berjalan sangat buruk\nDiperlukan perubahan dalam sikap, pola pikir, dan aktivitas kehidupan. Ketidakbahagiaan dapat menjadi penghalang untuk berfungasi secara normal, oleh karena itu konseling dapat membantu"#Output hasil

    else: #Kondisi kebahagiaan jika skor dibawah 10
        result["parameter"] = "Sangat Tidak Puas"#Output hasil
        result[
            "note"
        ] = "Anda secara substansi tidak bahagia dengan kehidupan Anda saat ini\nKehilangan orang yang dicintai, pengangguran, kecanduan alkohol, atau kecanduan bisa menjadi alasannya\nAnda perlu mencari bantuan profesional"#Output hasil

    return result #kembalikan hasil
