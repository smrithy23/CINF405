#enums for priorities 
#attributes for the class

class todoList:
    def __init__(self):
        #tasks is a list of tasks the user wants to add
        self.tasks = [] 
    
    #add task
    def add_task(self,task):
        self.tasks.append(task)
        print("Task added")

    #displays the current list
    def display_list(self):
        print("To-do list:")
        for i in range(len(self.tasks)):
            print(str(i) + ":" + self.tasks[i])

    #remove task
    #display task

    #Edit task
    def __str__(self):
        return self.tasks