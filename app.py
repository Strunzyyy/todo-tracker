from flask import Flask, request, redirect
import models
import views

app = Flask(__name__)

@app.route("/")
def index():
    todos = models.alle_todos()
    return views.render_todos(todos)

@app.route("/add", methods=["POST"])
def add():
    text = request.form["text"]
    models.todo_hinzufuegen(text)
    return redirect("/")

@app.route("/done/<int:todo_id>")
def done(todo_id):
    models.todo_erledigt(todo_id)
    return redirect("/")

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    models.todo_loeschen(todo_id)
    return redirect("/")

if __name__ == "__main__":
    models.init_db()
    app.run(host="0.0.0.0", debug=True)