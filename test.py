from main import save
#test 1 - add user
users_table = [{'eya2986407':'eyaly'}, {'eyal322986407':'eyalyeh'}]
def add_user(user_name,password):
    dict1 = {}
    print('''
    User Name Instructions:
    1. Must to be just letters
    2. More than 4 letters  
          
    Password Instructions:
    Please make sure that your password is:
    1. Passwords must be a minimum of seven characters in length.
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
    
    dict1.update({user_name:password})
    #save(user_dict)
    return users_table
    

# user_name = input("Enter user name according to the instructions: ")
# password = input("Enter password according to the instructions: ")
#print(add_user(user_name = 'ohadyehuh',password = 'eyal123' ))
#print(users_table['eyaly'])
#vdvd#


#2 

def delete_user(users_table:list,password_to_delete:str):
    '''The password is the key so it is 1 in a kind'''
    for user in users_table:
        if password_to_delete == user.keys():
            del(user_password)
            save(users_table)
             
            
      
    

# password_to_delete = input("ENTER PASSWORD: ")
print(delete_user(users_table,password_to_delete = 'eya2986407'))
print(users_table)


