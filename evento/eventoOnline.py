from evento.Evento import Evento
from pessoa import Produtor
from datetime import datetime

#___________________________________________________________________________________________________________________________
class EventoOnline(Evento):
    def __init__(self, id: str, titulo: str, data: datetime, local: str, capacidade: int, link_transmissao: str):
        super().__init__(id, titulo, data, local, capacidade)
        self.link_transmissao = link_transmissao
        self._participantes = [] # Lista de participantes que relaciona com comentário, interacao, avaliacao, capacidade e etc...
        self._avaliacoes = avaliacoes = [] # Lista de avaliações do evento
        self._comentarios = []
        self._ingressos_vendidos = 0
        self._produtor = Produtor()
        
    def __str__(self):
        return (f"Evento Online: {self.titulo}\n"
                f"Data: {self.data.strftime('%d/%m/%Y %H:%M')}\n"
                f"Local: {self.local}\n"
                f"Capacidade: {self._capacidade}\n"
                f"Ingressos Vendidos: {self._ingressos_vendidos}\n"
                f"Link de Transmissão: {self.link_transmissao}")

    