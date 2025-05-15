from evento.eventoBase import EventoBase
from ingresso.ingressoBase import Ingresso
from pessoa.PessoaBase import Participante, VendedorIngresso
from datetime import datetime
#___________________________________________________________________________________________________________________________        
class Transacao:
    """ Classe que representa uma transação de compra de ingresso. """
    def __init__(self, comprador: Participante, vendedor: VendedorIngresso, ingresso: Ingresso):
        self._comprador = comprador
        self._vendedor = vendedor
        self._ingresso = ingresso
        self._valor = ingresso.preco
        self._data = datetime.now()
        
    def __str__(self):
        return (f"Transação: {self._comprador} comprou o ingresso '{self._ingresso.evento.titulo}' "
                f"de {self._vendedor} no valor de R${self._valor:.2f} em {self._data.strftime('%d/%m/%Y %H:%M')}")
    
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