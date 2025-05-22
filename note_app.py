from flask import Flask, render_template_string, request, redirect, url_for
from pathlib import Path

app = Flask(__name__)
NOTES_DIR = Path("notes")
NOTES_DIR.mkdir(exist_ok=True)

INDEX_TEMPLATE = """
<!doctype html>
<title>LLM Notes</title>
<h1>LLM Notes</h1>
<ul>
  {% for note in notes %}
    <li><a href="{{ url_for('edit_note', filename=note) }}">{{ note }}</a></li>
  {% else %}
    <li>No notes found.</li>
  {% endfor %}
</ul>
<h2>Create a new note</h2>
<form action="{{ url_for('new_note') }}" method="post">
  <input name="filename" placeholder="note.md">
  <input type="submit" value="Create">
</form>
"""

EDIT_TEMPLATE = """
<!doctype html>
<title>{{ filename }}</title>
<h1>Editing {{ filename }}</h1>
<form method="post">
  <textarea name="content" rows="20" cols="80">{{ content }}</textarea><br>
  <input type="submit" value="Save">
</form>
<a href="{{ url_for('index') }}">Back to list</a>
"""

@app.route('/')
def index():
    notes = sorted(p.name for p in NOTES_DIR.glob('*') if p.is_file())
    return render_template_string(INDEX_TEMPLATE, notes=notes)

@app.route('/new', methods=['POST'])
def new_note():
    filename = request.form.get('filename', '').strip()
    if not filename:
        return redirect(url_for('index'))
    path = NOTES_DIR / filename
    path.touch(exist_ok=True)
    return redirect(url_for('edit_note', filename=filename))

@app.route('/note/<path:filename>', methods=['GET', 'POST'])
def edit_note(filename):
    path = NOTES_DIR / filename
    if request.method == 'POST':
        content = request.form.get('content', '')
        path.write_text(content, encoding='utf-8')
        return redirect(url_for('edit_note', filename=filename))
    content = path.read_text(encoding='utf-8') if path.exists() else ''
    return render_template_string(EDIT_TEMPLATE, filename=filename, content=content)

if __name__ == '__main__':
    app.run(debug=True)
