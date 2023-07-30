from main import login,add_user,delete_user,upload,add_task,search_user,search_person_tasks,upload_tasks,save_tasks
users_table = [{'eya2986407':'eyaly'}, {'ohad123':'eyalyeh'},{'ohad1234567':'ohadyehiely'}]
import datetime
import random

#1 - user login
#print(login(user_name = 'eyaly', password = 'eya2986407', users_table = users_table))
#output = 'welcome'

#2 - add user
#print(add_user(users_table))
#option1:
#user_name = 'eyalyehiely'
#password = 'eyal12345'
#output = User add successfully

#option2:
#user_name = 'tal'
#password = 'tal12345'
#output = try again + give u the option to sign in again

#3 - delete user
# print(delete_user(users_table = users_table, password_to_delete = 'eya2986407'))
# print(upload())
'''output = User deleted
[{'ohad123': 'eyalyeh'}]'''


#4 - add task
#data_test:
# task_names = ['House cleaning','buying milk','make dinner']
# names = ['eyal','tal','gal']
# tzs =['234252345','453252354','345234524']
# categories = {1:'cleaning', 2:'buying',3:'cooking'}
# accept_date = datetime.date.today()
# tasks_list = []
# save_tasks(tasks_list)
# # print(upload_tasks())
# for i in range(2):
#     print(add_task(task_name = random.choice(task_names), task_serial_num = int(len(tasks_list) + 1), name = random.choice(names), tz = random.choice(tzs),category= categories.get(2) ,accept_date = datetime.date.today(),mission_end_date = datetime.date(year = 2020,month = 8, day = 5), description = 'description ', status = False))

# print(len(tasks_list))







#5 - search user
#print(search_user(password ='ey2986407', users_table = users_table))


#6 -search_person_tasks
# print(search_person_tasks(tz, tasks_list):)

