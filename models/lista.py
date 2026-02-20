from sqlite3 import Cursor
from typing import Optional, Self, Any
from models.database import Database

class Lista:
    """
        Classe para representar uma lista, com métodos para salvar, obter, 
        excluir e atualizar registros com um banco de dados usando a classe Database.
    """
    def __init__(
        self: Self, 
        titulo_lista: Optional[str], 
        categoria: Optional[str] = None, 
        indicado: Optional[str] = None, 
        id_lista: Optional[int] = None
    ) -> None:
        self.titulo_lista: Optional[str] = titulo_lista
        self.categoria: Optional[str] = categoria
        self.indicado: Optional[str] = indicado
        self.id_lista: Optional[int] = id_lista

    @classmethod
    def id(cls, id: int) -> Self:
        with Database() as db:
            query: str = 'SELECT titulo_lista, categoria, indicado FROM listas WHERE id = ?;'
            params: tuple = (id,)
            resultado = db.buscar_tudo(query, params)
            
            [[titulo, cat, ind]] = resultado

        return cls(id_lista=id, titulo_lista=titulo, categoria=cat, indicado=ind)

    def salvar_lista(self: Self) -> None:
        with Database() as db:
            query: str = "INSERT INTO listas (titulo_lista, categoria, indicado) VALUES (?, ?, ?);"
            params: tuple = (self.titulo_lista, self.categoria, self.indicado)
            db.executar(query, params)

    @classmethod
    def obter_listas(cls) -> list[Self]:
        with Database() as db:
            query: str = 'SELECT titulo_lista, categoria, indicado, id FROM listas;'
            resultados: list[Any] = db.buscar_tudo(query)
            listas: list[Any] = [cls(titulo, cat, ind, id) for titulo, cat, ind, id in resultados]
            return listas

    def excluir_lista(self) -> Cursor:
        with Database() as db:
            query: str = 'DELETE FROM listas WHERE id = ?;'
            params: tuple = (self.id_lista,)
            resultado: Cursor = db.executar(query, params)
            return resultado

    def atualizar_lista(self) -> Cursor:
        with Database() as db:
            query: str = 'UPDATE listas SET titulo_lista = ?, categoria = ?, indicado = ? WHERE id = ?;'
            params: tuple = (self.titulo_lista, self.categoria, self.indicado, self.id_lista)
            resultado: Cursor = db.executar(query, params)
            return resultado