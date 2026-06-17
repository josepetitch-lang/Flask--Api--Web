from flask import Flask

app = Flask(__name__)
@app.route("/")

def home():
    return "Hola we, estoy desde flask"
def products():
    return "Retorna la lista de productos xd"


if __name__ == "__main__":
    app.run(debug = True, port = 8000)