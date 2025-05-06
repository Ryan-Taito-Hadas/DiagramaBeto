from abc import ABC, abstractmethod

#Login Interface____________________________________________________________________________________________________________
class ILogin(ABC):  
    @abstractmethod
    def login(self, senha: str) -> bool:
        pass

    @abstractmethod
    def esta_autenticado(self) -> bool:
        pass