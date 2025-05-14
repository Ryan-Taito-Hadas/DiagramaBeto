from abc import ABC, abstractmethod

#Login Method_____________________________________________________________________________________________________

def autenticar(ABC):
    
    """ Método de autenticação. """
    
    @abstractmethod
    def autenticar(self, senha: str) -> bool:
            pass
        
        
        
        