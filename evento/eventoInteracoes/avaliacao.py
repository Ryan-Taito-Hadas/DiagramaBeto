from evento.eventoBase import EventoBase
from pessoa.pessoaBase import PessoaBase
from datetime import datetime
from typing import List, Optional

#___________________________________________________________________________________________________________________________
class Avaliacao:
    def __init__(self, nota: float, autor: PessoaBase):
        self.nota = nota
        self.autor = autor