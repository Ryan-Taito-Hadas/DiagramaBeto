from abc import ABC
from datetime import datetime
from uuid import uuid4
from typing import List, Optional
from evento.Evento import EventoBase
from pessoa.Pessoa import PessoaBase


p = PessoaBase(cpf='', nome='NICOLAS WOLF', email='', senha='111111', dataNasc=datetime.now(), id=str(uuid4()))
print(p.nome)

p.login('111111')
