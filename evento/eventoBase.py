from abc import ABC, abstractmethod
from datetime import datetime
from evento.eventoInteracoes.avaliacao import Avaliacao
from evento.eventoInteracoes.interacao import Interacao
from evento.eventoInteracoes.comentario import Comentario
from pessoa.pessoaBase import Produtor
from functools import wraps
from typing import List, Optional
from uuid import uuid4


#___________________________________________________________________________________________________________________________
class IEventoGerenciavel(ABC):
    
    @abstractmethod
    def publicar_evento(self, evento: "EventoBase") -> None:
        pass

    @abstractmethod
    def editar_evento(self, evento: "EventoBase") -> None:
        pass

    @abstractmethod
    def excluir_evento(self, evento: "EventoBase") -> None:
        pass

    @abstractmethod
    def listar_eventos(self) -> List['EventoBase']:
        pass



#___________________________________________________________________________________________________________________________
class EventoBase(ABC):
    def __init__(self, id: str, titulo: str, data: datetime, local: str, capacidade: int):
        self._id = id
        self._titulo = titulo
        self._data = data
        self._local = local
        self._capacidade = capacidade # Limite de participantes
        self._produtor = Produtor()
        self._participantes = [] # Lista de participantes que relaciona com comentário, interacao, avaliacao, capacidade e etc...
        self._avaliacoes = Avaliacao()
        self._comentarios = Comentario()
        self._interacao = Interacao() 
        self._ingressos_vendidos = 0
        self._link_transmissao = None
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
    def exibir_detalhes(self):
        pass

    def comprar_ingresso(self, participante):
        if self._ingressos_vendidos < self._capacidade:
            self._ingressos_vendidos += 1
            return True
        return False

    def avaliar(self,nota: float, autor):       
        self._avaliacoes.append(Avaliacao(nota, autor))

    def adicionar_comentario(self, texto: str, autor):
        if autor not in self._participantes:
            raise PermissionError("Somente participantes do evento podem comentar.")
        
        self._comentarios.append(Comentario(texto, autor, datetime.now()))   

    def ativar_interacao(self):
        self._interacao = Interacao()

    def enviar_chat(self, autor, mensagem):
        if not self.interacao:
            raise Exception("Este evento não possui interatividade ao vivo.")
        self._interacao.enviar_mensagem(autor, mensagem)

    