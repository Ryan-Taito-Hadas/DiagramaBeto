from abc import ABC, abstractmethod

class Autenticar(ABC):
    """ Interface para classes que implementam autenticação """
    
    @abstractmethod
    def autenticar(self, senha: str) -> bool:
        """Autentica um usuário com base na senha fornecida"""
        pass