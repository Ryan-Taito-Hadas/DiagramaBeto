from evento.eventoBase import EventoBase
from datetime import datetime

#___________________________________________________________________________________________________________________________ 
class Ingresso:
    def __init__(self, preco: float, evento: EventoBase):
        self._preco = preco
        self._evento = evento
        self._data_compra = None
        self._comprador = None
    
    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, value):
        self._preco = value

    @property
    def evento(self):
        return self._evento

    @evento.setter
    def evento(self, value):
        self._evento = value
        
    def realizar_compra(self, comprador):
        if self._evento.tem_capacidade_disponivel():
            self._comprador = comprador
            self._data_compra = datetime.now()
            self._evento.adicionar_participante(comprador)
            return True
        return False
