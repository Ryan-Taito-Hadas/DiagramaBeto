from pessoa.Pessoa import Pessoa

class VendedorIngresso(Pessoa):
    def __init__(self, id, nome, email, cpf, dataNasc, senha):
        super().__init__(id, nome, email, cpf, dataNasc, senha)
