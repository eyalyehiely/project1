


user_dict = {'eyaly': 'eya2986407', 'eyalyeh': 'eyal322986407'}


def add_user(user_name,password):
    print('''
    User Name Instructions:
    1. Must to be just letters
    2. More than 4 letters  
          
    Password Instructions:
    Please make sure that your password is:
    1. Passwords must be a minimum of seven characters in length.
    2. Must consist both numbers and signs/letters.''')
    for user in user_dict:
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
    
    user_dict.update({user_name:password})
    #save(user_dict)
    return user_dict
    


# user_name = input("Enter user name according to the instructions: ")
# password = input("Enter password according to the instructions: ")



def login():
    pass