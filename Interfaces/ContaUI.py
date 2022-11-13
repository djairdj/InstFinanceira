from Classes.Agencia import Agencia
from Classes.Conta import Conta


class ContaUI:
    def __init__(self, bancoUI, conta):
        self.conta = conta
        self.bancoI = bancoUI

    def __str__(self):
        return f'{self.conta}, Banco: {self.bancoI.banco.nome}'

    def menu(self):
        opt = '-1'
        while opt != '0':
            men = ("\n"
                   ",___________________________,\n"
                   "|_____Manipular Conta_______|\n"
                   "| 0 - Sair do Menu          |\n"
                   "| 1 - Depositar             |\n"
                   "| 2 - Sacar                 |\n"
                   "| 3 - Transferir            |\n"
                   "| 4 - Mostrar saldo         |\n"
                   "| 5 - Mostrar conta         |\n"
                   "|---------------------------|\n"
                   )
            print(men)
            opt = input("Escolha uma das opções acima: ")
            if opt == '0':
                print("Saindo do menu!")
            elif opt == '1':
                self.depositar(float(input('Digite o valor para depósito: ')))
                print("Depósito realizado.")
            elif opt == '2':
                senha = input("Digite a senha exata da conta: ")
                if senha == self.conta.senha:
                    if self.sacar(float(input('Digite o valor para saque: '))):
                        print("Saque realizado!")
                    else:
                        print("Saldo insuficiente.")
                else:
                    print("Senha errada, não é possível sacar.")
            elif opt == '3':
                senha = input("Digite a senha exata da conta: ")
                if senha == self.conta.senha:
                    self.menu_transferir(self.bancoI)
                else:
                    print("Senha errada, não é possível transferir.")
            elif opt == '4':
                senha = input("Digite a senha exata da conta: ")
                if senha == self.conta.senha:
                    print(f'Saldo: $ {self.conta.saldo}')
                else:
                    print("Senha errada.")
            elif opt == '5':
                print(self)
            else:
                print("Opção inválida!")

            self.conta.atualiza_dados()

    def sacar(self, valor: float):
        if self.conta.saldo >= valor:
            self.conta.saldo = self.conta.saldo - valor
            return True

    def depositar(self, valor: float):
        if isinstance(valor, float) and valor > 0:
            self.conta.saldo += valor

    def transferir(self, valor: float, outra_conta):
        if self.sacar(valor):
            nova_conta_ui = ContaUI(self.bancoI, outra_conta)
            nova_conta_ui.depositar(valor)
            print("Transferência realizada com sucesso.")
        else:
            print('Saldo insuficiente.')

    def menu_transferir(self, bancoI_da_conta):
        number = input("Informe só o número da conta de destino: ")
        digito = input("Informe só o dígito da conta de destino: ")
        num_conta = f'{number} - {digito}'
        s = input('Vai transferir entre contas da mesma agência? (s/n) ').upper()
        if s == 'S':
            agencia = bancoI_da_conta.pegar_agencia(self.conta.agencia)
            agencia_interface = bancoI_da_conta.pegar_agenciaUI(self.conta.agencia)
            other_conta = agencia_interface.pegar_conta(num_conta)
            if isinstance(agencia, Agencia):
                if isinstance(other_conta, Conta):
                    valor = float(input('Digite o valor a ser transferido: '))
                    print(f"\nDestino:\nBanco: {bancoI_da_conta.banco.nome}")
                    print(f"Código da agência: {agencia.numero}")
                    print(f"Recebedor: {other_conta.nome_titular}, CPF: ...{other_conta.cpf_titular[4:11]}...")
                    print(f'Valor da Transferência: $ {valor}')
                    confirm = input("Confirmar transação?? (S/N) ").upper()
                    if confirm == "S":
                        self.transferir(valor, other_conta)
                    else:
                        print("Até a próxima.")
                else:
                    print('Agencia não possui essa conta de destino.')
            else:
                print("Sua conta não está na sua agência.")
        else:
            cod_agencia = input("Informe o código da agencia de destino: ")
            agencia = bancoI_da_conta.pegar_agencia(cod_agencia)
            if isinstance(agencia, Agencia):
                agencia_interface = bancoI_da_conta.pegar_agenciaUI(cod_agencia)
                other_conta = agencia_interface.pegar_conta(num_conta)
                if isinstance(other_conta, Conta):
                    valor = float(input('Digite o valor a ser transferido: '))
                    print(f"\nDestino:\nBanco: {bancoI_da_conta.banco.nome}")
                    print(f"Código da agência: {agencia.numero}")
                    print(f"Recebedor: {other_conta.nome_titular}, CPF: ...{other_conta.cpf_titular[4:11]}...")
                    print(f'Valor da Transferência: $ {valor}')
                    confirm = input("Confirmar transação?? (S/N) ").upper()
                    if confirm == "S":
                        self.transferir(valor, other_conta)
                    else:
                        print("Até a próxima.")
                else:
                    print('Agencia informada não possui essa conta de destino.')
            else:
                print('Não há agência com esse código, cadastrada.')
