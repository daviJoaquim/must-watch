from flask import Flask, redirect, render_template, request, url_for
from models.database import init_db
from models.lista import Lista

app = Flask(__name__)
init_db()

@app.route('/')
def home():
    return render_template('home.html', titulo='Home')

@app.route('/lista', methods=['GET', 'POST'])
def lista():
    if request.method == 'POST':
        titulo_lista = request.form['titulo-lista']
        tipo_de_categoria = request.form['tipo_de_categoria']
        indicado = request.form['indicado']
        
        lista = Lista(titulo_lista, tipo_de_categoria, indicado)
        lista.salvar_lista()

    listas = Lista.obter_listas()
    return render_template('lista.html', titulo='Sua Lista de Desejos', listas=listas)

@app.route('/delete/<int:idLista>')
def delete(idLista):
    lista = Lista.id(idLista)
    lista.excluir_lista()
    return redirect(url_for('lista'))

@app.route('/update/<int:idLista>', methods=['GET', 'POST'])
def update(idLista):
    lista_selecionada = Lista.id(idLista)

    if request.method == 'POST':
        titulo_lista = request.form['titulo-lista']
        tipo_de_categoria = request.form['tipo_de_categoria']
        lista = Lista(titulo_lista, tipo_de_categoria, id_lista=idLista)
        lista.atualizar_lista()

    listas = Lista.obter_listas()
    return render_template(
        'lista.html', 
        titulo=f'Editando a lista ID: {idLista}',
        lista_selecionada=lista_selecionada,
        listas=listas
    )

@app.route('/ola')
def ola_mundo():
    return "Olá, Mundo!"
