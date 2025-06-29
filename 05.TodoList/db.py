import sqlite3


class Todo:
    def __init__(self, id, title, completed):
        self.id = id
        self.title = title
        self.completed = completed



class Db:
    def __init__(self):
        self.conn = sqlite3.connect(".\\db.sqlite3")
        self.cur = self.conn.cursor()

        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS todos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                completed INTEGER NOT NULL DEFAULT 0
            )
        """)

    def add_todo(self, title: str):
        self.cur.execute("""
            INSERT INTO todos (title) VALUES (?)
        """, (title,))
        self.conn.commit()

    def get_all_todos(self) -> list[Todo]:
        self.cur.execute("""
            SELECT * FROM todos
        """)
        todos = []
        res = self.cur.fetchall()
        for item in res:
            todos.append(Todo(*item))
        return todos

    def delete_todo(self, id: int):
        self.cur.execute("""
            DELETE FROM todos WHERE id=?
        """, (id,))
        self.conn.commit()

    def get_todo(self, id: int) -> Todo:
        self.cur.execute("""
            SELECT FROM todos WHERE id=?
        """, (id,))
        todo = self.cur.fetchone()
        return Todo(*todo)

    def toggle_complete(self, todo: Todo):
        self.cur.execute("""
            UPDATE todos SET completed=? WHERE id=?
        """, (not todo.completed, todo.id))
        self.conn.commit()

    def __del__(self):
        self.cur.close()
        self.conn.close()
