from evento.eventoBase import EventoBase
from pessoa import Produtor

#___________________________________________________________________________________________________________________________
class EventoPresencial(EventoBase):
    def __init__(self, id: str, titulo: str, data: str, local: str, capacidade: int, endereco: str):
        super().__init__(id, titulo, data, local, capacidade)
        self.endereco = endereco
        self._ingressos_vendidos = 0
        self._participantes = []
        self._ingressos_vendidos = 0
        self._produtor = Produtor()
        
    def __str__(self):
        return (f"Evento Presencial: {self.titulo}\n"
                f"Data: {self.data.strftime('%d/%m/%Y %H:%M')}\n"
                f"Local: {self.local}\n"
                f"Capacidade: {self._capacidade}\n"
                f"Ingressos Vendidos: {self._ingressos_vendidos}\n")
