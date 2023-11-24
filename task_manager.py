from database_manager import DatabaseManager

class TaskManager:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def add_task(self, title, description='', priority='low', due_date=None):
        self.db_manager.insert_task(title, description, priority, due_date)

    def edit_task(self, task_id, title, description='', priority='low', due_date=None):
        self.db_manager.update_task(task_id, title, description, priority, due_date)

    def remove_task(self, task_id):
        self.db_manager.delete_task(task_id)

    def mark_complete(self, task_id):
        self.db_manager.mark_task_as_completed(task_id)

    def list_tasks(self):
    # Fetch tasks from the database
        tasks = self.db_manager.fetch_all_tasks()

        # Sort tasks based on a specific attribute (e.g., ID, creation time)
        sorted_tasks = sorted(tasks, key=lambda task: task[0])  # Assuming each task has an 'id' attribute

        return sorted_tasks
    
    def update_task_completion(self, task_id, completed):
        self.db_manager.update_task_completion(task_id, completed)

    def close(self):
        self.db_manager.close_connection()

if __name__ == "__main__":
    # Example usage
    db_manager = DatabaseManager()
    task_manager = TaskManager(db_manager)

    # Adding tasks
    task_manager.add_task("Task 1", "Description of Task 1", "high", "2023-12-01")
    task_manager.add_task("Task 2", "Description of Task 2", "medium")

    # Editing a task
    task_manager.edit_task(1, "Updated Task 1", "New Description", "low", "2023-11-30")

    # Marking a task as complete
    task_manager.mark_complete(2)

    # Listing all tasks
    task_manager.list_tasks()

    # Cleaning up
    task_manager.close()
