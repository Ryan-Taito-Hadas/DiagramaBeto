from datetime import datetime
from typing import List, Optional

#___________________________________________________________________________________________________________________________
class Comentario:
    def __init__(self, texto: str, autor, data: datetime):
        self.texto = texto
        self.autor = autor
        self.data = data

