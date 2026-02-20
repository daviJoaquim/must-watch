from flask import Flask, redirect, render_template, request, url_for
from models.database import init_db
from models.lista import Lista

app = Flask(__name__)

init_db()

@app.route('/')
def home():
    return render_template('home.html', titulo='Home')

@app.route('/lista', methods=['GET','POST'])
def lista():
    listas = None

    if request.method == 'POST':
        titulo_lista = request.form['titulo_lista']
        categoria = request.form['categoria']
        indicado = request.form['indicado']
    
        nova_lista = Lista(titulo_lista, categoria, indicado)
        nova_lista.salvar_lista()
        return redirect(url_for('lista'))

    listas = Lista.obter_listas()
    return render_template('lista.html', titulo='Sua Lista de Desejos', atividades=listas)

@app.route('/delete/<int:idLista>')
def delete(idLista):
    item_lista = Lista.id(idLista)
    item_lista.excluir_lista()
    return redirect(url_for('lista'))

@app.route('/update/<int:idLista>', methods=['GET', 'POST']) 
def update(idLista):
    if request.method == 'POST':
        titulo_lista = request.form['titulo_lista']
        categoria = request.form['categoria']
        indicado = request.form['indicado']
        item_lista = Lista(titulo_lista, categoria, indicado, idLista)
        item_lista.atualizar_lista()
        return redirect(url_for('lista'))

    listas = Lista.obter_listas()
    lista_selecionada = Lista.id(idLista)
    return render_template('lista.html', titulo=f'Editando o item ID: {idLista}', lista_selecionada=lista_selecionada, atividades=listas)

@app.route('/ola')
def ola_mundo():
    return "Olá, Mundo!"