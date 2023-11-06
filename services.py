import os
from crud import data_users


def install_dependencies():
    os.system("pip install prettytable")


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def enter_continue():
    input("\nKlik enter untuk lanjut...")


def check_role(role):
    if role == "admin":
        return True

    return False


def get_len_data():
    return len(data_users[1:])
