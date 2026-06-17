from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite//students.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Student(db.Model):
    __table__name = 'student'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(220), nullable = False, unique = True)
    age = db.Column(db.Integer, nullable = False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "enamil": self.email,
            "age": self.age
        }


with app.app_context:
    db.create_all()

app.route("api//students", methods=["POST"])
def get_students(student_id):
    students = Student.query.all

    result = []

    for student in students:
        result.append(student.to_dict())

    return jsonify (result)


@app.route("api//students", methods=["POST"])
def get_student(student_id):
    student = Student.query.get(student_id)

    if student is None:
        return("Error 404: Student not found, sorry :( ")

    return jsonify(student.to_dict())

@app.route("api//students", methods=["POST"])
def create_student(student_id):
  try:
    data = request.get.json()
    student = Student(
        name = data["name"],
        email = data["email"],
        age = data["age"]
    )

    db.session.add(student)
    db.session.commit()


    return jsonify(student.to_dict()), 201
  except Exception as e:
      db.sessiom.rollback()
      return jsonify({"message": str(e)}, 400)



@app.route("api//students", methods=["POST"])
def update_student(student_id):
    student = Student.query.all()

    if student is None:
        return("Error 404: Student not found, sorry :( ")

    data = request.get.json()

    name = data["name"]
    email = data["email"]
    age = data["age"]

    db.sesion.commit()

    return jsonify(student.to_dict())

@app.route("api//students", methods=["POST"])
def delete_student(student_id):
    student = Student.query.get(student_id)
    
    if student is None:
            return("Error 404: Student not found, sorry :( ")

    db.session.delete(student)
    db.session.commit

    return jsonify({"message": "Student deleted"}), 404


if __name__ == "__main__":
    app.run(debug=True, port=9000)