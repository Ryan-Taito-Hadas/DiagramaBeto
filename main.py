from abc import ABC
from datetime import datetime
from uuid import uuid4
from typing import List, Optional
from evento.eventoBase import EventoBase
from pessoa.PessoaBase import PessoaBase


p = PessoaBase(cpf='', nome='NICOLAS WOLF', email='', senha='111111', dataNasc=datetime.now(), id=str(uuid4()))
print(p.nome)

p.login('111111')
