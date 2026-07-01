from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///student.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

with app.app_context():
    db.create_all()

    if not Student.query.first():
        db.session.add(Student(name="Athif"))
        db.session.commit()


@app.route("/api/students", methods=["GET"])
def get_students():
    students = Student.query.all()

    return jsonify([
        {
            "id": s.id,
            "name": s.name
        }
        for s in students
    ])


@app.route("/api/students/<int:id>/enroll", methods=["POST"])
def enroll(id):

    data = request.get_json()

    course_id = data.get("course_id")

    try:
        response = requests.get(
            f"http://localhost:5001/api/courses/{course_id}"
        )

        if response.status_code != 200:
            return jsonify({
                "message": "Course not found"
            }), 404

    except requests.exceptions.ConnectionError:
        return jsonify({
            "message": "Course Service unavailable"
        }), 503

    return jsonify({
        "student_id": id,
        "course_id": course_id,
        "message": "Enrollment successful"
    })


if __name__ == "__main__":
    app.run(port=5002, debug=True)