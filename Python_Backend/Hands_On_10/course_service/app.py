from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///course.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

with app.app_context():
    db.create_all()

    if not Course.query.first():
        db.session.add(Course(name="Python"))
        db.session.add(Course(name="Java"))
        db.session.commit()


@app.route("/api/courses", methods=["GET"])
def get_courses():
    courses = Course.query.all()

    return jsonify([
        {
            "id": c.id,
            "name": c.name
        }
        for c in courses
    ])


@app.route("/api/courses/<int:id>", methods=["GET"])
def get_course(id):
    course = Course.query.get(id)

    if not course:
        return jsonify({"message": "Course not found"}), 404

    return jsonify({
        "id": course.id,
        "name": course.name
    })


if __name__ == "__main__":
    app.run(port=5001, debug=True)