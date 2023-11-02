#getters and setter

class Task:
    def __init__(self, task, duedate, priority):
        self.task = task
        self.duedate = duedate
        self.priority = priority
        #when new task is added, set it default to false
        self.completion = False

        
    
