from flask import Flask, render_template, request, redirect, url_for
from models.lista import Lista
from models.database import init_db

app = Flask(__name__)

init_db()

@app.route('/')
def home():
    return render_template('home.html', titulo='Home')

@app.route('/lista', methods=['GET', 'POST'])
def agenda():
    listas = None
    
    if request.method == 'POST':
        titulo_lista = request.form['titulo-lista']
        categorias = request.form['categorias']
        lista = Lista(titulo_lista, categorias)
        lista.salvar_listas()

    listas = Lista.obter_listas()
    return render_template('lista.html', titulo='Lista de Desejos', listas=listas)

@app.route('/delete/<int:idLista>')
def delete(idLista):
    lista = Lista.id(idLista)
    lista.excluir_lista() 
    # return render_template('agenda.html', titulo="Agenda", tarefas=tarefas)
    return redirect(url_for('lista'))

@app.route('/update/<int:idLista>', methods = ['GET', 'POST'])
def update(idLista):
    listas = None
        
    if request.method == 'POST':
        titulo = request.form['titulo-lista']
        data = request.form['categorias']
        lista = Lista(titulo, data, idLista)
        lista.atualizar_lista()
        return redirect(url_for('lista'))
        
    listas = Lista.obter_listas()
    lista_selecionada = Lista.id(idLista)
    
    return render_template('lista.html', titulo=f'Editando a lista ID: {idLista}',
    listas=listas, lista_selecionada=lista_selecionada)

@app.route('/ola')
def ola_mundo():
    return "Olá, Mundo!"