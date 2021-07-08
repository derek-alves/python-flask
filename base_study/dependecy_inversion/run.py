from typing import Type
from db.mysql_repository import MySqlRepositorio


class Usuario:

    def __init__(self, repositorio: Type[MySqlRepositorio]) -> None:
        self.__repositorio = repositorio

    def armazenar_dado(self, dado: any) -> None:
        self.__repositorio.inserir(dado)

    def remover_dado(self, dado: any) -> None:
        self.__repositorio.deletar(dado)
