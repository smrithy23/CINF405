import tkinter as tk
from tkinter import ttk, messagebox
from task_manager import TaskManager
from database_manager import DatabaseManager

class TaskManagerUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Task Manager")

        # Initialize DatabaseManager and TaskManager
        self.db_manager = DatabaseManager()
        self.task_manager = TaskManager(self.db_manager)

        # UI Elements
        self.setup_ui()

    def setup_ui(self):
        # Task entry fields
        ttk.Label(self.master, text="Title:").grid(row=0, column=0)
        self.title_entry = ttk.Entry(self.master)
        self.title_entry.grid(row=0, column=1)

        ttk.Label(self.master, text="Description:").grid(row=1, column=0)
        self.description_entry = ttk.Entry(self.master)
        self.description_entry.grid(row=1, column=1)

        ttk.Label(self.master, text="Priority:").grid(row=2, column=0)
        self.priority_entry = ttk.Combobox(self.master, values=["low", "medium", "high"])
        self.priority_entry.grid(row=2, column=1)
        self.priority_entry.set("low")

        ttk.Label(self.master, text="Due Date (YYYY-MM-DD):").grid(row=3, column=0)
        self.due_date_entry = ttk.Entry(self.master)
        self.due_date_entry.grid(row=3, column=1)

        # Buttons
        ttk.Button(self.master, text="Add Task", command=self.add_task).grid(row=4, column=1, sticky=tk.W)
        ttk.Button(self.master, text="Refresh List", command=self.refresh_tasks).grid(row=4, column=1, sticky=tk.E)

        # Task list
        self.task_tree = ttk.Treeview(self.master, columns=("ID", "Title", "Description", "Priority", "Due Date", "Completed"), show="headings")
        self.task_tree.grid(row=5, column=0, columnspan=2)
        for col in self.task_tree["columns"]:
            self.task_tree.heading(col, text=col)

        # Single "Mark Complete" button
        self.complete_button = ttk.Button(self.master, text="Mark Complete", command=self.mark_task_complete)
        self.complete_button.grid(row=6, column=0, sticky=tk.W)

        self.refresh_tasks()


    def add_task(self):
        title = self.title_entry.get()
        description = self.description_entry.get()
        priority = self.priority_entry.get()
        due_date = self.due_date_entry.get()

        if title:
            self.task_manager.add_task(title, description, priority, due_date)
            self.refresh_tasks()
        else:
            messagebox.showerror("Error", "Title is required to add a task.")

    def refresh_tasks(self):
    # Remove all current items in the Treeview
        for i in self.task_tree.get_children():
            self.task_tree.delete(i)

        # Insert new tasks into the Treeview
        for task in self.task_manager.list_tasks():
            self.task_tree.insert('', 'end', values=task)


    def mark_task_complete(self):
        selected_item = self.task_tree.selection()
        if selected_item:
            # Assuming the first column in your Treeview is the task ID
            task_id = self.task_tree.item(selected_item[0], 'values')[0]
            self.task_manager.update_task_completion(task_id, True)
            self.refresh_tasks()
        else:
            messagebox.showinfo("Info", "Please select a task to mark as complete.")

    def on_close(self):
        self.task_manager.close()
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerUI(root)
    root.protocol("WM_DELETE_WINDOW", app.on_close)
    root.mainloop()
