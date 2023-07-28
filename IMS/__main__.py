import os
import time
from getpass import getpass

while True:
    print("\nPlease select access level\n1. Admin\n2. Student\n3. Exit")

    user_input = int(input(">> "))
    if user_input == 1:
        os.system('cls')
        print("\n===== Login Page =====")

        user_name = input("Username :- ")
        password = getpass("Password :- ")
        if user_name == "jnv" and password == "jnv_cachar":
            os.system('cls')
            from IMS.admin.admin_input import adminn
            adminn()
        else:
            print("Wrong password try again!")
            time.sleep(1)
            os.system('cls')
    elif user_input == 2:
        from IMS.student.student_input import studentt
        studentt()
    elif user_input == 3:
        break