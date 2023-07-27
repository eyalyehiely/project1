from main import login, add_user, upload, add_task, delete_user, search_user, search_person_tasks,update_task
action = None
users_table = []
tasks_list = []
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
    5. search for user
    6. search all task per user
    7.Update task by a key
    8. sort by categories
    9. show all tasks
    10. exit
                           
    ##. exit
    '''))
    
       
        #Add user to Data Base
        if action == 1:
            print(add_user(users_table))
        
        #Show users data base
        elif action == 2:
            print("These are all users:", upload())


        #Delete user
        elif action == 3:
            password_to_delete = input("Enter user's password that u want to delete: ")
            delete_user(users_table,password_to_delete)

        #Add task
        elif action == 4:
            categories = {}
            task_name = input("Enter task name:")
            task_num = len(tasks_list ) + 1
            name = input("Enter who's going to do the task:")
            tz = input("Enter id of the executing: ")
            category = categories.get(key = int(input('''Enter which category the task belongs to:
                                         1. cleaning
                                         2. buying
                                         3. cooking'''))) 
            accept_date = datetime.today()
            mission_end_date = input("Enter end date for the task:")  
            description = input("Enter task description:")  
            
            print(add_task((task_name, task_num, name, tz, category, accept_date, mission_end_date, description)))


        #Search user 
        elif action == 5:
            password = input("Enter password to search user: ")
            search_user(users_table,password)

         #Search tasks for person 
        elif action == 6:
            tz = input("Enter Id to search user: ")
            print(search_person_tasks(tasks_list,tz))

        #Update task by a key
        elif action == 7: 
            key = int(input('''Update 1 of the followings: 
            1: Task Name
            2: Person Name
            3: Mission End Date'''))
            update_task(tasks_list,key)
    
        
        elif action == 8: 
            pass


        elif action == 9: 
            pass


        
        elif action == 10:
            break
        pass