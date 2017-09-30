from flask import Flask

app = Flask(__name__)


@app.route('/')
def hola():
    return 'Hola mundo!'


# /calcular/suma/5/6
# /calcular/resta/5/6
# /calcular/producto/5/6
# /calcular/cociente/5/6
@app.route('/saludo/<nombre>')
def saludo(nombre):
    return 'Hola qué tal {}!'.format(nombre)

app.run(debug=True)
