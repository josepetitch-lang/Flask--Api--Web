from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://students.db"

db = SQLAlchemy(app)

class Student(db.Model):
    id =db.Column(db.Integer, primary_Key = True) ,
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(120), nullable = False, unique = True)
    age = db.Column(db.integer, nullable = False)


with app.app_context:
    db.create_all()

migrate = Migrate(app,  db)

if __name__ == "__main__":
    app.run(debug = True, port=9000)
