#This file contain only functions 
import pickle


#1 - adding user
def add_user(user_name:str,password:str,users_data_base:dict):
    print('''
    User Name Instructions:
    1. Must to be just letters
    2. More than 4 letters  
          
    Password Instructions:
    Please make sure that your password is:
    1. Passwords must be a minimum of seven characters in length.
    2. Must consist both numbers and signs/letters.''')
    for user in users_data_base:
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
    
    users_data_base.update({user_name:password})
    save(users_data_base)
    return users_data_base
    

#2 - save data base
def save(dict_to_save:dict):
    #saving data base to pickle
    with open ("users.pickle",'wb') as f:
        pickle.dump(dict_to_save,f)



#3 - upload data base
def upload():
    #uploading data base from pickle
    with open ("users.pickle",'rb') as f:
        users_data_base = pickle.load(f)
    return users_data_base



def login(user_name:str, password:str, users_data_base):
    for user in users_data_base:
        if ((user_name == user) and (password == user[user_name])):
            return("Welcome")
        else:
            return("Not such user")