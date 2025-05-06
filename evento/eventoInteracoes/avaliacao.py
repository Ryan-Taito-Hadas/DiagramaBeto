from datetime import datetime
from typing import List, Optional

#___________________________________________________________________________________________________________________________
class Avaliacao:
    def __init__(self, nota: float, autor):
        self.nota = nota
        self.autor = autor