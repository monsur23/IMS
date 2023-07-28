from IMS.db_funcs import add_items, remove_items, display_items, all_issued_items
import os

def add_data():
    os.system('cls')
    print("===== Add Items =====")
    while True:
        name = input("Enter item name : ")
        if name == "exit":
            os.system('cls')
            break
        quantity = input("Enter item quantity : ")
        date_received = input("Enter date received : ")

        add_items(name, quantity, date_received)
        print("--------------enter exit to exit---------------")

def remove_data():
    os.system('cls')
    print("===== Remove Items =====")
    while True:
        name = input("Enter item name : ")
        if name == "exit":
            os.system('cls')
            break

        remove_items(name)
        print("--------------enter exit to exit---------------")

def display_data():
    os.system('cls')
    display_items()


def check_who_issued():
    all_issued_items()