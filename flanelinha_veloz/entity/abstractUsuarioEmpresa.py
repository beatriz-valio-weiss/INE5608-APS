from abc import abstractmethod
from datetime import datetime as dt

from flanelinha_veloz.entity.abstractUsuario import Usuario


class UsuarioEmpresa(Usuario):
    @abstractmethod
    def __init__(self, cpf: int, data_nascimento: dt, email: str, genero: str,
                 nome: str, senha: str, sobrenome: str, 
                 turno: list, dias_trabalhados: list):
        super().__init__(cpf, data_nascimento, email, genero, nome, senha,
                         sobrenome)
        if isinstance(turno, list):
            self.__turno = turno
        if isinstance(dias_trabalhados, list):
            self.__dias_trabalhados = dias_trabalhados

    @property
    def turno(self) -> list:
        return self.__turno

    @turno.setter
    def turno(self, turno: list):
        if isinstance(turno, list):
            self.__turno = turno

    @property
    def dias_trabalhados(self) -> list:
        return self.__dias_trabalhados

    @dias_trabalhados.setter
    def dias_trabalhados(self, dias_trabalhados: list):
        if isinstance(dias_trabalhados, list):
            self.__dias_trabalhados = dias_trabalhados
