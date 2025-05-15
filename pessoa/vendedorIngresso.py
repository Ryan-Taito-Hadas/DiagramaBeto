from pessoa.PessoaBase import PessoaBase 

#___________________________________________________________________________________________________________________________
class VendedorIngresso(PessoaBase):
    def __init__(self, id, nome, email, cpf, dataNasc, senha):
        super().__init__(id, nome, email, cpf, dataNasc, senha)
