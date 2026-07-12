import sqlite3

conn = sqlite3.connect("todos.db")
cursor = conn.cursor()

# UPDATE - Aufgabe 1 als erledigt markieren
cursor.execute("UPDATE todos SET erledigt = 1 WHERE id = 1")
conn.commit()

# DELETE - Aufgabe 2 löschen
cursor.execute("DELETE FROM todos WHERE id = 2")
conn.commit()

# READ - schauen was übrig ist
cursor.execute("SELECT * FROM todos")
alle = cursor.fetchall()

print("Nach Update und Delete:")
for zeile in alle:
    print(zeile)

conn.close()