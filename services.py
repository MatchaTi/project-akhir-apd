import os
# mengambil variable dari file crud
from crud import data_users

# fungsi untuk menginstall prettytable
def install_dependencies():
    os.system("pip install prettytable")

# fungsi untuk membersihkan terminal
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

#fungsi untuk memberi jeda di tiap output
def enter_continue():
    input("\nKlik enter untuk lanjut...")

#fungsi untuk mengecek role user
def check_role(role):
    # jika role user adalah admin maka,
    if role == "admin":
        # kembalikan nilai True
        return True
    #jika role user bukan admin maka, 
    #kembalikan nilai false
    return False

#fungsi untuk menghitung jumlah data user
def get_len_data():
    # mengembalikan jumlah panjang data user 
    return len(data_users[1:])
