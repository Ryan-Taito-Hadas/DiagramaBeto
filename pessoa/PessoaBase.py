from autenticar import autenticar
from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Optional



# ABC CLASS PessoaBase______________________________________________________________________________________________________
class PessoaBase(autenticar):
    def __init__(self, id: str, nome: str, email: str, cpf: str, dataNasc: str, senha: str):
        """ Construtor da classe Pessoa.  """
        
        self._nome = nome
        self._id = id
        self._email = email
        self._cpf = cpf
        self._dataNasc = dataNasc
        self._senha = senha
        self._autenticado = False
        self._eventos_inscritos = []
        
    def autenticar(self, senha: str) -> bool:
        """ Método de autenticação. """
        if senha == self._senha:
            self._autenticado = True
            return True
        else:
            raise ValueError("Senha incorreta.")

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, value):
        self._cpf = value

    @property
    def dataNasc(self):
        return self._dataNasc

    @dataNasc.setter
    def dataNasc(self, value):
        self._dataNasc = value