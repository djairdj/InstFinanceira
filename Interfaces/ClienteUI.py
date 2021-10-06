from Classes.Cliente import Cliente
from Classes.Conta import Conta
from Interfaces.ContaUI import ContaUI
from Classes.Endereco import Endereco
from Classes.Telefone import Telefone


class ClienteUI:
    def __init__(self, bancoUI, cliente):
        self.bancoI = bancoUI
        self.client = cliente

    def __str__(self):
        return 'ClienteUI Nao implementado'

    def menu(self):
        """
       :return: Sem retorno
        """
        option = '-1'
        while option != '0':
            men = ("\n"
                   ",___________________________,\n"
                   "|_______Menu Cliente________|\n"
                   "| 0 - Sair do Menu          |\n"
                   "| 1 - Adicionar telefone(s) |\n"
                   "| 2 - Remover telefone(s)   |\n"
                   "| 3 - Listar telefone(s)    |\n"
                   "| 4 - Adicionar endereço(s) |\n"
                   "| 5 - Remover endereço(s)   |\n"
                   "| 6 - Listar endereço(s)    |\n"
                   "| 7 - Alterar nome          |\n"
                   "| 8 - Alterar email         |\n"
                   "| 9 - Gerir Contas          |\n"
                   "| 10 - Exibir Cliente       |\n"
                   "|---------------------------|")
            print(men)
            option = input("Escolha uma opção acima: ")
            if option == '0':
                print("Saindo do Menu!")
            elif option == '1':
                self.add_telefone(self.define_novo_telefone())
            elif option == '2':
                self.remover_telefone()
            elif option == '3':
                print(self.lista_de_telefones())
            elif option == '4':
                self.adicionar_address(self.define_novo_address())
            elif option == '5':
                self.remover_address()
            elif option == '6':
                print(self.lista_de_address())
            elif option == '7':
                self.client.nome = input("Informe o novo nome do cliente: ").upper()
            elif option == '8':
                self.client.email = Cliente.ajustar_email_cliente()
            elif option == '9':
                self.menu_gerir_contas()
            elif option == '10':
                print(self.client)
            else:
                print("Opção inválida!")

    def menu_gerir_contas(self):
        opt = '-1'
        while opt != '0':
            men = ('\n'
                   ',___________________________,\n'
                   '|_______Gerir Contas________|\n'
                   '| 0 - Sair do Menu          |\n'
                   '| 1 - Adicionar conta       |\n'
                   '| 2 - Remover conta         |\n'
                   '| 3 - Listar conta(s)       |\n'
                   # "| 4 - Mostrar saldo         |\n"
                   '| 4 - Operar conta          |\n'
                   '|---------------------------|\n'
                   )
            print(men)
            opt = input("Escolha uma das opções acima: ")
            if opt == '0':
                print("Saindo do menu!")
            elif opt == '1':
                self.adicionar_conta()
            elif opt == '2':
                self.menu_remover_conta()
            elif opt == '3':
                if len(self.client.contas) > 0:
                    # listar_contas_cliente(banco, cliente.cpf)
                    print(self.lista_de_contas(), end='')
                else:
                    print('Cliente sem contas para listar.')
            # elif opt == '4':
            #     print("aqui é pra mostrar saldo")
            elif opt == '4':
                self.operar_conta()
            else:
                print("Opção inválida.")

    def operar_conta(self):
        if len(self.client.contas) > 0:
            print(self.enumerar_contas())
            n = input('Escolha uma conta pela ordem: ')
            n = int(n) - 1 if n.isdigit() else -1
            if 0 <= n < len(self.client.contas):
                conta_ui = ContaUI(self.bancoI, self.client.contas[n])
                conta_ui.menu()
            else:
                print('Escolha um número correspondente na próxima vez.')
        else:
            print('Cliente sem contas pra gerir.')

    def adicionar_conta(self):
        if len(self.bancoI.banco.agencias) > 0:
            self.bancoI.enumerar_agencias()
            n = input('Escolha o número da agência: ')
            n = int(n) if n.isdigit() else -1
            if 0 < n <= len(self.bancoI.banco.agencias):
                conta = Conta(self.client, self.bancoI.banco.agencias[n - 1].numero)
                self.bancoI.banco.agencias[n - 1].contas.append(conta)
                self.add_conta(conta)
                # tem uma mensagem lá no __init__() da Conta
            else:
                print('Escolha um número correspondente na próxima vez.')
        else:
            print('O banco não possui agências para adicionar a conta.')

    def add_conta(self, conta: Conta):
        self.client.contas.append(conta)

    def menu_remover_conta(self):
        if len(self.client.contas) > 0:
            print(self.enumerar_contas())
            n = input('Escolha uma conta pela ordem: ')
            n = int(n) - 1 if n.isdigit() else -1
            if 0 <= n < len(self.client.contas):
                conta_pra_remover = self.client.contas[n]
                escolha = "S"
                if conta_pra_remover.saldo > 0:
                    print("Essa conta possui saldo positivo.")
                    escolha = input("Deseja excluir ela mesmo assim? (S/N) ").upper()
                    if escolha != "S":
                        print("Operação cancelada.")
                if escolha == "S":
                    for ag in self.bancoI.banco.agencias:
                        if ag.numero == conta_pra_remover.agencia:
                            ag.contas.remove(conta_pra_remover)
                            break
                    self.client.contas.remove(conta_pra_remover)
            else:
                print('Escolha um número correspondente na próxima vez.')
        else:
            print('Não há contas para remover.')

    def enumerar_contas(self):
        info = ''
        for c in range(len(self.client.contas)):
            info += f'{c + 1}ª - {self.client.contas[c].__str__()}'
            if c < len(self.client.contas) - 1:
                info += '\n'
        return info

    def lista_de_contas(self):
        if len(self.client.contas) > 0:
            info = ''
            for c in range(len(self.client.contas)):
                info += self.client.contas[c].__str__()
                if c < len(self.client.contas) - 1:
                    info += '\n'
            return info
        else:
            return "Sem contas cadastradas."

    def adicionar_address(self, address: Endereco):
        if isinstance(address, Endereco):
            self.client.address.append(address)
        else:
            print('objeto não correspondente ao tipo Endereço')

    def enumerar_address(self):
        info = ''
        for c in range(len(self.client.address)):
            info += f'{c + 1}º - {self.client.address[c].__str__()}'
            if c < len(self.client.address) - 1:
                info += '\n'
        return info

    def lista_de_address(self):
        if len(self.client.address) > 0:
            info = ''
            for c in range(len(self.client.address)):
                info += self.client.address[c].__str__()
                if c < len(self.client.address) - 1:
                    info += '\n'
            return info
        else:
            return 'Sem endereços cadastrados.'

    def remover_address(self):
        if len(self.client.address) > 0:
            print(self.enumerar_address())
            n = input('Escolha um número pra remover o endereço: ')
            n = int(n) - 1 if n.isdigit() else -1
            if 0 <= n < len(self.client.address):
                self.client.address.remove(self.client.address[n])
                print("Endereço removido.")
            else:
                print("Escolha uma opção válida na próxima.")
        else:
            print("Sem endereços para remover.")

    def add_telefone(self, phone: Telefone):
        if isinstance(phone, Telefone):
            self.client.telefones.append(phone)
        else:
            print('objeto não correspondente ao tipo Telefone')

    def enumerar_telefones(self):
        info = ''
        for c in range(len(self.client.telefones)):
            info += f'{c + 1}º - {self.client.telefones[c].__str__()}'
            if c < len(self.client.telefones) - 1:
                info += '\n'
        return info

    def lista_de_telefones(self):
        if len(self.client.telefones) > 0:
            info = ''
            for c in range(len(self.client.telefones)):
                info += self.client.telefones[c].__str__()
                if c < len(self.client.telefones) - 1:
                    info += '\n'
            return info
        else:
            return 'Sem telefones cadastrados.'

    def remover_telefone(self):
        if len(self.client.telefones) > 0:
            print(self.enumerar_telefones())
            n = int(input('Escolha um número pra remover o telefone: ')) - 1
            if 0 <= n < len(self.client.telefones):
                self.client.telefones.remove(self.client.telefones[n])
                print("Telefone removido.")
            else:
                print("Escolha uma opção válida na próxima.")
        else:
            print("Sem telefones para remover.")

    @staticmethod
    def define_novo_address() -> Endereco:
        rua = input('Informe o nome da rua: ')
        number = input('Informe o número: ')
        complemento = input("Digite o complemento: ")
        cep = input("Digite o CEP: ")

        city = input("Digite o nome da cidade: ").upper()
        uf = input("Digite a sigla da Unidade Federativa(UF): ").upper()
        end = Endereco(rua, number, complemento, cep, city, uf)
        return end

    @staticmethod
    def define_novo_telefone() -> Telefone:
        ddd = input('Informe o DDD: ')
        phone = input('Informe o telefone: ')
        telefone = Telefone(ddd, phone)
        return telefone
