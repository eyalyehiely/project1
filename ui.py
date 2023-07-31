from main import upload,upload_tasks, login, add_user, upload, add_task, delete_user, search_user, search_person_tasks,update_task,changing_status,checking_status,upload_tasks,search_by_category,delete_task
import datetime
action = None
users_table = []
tasks_list = []
categories = {1:'cleaning', 2:'buying',3:'cooking'}

answer = int(input("1 : sign in / 2 : login: "))
if answer == 2:
    
    for i in range(3):
        print("You have",abs((i-3)),"tries to login: ")
        user_name = input("Enter your user name: ")
        password = input("Enter your password: ")
        approval = print(login(user_name, password, users_table = upload()))
        if approval == "welcome":
            break
    if approval != 'welcome' :
        print("You have been transferred to the Sign in window: ")
        approval = print((add_user(users_table = upload())))
        
elif answer == 1:
    print("Sign in window")
    approval = print((add_user(users_table = upload())))


    while approval == "welcome" or approval == "User add successfully" or action != 12:
        action = int(input('''
    Welcome - U arrived to the Task menu.
    Please press one of the following actions:
    1. Add user to Data Base
    2. Show users Data Base
    3. Delete specific user
    4. Add mission
    5. Search for user
    6. Search all task per user
    7. Update task by a key
    8. Search tasks by categories
    9. Show all tasks
    10.Changing task status
    11.Show tasks status
    12.Delete task
    13.Exit
    '''))

        
        #Add user to Data Base
        if action == 1:
            print(add_user(users_table = upload()))
        
        #Show users data base
        elif action == 2:
            print("These are all users:", upload())


        #Delete user
        elif action == 3:
            password_to_delete = input("Enter user's password that u want to delete: ")
            delete_user(password_to_delete, users_table = upload())

        #Add task
        elif action == 4:
            task_name = input("Enter task name: ")
            task_serial_num = int(input("give task unique number: "))
            name = input("Enter who's going to do the task: ")
            tz = input("Enter id of the executing: ")
            key = int(input('''Enter digit for the category that the task belongs to:
                                            1. cleaning
                                            2. buying
                                            3. cooking
                            '''))
            category = categories.get(key,"No such category")
            accept_date = datetime.date.today()
            print("Enter end date for the task:")  
            day = (datetime.date(input("Enter finish day:")))
            month = (datetime.date(input("Enter finish month:")))
            year = (datetime.date(input("Enter finish year:")))
            mission_end_date = datetime.date(year,month,day)
            description = input("Enter task description:") 
            status = False  
        
            print(add_task((task_name, task_serial_num, name, tz, category, accept_date, mission_end_date, description, status)))


        #Search user 
        elif action == 5:
            password = input("Enter password to search user: ")
            print(search_user(password, users_table = upload()))



            #Search tasks for person 
        elif action == 6:
            tz = input("Enter Id to search user: ")
            print(search_person_tasks(tz, tasks_list = upload_tasks()))



        #Update task by a key
        elif action == 7: 
            num = int(input("Enter taske serial number that u want to update: "))
            key = int(input('''Update 1 of the followings, press number between 1 to 3: 
            1: Task Name
            2: Person Name
            3: Mission End Date'''))
            update_task(key, tasks_list = upload_tasks(),serial_num = num)

        #Search task by category
        elif action == 8: 
            key = input("Enter the name of the category that u wanna search: ")
            print(search_by_category(key, tasks_list = upload_tasks()))



        #Show all tasks data
        elif action == 9: 
            print(upload_tasks())


        #Change task status
        elif action == 10:
            serial_num = int(input("Enter task serial number to search: "))
            print(changing_status(serial_num, tasks_list = upload_tasks()))



        #Show tasks status
        elif action == 11:
            status_value = bool(input("Enter which status do you want to check: True/False "))
            checking_status(status_value, tasks_list = upload_tasks())
        


        #Delete task
        elif action == 12:
            serial_num = int(input("Enter task's serial num that u want to delete: "))
            print(delete_task(serial_num, tasks_list = upload_tasks()))
        #break
        elif action == 13:
            print("U left the menu, bye...")
            break
        