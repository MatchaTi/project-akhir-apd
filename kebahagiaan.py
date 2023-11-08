# fungsi fitur kebahagiaan
def kebahagiaan():
    while True:
        try:
            # menampilkan nilai dari skor 1-7
            print("Skor 1 - 3 = Kurang Puas")
            print("Skor 4 = Netral")
            print("Skor 5 - 7 = Puas")
            # input skor kebahagiaan dari pertanyaan 1-5
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
            # error handling jika input skor dibawah 0
            if state1 < 1 or state2 < 1 or state3 < 1 or state4 < 1 or state5 < 1:
                # membuat pesan error sendiri dengan output kesalahan input
                raise Exception("Angka tidak boleh minus!")
            # keluar dari loop
            break
        # error handling jika input bukan bilangan bulat
        except ValueError:
            # output kesalahan input
            print("Input harus berupa bilangan bulat!")
        # menangkap pesan error yang telah dibuat tadi
        except Exception as e:
            print(e)
    # menghitung jumlah skor
    Skor = state1 + state2 + state3 + state4 + state5
    # Hasil
    result = {"program": "kebahagiaan", "skor": Skor, "parameter": "", "note": ""}
    # kondisi kebahagiaan jika skor lebih dari 30
    if Skor > 30:
        # Output hasil
        result["parameter"] = "Sangat Puas"
        # Output catatan tambahan
        result[
            "note"
        ] = "Skor ini memberi tahu Anda bahwa Anda mencintai hidup Anda dan menganggapnya menyenangkan serta segala sesuatunya berjalan sengan baik untuk Anda"
    # Kondisi kebahagiaan jika skor lebih dari 25 dan kurang atau sama dengan 30
    elif Skor > 25 and Skor <= 30:
        result["parameter"] = "Puas"  # Output hasil
        # Output catatan tambahan
        result[
            "note"
        ] = "Anda menyukai hidup Anda dan menemukan bahwa sebagian besar bidang kehidupan Anda berjalan dengan sangat baik untuk Anda"
    # Kondisi kebahagiaan jika skor lebih dari 20 dan kurang atau sama dengan 25
    elif Skor > 20 and Skor <= 25:
        # Output hasil
        result["parameter"] = "Sedikit Puas"
        # Output catatan tambahan
        result[
            "note"
        ] = "Anda menyukai hdiup Anda dan menemukan bahwa sebagian besar bidang kehidupan Anda berjalan dengan sangat baik untuk Anda"
    # Kondisi kebahagiaan jika skor sama dengan 20
    elif Skor == 20:
        # Output hasil
        result["parameter"] = "Netral"
        # Output catatan tambahan
        result[
            "note"
        ] = "Ini adalah skor rata-rata\nAnda secara umum puas dengan kehidupan Anda, namun ada bebrapa area yang perlu ditingkatkan\nAnda ingin naik ke tingkat yang lebih tinggi dengan melakukan perubahan dalam hidup"
    # Kondisi kebahagiaan jika skor lebih dari atau sama dengan 15 dan kurang dari 20
    elif Skor >= 15 and Skor < 20:
        # Output hasil
        result["parameter"] = "Sedikit Tidak Puas"
        # Output catatan tambahan
        result[
            "note"
        ] = "Anda memililki masalah kecil namun signifikan dalam beberapa bidang kehidupan atau banyak bidang kehidupan Anda yang berjalan dengan baik, namun ada satu bidang yang memiliki masalah besar\nHarapan yang moderat dan perubahan hidup dapat membantu menyelesaikan masalah"
    # Kondisi kebahagiaan jika skor lebih dari atau sama dengan 10 dan kurang dai 15
    elif Skor >= 10 and Skor < 15:
        # Output hasil
        result["parameter"] = "Tidak Puas"
        # Output catatan tambahan
        result[
            "note"
        ] = "Anda sangat tidak puas\nAda banyak area dalam hidup Anda yang bermasalah atau satu atau dua area dalam hidup Anda yang berjalan sangat buruk\nDiperlukan perubahan dalam sikap, pola pikir, dan aktivitas kehidupan. Ketidakbahagiaan dapat menjadi penghalang untuk berfungasi secara normal, oleh karena itu konseling dapat membantu"
    # Kondisi kebahagiaan jika skor dibawah 10
    else:
        # Output hasil
        result["parameter"] = "Sangat Tidak Puas"
        # Output catatan tambahan
        result[
            "note"
        ] = "Anda secara substansi tidak bahagia dengan kehidupan Anda saat ini\nKehilangan orang yang dicintai, pengangguran, kecanduan alkohol, atau kecanduan bisa menjadi alasannya\nAnda perlu mencari bantuan profesional"
    # Output catatan tambahan
    return result
