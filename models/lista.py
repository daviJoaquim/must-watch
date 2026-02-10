from models.database import Database
from typing import Self, Any, Optional
from sqlite3 import Cursor

class Lista:
    """
        Classe para representar uma tarefa, com métodos para salvar, obter,
        excluir e atualizar tarefas em um banco de dados usando a classe
        `Database`
    """
    def __init__(self: Self, titulo_lista: Optional[str], categorias: 
    Optional[str] = None, id_lista: Optional[int] = None) -> None:
        self.titulo_lista: Optional[str] = titulo_lista
        self.categorias: Optional[str] = categorias
        self.id_lista: Optional[int] = id_lista
    
    @classmethod
    def id(cls, id: int) -> Self:
        with Database() as db:
            query: str = 'SELECT titulo_lista, categorias FROM listas WHERE id = ?;'
            params: tuple = (id,)
            resultado: list[Any] = db.buscar_tudo(query, params)
            
            [[titulo, categoria]] = resultado
            
            return cls(id_lista=id, titulo_lista=titulo, categorias=categoria)
    
    def salvar_listas(self: Self) -> None:
        with Database() as db:
            query: str = 'INSERT INTO listas (titulo_lista, categorias) VALUES (?, ?);'
            params: tuple = (self.titulo_lista, self.categorias)
            db.executar(query, params)

    @classmethod
    def obter_listas(cls) -> list[Self]:
        with Database() as db:
            query: str = 'SELECT titulo_lista, categorias, id FROM listas;'
            resultados: list[Any] = db.buscar_tudo(query)
            listas: list[Self] = [cls(titulo, categorias, id) for titulo, categorias, id in resultados]
            return listas
        
    def excluir_lista(self) -> Cursor:
        with Database() as db:
            query: str = 'DELETE FROM listas WHERE id = ?;'
            params: tuple = (self.id_lista,)
            resultado: Cursor = db.executar(query, params)
            return resultado
    
    def atualizar_lista(self) -> Cursor:
        with Database() as db:
            query: str = 'UPDATE listas SET titulo_lista = ?, categorias = ? WHERE id = ? ;'
            params: tuple = (self.id_lista, self.titulo_lista, self.categorias)
            resultados: Cursor = db.executar(query, params)
            return resultados