from main import add_user,delete_user,upload,add_task,upload_tasks,save_tasks,update_task,delete_task,updating_status
users_table = [{'eya2986407':'eyaly'}, {'tal123':'talmanor'},{'ohad1234567':'ohadyehiely'}]
import datetime
import random
import math
#checking only crud function:
#-------------------------------------------#

#1 - add user
#print(add_user(users_table))
#option1:
#user_name = 'eyalyehiely'
#password = 'eyal12345'
#output = User add successfully
#print(upload())
#-------------------------------------------#


#2 - show users data base
#print(upload(users_table))
#-------------------------------------------#
#3 - delete user
#print(delete_user(users_table = upload(), password_to_delete = 'eya2986407'))
#print(upload())
#output = User deleted

#-------------------------------------------#



# 4 - add task
#tasks_list = []
# task_names = ['House cleaning','buying milk','make dinner']
# names = ['eyal','tal','gal']
# tzs =['234252345','453252354','345234524']
# categories = {1:'cleaning', 2:'buying',3:'cooking'}
# accept_date = datetime.date.today()
#task_serial_num = 123123

#print(add_task(task_name = random.choice(task_names), task_serial_num = task_serial_num, name = random.choice(names), tz = random.choice(tzs),category= categories.get(2) ,accept_date = datetime.date.today(),mission_end_date = datetime.date(year = 2020,month = 8, day = 5), description = 'description ', status = 'Not finished'))

#print(upload_tasks())
#-------------------------------------------------#

#7 - update task by a key
#print(update_task(key = 1 , tasks_list  = upload_tasks(),serial_num = 123123 ))
#-------------------------------------------------#


#9 - show all tasks
#print(upload_tasks())
#-------------------------------------------------#


#10 - changing status
# done = 'y'
# serial num = 123123
# updating_status(done,serial_num, tasks_list = upload_tasks()):
#-------------------------------------------------#

#13 - delete task
#print(delete_task(serial_num = 123123, tasks_list = upload_tasks()))




#-----------------------------------------#
#for Me:
# from main import save_tasks,save
# users_table = []
# save(users_table)

#---------------

# tasks_list = []
# save_tasks(tasks_list)

#-----------------------------------------#



