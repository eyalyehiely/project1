import datetime

# class User:
#     def __init__(self,user_name = 'def', password = 'def', tz = 'def'):
#         self.user_name = user_name
#         self.password = password
#         self.tz = tz

class Task:
    def __init__(self, task_name:str = "def",task_serial_num:int = None, name:str = 'def',category:dict = {} ,accept_date =None,mission_end_date = None, description:str = 'def',tz = 'def',status = 'Not finished'):
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
        return f"\nTask Name:\t{self.task_name}\nSerial Num:\t{self.task_serial_num}\nPerson Name:\t{self.name}\nId:\t\t{self.tz}\nCategory:\t{self.category}\nAccepting Date:\t{self.accept_date}\nEnd Date:\t{self.mission_end_date}\nDescription:\t{self.description}\nTask Status:\t{self.status}\n\n"
    

