def render_todos(todos):
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