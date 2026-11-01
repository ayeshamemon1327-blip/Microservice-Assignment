from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def connect_db():
    return sqlite3.connect("students.db")

with connect_db() as db:
    db.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)

@app.route("/students", methods=["GET"])
def get_students():
    with connect_db() as db:
        db.row_factory = sqlite3.Row
        rows = db.execute("SELECT * FROM students").fetchall()
        return jsonify([dict(row) for row in rows])

@app.route("/students/<int:id>", methods=["GET"])
def get_student(id):
    with connect_db() as db:
        db.row_factory = sqlite3.Row
        row = db.execute(
            "SELECT * FROM students WHERE id=?", (id,)
        ).fetchone()

        if row is None:
            return jsonify({"error": "Student not found"}), 404

        return jsonify(dict(row))

@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json(silent=True) or {}

    if not all(data.get(k) for k in ("name", "department", "email")):
        return jsonify({"error": "All fields are required"}), 400

    with connect_db() as db:
        cursor = db.execute(
            "INSERT INTO students (name, department, email) VALUES (?, ?, ?)",
            (data["name"], data["department"], data["email"])
        )
        return jsonify({
            "message": "Student added",
            "id": cursor.lastrowid
        }), 201

@app.route("/students/<int:id>", methods=["PUT"])
def update_student(id):
    data = request.get_json(silent=True) or {}

    if not all(data.get(k) for k in ("name", "department", "email")):
        return jsonify({"error": "All fields are required"}), 400

    with connect_db() as db:
        cursor = db.execute(
            "UPDATE students SET name=?, department=?, email=? WHERE id=?",
            (data["name"], data["department"], data["email"], id)
        )

        if cursor.rowcount == 0:
            return jsonify({"error": "Student not found"}), 404

        return jsonify({"message": "Student updated"})

@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):
    with connect_db() as db:
        cursor = db.execute("DELETE FROM students WHERE id=?", (id,))

        if cursor.rowcount == 0:
            return jsonify({"error": "Student not found"}), 404

        return jsonify({"message": "Student deleted"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)