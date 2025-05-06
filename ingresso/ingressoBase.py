from evento.eventoBase import EventoBase

#___________________________________________________________________________________________________________________________ 
class Ingresso:
    def __init__(self, preco: float, evento: EventoBase):
        self._preco = preco
        self._evento = evento
    
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
