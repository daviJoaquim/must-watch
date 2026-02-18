# ----------------------------
# Database.py
# ----------------------------
from sqlite3 import connect, Connection, Cursor
from typing import Any, Optional, Self, Type
from types import TracebackType
from dotenv import load_dotenv
import os
import traceback

load_dotenv()
DATABASE = os.getenv("DATABASE")


class Database:
    def __init__(self) -> None:
        self.con: Connection = connect(DATABASE)
        self.cursor: Cursor = self.con.cursor()

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Optional[Type[BaseException]], exc_val: Optional[BaseException], exc_tb: Optional[TracebackType]) -> None:
        if exc_type is not None:
            print('Exceção capturada no contexto:')
            print(f'Tipo: {exc_type.__name__}')
            print(f'Mensagem: {exc_val}')
            if exc_tb is not None:
                print('Traceback completo:')
                traceback.print_tb(exc_tb)
        self.con.commit()
        self.con.close()

    def executar(self, query: str, params: Optional[tuple] = None) -> Cursor:
        if params is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, params)
        return self.cursor

    def buscar_tudo(self, query: str, params: Optional[tuple] = None) -> list[Any]:
        if params is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def close(self) -> None:
        self.con.close()


# 🔹 Função init_db fora da classe
def init_db():
    with Database() as db:
        query = """CREATE TABLE IF NOT EXISTS listas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo_lista TEXT,
                    categorias TEXT
                   );"""
        db.executar(query)
