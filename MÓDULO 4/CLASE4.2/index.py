from flask import Flask #kslkslkdlkslsklsklsklskslkslksls

app = Flask(__name__)

@app.route("/")

def home():
    return "Bienvenido a... sabrá Dios, yo no jaja"

@app.route("/libros")
def libros():
    return ["Libros de mierda:", "Nose," "Cien anos de soledad"]

@app.route("/soledad")
def cero_alegrías():
    return "sjsksjksjskjskjs, soy del arsenal" # ok a nadie le importa :'D

if __name__ == "__main__":
    app.run(debug = True, port = 8000)
    
    

