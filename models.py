import sqlite3

def get_connection():
    return sqlite3.connect("todos.db")

def init_db():
    conn = get_connection()
    conn.execute("""
    CREATE TABLE IF NOT EXISTS todos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text TEXT NOT NULL,
        erledigt INTEGER DEFAULT 0
    )
    """)
    conn.commit()
    conn.close()

def alle_todos():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, text, erledigt FROM todos")
    todos = cursor.fetchall()
    conn.close()
    return todos

def todo_hinzufuegen(text):
    conn = get_connection()
    conn.execute("INSERT INTO todos (text) VALUES (?)", (text,))
    conn.commit()
    conn.close()

def todo_erledigt(todo_id):
    conn = get_connection()
    conn.execute("UPDATE todos SET erledigt = 1 WHERE id = ?", (todo_id,))
    conn.commit()
    conn.close()

def todo_loeschen(todo_id):
    conn = get_connection()
    conn.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
    conn.commit()
    conn.close()