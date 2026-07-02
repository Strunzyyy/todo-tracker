from flask import Flask
from todo import laden

app = Flask(__name__)

@app.route("/")
def startseite():
    todos = laden()
    ergebnis = "<h1>Meine Aufgaben</h1>"
    for t in todos:
        status = "✓" if t["erledigt"] else "✗"
        ergebnis += f"<p>[{status}] {t['text']}</p>"
    return ergebnis

if __name__ == "__main__":
    app.run(debug=True)