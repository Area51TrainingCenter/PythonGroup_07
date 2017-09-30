from flask import Flask


app = Flask(__name__)


@app.route('/calcular/<operacion>/<float:a>/<float:b>')
def calcular(operacion, a, b):
    if operacion == 'suma':
        return str(a + b)
    elif operacion == 'resta':
        return str(a - b)
    elif operacion == 'producto':
        return str(a * b)
    elif operacion == 'cociente':
        return str(a / b)

app.run(debug=True)
