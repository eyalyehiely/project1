from main import save
#test 1 - add user
# users_table = [{'eya2986407':'eyaly'}, {'ohad123':'eyalyeh'}]
# def add_user(user_name,password):
#     dict1 = {}
  
#     print('''
#     User Name Instructions:
#     1. Must to be just letters
#     2. More than 4 letters  
          
#     Password Instructions:
#     Please make sure that your password is:
#     1. Passwords must be a minimum of seven characters in length.
#     2. Must consist both numbers and signs/letters.''')
#     for user in users_table:
#         if ((len(user_name) > 4) and (user_name.isalpha) and (user_name != user )):
#             print("User name is ok ! - continue to password")
#         else:
#             print("User name is not ok")
#             exit()
        

    #     if((len(password) >= 7) and (password.isdigit != True)):
    #         print("Password is ok")
    #     else:
    #         print("Password is not ok")
    #         exit()
    
    # dict1.update({user_name:password})
    # #save(user_dict)
    # return users_table
    

# user_name = input("Enter user name according to the instructions: ")
# password = input("Enter password according to the instructions: ")
#print(add_user(user_name = 'ohadyehuh',password = 'eyal123' ))
#print(users_table['eyaly'])
#vdvd#


#2 

# def delete_user(users_table:list,password_to_delete:str):
#     '''The password is the key so it is 1 in a kind'''
#     for users in users_table:
#         for password in users:
#             if password_to_delete == password:
#                 users_table.remove(users)
#                 save(users_table)
#                 print("User deleted")
            
#         else:
#             continue

# password_to_delete = input("ENTER PASSWORD: ")
# delete_user(users_table,password_to_delete='eya2986407')
# print(users_table)



# def search_user(users_table:list,password:str):
#    for users in users_table:
#         for passwords in users:
#             if password == passwords:
#                 print(users)



# search_user(users_table,password='ohad123')


# import random
# x= random.choice(20)
# print(x)



# sta = bool(input("Enter which status do you want to check: True/False "))

# print(type(sta))



#users_table = [{'eya2986407':'eyaly'}, {'ohad123':'eyalyeh'}]

# users_table = []

# def login(user_name:str, password:str, users_table:list):
#     for user in users_table:
#         for parameter_password in user:
#             if ((user_name == user.get(password)) and (password == parameter_password)):
#                 return("Welcome")
#     else:
#         return("No such user")
    

# print(login(user_name = 'eyalyu',password = 'eyal2001', users_table = users_table))



#login/sign in 

from main import login, add_user
import datetime
action = None
users_table = []
tasks_list = []

answer = int(input("1 : sign in / 2 : login: "))
if answer == 2:
    for i in range(3):
        print("You have",abs((i-3)),"tries to login")
        user_name = input("Enter your user name: ")
        password = input("Enter your password: ")
        approval = login(user_name, password, users_table)
        if approval == "Welcome":
            continue
    else:
        print("You transferred to the Sign in window")
        approval = (add_user(users_table))
else:
    print("Sign in window")
    approval = (add_user(users_table)) 
