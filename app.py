from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

notes = []

@app.route("/")
def index():
    return render_template("index.html", notes=notes)

@app.route("/add", methods=["POST"])
def add_note():
    text = request.form.get("note")
    if text:
        notes.append({
            "text": text,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "done": False
        })
    return redirect("/")

@app.route("/delete/<int:note_id>")
def delete_note(note_id):
    if 0 <= note_id < len(notes):
        notes.pop(note_id)
    return redirect("/")

@app.route("/toggle/<int:note_id>")
def toggle_note(note_id):
    if 0 <= note_id < len(notes):
        notes[note_id]["done"] = not notes[note_id]["done"]
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
