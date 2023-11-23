import sqlite3
from datetime import datetime

def connect_db():
    return sqlite3.connect('tasks.db')

def create_table(conn):
    try:
        conn.execute('''CREATE TABLE tasks 
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                         title TEXT NOT NULL,
                         status TEXT NOT NULL,
                         priority TEXT,
                         due_date DATE,
                         notes TEXT);''')
        print("Table created successfully")
    except Exception as e:
        print(e)

def add_task(conn, title, priority, due_date, notes):
    conn.execute("INSERT INTO tasks (title, status, priority, due_date, notes) VALUES (?, 'Pending', ?, ?, ?)", 
                 (title, priority, due_date, notes))
    conn.commit()

def edit_task(conn, task_id, title=None, priority=None, due_date=None, notes=None):
    task = conn.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()
    if task:
        conn.execute("UPDATE tasks SET title = ?, priority = ?, due_date = ?, notes = ? WHERE id = ?", 
                     (title or task[1], priority or task[3], due_date or task[4], notes or task[5], task_id))
        conn.commit()

def mark_complete(conn, task_id):
    conn.execute("UPDATE tasks SET status = 'Completed' WHERE id = ?", (task_id,))
    conn.commit()

def remove_task(conn, task_id):
    conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()

def display_tasks(conn):
    cursor = conn.execute("SELECT id, title, status, priority, due_date, notes FROM tasks")
    for row in cursor:
        print(f"ID: {row[0]}, Title: {row[1]}, Status: {row[2]}, Priority: {row[3]}, Due Date: {row[4]}, Notes: {row[5]}")



# Example Usage
conn = connect_db()
create_table(conn)
add_task(conn, "Finish Python Project", "High", datetime.now().date(), "Important task")
display_tasks(conn)
