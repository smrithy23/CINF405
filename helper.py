import todofunctions

def display_options():
    print("Choose an option:")
    print("1. Add a new task")
    print("2. Mark task as completed")
    print("3. Remove the task")
    print("4. Edit pre-existing task")
    print("5. Add priority")

def main():
    list_obj = todofunctions.todoList()
    #list_obj.add_task("Eat dinner")
    list_obj.add_task("Finish dinner",3)
    list_obj.display_list()

main()