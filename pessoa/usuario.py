from pessoa.Pessoa import PessoaBase
from typing import List

#___________________________________________________________________________________________________________________________
class Usuario(PessoaBase):
    """ Classe que representa um usuário do sistema. """
    def __init__(self, nome: str, id_: str, email: str, cpf: str, data_nasc: str, ingressos_comprados: List):
        super().__init__(nome, id_, email, cpf, data_nasc)
        self._ingressos_comprados = [] 
        self._preferencias = []         
        self._avaliacoes_realizadas = {}
        self._transacoes = []
        
    def __str__(self):
        return self.nome
    
    def comprar_ingresso(self, ingresso):
        self._ingressos_comprados.append(ingresso)

    def avaliar_evento(self, evento, nota: float):
        self._avaliacoes_realizadas[evento] = nota
    
    def registrar_transacao(self, transacao):
        self._transacoes.append(transacao)
        
    def comentar_evento(self, evento, texto: str):
        pass

    def login(self, senha: str) -> bool:
        return True