from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/saludo/<nombre>')
def saludo(nombre):
    contexto = {
        'nombre': nombre,
        'edad': 14
    }
    return render_template('saludo.html', **contexto)


@app.route('/lista')
def lista():
    lista_personas = [
        {'nombre': 'moises', 'edad': 19},
        {'nombre': 'juan', 'edad': 23},
        {'nombre': 'pedro', 'edad': 45},
        {'nombre': 'josue', 'edad': 20},
        {'nombre': 'judas', 'edad': 12},
    ]
    return render_template('lista.html', lista=lista_personas)


@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        nombre = request.form['nombre']
    else:
        nombre = ''
    return render_template('formulario.html', nombre=nombre)

app.run(debug=True)
