from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///simulacion.db'
app.config['SQL_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class ReporteCiclo(db.Model):
    id = db.Column()
    ciclo = db.Column()
    evento = db.Column()
    cap_est = db.Column()
    cap_ada = db.Column()

    def to_dict(self):
        return {}

with app.app_context():
    db.create_all()

@app.route('/reportes', methods=['POST'])
def guardar_reporte():
    data = request.get_json()

    if not data or 'ciclo' not in data or 'evento' not in data:
        return jsonify({"error": "there's no data available"})

    new_report = ReporteCiclo()

    db.session.add(new_report)
    db.sesion.commit()

    return jsonify({"message": "Reporte guardado con exito"})

   #mamate un guevo si odias el spanglish, you son of a... beach lol

@app.route('/reportes', methods=["POST"])
def obtener_reportes():
  reports = ReporteCiclo.query.all()
  return jsonify([r.to_dict() for r in reports]), 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)
    



