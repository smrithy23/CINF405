import psycopg2
from psycopg2 import Error


class DatabaseManager:
    def __init__(self):
        self.connection = None
        try:
            self.connection = psycopg2.connect(
                host="cinf-405.cnyo73utyr2l.us-east-1.rds.amazonaws.com",
                user="postgres",
                password="postgres",
            )
            self.create_task_table()
        except Error as e:
            print(f"Error connecting to PostgreSQL database: {e}")

    def check_connection(self):
        if self.connection:
            return True
        return False

    def create_task_table(self):
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS tasks (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            description TEXT,
            priority TEXT DEFAULT 'low',
            due_date DATE,
            completed BOOLEAN DEFAULT FALSE
        )
        '''
        self.execute_query(create_table_query)

    def execute_query(self, query, values=None):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, values)
            self.connection.commit()
        except Error as e:
            print(f"Error executing query: {e}")

    def insert_task(self, title, description, priority, due_date):
        insert_query = '''
        INSERT INTO tasks (title, description, priority, due_date)
        VALUES (%s, %s, %s, %s)
        '''
        self.execute_query(insert_query, (title, description, priority, due_date))

    def update_task(self, task_id, title, description, priority, due_date):
        update_query = '''
        UPDATE tasks
        SET title = %s, description = %s, priority = %s, due_date = %s
        WHERE id = %s
        '''
        self.execute_query(update_query, (title, description, priority, due_date, task_id))

    def delete_task(self, task_id):
        delete_query = 'DELETE FROM tasks WHERE id = %s'
        self.execute_query(delete_query, (task_id,))

    def mark_task_as_completed(self, task_id):
        update_query = 'UPDATE tasks SET completed = TRUE WHERE id = %s'
        self.execute_query(update_query, (task_id,))

    def update_task_completion(self, task_id, completed):
        update_query = "UPDATE tasks SET completed = %s WHERE id = %s"
        self.execute_query(update_query, (completed, task_id))


    def fetch_all_tasks(self):
        fetch_query = 'SELECT * FROM tasks'
        cursor = self.connection.cursor()
        try:
            cursor.execute(fetch_query)
            tasks = cursor.fetchall()
            return tasks
        except Error as e:
            print(f"Error fetching data: {e}")
            return []

    def close_connection(self):
        if self.connection:
            self.connection.close()


if __name__ == "__main__":
    db_manager = DatabaseManager()

    # Check if the connection is working
    if db_manager.check_connection():
        # Perform database operations
        # ...

    # Close the connection when done
        db_manager.close_connection()