from evento.eventoBase import EventoBase
from ingresso.ingressoBase import Ingresso
from pessoa.pessoaBase import Participante, VendedorIngresso
import datetime

#___________________________________________________________________________________________________________________________        
class Transacao:
    def __init__(self, comprador: Participante, vendedor: VendedorIngresso, ingresso: Ingresso):
        self._comprador = comprador
        self._vendedor = vendedor
        self._ingresso = ingresso
        self._valor = ingresso.preco
        self._data = datetime.now()
        
    def __str__(self):
        return f"Ingresso para '{self.ingresso.evento.titulo}' comprado por {self.comprador} e vendido por {self.vendedor} no valor de - R${self.valor:.2f}"
    
    @property
    def comprador(self):
        return self._comprador

    @comprador.setter
    def comprador(self, value):
        self._comprador = value

    @property
    def vendedor(self):
        return self._vendedor

    @vendedor.setter
    def vendedor(self, value):
        self._vendedor = value

    @property
    def ingresso(self):
        return self._ingresso

    @ingresso.setter
    def ingresso(self, value):
        self._ingresso = value

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, value):
        self._valor = value


    def __str__(self):
        return f"Ingresso para '{self.ingresso.evento.titulo}' comprado por {self.comprador} e vendido por {self.vendedor} no valor de - R${self.valor:.2f}"

    def registrar(self):
        self.comprador.registrar_transacao(self)