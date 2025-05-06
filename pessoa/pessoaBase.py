from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Optional
from entidadeBase.entidadeBase import EntidadeBase
from interfaces.iLogin import ILogin
from decorators.requerLogin import requer_login

# ABC CLASS PessoaBase______________________________________________________________________________________________________
class PessoaBase(EntidadeBase, ILogin):
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
        
    def login(self, senha: str) -> bool:
        if senha == self._senha:
            self._autenticado = True
            print(f"[LOGIN] {self._nome} autenticado com sucesso.")
            return True
        print("[ERRO] Senha incorreta.")
        return False      
    
    def esta_autenticado(self) -> bool:
        return self._autenticado

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
        
        



        
#Sub Class Produtor_________________________________________________________________________________________________________

class Produtor(PessoaBase):
    def __init__(self, nome: str, id_: str, email: str, cpf: str, data_nasc: str, descricao: str):
        super().__init__(nome, id_, email, cpf, data_nasc)
        self.__descricao = descricao
        self.__eventos_criados = []
    
    @requer_login
    def publicar_evento(self, evento) -> None:
        self.__eventos_criados.append(evento)
        print(f"Evento '{evento.titulo}' publicado com sucesso.")

    @requer_login
    def editar_evento(self, evento) -> None:
        for idx, e in enumerate(self.__eventos_criados):
            if e == evento:
                #substituir por um novo objeto ou atualizar campos
                print(f"Evento '{e.titulo}' editado.")
                return
        print("Evento não encontrado.")

    @requer_login
    def excluir_evento(self, evento) -> None:
        if evento in self.__eventos_criados:
            self.__eventos_criados.remove(evento)
            print(f"Evento '{evento.titulo}' removido com sucesso.")
        else:
            print("Evento não encontrado.")

    def listar_eventos(self) -> List[str]:
        return [f"{idx + 1}. {evento.titulo}" for idx, evento in enumerate(self.__eventos_criados)]