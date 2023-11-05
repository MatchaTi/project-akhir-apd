from services import clear_screen, enter_continue
from program import bmi, kalori, hidrasi, kebahagiaan


def menu_user(name):
    print(f"Profile = {name}")
    print("Pilih Layanan:")
    print("[1] Kalkulator BMI")
    print("[2] Kalkulator Kalori")
    print("[3] Kalkulator Hidrasi")
    print("[4] Kalkulator Kebahagiaan")
    print("[5] Logout")


def main_user(name):
    while True:
        clear_screen()
        menu_user(name["nama"])

        pilihan = input("Pilih layanan: ")

        if pilihan == "1":
            bmi()
            enter_continue()
        elif pilihan == "2":
            kalori()
            enter_continue()
        elif pilihan == "3":
            hidrasi()
            enter_continue()
        elif pilihan == "4":
            kebahagiaan()
            enter_continue()
        elif pilihan == "5":
            return
        else:
            print(f"Pilihan [{pilihan}] tidak tersedia!")
            enter_continue()
