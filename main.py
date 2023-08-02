#This file contains only functions 
import pickle
import datetime
from task_class import Task
users_table = []
tasks_list = []
categories = {1:'cleaning', 2:'buying',3:'cooking'}

## - save user data base
def save(list_to_save:list):
    #saving data base to pickle
    with open ("users.pickle",'wb') as f:
        pickle.dump(list_to_save,f)

## - upload user data base
def upload():
    #uploading database from pickle
    with open ("users.pickle",'rb') as f:
        table = pickle.load(f)
    return table


## - save tasks data base
def save_tasks(list_to_save:list):
    #saving data base to pickle
    with open ("tasks.pickle",'wb') as f:
        pickle.dump(list_to_save,f)

## - upload tasks data base
def upload_tasks():
    #uploading database from pickle
    with open ("tasks.pickle",'rb') as f:
        tasks_table = pickle.load(f)
    return tasks_table


#1 - user login
def login(user_name:str, password:str, users_table:list):
    for user in users_table:

        for parameter_password in user:
            print(parameter_password)
            if ((user_name == user.get(parameter_password)) and (password == parameter_password)):
                return("welcome")

    return("No such user")
    



#2 - add user
def add_user(users_table:list):
    dict1 = {}
    print('''
    Add user:
          
    User Name Instructions:
    1. Must to be just letters.
    2. More than 4 letters.
          
    Password Instructions:
    Please make sure that your password is:
    1. minimum of 7 characters.
    2. Must consist both numbers and signs/letters.''')
    if users_table == []:
        user_name = input("Enter new user name: ")
        password = input("Enter new password: ")
        answer1 = False
        answer2 = False
        if((len(password) >= 7) and (password.isdigit() == False)):
               answer1 = True
        
        if((len(user_name) > 4) and (user_name.isalpha() == True)):
            answer2 = True


        if ((answer1 == True) and (answer2 == True)):
            dict1.update({password:user_name})
            users_table.append(dict1)
            save(users_table)
            return("User add successfully")
        else:
            return("Try again later")

    
    else:
        user_name = input("Enter new user name: ")
        password = input("Enter new password: ")
        answer1 = False
        answer2 = False
        for user in users_table:
            for parameter_password in user:
                if((len(password) >= 7) and (password.isdigit() == False) and (password != parameter_password)):
                    answer1 = True
            
            if((len(user_name) > 4) and (user_name.isalpha() == True)):
                answer2 = True


        if ((answer1 == True) and (answer2 == True)):
            dict1.update({password:user_name})
            users_table.append(dict1)
            save(users_table)
            return("User add successfully")
        else:
            print("Try Again")
            print(add_user(users_table))

            
    


#3 - delete user
def delete_user(password_to_delete:str, users_table:list):
    '''The password is the key so it is 1 in a kind'''
    for users in users_table:
        for password in users:
            if password_to_delete == password:
                users_table.remove(users)
                save(users_table)
                return("User deleted")
            
            else:
                continue
    return("No such user")
    




#4 - Add task
def add_task (task_name:str, task_serial_num:int, name:str, tz:str,category:dict, accept_date:datetime, mission_end_date:datetime, description:str,status:str):
    task1 = Task(task_name = task_name, task_serial_num = task_serial_num, name = name, tz = tz,category = category, accept_date = accept_date, mission_end_date = mission_end_date, description = description,status = status)
    tasks_list = upload_tasks()
    tasks_list.append(task1)
    save_tasks(tasks_list)
    return tasks_list


#5 search user - by password
def search_user(password:str, users_table:list):
   for user in users_table:
        for passwords in user:
            if password == passwords:
                return(f"The user is: {user}")
        #return ("No such user")



#6 search tasks for person  - by tz
def search_person_tasks(tz:str, tasks_list:list):
    person_tasks = []
    for task in tasks_list:
        if tz == task.tz:
            person_tasks.append(task)
    return person_tasks


#7 - update
def update_task(key:str, tasks_list:list,serial_num:int):
    
    for task in tasks_list:
        if ((key == 1) and (task.task_serial_num == serial_num)):
            new_name = input("Enter a new task name: ")
            task.task_name = new_name
            print("Task name updated")
            save_tasks(tasks_list)
            return task

        elif ((key == 2) and (task.task_serial_num == serial_num)):
            person_name = input("Enter a new person name: ")
            new_tz = input("Enter a new Id name: ")
            task.name = person_name
            task.tz = new_tz
            print("Details updated")
            save_tasks(tasks_list)
            return task

            
        
        elif ((key == 3) and (task.task_serial_num == serial_num)):
            
            day = int(input("Enter finish day:"))
            month = int(input("Enter finish month:"))
            year = int(input("Enter finish year:"))
            mission_end_date = datetime.date(year,month,day)
            task.mission_end_date = mission_end_date
            print("Date updated")
            save_tasks(tasks_list)
            return task
    else:
        print("Serial number doesn't match")



#8 - search tasks by category
def search_by_category(key,tasks_list):
    category_list = []
    for task in tasks_list:
        if key == task.category :
            category_list.append(task)
    return category_list



#9 - show all tasks
## in ui


#10 - update status
def updating_status(done:str,serial_num:int, tasks_list:list):
    for task in tasks_list:
        if serial_num == task.task_serial_num:
            if done == 'y':
                task.status = 'Finished'
                print("Status has changed! ")
                save(tasks_list)
                return task
            elif done == 'y':
                task.status = 'Not finished'
                save(tasks_list)
                return task

            elif ((done != 'y') and (done != 'n')) :
                print("Not valid text, please try again")
        





#11 - Show Tasks status
def checking_status(status_value:str,tasks_list:list):
    status_list = []
    if status_value == 't':
        status_value = 'Finished'
    elif status_value == 'f':
        status_value = 'Not finished'
    else: 
        print("No valid data")

    for task in tasks_list:
        if status_value == task.status:
            status_list.append(task)
    return status_list



#12 - search task by serial num
def search_task(serial_num:int, tasks_list:list):
   for task in tasks_list:
        if serial_num == task.task_serial_num:
            return(f"The task is: {task}")




#13 - delete task
def delete_task(serial_num:int, tasks_list:list):
    '''The serial num is the key, so it is 1 in a kind'''
    for task in tasks_list:
        if task.task_serial_num == serial_num:
                tasks_list.remove(task)
                save(tasks_list)
                return(f"Task deleted\n{tasks_list}")


def menu():
    while True:
        action = int(input('''
    Welcome - U arrived to the Task menu.
    Please press one of the following actions:
    1. Add user to Data Base
    2. Show users Data Base
    3. Delete specific user
    4. Add mission
    5. Search user
    6. Search all task per user
    7. Update task by a key
    8. Search tasks by categories
    9. Show all tasks
    10.Changing task status
    11.Show tasks status
    12.Search task by serial number
    13.Delete task
    14.Exit
    '''))

        # Add user to Data Base
        if action == 1:
            print(add_user(users_table=upload()))

        # Show users data base
        elif action == 2:
            print("These are all users:", upload())


        # Delete user
        elif action == 3:
            password_to_delete = input("Enter user's password that u want to delete: ")
            delete_user(password_to_delete, users_table=upload())

        # Add task
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
            category = categories.get(key, "No such category")
            accept_date = datetime.date.today()
            print("Enter end date for the task:")
            day = int(input("Enter finish day:"))
            month = int(input("Enter finish month:"))
            year = int(input("Enter finish year:"))
            mission_end_date = datetime.date(year, month, day)
            description = input("Enter task description:")
            status = 'Not finished'
            print(add_task(task_name, task_serial_num, name, tz, category, accept_date, mission_end_date, description,
                           status))


        # Search user
        elif action == 5:
            password = input("Enter password to search user: ")
            print(search_user(password, users_table=upload()))

            # Search tasks for person
        elif action == 6:
            tz = input("Enter Id to search user: ")
            print(search_person_tasks(tz, tasks_list=upload_tasks()))



        # Update task by a key
        elif action == 7:
            num = int(input("Enter task serial number that u want to update: "))
            key = int(input('''Update 1 of the followings, press number between 1 to 3: 
            1: Task Name
            2: Person Name
            3: Mission End Date  '''))
            update_task(key, tasks_list=upload_tasks(), serial_num=num)

        # Search task by category
        elif action == 8:
            key = input("Enter the name of the category that u wanna search: ")
            print(search_by_category(key, tasks_list=upload_tasks()))



        # Show all tasks data
        elif action == 9:
            print(upload_tasks())


        # Change task status
        elif action == 10:
            serial_num = int(input("Enter task serial number to change status: "))
            done = input("The mission is done ? --> y/n ")
            print(updating_status(done, serial_num, tasks_list=upload_tasks()))



        # Show tasks status
        elif action == 11:
            status_value = input("Enter which status do you want to check --> t/f  ")
            print(checking_status(status_value, tasks_list=upload_tasks()))


        # search task by serial number
        elif action == 12:
            serial_num = int(input("Enter task's serial num that u want to search: "))
            print(search_task(serial_num, tasks_list=upload_tasks()))

        # Delete task
        elif action == 13:
            serial_num = int(input("Enter task's serial num that u want to delete: "))
            print(delete_task(serial_num, tasks_list=upload_tasks()))
        # break
        elif action == 14:
            print("U left the menu, bye...")
            break

#14 - exit from menu
