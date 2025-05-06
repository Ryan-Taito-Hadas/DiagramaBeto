from abc import ABC, abstractmethod
from typing import List, Optional
from datetime import datetime

#___________________________________________________________________________________________________________________________
class IEventoGerenciavel(ABC):
    
    @abstractmethod
    def publicar_evento(self) -> bool:
        """Publica o evento tornando-o visível para o público"""
        pass

    @abstractmethod
    def editar_evento(self, titulo: Optional[str] = None, 
                      data: Optional[datetime] = None,
                      local: Optional[str] = None,
                      capacidade: Optional[int] = None) -> bool:
        """Edita as informações do evento"""
        pass

    @abstractmethod
    def excluir_evento(self) -> bool:
        """Remove o evento do sistema"""
        pass

    @abstractmethod
    def listar_eventos(self) -> List["EventoBase"]:
        pass