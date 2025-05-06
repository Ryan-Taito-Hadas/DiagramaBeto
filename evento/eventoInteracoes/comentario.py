from evento.eventoBase import EventoBase
from pessoa.pessoaBase import PessoaBase
from datetime import datetime
from typing import List, Optional

#___________________________________________________________________________________________________________________________
class Comentario:
    def __init__(self, texto: str, autor: PessoaBase, data: datetime):
        self.texto = texto
        self.autor = autor
        self.data = data
