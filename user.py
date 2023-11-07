from services import clear_screen, enter_continue
from program import kalori
from hidrasi import hidrasi
from crud import user_screening
from kebahagiaan import kebahagiaan
from bmi import bmi


def menu_user(name):
    print(f"Profile = {name}")
    print("Pilih Layanan:")
    print("[1] Kalkulator BMI")
    print("[2] Kalkulator Kalori")
    print("[3] Kalkulator Hidrasi")
    print("[4] Kalkulator Kebahagiaan")
    print("[5] Logout")


def main_user(user):
    while True:
        clear_screen()
        menu_user(user["nama"])

        pilihan = input("Pilih layanan: ")

        if pilihan == "1":
            result = bmi()
            user_screening(user["nama"], user["password"], result)
            enter_continue()
        elif pilihan == "2":
            kalori()
            enter_continue()
        elif pilihan == "3":
            result = hidrasi()
            user_screening(user["nama"], user["password"], result)
            enter_continue()
        elif pilihan == "4":
            result = kebahagiaan()
            user_screening(user["nama"], user["password"], result)
            enter_continue()
        elif pilihan == "5":
            return
        else:
            print(f"Pilihan [{pilihan}] tidak tersedia!")
            enter_continue()
