from Classes.Agencia import Agencia
from Classes.Cliente import Cliente
from Interfaces.ClienteUI import ClienteUI
from Classes.Conta import Conta
from Interfaces.ContaUI import ContaUI


class AgenciaUI:
    def __init__(self, bancoUI, agencia: Agencia):
        if isinstance(agencia, Agencia):
            self.bancoI = bancoUI
            self.agencia = agencia
        else:
            print("Um ou mais argumentos inválidos.")

    def menu_agencia(self):
        """
        :return: Sem retorno
        """
        largura = 28
        option = '-1'
        while option != '0':
            print(",{},".format("_" * largura))
            print("|{0}Menu Agencia{0}|".format("." * int(largura / 2 - 6)))
            print("|{}|".format("_" * largura))
            print("| 0 - Sair\t\t\t\t\t |")
            print("| 1 - Adicionar Conta(s)\t |")
            print("| 2 - Listar Conta(s)\t\t |")
            print("| 3 - Remover Conta(s)\t\t |")
            print("| 4 - Ajustar Conta \t\t |")
            print("| 5 - Exibir Clientes \t\t |")

            print("|{}|".format("-" * largura))
            option = input("Escolha uma opção acima: ")
            if option == '0':
                print("Saindo do Menu!")
            elif option == '1':
                self.adicionar_conta()
            elif option == '2':
                self.listar_contas()
            elif option == '3':
                self.remover_conta()
            elif option == '4':
                self.ajustar_conta()
            elif option == '5':
                self.listar_clientes_agencia()
            else:
                print("Opção inválida.")

    def adicionar_conta(self):
        essa_nova_conta = self.define_nova_conta()
        ajuste = input('Nova conta criada!\nDeseja alterar essa conta (s/n)? ').upper()
        if ajuste == 'S':
            conta_ui = ContaUI(self.bancoI, essa_nova_conta)
            conta_ui.menu()

    def define_nova_conta(self) -> Conta:
        uma_conta = Conta
        titularidade = input('Informe o titular: ').upper()
        cpf = Cliente.ajusta_cpf(input('Digite o cpf: '))
        while cpf == '000.000.000-00':
            print("Adicione um cpf válido!")
            cpf = Cliente.ajusta_cpf(input('Digite o cpf: '))
        if self.existe_cliente_na_agencia(cpf):
            print('Ele já é cliente dessa agência!')
            client = self.bancoI.get_cliente_banco(cpf)
            if isinstance(client, Cliente):
                m = input('Deseja mostrar os dados desse cliente (s/n)? ').upper()
                print(client) if m == 'S' else print(end='')
                print('-' * 25)
                uma_conta = Conta(client, self.agencia.numero)
                cliente_interface = ClienteUI(self.bancoI, client)
                cliente_interface.add_conta(uma_conta)
                self.agencia.contas.append(uma_conta)
            else:
                print("Não foi possível capturar os dados do cliente.")
        else:
            possible_client = self.bancoI.pegar_cliente(cpf)
            if isinstance(possible_client, Cliente):  # Achei o cliente
                print('Existe esse cliente no banco mas não nessa agência')
                m = input('deseja mostrar os dados desse cliente (s/n)? ').upper()
                print(possible_client) if m == 'S' else print(end='')
                uma_conta = Conta(possible_client, self.agencia.numero)
                cliente_interface = ClienteUI(self.bancoI, possible_client)
                cliente_interface.add_conta(uma_conta)
                self.agencia.contas.append(uma_conta)
            else:
                print('É um novo cliente, edite-o')
                print('Defina o endereço:')
                address = ClienteUI.define_novo_address()
                print('Defina o telefone dele:')
                telefone = ClienteUI.define_novo_telefone()
                cli = Cliente(titularidade, address, telefone, cpf)
                uma_conta = Conta(cli, self.agencia.numero)
                cliente_interface = ClienteUI(self.bancoI, cli)
                cliente_interface.add_conta(uma_conta)
                self.agencia.contas.append(uma_conta)
                self.bancoI.adicionar_cliente(cli)
                # print('Revise suas Informações')
                # cliente_interface.menu()
        return uma_conta

    def pegar_conta(self, code_conta: str):
        for c in self.agencia.contas:
            if c.numero == code_conta:
                return c
        return

    def existe_cliente_na_agencia(self, valor: str) -> bool:
        valor = valor.upper()
        for conta in self.agencia.contas:
            if valor == conta.nome_titular or valor == conta.cpf_titular:
                return True
        return False

    def enumerar_contas(self):
        info = ''
        for c in range(len(self.agencia.contas)):
            info += f'{c + 1}º - {self.agencia.contas[c].__str__()}'
            if c < len(self.agencia.contas) - 1:
                info += '\n'
        return info

    def listar_contas(self):
        if len(self.agencia.contas) > 0:
            print('Contas:')
            for cc in self.agencia.contas:
                print(cc)
        else:
            print('Não há contas para exibir.')

    def remover_conta(self):
        if len(self.agencia.contas) > 0:
            print(self.enumerar_contas())
            n = input('Escolha um número pra remover a conta: ')
            n = int(n) - 1 if n.isdigit() else -1
            if 0 <= n < len(self.agencia.contas):
                conta_em_foco = self.agencia.contas[n]
                excluir = "S"
                if conta_em_foco.saldo > 0:
                    print("A conta possui saldo positivo!")
                    excluir = input("Deseja excluir ela mesmo assim? (S/N) ")
                    if excluir != "S":
                        print("Remoção cancelada!")
                if excluir == "S":
                    conta_em_foco.cliente_titular.contas.remove(conta_em_foco)
                    self.agencia.contas.remove(conta_em_foco)
                    print("Conta removida.")
            else:
                print("Opção inválida!")
        else:
            print("Não há contas para mostrar.")

    def listar_clientes_agencia(self):
        if len(self.agencia.contas) > 0:
            clientes = set()
            for cada_conta in self.agencia.contas:
                clientes.add(cada_conta.cliente_titular)
            for cli in clientes:
                print(f'Nome: {cli.nome}, CPF: {cli.cpf}')
        else:
            print("Não há clientes dessa agência")

    def ajustar_conta(self):
        if len(self.agencia.contas) > 0:
            print(self.enumerar_contas())
            n = input('Escolha um número pra escolher a conta: ')
            n = int(n) - 1 if n.isdigit() else -1
            if 0 <= n < len(self.agencia.contas):
                essa_conta = self.agencia.contas[n]
                contaUI = ContaUI(self.bancoI, essa_conta)
                contaUI.menu()
            else:
                print("Opção inválida!")
        else:
            print("Não há conta cadastrada para ajuste.")
