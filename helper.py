import todofunctions

def main():
    list_obj = todofunctions.todoList()
    list_obj.add_task("Eat dinner")
    list_obj.add_task("Finish dinner")
    list_obj.display_list()

main()