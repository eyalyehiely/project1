from itertools import count
from main import login,add_user,delete_user,upload,add_task,search_user,search_person_tasks,upload_tasks,save_tasks,update_task,search_by_category,checking_status,delete_task
users_table = [{'eya2986407':'eyaly'}, {'ohad123':'eyalyeh'},{'ohad1234567':'ohadyehiely'}]
import datetime
import random
import math

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
#print(upload())
'''output = User deleted
[{'ohad123': 'eyalyeh'}]'''

tasks_list = []
# 4 - add task
# data_test:
task_names = ['House cleaning','buying milk','make dinner']
names = ['eyal','tal','gal']
tzs =['234252345','453252354','345234524']
categories = {1:'cleaning', 2:'buying',3:'cooking'}
accept_date = datetime.date.today()


for i in range(2):
    task_serial_num = int(input("give task unique number"))
    print(add_task(task_name = random.choice(task_names), task_serial_num = task_serial_num, name = random.choice(names), tz = random.choice(tzs),category= categories.get(2) ,accept_date = datetime.date.today(),mission_end_date = datetime.date(year = 2020,month = 8, day = 5), description = 'description ', status = False))



#print(delete_task(12,tasks_list))


#print(upload_tasks())

#5 - search user
#print(search_user(password ='ohad123', users_table = upload()))


#6 -search_person_tasks
#print(search_person_tasks(tz = '345234524' , tasks_list= upload_tasks()))
#output = relevant task according the Id


#7 - update task by a key
# print(update_task(key = 1 , tasks_list  = upload_tasks()))


#8 - search tasks by category
#print(search_by_category(tasks_list = upload_tasks(), key = 'buying'))


#9 - show all tasks
#print(upload_tasks())


#10 - changing status
# changing_status(serial_num, tasks_list = upload_tasks()):

#11 - show tasks status
#print(checking_status(status_value = True, tasks_list = upload_tasks()))
#output = []
print(list)