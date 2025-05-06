from evento.eventoBase import EventoBase
from evento.eventoInteracoes.avaliacao import Avaliacao
from evento.eventoInteracoes.interacao import Interacao
from evento.eventoInteracoes.comentario import Comentario
from pessoa import Produtor
from datetime import datetime

#___________________________________________________________________________________________________________________________
class EventoOnline(EventoBase):
    def __init__(self, id: str, titulo: str, data: datetime, local: str, capacidade: int, link_transmissao: str):
        super().__init__(id, titulo, data, local, capacidade)
        self.link_transmissao = link_transmissao
        self._participantes = [] # Lista de participantes que relaciona com comentário, interacao, avaliacao, capacidade e etc...
        self._avaliacoes = Avaliacao()
        self._comentarios = Comentario()
        self._interacao = Interacao() 
        self._ingressos_vendidos = 0
        self._produtor = Produtor()
        
    def __str__(self):
        return (f"Evento Online: {self.titulo}\n"
                f"Data: {self.data.strftime('%d/%m/%Y %H:%M')}\n"
                f"Local: {self.local}\n"
                f"Capacidade: {self._capacidade}\n"
                f"Ingressos Vendidos: {self._ingressos_vendidos}\n"
                f"Link de Transmissão: {self.link_transmissao}")

    def avaliar(self, nota: float, autor):
        if autor not in self._participantes:
            raise PermissionError("Somente participantes do evento podem avaliar.")
        self._avaliacoes.append(Avaliacao(nota, autor))

    def adicionar_comentario(self, texto: str, autor):
        if autor not in self._participantes:
            raise PermissionError("Somente participantes do evento podem comentar.")
        self._comentarios.append(Comentario(texto, autor, datetime.now()))   

    def ativar_interacao(self):
        self._interacao = Interacao()

    def enviar_chat(self, autor, mensagem):
        if not self.interacao:
            raise Exception("Este evento não possui interatividade ao vivo.")
        self._interacao.enviar_mensagem(autor, mensagem)