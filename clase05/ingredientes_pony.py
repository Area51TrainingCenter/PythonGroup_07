from flask import Flask, render_template, request, redirect
from pony.orm import *
from models import Ingrediente

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@db_session
def home():
    if request.method == 'POST':
        ingrediente = Ingrediente(nombre=request.form['ingrediente'])

    ingredientes = select(i for i in Ingrediente)

    return render_template('compras.html', ingredientes=ingredientes)


@app.route('/editar/<int:id>', methods=['GET', 'POST'])
@db_session
def editar(id):
    ingrediente = Ingrediente[id]

    if request.method == 'POST':
        ingrediente.nombre = request.form['ingrediente']
        return redirect('/')

    return render_template('editar.html', ingrediente=ingrediente)


@app.route('/borrar/<int:id>')
@db_session
def borrar(id):
    ingrediente = Ingrediente[id]
    ingrediente.delete()
    return redirect('/')

app.run(debug=True)
