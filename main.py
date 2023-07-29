#This file contains only functions 
import pickle
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
            if ((user_name == user.get(password)) and (password == parameter_password)):
                return("Welcome")
    else:
        return("No such user")
    



#2 - adding user
def add_user(users_table:list):
    dict1 = {}
    print('''
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
            return("Try again later")
            

    
    


#3 - delete user
def delete_user(users_table:list,password_to_delete:str):
    '''The password is the key so it is 1 in a kind'''
    for users in users_table:
        for password in users:
            if password_to_delete == password:
                users_table.remove(users)
                save(users_table)
                print("User deleted")
            
        else:
            continue
    




#4 - Add task
def add_task (task_name:str, task_serial_num:int, name:str, tz:str, accept_date:str, mission_end_date:str, description:str,status:bool):
    task1 = Task(task_name = task_name, task_serial_num = task_serial_num, name = name, tz = tz, accept_date = accept_date, mission_end_date = mission_end_date, description = description,status = status)
    tasks_list.append(task1)
    save_tasks(tasks_list)
    return task1


#5 search user - by password
def search_user(users_table:list,password:str):
   for users in users_table:
        for passwords in users:
            if password == passwords:
                print(users)



#6 search tasks for person  - by tz
def search_person_tasks(tasks_list:list,tz:str):
    person_tasks = []
    for task in tasks_list:
        if tz == task.tz:
            person_tasks.append(task)
    return person_tasks


#7 - update
def update_task(tasks_list:list,key:str):
    
    for task in tasks_list:
        if key == 1:
            new_name = input("Enter a new task name: ")
            task.task_name = new_name
            print("Task name updated")
            save(tasks_list)

        elif key == 2:
            person_name = input("Enter a new person name: ")
            new_tz = input("Enter a new Id name: ")
            task.name = person_name
            task.tz = new_tz
            print("Details updated")
            save(tasks_list)
            
        
        elif key == 3:
            new_end_date = input("Enter a new end date: ")
            task.mission_end_date = new_end_date
            print("Date updated")
            save_tasks(tasks_list)


#8 - search tasks by category
def search_by_category(tasks_list,key):
    category_list = []
    for task in tasks_list:
        if task.category == key:
            category_list.append(task)



#9 - show all tasks


#10 - changing status
def changing_status(tasks_list:list, serial_num:int):
    for task in tasks_list:
        if task.task_serial_num == serial_num:
            answer = input("Enter Yes for done, No for not")
            if answer.capitalize() == 'Yes':
                task.status = True
                print("Status has changed! ")
                save_tasks(tasks_list)
        else:
            print("Serial number not found")
    return task



#11 - Tasks status
def checking_status(tasks_list:list, status_value:bool):
    status_list= []
    for task in tasks_list:
        if status_value == task.status:
            status_list.append(task)
    return status_list


#12 - exit