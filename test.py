from main import login,add_user,delete_user,upload,add_task,search_user,search_person_tasks
users_table = [{'eya2986407':'eyaly'}, {'ohad123':'eyalyeh'},{'ohad1234567':'ohadyehiely'}]
import datetime

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

datetime.timedelta
#4 - add task
tasks_list = []
print(add_task(task_name = 'House cleaning', task_serial_num = len(tasks_list) + 1, name = 'Eyal', tz = '322986407', accept_date = datetime.datetime.now(), mission_end_date = datetime.timedelta(year = 2023, month = 1 ,day = 5), description = 'Your mission is to clean the house ', status = False))


#5 - search user
#print(search_user(password ='ey2986407', users_table = users_table))


#6 -search_person_tasks
# print(search_person_tasks(tz, tasks_list):)