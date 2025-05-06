from evento.eventoBase import EventoBase

#___________________________________________________________________________________________________________________________
class EventoPresencial(EventoBase):
    def verificar_local(self):
        print(f"Verificando local do evento: {self.local}")

    def exibir_detalhes(self):
        print(f"[EVENTO PRESENCIAL] {self.titulo} - Local: {self.local}")