from sqlite3 import Cursor
from typing import Optional, Self, Any
from models.database import Database

class Lista:
    """
        Classe Para representar atividade, com metodos para salvar, obter, excluir e  atualizar tarefas com um banco de dados usando a classe Database.
    """
    def __init__(self: Self, titulo_lista: Optional[str], tipo_de_categoria: Optional[str] = None ,indicado:Optional[str] = None, id_lista:Optional[int] = None)-> None:
        self.titulo_lista: Optional[str] = titulo_lista
        self.tipo_de_categoria: Optional[str]  = tipo_de_categoria
        self.indicado: Optional[str] = indicado
        self.id_lista: Optional[int] = id_lista
        

    @classmethod
    def id(cls, id: int) -> Self:
        with Database() as db:
            query: str = 'SELECT titulo_lista, tipo_de_categoria, indicado FROM lista WHERE id = ?;'
            params: tuple = (id,)
            resultado = db.buscar_tudo(query, params)
            print(resultado)

            [[titulo, tipo, indicado]] = resultado

        return cls(id_lista=id, titulo_lista=titulo, tipo_de_atividade=tipo, indicado=indicado)
        
    def salvar_lista(self: Self)-> None:
        with Database() as db:
            query: str = " INSERT INTO atividades (titulo_lista, tipo_de_categoria, indicado) VALUES (?, ?, ?);"
            params: tuple = (self.titulo_lista, self.tipo_de_categoria, self.indicado)
            db.executar(query, params)

    @classmethod
    def obter_listas(cls) -> list[Self]:
        with Database() as db:
            query = 'SELECT titulo_lista, categorias, id FROM listas;'
            resultados: list[Any] = db.buscar_tudo(query)
            listas = [cls(titulo, categorias, id_lista=id) for titulo, categorias, id in resultados]
            return listas
    
    def excluir_lista(self) -> Cursor:
        with Database() as db:
            query: str = 'DELETE FROM atividades WHERE id = ?;'
            params: tuple = (self.id_lista,)
            resultado: Cursor = db.executar(query, params)
            return resultado
    
    def atualizar_lista(self) -> Cursor:
           with Database() as db:
            query: str = 'UPDATE atividades SET titulo_atividade = ?, tipo_de_atividade = ?, indicado_por = ? WHERE id = ?;'
            params: tuple = (self.titulo_lista, self.tipo_de_categoria,self.indicado, self.id_lista)
            resultado: Cursor = db.executar(query, params)
            return resultado
    