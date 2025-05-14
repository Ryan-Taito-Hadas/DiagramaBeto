from abc import ABC
from datetime import datetime
from uuid import uuid4
from typing import List, Optional
from entidadeBase.entidadeBase import EntidadeBase
from evento.eventoBase import EventoBase
from pessoa.pessoa import PessoaBase
from evento.eventoInteracoes.avaliacao import Avaliacao
from evento.eventoInteracoes.interacao import Interacao
from evento.eventoInteracoes.comentario import Comentario

p = PessoaBase(cpf='', nome='NICOLAS WOLF', email='', senha='111111', dataNasc=datetime.now(), id=str(uuid4()))
print(p.nome)

p.login('111111')
