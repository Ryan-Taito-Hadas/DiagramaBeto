from evento.eventoBase import EventoBase
from datetime import datetime

#___________________________________________________________________________________________________________________________
class EventoOnline(EventoBase):
    def __init__(self, id: str, titulo: str, data: datetime, local: str, capacidade: int, link_transmissao: str):
        super().__init__(id, titulo, data, local, capacidade)
        self.link_transmissao = link_transmissao

    def exibir_detalhes(self):
        print(f"[EVENTO ONLINE] {self.titulo} - Link: {self.link_transmissao}")