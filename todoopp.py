class Todo:
    def __init__(self, text, erledigt=False):
        self.text = text
        self.erledigt = erledigt

    def abhaken(self):
        self.erledigt = True


meine_aufgabe = Todo("Dokumentation schreiben")
print(meine_aufgabe.erledigt)

meine_aufgabe.abhaken()

print(meine_aufgabe.erledigt)