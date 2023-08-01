#This file contains only functions 
import pickle
import datetime
from task_class import Task
users_table = []
tasks_list = []

## - save user data base
def save(list_to_save:list):
    #saving data base to pickle
    with open ("users.pickle",'wb') as f:
        pickle.dump(list_to_save,f)

## - upload user data base
def upload():
    #uploading data base from pickle
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
    #uploading data base from pickle
    with open ("tasks.pickle",'rb') as f:
        tasks_table = pickle.load(f)
    return tasks_table


#1 - user login
def login(user_name:str, password:str, users_table:list):
    for user in users_table:
        for parameter_password in user:
            if ((user_name == user.get(parameter_password)) and (password == parameter_password)):
                return("welcome")
    else:
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
def add_task (task_name:str, task_serial_num:int, name:str, tz:str,category:dict, accept_date:datetime, mission_end_date:datetime, description:str,status:bool):
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
    '''The serial num is the key so it is 1 in a kind'''
    for task in tasks_list:
        if task.task_serial_num == serial_num:
                tasks_list.remove(task)
                save(tasks_list)
                return(f"Task deleted\n{tasks_list}")
       
  



#14 - exit from menu



