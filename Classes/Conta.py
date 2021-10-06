import random


class Conta:
    numeral: int = 9999
    digit: int = 0

    def __init__(self, cliente_titular, numero_agencia: str):
        self.cliente_titular = cliente_titular
        Conta.digit = (Conta.digit + 1) % 10
        Conta.numeral = Conta.numeral + 1
        self.numero: str = f'{self.numeral} - {self.digit}'
        self.nome_titular: str = cliente_titular.nome.upper()
        self.cpf_titular = cliente_titular.cpf
        self.agencia: str = numero_agencia
        self.saldo: float = 0.0
        self.senha: str = str(random.randint(1000, 9999))
        print(f"Conta Criada!\nSua senha de 4 dígitos é: {self.senha}, anote-a.")

    def __str__(self):
        self.atualiza_dados()
        resposte = 'Titular: ' + self.nome_titular
        resposte += (', Agência: ' + self.agencia) if self.agencia != '' else ''
        resposte += ', Nº da Conta: ' + self.numero
        # resposte += ', Saldo: R$ ' + str(self.saldo)
        return resposte

    def definir_senha(self, nome_do_titular: str, senha_antiga: str):
        if nome_do_titular.upper() == self.nome_titular and (senha_antiga == self.senha):
            nova_senha = input("Informe a nova senha e não esqueça ela!: ")
            confirmada = input("Repita a nova senha, só por precaução... ")
            if confirmada == nova_senha:
                self.senha = confirmada
            else:
                print("Senhas não conferem, tente outra vez.")
        else:
            print("Tente outra vez.")

    def atualiza_dados(self):
        self.cpf_titular = self.cliente_titular.cpf
        self.nome_titular = self.cliente_titular.nome