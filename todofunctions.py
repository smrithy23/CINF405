#enums for priorities 
#attributes for the class

class todoList:
    def __init__(self):
        #dictionary to add task
        self.tasks = {} 
   
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
    
    #mark as completed
    def mark_task(self,taskid):
        if taskid in self.tasks:
            self.tasks[taskid]['Completed'] = True
            print("Task has been masked as completed.")
        else:
            print("Invalid task number")
    #remove task

    #Edit task
    def __str__(self):
        return self.tasks