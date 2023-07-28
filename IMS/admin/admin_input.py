import os
# Admin access level

def adminn():
    print("======= Welcome to the Admin Inventory Management System =======")
    
    while True:
        print("1. Display all items")
        print("2. Add items")
        print("3. Remove items")
        print("4. All issued items")
        print("5. Exit")
         
        n = int(input(">> "))
        if (n == 1):
            from IMS.admin.admin_funcs import display_data
            display_data()
        elif (n == 2):
            from IMS.admin.admin_funcs import add_data
            add_data()
        elif (n == 3):
            from IMS.admin.admin_funcs import remove_data
            remove_data()
        elif (n == 4):
            from IMS.admin.admin_funcs import check_who_issued
            check_who_issued()
        elif (n == 5):
            os.system('cls')
            break
        else:
            print("Invalid Choice...!!!")