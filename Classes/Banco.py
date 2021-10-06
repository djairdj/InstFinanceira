from Classes.Agencia import Agencia


class Banco:
    def __init__(self, nome: str):
        self.nome = nome.upper()  # é só FRU-FRU
        self.agencias = []
        self.clientes: list = []

    def __str__(self):
        return 'Nao implementado'


