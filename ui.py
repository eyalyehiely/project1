from main import login,add_user,upload
action = None
users_table = []
user_name = input("Enter your user name: ")
password = input("Enter your password: ")

while approval != 'Welcome':
    print(add_user(users_table)) 
    approval = login(user_name, password, users_table)
    if approval == 'welcome':
        continue


while action != 10:
    action = int(input('''
Welcome - U arrived to the Task menu.
Please press one of the following actions:
1. Login
2. Add user to Data Base
3. Show users Data Base
4. Delete specific user
5. Add mission
6. exit
'''))

    #login
    if action == 1:
        print()



    #Add user to Data Base
    elif action == 2:
        print(add_user(users_table))
    
    #show data base
    elif action == 3:
        print(upload())
    

    elif action == 4:
        pass

    elif action == 5:
        pass

    elif action == 6:
        pass
    