import os

# Student access level

def studentt():
    os.system('cls')
    print("===== Issue items from here =====")
    
    while True:
        print("1. Available items")
        print("2. Issue item")
        print("3. Return item")
        print("4. Check issued item")
        print("5. Exit")
         
        n = int(input(">> "))
        if (n == 1):
            from IMS.admin.admin_funcs import display_data
            display_data()
        elif (n == 2):
            from IMS.student.student_funcs import issue_data
            issue_data()
        elif (n == 3):
            from IMS.student.student_funcs import return_data
            return_data()
        elif (n == 4):
            from IMS.student.student_funcs import check_issued_items
            check_issued_items()
        elif (n == 5):
            os.system('cls')
            break
        else:
            print("Invalid Choice...!!!")