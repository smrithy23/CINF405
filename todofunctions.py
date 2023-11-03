#enums for priorities 
#attributes for the class

class todoList:
    def __init__(self):
        #dictionary to add task
        self.tasks = {} 
    
    #add task
    # def add_task(self,task):
    #     numtasks = len(self.tasks)
    #     self.tasks[numtasks+1] = {'Task':task, 'Priority': 0, 'Completed':False }
    #     print("Task added in 1")
    
    #To add task, sets priority for the task, and defaults the completed to False
    def add_task(self,task,priority):
        numtasks = len(self.tasks)
        self.tasks[numtasks+1] = {'Task':task, 'Priority': priority, 'Completed':False }
        print("Task added sucessfully")

    #displays the current list
    def display_list(self):
        print("To-do list")
        print("----------")
        for k,v in self.tasks.items():
            print("Task ID:", k)

            for key in v:
                print(key + ':', v[key])

            print("\n")
    #remove task
    #display task

    #Edit task
    def __str__(self):
        return self.tasks