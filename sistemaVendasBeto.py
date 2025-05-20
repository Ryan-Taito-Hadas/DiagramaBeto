from abc import ABC, abstractmethod
import os
from datetime import datetime

# __________________________________________ Variáveis globais ________________________________________

participantes = []
produtores = []
vendedores = []
eventos = []
ingressos = []
avaliacoes = []
transacoes = []

# ____________________________________________ Utilitários ____________________________________________

def clearScreen():
    '''Limpa a tela do console.''' 
    os.system('cls' if os.name == 'nt' else 'clear')

def endProgram():
    '''Encerra o programa e exibe uma mensagem de encerramento.'''
    clearScreen()
    print("Sessão encerrada.")  
    exit()

def cadastrar_pessoa():
    '''Cadastra uma nova pessoa no sistema.'''
    print("\n=== Cadastro de Pessoa ===")
    nome = input("Nome: ")
    tipo = input("Tipo [participante | produtor | vendedor]: ").lower()

    cpf = ""
    id_ = ""
    nasc = ""

    if tipo in ["produtor", "vendedor"]:
        cpf = input("CPF: ")
        id_ = input("ID: ")
        nasc = input("Data de Nascimento: ")

    if tipo == "participante":
        novo_participante = Participante(nome)
        participantes.append(novo_participante)
        print("[Sucesso] Participante cadastrado com sucesso.")

    elif tipo == "produtor":
        if not (cpf and id_ and nasc):
            print("[Erro] CPF, ID e Data de Nascimento são obrigatórios para produtores.")
            return
        novo_produtor = Produtor(nome, cpf, id_, nasc)
        produtores.append(novo_produtor)
        print("[Sucesso] Produtor cadastrado com sucesso.")

    elif tipo == "vendedor":
        if not (cpf and id_ and nasc):
            print("[Erro] CPF, ID e Data de Nascimento são obrigatórios para vendedores.")
            return
        novo_vendedor = Vendedor(nome, cpf, id_, nasc)
        vendedores.append(novo_vendedor)
        print("[Sucesso] Vendedor cadastrado com sucesso.")

# ____________________________________________ Classes ____________________________________________

class Evento:
    def __init__(self, id_: str, tipo: str, titulo: str, data: str, local: str, capacidade: int):
        self._valor_ingresso = 0.0
        self._id = id_
        self._tipo = tipo
        self._titulo = titulo
        self._data = data
        self._local = local
        self._capacidade = capacidade
        self._ingressos = []

        if tipo.lower() == "online":             # define por padrão o valor do ingresso de um evento presencial pra 49.50 e de um online para 29.99
            self._valor_ingresso = 29.99
        elif tipo.lower() == "presencial":
            self._valor_ingresso = 49.50
        else:
            self._valor_ingresso = 0.0

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, novo_titulo):
        self._titulo = novo_titulo

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, novo_tipo):
        self._tipo = novo_tipo

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, nova_data):
        self._data = nova_data

    @property
    def local(self):
        return self._local

    @local.setter
    def local(self, novo_local):
        self._local = novo_local

    @property
    def capacidade(self):
        return self._capacidade

    @capacidade.setter
    def capacidade(self, nova_capacidade):
        self._capacidade = nova_capacidade

    @property
    def valor_ingresso(self):
        return self._valor_ingresso

    @valor_ingresso.setter
    def valor_ingresso(self, valor):
        self._valor_ingresso = valor

    def adicionar_ingresso(self, ingresso):
        ''' Adiciona um ingresso ao evento. '''
        self._ingressos.append(ingresso)

class Ingresso:
    def __init__(self, valor: float, tipo: str):
        self.valor = valor
        self.tipo = tipo

class Avaliacao:
    def __init__(self, participante, evento, nota: float, comentario: str):
        self.participante = participante
        self.evento = evento
        self.nota = nota
        self.comentario = comentario

    def exibir(self):
        ''' Exibe os detalhes da avaliação. '''
        print(f"Evento: {self.evento.titulo}, Nota: {self.nota}, Comentário: {self.comentario}")

class Transacao:
    def __init__(self, data: str, tipo: str, valor: float, participante, ingresso, status="Confirmada"):
        self.data = data
        self.tipo = tipo
        self.valor = valor
        self.participante = participante
        self.ingresso = ingresso
        self.status = status  # Novo atributo

    def registrar(self):
        ''' Registra a transação. '''
        print(f"[Transação - {self.status}] {self.tipo} no valor de R$ {self.valor:.2f} realizada em {self.data}.")

class PessoaBase(ABC):
    def __init__(self, nome: str, cpf: str, id_: str, data_nasc: str):
        self._nome = nome
        self._cpf = cpf
        self._id = id_
        self._data_nasc = data_nasc
        self._ingressos = []

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, novo_cpf):
        self._cpf = novo_cpf

    @property
    def id_(self): 
        return self._id

    @id_.setter
    def id_(self, novo_id):
        self._id = novo_id

    @property
    def data_nasc(self):
        return self._data_nasc

    @data_nasc.setter
    def data_nasc(self, nova_data):
        self._data_nasc = nova_data

    @property
    def ingressos(self):
        return self._ingressos

    @abstractmethod
    def tipo(self):
        pass

    def __str__(self):
        return f"{self.tipo()}: {self.nome} (ID: {self.id_})"

class Participante(PessoaBase):
    def __init__(self, nome):
        super().__init__(nome, '', '', '')
        self.avaliacoes = []

    def tipo(self):
        return "Participante"

    def comprar_ingresso(self, ingresso):
        ''' Registra a compra de um ingresso. '''
        self._ingressos.append(ingresso)
        print(f"Ingresso adicionado ao participante {self.nome}.")

    def avaliar(self):
        ''' Registra a avaliação do participante. '''
        print(f"Participante {self.nome} realizou uma avaliação.")

class Produtor(PessoaBase):
    def __init__(self, nome, cpf, id_, data_nasc):
        super().__init__(nome, cpf, id_, data_nasc)

    def tipo(self):
        return "Produtor"

    def criar_evento(self):
        ''' Registra a criação de um evento. '''
        print(f"{self.nome} criou um evento.")

    def excluir_evento(self):
        ''' Registra a exclusão de um evento. '''
        print(f"{self.nome} excluiu um evento.")

class Vendedor(PessoaBase):
    def __init__(self, nome: str, cpf: str, id_: str, data_nasc: str):
        super().__init__(nome, cpf, id_, data_nasc)
        self._vendas = []

    def tipo(self):
        return "Vendedor"

    def vender_ingresso(self, ingresso):
        ''' Registra a venda de um ingresso. '''
        self._vendas.append(ingresso)
        print(f"{self.nome} vendeu um ingresso.")

    def total_vendas(self):
        ''' Retorna o total de vendas realizadas pelo vendedor. '''
        return len(self._vendas)

class MenuParticipante:
    def __init__(self, participantes, eventos, vendedores, ingressos, avaliacoes):
        self.participantes = participantes
        self.eventos = eventos
        self.vendedores = vendedores
        self.ingressos = ingressos
        self.avaliacoes = avaliacoes

    def exibir_menu(self):
        ''' Exibe o menu do participante e processa as opções escolhidas. '''
        while True:
            print("\n===== Menu do Participante =====")
            print("1 - Comprar Ingresso")
            print("2 - Avaliar Evento")
            print("3 - Listar Eventos")
            print("4 - Ver Transações")
            print("0 - Voltar ao Menu Principal")

            try:
                opcao = input("Escolha uma opção: ").strip()

                match opcao:
                    case "1":
                        self.comprar_ingresso()
                    case "2":
                        self.avaliar_evento()
                    case "3":
                        self.listar_eventos()
                    case "4":
                        self.ver_transacoes()
                    case "0":
                        print("Voltando ao menu principal...")
                        break
                    case _:
                        print("Opção inválida. Por favor, tente novamente.")
            except ValueError:
                print("Entrada inválida!")

    def comprar_ingresso(self):
        ''' Permite ao participante comprar um ingresso. '''
        print("\n=== Comprar Ingresso ===")
        if not self.vendedores or not self.participantes or not self.eventos:
            print("[Erro] Faltam dados para compra.")
            return

        for i, p in enumerate(self.vendedores):
            print(f"{i} - {p.nome}")
        idx_v = int(input("Escolha o vendedor: "))
        vendedor = self.vendedores[idx_v]

        for i, p in enumerate(self.participantes):
            print(f"{i} - {p.nome}")
        idx = int(input("Escolha o participante: "))
        participante = self.participantes[idx]

        for i, e in enumerate(self.eventos):
            print(f"{i} - {e.titulo}")
        idx_e = int(input("Escolha o evento: "))
        evento = self.eventos[idx_e]
        if len(evento._ingressos) >= evento.capacidade:
            print("[Erro] Capacidade máxima atingida para este evento. Não é possível vender mais ingressos.")
            return

        tipo_ingresso = input("Tipo de ingresso [inteiro | meia]: ")
        if tipo_ingresso == "inteiro":
            valor = evento.valor_ingresso
        elif tipo_ingresso == "meia":
            valor = evento.valor_ingresso / 2
        else:
            print("[Erro] Tipo inválido de ingresso.")
            return
        print(f"Valor a pagar: R$ {valor:.2f}")
        confirmar = input("Confirmar pagamento? (s/n): ").strip().lower()
        data_transacao = datetime.now().strftime("%d/%m/%Y %H:%M")
        if confirmar != "s":
            transacao_cancelada = Transacao(data_transacao, "Compra", valor, participante, None, status="Cancelada")
            transacoes.append(transacao_cancelada)
            print("[Cancelado] Compra de ingresso não confirmada.")
            return
        ingresso = Ingresso(valor, tipo_ingresso)
        ingresso.evento = evento
        
        evento.adicionar_ingresso(ingresso)
        participante.comprar_ingresso(ingresso)
        self.ingressos.append(ingresso)
        vendedor.vender_ingresso(ingresso)
        print("[Sucesso] Ingresso comprado com sucesso.")

    def avaliar_evento(self):
        ''' Permite ao participante avaliar um evento. '''
        print("\n=== Avaliar Evento ===")
        for i, p in enumerate(self.participantes):
            print(f"{i} - {p.nome}")
        idx = int(input("Escolha o participante: "))
        participante = self.participantes[idx]

        for i, e in enumerate(self.eventos):
            print(f"{i} - {e.titulo}")
        idx_e = int(input("Escolha o evento: "))
        evento = self.eventos[idx_e]

        nota = float(input("Nota (0 a 10): "))
        comentario = input("Comentário: ")
        self.avaliacoes.append(Avaliacao(participante, evento, nota, comentario))
        participante.avaliar()
        print("[Sucesso] Avaliação registrada.")

    def listar_eventos(self):
        ''' Lista todos os eventos disponíveis. '''
        print("\n=== Lista de Eventos ===")
        for i, e in enumerate(self.eventos):
            print(f"{i} - {e.titulo} | Tipo: {e.tipo} | Data: {e.data}| Valor: {e.valor_ingresso} | Capacidade: {e.capacidade} | Vendidos: {len(e._ingressos)}")
            
    def ver_transacoes(self):
        ''' Permite ao participante ver suas transações. '''
        print("\n=== Transações Realizadas ===")
        for i, p in enumerate(self.participantes):
            print(f"{i} - {p.nome}")
        try:
            idx = int(input("Escolha o participante: "))
            participante = self.participantes[idx]
        except (IndexError, ValueError):
            print("[Erro] Participante inválido.")
            return

        encontrou = False
        for t in transacoes:
            if t.participante == participante:
                status = getattr(t, "status", "Confirmada")
                evento_nome = getattr(t.ingresso.evento, "titulo", "Desconhecido") if t.ingresso else "Sem evento"
                print(f"{t.data} | {t.tipo} | Evento: {evento_nome} | Valor: R$ {t.valor:.2f} | Status: {status}")
                encontrou = True
        if not encontrou:
            print("Nenhuma transação encontrada para este participante.")   

class MenuProdutor:
    def __init__(self, produtores, eventos):
        self.produtores = produtores
        self.eventos = eventos

    def exibir_menu(self):
        ''' Exibe o menu do produtor e processa as opções escolhidas. '''
        while True:
            print("\n=== MENU PRODUTOR ===")
            print("1. Criar Evento")
            print("2. Listar Eventos")
            print("3. Excluir Evento")
            print("0. Voltar ao Menu Principal")

            opcao = input("Escolha uma opção: ")

            match opcao:
                case "1":
                    self.criar_evento()
                case "2":
                    self.listar_eventos()
                case "3":
                    self.excluir_evento()
                case "0":
                    break
                case _:
                    print("Opção inválida!")
    
    def excluir_evento(self):
        ''' Permite ao produtor excluir um evento da lista. '''
        if not self.eventos:
            print("[Aviso] Nenhum evento cadastrado.")
            return

        print("\n=== Excluir Evento ===")
        for i, e in enumerate(self.eventos):
            print(f"{i} - {e.titulo} | Tipo: {e.tipo} | Data: {e.data}")

        try:
            idx = int(input("Escolha o número do evento a excluir: "))
            evento_excluido = self.eventos.pop(idx)
            print(f"[Sucesso] Evento '{evento_excluido.titulo}' excluído com sucesso.")
        except (IndexError, ValueError):
            print("[Erro] Índice inválido. Nenhum evento foi excluído.")
            
    def criar_evento(self):
        ''' Permite ao produtor criar um novo evento. '''
        print("\n=== Criar Evento ===")
        for i, p in enumerate(self.produtores):
            print(f"{i} - {p.nome}")
        idx = int(input("Escolha o produtor: "))
        produtor = self.produtores[idx]

        id_ = input("ID do evento: ")
        tipo = input("Tipo [online | presencial]: ")
        titulo = input("Título: ")
        data = input("Data: ")
        local = input("Local: ")
        capacidade = int(input("Capacidade: "))
        valor = float(input("Valor do ingresso: "))
        novo_evento = Evento(id_, tipo, titulo, data, local, capacidade)
        novo_evento.valor_ingresso = valor
        self.eventos.append(novo_evento), 
        produtor.criar_evento()
        print("[Sucesso] Evento criado com sucesso.")

    def listar_eventos(self):
        ''' Lista todos os eventos criados pelos produtores. '''
        print("\n=== Lista de Eventos ===")
        for i, e in enumerate(self.eventos):
            print(f"{i} - {e.titulo} | Tipo: {e.tipo} | Data: {e.data}| Valor: {e.valor_ingresso} | Capacidade: {e.capacidade} | Vendidos: {len(e._ingressos)}")

class MenuVendedor:
    def __init__(self, vendedores, eventos):
        self.vendedores = vendedores
        self.eventos = eventos

    def exibir_menu(self):
        while True:
            print("\n=== MENU VENDEDOR ===")
            print("1. Ver Total de Vendas")
            print("2. Listar Todas as Vendas")
            print("3. Filtrar Vendas por Evento")
            print("4. Listar Eventos Disponíveis")
            print("0. Voltar ao Menu Principal")

            opcao = input("Escolha uma opção: ")

            match opcao:
                case "1":
                    self.ver_total_vendas()
                case "2":
                    self.listar_vendas_detalhadas()
                case "3":
                    self.filtrar_vendas_por_evento()
                case "4":
                    self.listar_eventos()
                case "0":
                    break
                case _:
                    print("Opção inválida!")

    def selecionar_vendedor(self):
        ''' Seleciona um vendedor da lista de vendedores. '''
        if not self.vendedores:
            print("[Aviso] Nenhum vendedor cadastrado.")
            return None

        for i, v in enumerate(self.vendedores):
            print(f"{i} - {v.nome}")
        try:
            idx = int(input("Escolha o vendedor: "))
            return self.vendedores[idx]
        except (IndexError, ValueError):
            print("[Erro] Índice inválido.")
            return None

    def ver_total_vendas(self):
        print("\n=== Ver Total de Ingressos Vendidos ===")
        vendedor = self.selecionar_vendedor()
        if vendedor:
            print(f"\n{vendedor.nome} vendeu {len(vendedor._vendas)} ingresso(s).")

    def listar_vendas_detalhadas(self):
        print("\n=== Listar Todas as Vendas ===")
        vendedor = self.selecionar_vendedor()
        if vendedor:
            if not vendedor._vendas:
                print(f"{vendedor.nome} ainda não realizou vendas.")
                return
            for i, ingresso in enumerate(vendedor._vendas):
                evento = getattr(ingresso, "evento", None)
                titulo = evento.titulo if evento else "Desconhecido"
                print(f"{i + 1}. Evento: {titulo} | Tipo: {ingresso.tipo} | Valor: R$ {ingresso.valor:.2f}")

    def filtrar_vendas_por_evento(self):
        print("\n=== Filtrar Vendas por Evento ===")
        vendedor = self.selecionar_vendedor()
        if not vendedor or not vendedor._vendas:
            print("Nenhuma venda para filtrar.")
            return

        eventos_vendidos = list(set(
            getattr(ingresso, "evento", None)
            for ingresso in vendedor._vendas if hasattr(ingresso, "evento")
        ))

        if not eventos_vendidos:
            print("Este vendedor não vendeu ingressos associados a eventos.")
            return

        for i, evento in enumerate(eventos_vendidos):
            print(f"{i} - {evento.titulo}")
        try:
            idx = int(input("Escolha o evento: "))
            evento_escolhido = eventos_vendidos[idx]
            print(f"\nVendas do evento: {evento_escolhido.titulo}")
            for ingresso in vendedor._vendas:
                if hasattr(ingresso, "evento") and ingresso.evento == evento_escolhido:
                    print(f"- Tipo: {ingresso.tipo} | Valor: R$ {ingresso.valor:.2f}")
        except (IndexError, ValueError):
            print("Evento inválido.")

    def listar_eventos(self):
        ''' Lista todos os eventos disponíveis no sistema. '''
        print("\n=== Lista de Eventos Disponíveis ===")
        if not self.eventos:
            print("[Aviso] Nenhum evento cadastrado.")
            return

        for i, e in enumerate(self.eventos):
            print(f"{i} - {e.titulo} | Tipo: {e.tipo} | Data: {e.data} | Valor: R$ {e.valor_ingresso:.2f} | Capacidade: {e.capacidade} | Vendidos: {len(e._ingressos)}")

class MenuAdmin:
    def __init__(self, participantes, produtores, vendedores):
        self.participantes = participantes
        self.produtores = produtores
        self.vendedores = vendedores
        
    def cadastrar_pessoa(self):
        ''' Cadastra uma nova pessoa no sistema. '''
        print("\n=== Cadastro de Pessoa ===")
        nome = input("Nome: ")
        tipo = input("Tipo [participante | produtor | vendedor]: ").lower()

        cpf = ""
        id_ = ""
        nasc = ""

        if tipo in ["produtor", "vendedor"]:
            cpf = input("CPF: ")
            id_ = input("ID: ")
            nasc = input("Data de Nascimento: ")

        if tipo == "participante":
            novo_participante = Participante(nome)
            self.participantes.append(novo_participante)
            print("[Sucesso] Participante cadastrado com sucesso.")

        elif tipo == "produtor":
            if not (cpf and id_ and nasc):
                print("[Erro] CPF, ID e Data de Nascimento são obrigatórios para produtores.")
                return
            novo_produtor = Produtor(nome, cpf, id_, nasc)
            self.produtores.append(novo_produtor)
            print("[Sucesso] Produtor cadastrado com sucesso.")

        elif tipo == "vendedor":
            if not (cpf and id_ and nasc):
                print("[Erro] CPF, ID e Data de Nascimento são obrigatórios para vendedores.")
                return
            novo_vendedor = Vendedor(nome, cpf, id_, nasc)
            self.vendedores.append(novo_vendedor)
            print("[Sucesso] Vendedor cadastrado com sucesso.")
        else:
            print("[Erro] Tipo de pessoa inválido. Cadastro cancelado.")

    def editar_pessoa(self):
        ''' Permite ao admin editar os dados de uma pessoa cadastrada. '''
        print("\n=== Editar Pessoa ===")
        print("Tipos disponíveis: participante | produtor | vendedor")
        tipo = input("Digite o tipo da pessoa a editar: ").lower()

        if tipo == "participante":
            lista = self.participantes
        elif tipo == "produtor":
            lista = self.produtores
        elif tipo == "vendedor":
            lista = self.vendedores
        else:
            print("[Erro] Tipo de pessoa inválido.")
            return

        if not lista:
            print(f"[Aviso] Nenhum {tipo} cadastrado.")
            return

        for i, p in enumerate(lista):
            print(f"{i} - {p.nome} | ID: {p.id_}")
        try:
            idx = int(input("Escolha a pessoa a ser editada: "))
            pessoa = lista[idx]
        except (IndexError, ValueError):
            print("[Erro] Pessoa inválida.")
            return

        novo_nome = input("Novo nome (Enter para manter): ")
        novo_cpf = input("Novo CPF (Enter para manter): ")
        novo_id = input("Novo ID (Enter para manter): ")
        nova_data = input("Nova data de nascimento (Enter para manter): ")

        if novo_nome:
            pessoa.nome = novo_nome
        if novo_cpf:
            pessoa.cpf = novo_cpf
        if novo_id:
            pessoa.id_ = novo_id
        if nova_data:
            pessoa.data_nasc = nova_data

        print("[Sucesso] Dados pessoais atualizados com sucesso.")

    def listar_contas(self):
        ''' Lista todos os participantes, produtores e vendedores cadastrados com seus dados. '''
        print("\n=== PARTICIPANTES CADASTRADOS ===")
        if not self.participantes:
            print("[Nenhum participante cadastrado]")
        else:
            for p in self.participantes:
                print(f"Nome: {p.nome} | ID: {p.id_} | CPF: {p.cpf} | Nascimento: {p.data_nasc}")

        print("\n=== PRODUTORES CADASTRADOS ===")
        if not self.produtores:
            print("[Nenhum produtor cadastrado]")
        else:
            for p in self.produtores:
                print(f"Nome: {p.nome} | ID: {p.id_} | CPF: {p.cpf} | Nascimento: {p.data_nasc}")

        print("\n=== VENDEDORES CADASTRADOS ===")
        if not self.vendedores:
            print("[Nenhum vendedor cadastrado]")
        else:
            for v in self.vendedores:
                print(f"Nome: {v.nome} | ID: {v.id_} | CPF: {v.cpf} | Nascimento: {v.data_nasc}")

    def ver_transacoes(self):
        print("\n=== TODAS AS TRANSAÇÕES REGISTRADAS ===")
        if not transacoes:
            print("[Aviso] Nenhuma transação foi registrada.")
            return

        for t in transacoes:
            nome = t.participante.nome if hasattr(t.participante, "nome") else str(t.participante)
            status = getattr(t, "status", "Confirmada")
            evento_nome = getattr(t.ingresso.evento, "titulo", "Desconhecido") if t.ingresso else "Sem evento"
            print(f"{t.data} | Participante: {nome} | {t.tipo} | Evento: {evento_nome} | Valor: R$ {t.valor:.2f} | Status: {status}")

    def exibir_menu(self):
        ''' Exibe o menu do admin e processa as opções escolhidas. '''
        while True:
            print("\n===== Menu do Admin =====")
            print("1 - Cadastrar Pessoa")
            print("2 - Editar Pessoa")
            print("3 - Listar Contas Cadastradas")
            print("4 - Ver Todas as Transações")
            print("0 - Voltar ao Menu Principal")

            try:
                opcao = input("Escolha uma opção: ").strip()

                match opcao:
                    case "1":
                        self.cadastrar_pessoa()
                    case "2":
                        self.editar_pessoa()
                    case "3":
                        self.listar_contas()
                    case "4":
                        self.ver_transacoes()
                    case "0":
                        print("Voltando ao menu principal...")
                        break
                    case _:
                        print("Opção inválida. Por favor, tente novamente.")
            except ValueError:
                print("Entrada inválida! Por favor, digite um número.")

class MenuEvento:
    def __init__(self, eventos, avaliacoes):
        self.eventos = eventos
        self.avaliacoes = avaliacoes

    def exibir_menu(self):
        ''' Exibe o menu de eventos e processa as opções escolhidas. '''
        while True:
            print("\n===== Menu de Eventos =====")
            print("1 - Listar Todos os Eventos")
            print("2 - Ver Detalhes de um Evento")
            print("3 - Ver Avaliações de um Evento")
            print("0 - Voltar ao Menu Principal")

            try:
                opcao = input("Escolha uma opção: ").strip()

                match opcao:
                    case "1":
                        self.listar_eventos()
                    case "2":
                        self.detalhes_evento()
                    case "3":
                        self.ver_avaliacoes_evento()
                    case "0":
                        print("Voltando ao menu principal...")
                        break
                    case _:
                        print("Opção inválida. Por favor, tente novamente.")
            except ValueError:
                print("Entrada inválida! Por favor, digite um número.")

    def listar_eventos(self):
        ''' Lista todos os eventos cadastrados no sistema. '''
        print("\n=== Lista de Eventos Disponíveis ===")
        if not self.eventos:
            print("[Aviso] Nenhum evento cadastrado.")
            return
        
        for i, e in enumerate(self.eventos):
            print(f"{i} - {e.titulo} | Tipo: {e.tipo} | Data: {e.data} | Local: {e.local}")

    def detalhes_evento(self):
        ''' Mostra todos os detalhes de um evento específico. '''
        self.listar_eventos()
        if not self.eventos:
            return

        try:
            idx = int(input("\nEscolha o número do evento para ver detalhes: "))
            evento = self.eventos[idx]
            
            print(f"\n=== DETALHES DO EVENTO ===")
            print(f"Título: {evento.titulo}")
            print(f"ID: {evento._id}")
            print(f"Tipo: {evento.tipo}")
            print(f"Data: {evento.data}")
            print(f"Local: {evento.local}")
            print(f"Valor do ingresso: R$ {evento.valor_ingresso:.2f}")
            print(f"Capacidade total: {evento.capacidade}")
            print(f"Ingressos vendidos: {len(evento._ingressos)}")
            print(f"Vagas restantes: {evento.capacidade - len(evento._ingressos)}")

        except (IndexError, ValueError):
            print("[Erro] Índice de evento inválido.")

    def ver_avaliacoes_evento(self):
        ''' Mostra todas as avaliações de um evento específico. '''
        self.listar_eventos()
        if not self.eventos:
            return

        try:
            idx = int(input("\nEscolha o número do evento para ver avaliações: "))
            evento = self.eventos[idx]
            
            print(f"\n=== AVALIAÇÕES DO EVENTO: {evento.titulo} ===")
            
            avaliacoes_do_evento = [a for a in self.avaliacoes if a.evento == evento]
            
            if not avaliacoes_do_evento:
                print("Este evento ainda não possui avaliações.")
                return
                
            nota_total = sum(a.nota for a in avaliacoes_do_evento)
            nota_media = nota_total / len(avaliacoes_do_evento)
            
            print(f"Nota média: {nota_media:.1f}/10 ({len(avaliacoes_do_evento)} avaliações)")
            print("\n--- Comentários ---")
            
            for i, avaliacao in enumerate(avaliacoes_do_evento):
                participante_nome = avaliacao.participante.nome if hasattr(avaliacao.participante, "nome") else "Anônimo"
                print(f"{i+1}. Nota: {avaliacao.nota}/10 | Participante: {participante_nome}")
                print(f"   \"{avaliacao.comentario}\"")
                print()
                
        except (IndexError, ValueError):
            print("[Erro] Índice de evento inválido.")

def menu_principal():
        ''' Exibe o menu principal e processa as opções escolhidas. '''
        while True:
            print("\n===== MENU PRINCIPAL =====")
            print("1. Menu Participante")
            print("2. Menu Produtor")
            print("3. Menu Vendedor")
            print("4. Menu Admin")
            print("5. Menu Evento")
            print("0. Sair")

            try:
                opcao = int(input("Escolha uma opção: ").strip())
                clearScreen()

                match opcao:
                    case 1:
                        menu = MenuParticipante(participantes, eventos, vendedores, ingressos, avaliacoes)
                        menu.exibir_menu()
                    case 2:
                        menu = MenuProdutor(produtores, eventos)
                        menu.exibir_menu()
                    case 3:
                        menu = MenuVendedor(vendedores, eventos)
                        menu.exibir_menu()
                    case 4:
                        menu = MenuAdmin(participantes, produtores, vendedores)
                        menu.exibir_menu()
                    case 5: 
                        menu = MenuEvento(eventos, avaliacoes)
                        menu.exibir_menu()
                    case 0:
                        endProgram()
                    case _:
                        print("Opção inválida!")
            except ValueError:
                print("Entrada inválida! Por favor, digite um número.")
                input("Pressione Enter para continuar...")
                clearScreen()

# ________________________________________ Usuários Criados__________________________________________
  
ProdutorZero = Produtor("Zé Produtor", "123456789-10", "12345CBA", "10/11/2012")
produtores.append(ProdutorZero)

ParticipanteZero = Participante("Bob Participante")
participantes.append(ParticipanteZero)

VendedorZero = Vendedor("Robert Downey Jr", "135798642-10", "13524BCA", "04/04/1965")
vendedores.append(VendedorZero)

# ________________________________________ Eventos Criados__________________________________________

EventoOnline = Evento("#123", "online", "Evento ONLINE tigrinho", "22/05/2025", "Casa do Manuel", 15 )
EventoOnline.valor_ingresso = 29.99
eventos.append(EventoOnline)

EventoPresencial = Evento("#321", "presencial", "Sorteio de moto", "23/05/2025", "Casa do Jorge", 20 )
EventoPresencial.valor_ingresso = 49.50
eventos.append(EventoPresencial)

menu_principal()