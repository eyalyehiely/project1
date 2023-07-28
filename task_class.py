import datetime

# class User:
#     def __init__(self,user_name = 'def', password = 'def', tz = 'def'):
#         self.user_name = user_name
#         self.password = password
#         self.tz = tz

class Task:
    def __init__(self, task_name:str = "def",task_serial_num:int = 0, name:str = 'def',category = {1:'cleaning',2:'buying',3:'cooking'}, accept_date = 'def', mission_end_date:int = 'def', description:str = 'def',tz = 'def',status = False ):
        self.task_name = task_name
        self.tz = tz
        self.task_serial_num = task_serial_num
        self.name = name
        self.category = category
        self.accept_date = accept_date
        self.mission_end_date = mission_end_date
        self.description = description
        self.status = status

    
    def __repr__(self):
        return f"\nTask Name:\t{self.task_name}\nTask Number:\t{self.task_serial_num}\nPerson Name:\t{self.name}\nId:\t{self.tz}\nCategory:\t{self.category}\nAccepting Date:\t{self.accept_date}\nMission End Date:\t{self.mission_end_date}\nDescription:\t{self.description}\nTask Status\t{self.status}\n\n"
    
    def __str__(self):
        pass

