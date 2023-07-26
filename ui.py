from main import login,add_user,upload,add_task
action = None
users_table = []
import datetime
approval = "No data"

while approval != 'Welcome':
    user_name = input("Enter your user name: ")
    password = input("Enter your password: ")
    print(add_user(users_table, user_name, password)) 
    approval =login(user_name, password, users_table)
    if approval == 'welcome':
        continue

    while action != 10:
        action = int(input('''
    Welcome - U arrived to the Task menu.
    Please press one of the following actions:
    1. Add user to Data Base
    2. Show users Data Base
    3. Delete specific user
    4. Add mission
    5. exit
    '''))
    
       
        #Add user to Data Base
        if action == 1:
            print(add_user(users_table))
        
        #Show users data base
        elif action == 2:
            print("These are all users:", upload())


        #Delete user
        elif action == 3:
            password_to_delete = input("Enter user's password that u want to delete")
            print(users_table,password_to_delete)

        
        elif action == 4:
            task_name = input("Enter task name:")
            task_num = int(input("Enter task number:"))
            name = input("Enter who's going to do the task:")
            tz = input("Enter id of the executing: ")
            category = input("Enter which category the task belongs to:")
            accept_date = datetime.today()
            mission_end_date = input("Enter end date for the task:")  
            description = input("Enter task description:")  
            
            print(add_task((task_name, task_num, name, tz, category,accept_date, mission_end_date, description)))
