from IMS.db_funcs import issue_item, return_item, check_items
from IMS import mclient
from datetime import datetime
import os
import time

def issue_data():
    os.system('cls')
    print("===== Issue items =====")
    while True:
        self_name = input("Enter your name :- ")
        if self_name == "exit":
            os.system('cls')
            break
        item_name = input("Item name :- ")
        x = issue_item(self_name, item_name)
        date = datetime.now().date()
        if x:
            aka = mclient["inventory"][f"{self_name}"]
            post = {
            "item_issued" : item_name,
            "date_issued" : str(date),
            }
            aka.insert_one(post)

            print(f"Issued 1 {item_name} to {self_name}")
            time.sleep(2)
            os.system('cls')
            break
        else:
            return
            break
    
def return_data():
    os.system('cls')
    print("===== Return items =====")
    while True:
        name = input("Enter your name :- ")
        if name == "exit":
            os.system('cls')
            break
        
        item_name = input("Item name :- ")
        return_item(name, item_name)
        break

def check_issued_items():
    os.system('cls')
    print("===== Check issued items =====")
    while True:
        name = input("Enter your name :- ")
        if name == "exit":
            break
        check_items(name)
        break