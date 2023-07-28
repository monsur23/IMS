from IMS import mclient
import os
import time

collection = mclient["inventory"]["items"]

def add_items(item_name, quantity, recieved_date):
    item = {
        "item_name" : item_name,
        "quantity" : int(quantity),
        "recieved_date" : recieved_date
    }
    collection.insert_one(item)

def remove_items(item_name):
    item = {
        "item_name" : item_name,
    }
    collection.delete_one(item)

def display_items():
    x = [item for item in collection.find()]
    if x:
        index = 0
        print("===== Items availale =====\n")
        for y in x:
            index += 1
            items = f"{index}> Item name - {y['item_name']}\n   Quantity -  {y['quantity']}\n   Date recieved - {y['recieved_date']}"
            print(items)
        print(" ")

    else:
        print("No items available!")

def issue_item(self_name, item_name):
    aka = mclient["inventory"][f"{self_name}"]
    x = [i for i in collection.find({"item_name" : item_name})]
    if x:
        for y in x:
            qut = y['quantity']
            new_qut = qut - 1
            update_query = {"$set": {"quantity": new_qut}}
            collection.update_one({"item_name": item_name}, update_query)
        return True
    else:
        print(f"{item_name} is not available in our inventory")
        time.sleep(2)
        os.system('cls')
        return False

def return_item(self_name, item_name):
    aka = mclient["inventory"][f"{self_name}"]
    cursor = aka.find({"item_issued" : item_name})
    x = list(cursor)
    if x:
        for y in x:
            kewf = y['item_issued']
            aka.delete_one({"item_issued" : kewf})
        print(f"{self_name} returned {item_name}")
        z = [i for i in collection.find({"item_name" : item_name})]
        if z:
            for m in z:
                qut = m['quantity']
                new_qut = qut + 1
                update_query = {"$set": {"quantity": new_qut}}
                collection.update_one({"item_name": item_name}, update_query)
    else:
        print('Item not matched!')

def check_items(name):
    coll = mclient["inventory"]
    coll_names = coll.list_collection_names()
    if name in coll_names:
        aka = mclient["inventory"][f"{name}"]
        items = aka.find({})
        index = 0
        for item in items:
            index += 1
            x = f"{index}. Item name - {item['item_issued']}\n   Date issued - {item['date_issued']}"
            print(x)
        print(" ")
    else:
        print("Your name is not registered yet. Issue an item to register your name.\n")

def all_issued_items():
    os.system('cls')
    print("===== All Issued Items =====")
    coll = mclient["inventory"]
    coll_names = coll.list_collection_names()
    for name in coll_names:
        if name != "items":          
            aka = mclient["inventory"][f"{name}"]
            items = aka.find({})
            yz = [i for i in items]
            if yz:
                i = 0
                print(f"\nStudent name - {name}")
                for m in yz:
                    i += 1
                    item_name = f" {i}. Item name - {m['item_issued']}\n    Date issued - {m['date_issued']}"
                    print(item_name)