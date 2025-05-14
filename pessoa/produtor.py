from pessoa.pessoa import PessoaBase
from typing import List
from decorators.loginAuth import requer_login
#Sub Class Produtor_________________________________________________________________________________________________________

class Produtor(PessoaBase):
    def __init__(self, nome: str, id_: str, email: str, cpf: str, data_nasc: str, descricao: str):
        super().__init__(nome, id_, email, cpf, data_nasc)
        self.__descricao = descricao
        self.__eventos_criados = []
    
    @requer_login
    def publicar_evento(self, evento) -> None:
        self.__eventos_criados.append(evento)
        print(f"Evento '{evento.titulo}' publicado com sucesso.")

    @requer_login
    def editar_evento(self, evento) -> None:
        for idx, e in enumerate(self.__eventos_criados):
            if e == evento:
                #substituir por um novo objeto ou atualizar campos
                print(f"Evento '{e.titulo}' editado.")
                return
        print("Evento não encontrado.")

    @requer_login
    def excluir_evento(self, evento) -> None:
        if evento in self.__eventos_criados:
            self.__eventos_criados.remove(evento)
            print(f"Evento '{evento.titulo}' removido com sucesso.")
        else:
            print("Evento não encontrado.")

    def listar_eventos(self) -> List[str]:
        return [f"{idx + 1}. {evento.titulo}" for idx, evento in enumerate(self.__eventos_criados)]