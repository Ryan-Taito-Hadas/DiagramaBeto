from datetime import datetime
from typing import List, Optional

#___________________________________________________________________________________________________________________________
class Interacao:
    def __init__(self):
        self.mensagens = []

    def enviar_mensagem(self, autor, mensagem: str):
        data_envio = datetime.now().strftime("%d/%m/%Y %H:%M")
        self.mensagens.append((autor.nome, mensagem, data_envio))
        print(f"[CHAT AO VIVO] {autor.nome} ({data_envio}): {mensagem}")
        if not self._interacao:
            raise Exception("Este evento não possui interatividade ao vivo.")
        self._interacao.enviar_mensagem(autor, mensagem)