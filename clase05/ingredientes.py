from flask import Flask, render_template, request, redirect
from pony.orm import *

app = Flask(__name__)

ingredientes = ['papa', 'camote', 'lechuga']


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        ingredientes.append(request.form['ingrediente'])

    return render_template('compras.html', ingredientes=enumerate(ingredientes))


@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    if request.method == 'POST':
        ingredientes[id] = request.form['ingrediente']
        return redirect('/')

    ingrediente = ingredientes[id]

    return render_template('editar.html', ingrediente=ingrediente)


@app.route('/borrar/<int:id>')
def borrar(id):
    del ingredientes[id]
    return redirect('/')

app.run(debug=True)
