#This file contain only functions 
import pickle
from task_class import Task
users_table = []

## - save data base
def save(list_to_save:list):
    #saving data base to pickle
    with open ("users.pickle",'wb') as f:
        pickle.dump(list_to_save,f)



## - upload data base
def upload():
    #uploading data base from pickle
    with open ("users.pickle",'rb') as f:
        users_table = pickle.load(f)
    return users_table



#1 - user login
def login(user_name:str, password:str, users_table:list):
    for user_password in users_table:
        if ((user_name == user_password['password']) and (password == user_password)):
            return("Welcome")
        else:
            return("No such user")
    return ("No such user")




#2 - adding user
def add_user(users_table:list,user_name:str, password:str):
    dict1 = {}
    print('''
    User Name Instructions:
    1. Must to be just letters.
    2. More than 4 letters.
          
    Password Instructions:
    Please make sure that your password is:
    1. minimum of 7 characters.
    2. Must consist both numbers and signs/letters.''')

    for user in users_table:
        if ((len(user_name) > 4) and (user_name.isalpha) and (user_name != user )):
            print("User name is ok ! - continue to password")
        else:
            print("User name is not ok")
            exit()
        

        if((len(password) >= 7) and (password.isdigit != True)):
            print("Password is ok")
        else:
            print("Password is not ok")
            exit()
    
    dict1.update({password:user_name})
    users_table.append(dict1)
    save(users_table)
    return ("User add successfully")
    


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
    



tasks_list = []
#4 - Add task
def add_task (task_name, task_num, name, tz,accept_date, mission_end_date, description):
    task1 = Task(task_name = task_name, task_num = task_num, name = name, tz = tz, accept_date = accept_date, mission_end_date = mission_end_date, description = description)
    tasks_list.append(task1)
    save(tasks_list)
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
            save(tasks_list)



       