class Agencia:
    def __init__(self, banco_number, number: str):
        self.numero = number
        self.contas = []
        self.banco = banco_number

    def __str__(self) -> str:
        # vou criar uma lista só de clientes sem repetição
        nomes_clientes = set()

        quantidade_contas = len(self.contas)
        resultado = ''
        # resultado += 'Banco: ' + (self.banco + '\n') if self.banco != '' else ''
        resultado += f'Agência Número: {self.numero}'
        resultado += '\nContas:\n' if quantidade_contas > 0 else ''

        for c in range(quantidade_contas):
            nomes_clientes.add(self.contas[c].nome_titular)
            resultado += self.contas[c].__str__()
            if c < len(self.contas) - 1:
                resultado += '\n'
        resultado += '\n' + '-' * 35

        # resultado += '\nClientes:\n' if quantidade_contas > 0 else ''
        # cont = 0
        # for s in nomes_clientes:
        #     resultado += s
        #     if cont < len(nomes_clientes) - 1:
        #         resultado += '\n'
        #     cont += 1
        return resultado

    # def adicionar_conta(self, conta):
    #     self.contas.append(conta)
