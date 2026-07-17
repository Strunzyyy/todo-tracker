# Daily Tracker Dashboard

Ein persönliches Dashboard, um meinen Alltag und meine bisherigen "Paper-Checklisten" digital zu erfassen und abzuhaken.
Des Weiteren einfach nur eine gute Möglichkeit um für SuD etc. zu lernen :)

## Ziel des Projekts

Statt handschriftlicher Listen möchte ich meine wiederkehrenden Tagesaufgaben zentral an einem Ort tracken – per Klick, übersichtlich und auswertbar :)

## Was ich gerne (täglich) tracken möchte

**Gesundheit & Ernährung**
- Nährstoffe: Zink, Magnesium, Ashwagandha, Schwarzkümmelöl, Vitamin D3/K2
- Kiwi & Paranusskerne
- Kefir, Kaffee, 400g Gemüse
- Mittagessen gekocht & für den nächsten Arbeitstag eingepackt
- Ernährung in Yazio getrackt (Ziel: ~1.800 kcal – 222g Carbs, 111g Protein, 49g Fett)

**Training**
- Krafttraining
- VO2-Max-Training (40 min Rad, je dreimal pro Woche)

**Produktivität & Routine**
- AP1-Lernen
- 30 min Lesen am Abend
- Finance-Aufgaben erledigen, wenn welche anstehen
- Zimmer & Bett sauber und ordentlich halten

**Sonstiges**
- Katze gefüttert (als Beispiel)

## Motivation

Ein bewusst kleines Projekt – nicht zwingend notwendig, aber ein guter Weg, um meine Routinen sichtbar zu machen - in erster Linie aber nur ein LERN-Projekt.

## Tech-Stack

- Python
- Flask
- JSON (Datenspeicherung)
- HTML / CSS (Frontend)
- Jinja2 (Templates)
- SQLite (Datenbank)
- JavaScript (Interaktivität)

## Projekt-Struktur

Aufgebaut nach dem MVC-Prinzip (Model – View – Controller), um Datenlogik, Darstellung und Steuerung sauber zu trennen:

```
todo-tracker/
├── app.py              # Controller - verbindet Model & View, definiert Flask-Routen
├── models.py           # Model - Datenbank-Logik (SQLite CRUD: Create, Read, Update, Delete)
├── views.py            # View - HTML-Darstellung
├── Dockerfile           # Bauanleitung für den Docker-Container
├── requirements.txt     # Python-Abhängigkeiten (z.B. Flask)
├── todos.db             # SQLite-Datenbank
└── README.md            # Diese Dokumentation
```

**Architektur-Prinzip:**
- `models.py`
- `views.py` 
- `app.py` 

## Setup & Ausführen

**Lokal (ohne Docker):**
```bash
pip install -r requirements.txt
python app.py
```

**Mit Docker:**
```bash
docker build -t todo-tracker .
docker run -p 5000:5000 todo-tracker
```

Anschließend im Browser erreichbar unter `http://127.0.0.1:5000`
