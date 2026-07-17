from flask import Flask, request, redirect
import sqlite3

app = Flask(__name__)

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

@app.route("/")
def index():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, text, erledigt FROM todos")
    todos = cursor.fetchall()
    conn.close()

    html = """
    <style>
        body { font-family: Arial, sans-serif; max-width: 600px; margin: 40px auto; background: #f4f4f4; }
        h1 { color: #333; }
        .todo { background: white; padding: 12px; margin: 8px 0; border-radius: 6px; display: flex; justify-content: space-between; align-items: center; }
        .erledigt { text-decoration: line-through; color: #999; }
        a { text-decoration: none; margin-left: 10px; font-size: 14px; }
        .btn-done { color: green; }
        .btn-del { color: red; }
        form { margin-top: 20px; display: flex; gap: 8px; }
        input { flex: 1; padding: 10px; border: 1px solid #ccc; border-radius: 6px; }
        button { padding: 10px 20px; background: #007bff; color: white; border: none; border-radius: 6px; cursor: pointer; }
    </style>
    <h1>Meine Todos</h1>
    """
    for todo_id, text, erledigt in todos:
        css_klasse = "erledigt" if erledigt else ""
        html += f'<div class="todo"><span class="{css_klasse}">{text}</span><span>'
        html += f'<a class="btn-done" href="/done/{todo_id}">✓ erledigt</a>'
        html += f'<a class="btn-del" href="/delete/{todo_id}">✗ löschen</a>'
        html += '</span></div>'
    html += '<form method="post" action="/add"><input name="text" placeholder="Neue Aufgabe..."><button>Hinzufügen</button></form>'
    return html

@app.route("/add", methods=["POST"])
def add():
    text = request.form["text"]
    conn = get_connection()
    conn.execute("INSERT INTO todos (text) VALUES (?)", (text,))
    conn.commit()
    conn.close()
    return redirect("/")

@app.route("/done/<int:todo_id>")
def done(todo_id):
    conn = get_connection()
    conn.execute("UPDATE todos SET erledigt = 1 WHERE id = ?", (todo_id,))
    conn.commit()
    conn.close()
    return redirect("/")

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    conn = get_connection()
    conn.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
    conn.commit()
    conn.close()
    return redirect("/")

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", debug=True)