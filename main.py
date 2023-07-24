#This file contain only functions 
import pickle
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





#1 - adding user
def add_user(users_table:list):
    dict1 = {}
    print('''
    User Name Instructions:
    1. Must to be just letters
    2. More than 4 letters  
          
    Password Instructions:
    Please make sure that your password is:
    1. Passwords must be a minimum of seven characters in length.
    2. Must consist both numbers and signs/letters.''')

    user_name = input("Please enter user name: ")
    password = input("Please enter password: ")

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
    
    dict1.update({user_name:password})
    users_table.append(dict1)
    save(users_table)
    return ("User add successfully")
    




#2 - user login
def login(user_name:str, password:str, users_table:list):
    for user in users_table:
        if ((user_name == user) and (password == user["user_name"])):
            return("Welcome")
        else:
            return("Not such user")
    return ("No data from data base")



print(add_user(users_table))