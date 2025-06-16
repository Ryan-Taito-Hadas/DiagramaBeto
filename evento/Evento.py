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