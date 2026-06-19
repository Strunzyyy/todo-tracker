import json
import os

DATEI = "todos.json"

def laden():
    if os.path.exists(DATEI):
        with open(DATEI, "r") as f:
            return json.load(f)
    return []

def speichern(todos):
    with open(DATEI, "w") as f:
        json.dump(todos, f, indent=2)

def hinzufuegen(todos, text):
    todos.append({"text": text, "erledigt": False})
    speichern(todos)
    print(f"Hinzugefügt: {text}")

def anzeigen(todos):
    if not todos:
        print("Keine Aufgaben.")
    for i, t in enumerate(todos):
        status = "✓" if t["erledigt"] else "✗"
        print(f"{i}: [{status}] {t['text']}")

def erledigt(todos, index):
    if 0 <= index < len(todos):
        todos[index]["erledigt"] = True
        speichern(todos)
        print(f"Erledigt: {todos[index]['text']}")

if __name__ == "__main__":
    todos = laden()
    anzeigen(todos)