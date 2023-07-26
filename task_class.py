import datetime
class Task:
    def __init__(self, task_name:str = "def",task_num:int = 0, name:str = 'def', category:str = 'def',accept_date = 'def', mission_end_date:int = 'def', description:str = 'def',tz = 'def' ):
        self.task_name = task_name
        self.tz = tz
        self.task_num = task_num
        self.name = name
        self.category = category
        self.accept_date = accept_date
        self.mission_end_date = mission_end_date
        self.description = description

    
    def __repr__(self):
        return f"\nTask Name:\t{self.task_name}\nTask Number:\t{self.task_num}\nPerson Name:\t{self.name}\nId:\t{self.tz}\nCategory:\t{self.category}\nAccepting Date:\t{self.accept_date}\nMission End Date:\t{self.mission_end_date}\nDescription:\t{self.description}\n\n"
    
    def __str__(self):
        pass

