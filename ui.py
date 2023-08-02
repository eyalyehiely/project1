from main import *

users_table = []
tasks_list = []
answer = int(input("Enter -> 1 : sign in or -> 2 : login: "))
if answer == 2:
    
    for i in range(3):
        print("You have",abs((i-3)),"tries to login: ")
        user_name = input("Enter your user name: ")
        password = input("Enter your password: ")
        approval = login(user_name, password, users_table = upload())
        if approval == "welcome":
            menu()
    print("You have been transferred to the Sign in window: ")
    approval = add_user(users_table = upload())
        
elif answer == 1:
    print("Sign in window")
    approval =add_user(users_table = upload())
    menu()



