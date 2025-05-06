from abc import ABC, abstractmethod
from datetime import datetime
from functools import wraps
from typing import List, Optional
from evento.eventoBase import EventoBase
from main import EntidadeBase



#Login Method Decorator_____________________________________________________________________________________________________
def requer_login(metodo):
        @wraps(metodo)
        def wrapper(self, *args, **kwargs):
            if hasattr(self, 'esta_autenticado') and callable(self.esta_autenticado):
                if not self.esta_autenticado():
                    print("Acesso negado: login necessário.")
                    return
            else:
                raise AttributeError("Classe não possui método 'esta_autenticado'")
            return metodo(self, *args, **kwargs)
        return wrapper


#Login Interface____________________________________________________________________________________________________________
class ILogin(ABC):  
    @abstractmethod
    def login(self, senha: str) -> bool:
        pass

    @abstractmethod
    def esta_autenticado(self) -> bool:
        pass






# ABC CLASS PessoaBase______________________________________________________________________________________________________
class PessoaBase(EntidadeBase, ILogin):
    def __init__(self, id: str, nome: str, email: str, cpf: str, dataNasc: str, senha: str):
        """ Construtor da classe Pessoa.  """
        
        self._nome = nome
        self._id = id
        self._email = email
        self._cpf = cpf
        self._dataNasc = dataNasc
        self._senha = senha
        self._autenticado = False
        self.__eventos_inscritos: List[EventoBase] = []
        
    def login(self, senha: str) -> bool:
        if senha == self._senha:
            self._autenticado = True
            print(f"[LOGIN] {self._nome} autenticado com sucesso.")
            return True
        print("[ERRO] Senha incorreta.")
        return False      
    
    def esta_autenticado(self) -> bool:
        return self._autenticado

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, value):
        self._cpf = value

    @property
    def dataNasc(self):
        return self._dataNasc

    @dataNasc.setter
    def dataNasc(self, value):
        self._dataNasc = value
        
        
        
        
        
        

#Sub Class Produtor_________________________________________________________________________________________________________

class Produtor(PessoaBase):
    def __init__(self, nome: str, id_: str, email: str, cpf: str, data_nasc: str, descricao: str):
        super().__init__(nome, id_, email, cpf, data_nasc)
        self.__descricao = descricao
        self.__eventos_criados: List["EventoBase"] = []
    
    @requer_login
    def publicar_evento(self, evento: "EventoBase") -> None:
        self.__eventos_criados.append(evento)
        print(f"Evento '{evento.titulo}' publicado com sucesso.")

    @requer_login
    def editar_evento(self, evento: "EventoBase") -> None:
        for idx, e in enumerate(self.__eventos_criados):
            if e == evento:
                #substituir por um novo objeto ou atualizar campos
                print(f"Evento '{e.titulo}' editado.")
                return
        print("Evento não encontrado.")

    @requer_login
    def excluir_evento(self, evento: "EventoBase") -> None:
        if evento in self.__eventos_criados:
            self.__eventos_criados.remove(evento)
            print(f"Evento '{evento.titulo}' removido com sucesso.")
        else:
            print("Evento não encontrado.")

    def listar_eventos(self) -> List[str]:
        return [f"{idx + 1}. {evento.titulo}" for idx, evento in enumerate(self.__eventos_criados)]   
    
    
    
#___________________________________________________________________________________________________________________________
class Participante(PessoaBase):
    def __init__(self, nome: str, id_: str, email: str, cpf: str, data_nasc: str, ingressos_comprados: List):
        super().__init__(nome, id_, email, cpf, data_nasc)
        self._ingressos_comprados = ingressos_comprados if ingressos_comprados is not None else [] #ser uma lista vazia apenas dificulta usar esse atributo em outra classe
        self._preferencias = []                                                                    #desse jeito caso não tenha nada vai ser uma [] mas ainda sendo um "ingressos_comprados"
        self._avaliacoes_realizadas = {}
    
    @requer_login
    def comprar_ingresso(self, ingresso):
        self._ingressos_comprados.append(ingresso)

    @requer_login
    def avaliar_evento(self, evento: "EventoBase", nota: float):
        self._avaliacoes_realizadas[evento] = nota

    def registrar_transacao(self, transacao):
        self._transacoes.append(transacao)
        
    @requer_login
    def comentar_evento(self, evento: "EventoBase", texto: str):
        pass

    def login(self, senha: str) -> bool:
        return True


#___________________________________________________________________________________________________________________________
class VendedorIngresso(PessoaBase):
    pass
