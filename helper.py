import todofunctions

#save and load needs to be done
def display_options():
    print("Choose an option:")
    print("1. Add a new task")
    print("2. Mark task as completed")
    print("3. Remove the task")
    print("4. Edit pre-existing task")
    print("5. Add priority")
    print("6. Exit")
    choice = input('\nPlease enter your choice (1-5):')
    choice = int(choice)
    return choice

def main():
    list_obj = todofunctions.todoList()
    print("Welcome")
    choice = display_options()
    flag = True
    #list_obj.add_task("Finish dinner",3)
    #list_obj.display_list()

    while (flag != False):
        if(choice == 1):
            taskName = input('Enter the name of the task:')
            print("Priority options:")
            print("1: High")
            print("2: Medium")
            print("3: Low")
            priority = input('Enter priority number:')
            priority = int(priority)
            while (priority < 1 or priority > 3):
                print("Please enter valid input (1,2,3)")
                priority = input('Enter priority number:')
                priority = int(priority)

            list_obj.add_task(taskName,priority)
            list_obj.display_list()
            choice = display_options()

        elif (choice == 2):
            list_obj.display_list()
            taskid = input("Enter the task number you would like to mark as completed:")
            taskid = int(taskid)
            list_obj.mark_task(taskid)
            list_obj.display_list()
            choice = display_options()
        elif (choice == 6):
            print("Goodbye")
            flag = False


main()