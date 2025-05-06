from abc import ABC, abstractmethod
from datetime import datetime
from functools import wraps
from typing import List, Optional
from uuid import uuid4


#___________________________________________________________________________________________________________________________
class EventoBase(ABC):
    def __init__(self, id: str, titulo: str, data: datetime, local: str, capacidade: int):
        self._id = id
        self._titulo = titulo
        self._data = data
        self._local = local
        self._capacidade = capacidade # Limite de participantes
    
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, value):
        self._titulo = value

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def local(self):
        return self._local

    @local.setter
    def local(self, value):
        self._local = value

    @property
    def capacidade(self):
        return self._capacidade

    @capacidade.setter
    def capacidade(self, value):
        self._capacidade = value

    @abstractmethod 
    def ativar_interacao(self):
        pass
    
    @abstractmethod            
    def avaliar(self,nota: float, autor):       
        pass
    
    @abstractmethod 
    def adicionar_comentario(self, texto: str, autor):
        pass   
          
    @abstractmethod
    def enviar_chat(self, autor, mensagem):
        pass

    