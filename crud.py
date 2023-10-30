import os
import json
from prettytable import PrettyTable

file_path = "users.json"

if not os.path.isfile(file_path):
    with open(file_path, "w") as json_file:
        json.dump([], json_file, indent=4)


def load_data():
    with open(file_path) as json_file:
        return json.load(json_file)


data_users = load_data()


def save_data(json_data):
    with open(file_path, "w") as json_file:
        json.dump(json_data, json_file, indent=4)


def create_data(json_data):
    data_users.append(json_data)
    save_data(data_users)


def show_data():
    table_fields = ["nama", "password", "gender", "verif", "role"]
    table = PrettyTable()
    table.padding_width = 5
    table.field_names = ["N0."] + table_fields

    for i, row in enumerate(data_users[1:], start=1):
        row_to_display = [i] + [row[col] for col in table_fields]
        table.add_row(row_to_display)

    print(table)


def update_status(index):
    data_users[index]["verif"] = True
    save_data(data_users)
