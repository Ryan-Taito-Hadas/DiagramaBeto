from abc import ABC
from datetime import datetime
from uuid import uuid4
from typing import List, Optional
from evento.eventoBase import EventoBase
from pessoa.pessoaBase import PessoaBase
from evento.eventoInteracoes.avaliacao import Avaliacao
from evento.eventoInteracoes.interacao import Interacao
from evento.eventoInteracoes.comentario import Comentario


#___________________________________________________________________________________________________________________________
class EntidadeBase(ABC):
    def __init__(self):
        self._id = str(uuid4())
        self._criado_em = datetime.now()
        self._alterado_em = datetime.now()

    @property
    def id(self):
        return self._id

    @property
    def criado_em(self):
        return self._criado_em

    @property
    def alterado_em(self):
        return self._alterado_em

    def atualizar(self):
        self._alterado_em = datetime.now()