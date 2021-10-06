from Classes.Agencia import Agencia
from Interfaces.AgenciaUI import AgenciaUI
from Classes.Cliente import Cliente
from Interfaces.ClienteUI import ClienteUI


class BancoUI:
    def __init__(self, banco):
        self.banco = banco

    def __str__(self):
        return 'Nao implementado'

    def menu(self):
        opt = '-1'
        while opt != '0':
            men = ("\n"
                   ",_______________________,\n"
                   "|_____Menu do Banco_____|\n"
                   "| 0 - Sair do Sistema   |\n"
                   "| 1 - Listar Agências   |\n"
                   "| 2 - Adicionar Agência |\n"
                   "| 3 - Remover Agência   |\n"
                   "| 4 - Ajustar Agência   |\n"
                   "| 5 - Listar Clientes   |\n"
                   "| 6 - Adicionar Cliente |\n"
                   "| 7 - Remover Cliente   |\n"
                   "| 8 - Alterar Cliente   |\n"
                   "|-----------------------|")
            print(men)
            opt = input("Escolha uma das opções acima: ")
            if opt == '0':
                print('Volte Sempre!', end='')
            elif opt == '1':
                self.listar_agencias()
            elif opt == '2':
                self.menu_adicionar_agencia()
            elif opt == '3':
                self.menu_remover_agencia()
            elif opt == '4':
                self.menu_ajustar_agencia()
            elif opt == '5':
                if len(self.banco.clientes) > 0:
                    print(self.listar_clientes())
                else:
                    print('Sem clientes pra mostrar!')
            elif opt == '6':
                client = self.define_novo_cliente()
                print('\nRevise as informações do Cliente:')
                cliente_interface = ClienteUI(self, client)
                cliente_interface.menu()
            elif opt == '7':
                self.menu_excluir_cliente()
            elif opt == '8':
                self.menu_alterar_cliente()
            else:
                print("Opção inválida.")

    def menu_adicionar_agencia(self):
        numb = input('Qual o código /n° da Agência? ')
        if isinstance(self.pegar_agencia(numb), Agencia):
            print('Já existe uma agencia com esse código.')
        else:
            ag = Agencia(self.banco, numb)
            self.adicionar_agencia(ag)

    def menu_remover_agencia(self):
        if len(self.banco.agencias) > 0:
            self.enumerar_agencias()
            n = int(input('Escolha um número pra remover a agência: ')) - 1
            if 0 <= n < len(self.banco.agencias):
                checagem = self.menu_excluir_agencia(n)
                if checagem >= 0:
                    self.remover_uma_agencia_e_conta_de_todos_clientes(self.banco.agencias[n])
                    self.banco.agencias.remove(self.banco.agencias[n])
                    print("Agência removida.")
                else:
                    print("Operação de exclusão cancelada!")
            else:
                print('Escolha um número correspondente na próxima vez.')
        else:
            print('O banco não possui agências para remover.')

    def enumerar_agencias(self):
        n = 1
        for a in self.banco.agencias:
            print(f'{n}ª Agência: ' + a.numero)
            n += 1

    def menu_excluir_agencia(self, index: int) -> int:
        cont = 0
        saldo_total_das_contas: float = 0.0
        numero_da_agencia = self.banco.agencias[index].numero
        for cada_cliente in self.banco.clientes:
            for cada_conta_do_cliente in cada_cliente.contas:
                if cada_conta_do_cliente.agencia == numero_da_agencia:
                    cont += 1
                    saldo_total_das_contas += cada_conta_do_cliente.saldo
        if cont > 0:
            print('Existem contas de clientes cadastradas nessa agência!')
            opt = input("Deseja excluir essa agência nº {} mesmo assim(s/n)? ".format(numero_da_agencia)).upper()
            if opt == 'S':
                print(f'O valor mínimo de R$ {saldo_total_das_contas} corresponde ao prejuízo em apagar essa agência.')
                opt = input(
                    "Tem realmente certeza que deseja apagar essa agência\ne todas as contas relacionadas a ela? ").upper()
                if opt == 'S':
                    return index
                else:
                    print('Muito bem!')
                    return -1
            else:
                return -1
        else:
            return index

    def remover_uma_agencia_e_conta_de_todos_clientes(self, agencia: Agencia):
        # Percorre todas as contas de cada cliente e apaga as que forem da agencia argumentada
        for index_cliente in range(len(self.banco.clientes)):
            for index_conta in range(len(self.banco.clientes[index_cliente].contas) - 1, -1, -1):
                if self.banco.clientes[index_cliente].contas[index_conta].agencia == agencia.numero:
                    self.banco.clientes[index_cliente].contas.remove(
                        self.banco.clientes[index_cliente].contas[index_conta])

    def menu_ajustar_agencia(self):
        if len(self.banco.agencias) > 0:
            self.enumerar_agencias()
            n = input('Escolha o número pra ajustar a agência: ')
            n = int(n) if n.isdigit() else -1
            if 0 < n <= len(self.banco.agencias):
                agencia_interface = AgenciaUI(self, self.banco.agencias[n - 1])
                agencia_interface.menu_agencia()
            else:
                print('Escolha um número correspondente na próxima vez.')
        else:
            print('O banco não possui agências para ajustar.')

    def define_novo_cliente(self) -> Cliente:
        nome = input("Qual o nome do novo cliente? ").upper()
        cpf = Cliente.ajusta_cpf(input('Digite o cpf: '))
        while cpf == '000.000.000-00':
            print("Adicione um cpf válido!")
            cpf = Cliente.ajusta_cpf(input('Digite o cpf: '))
        esse_valor = self.get_cliente_banco(cpf)
        if isinstance(esse_valor, Cliente):
            print(f'CPF do cliente, já associado ao banco {self.banco.nome}.')
            m = input('Deseja mostrar os dados desse cliente (s/n)? ').upper()
            print(esse_valor) if m == 'S' else print(end='')
            return esse_valor
        else:
            print('Defina o endereço:')
            address = ClienteUI.define_novo_address()
            print('Defina o telefone dele:')
            telefone = ClienteUI.define_novo_telefone()
            client = Cliente(nome, address, telefone, cpf)
            self.adicionar_cliente(client)
            return client

    def get_cliente_banco(self, valor_atributo: str):
        return self.pegar_cliente(valor_atributo.upper())

    def menu_excluir_cliente(self):
        if len(self.banco.clientes) > 0:
            opt = '-1'
            while opt != '0':
                men = ("\n"
                       ",_______________________,\n"
                       "|___Menu de Exclusão____|\n"
                       "| 0 - Sair do Menu      |\n"
                       "| 1 - Listar Clientes   |\n"
                       "| 2 - Excluir por CPF   |\n"
                       "| 3 - Remover por nome  |\n"
                       "|-----------------------|")
                print(men)
                opt = input("Escolha uma das opções acima: ")
                if opt == '0':
                    print("Saindo do menu de exclusão!")
                elif opt == '1':
                    if len(self.banco.clientes) > 0:
                        print(self.listagem_simples_clientes(), end='')
                    else:
                        print("Sem clientes")
                elif opt == '2':
                    if len(self.banco.clientes) > 0:
                        cp = Cliente.ajusta_cpf(input("Informe só os nºs do cpf: "))
                        if cp != '000.000.000-00':
                            cli = self.pegar_cliente(cp)
                            if isinstance(cli, Cliente):
                                self.banco.clientes.remove(cli)
                                print(f"Cliente do CPF nº {cli.cpf} removido.")
                            else:
                                print("Cliente não existe na base de dados.")
                        else:
                            print("Digite o cpf corretamente.")
                    else:
                        print("Sem clientes")
                elif opt == '3':
                    if len(self.banco.clientes) > 0:
                        nome = input("Digite o nome exato do Cliente: ").upper()
                        cliente = self.pegar_cliente(nome)
                        if isinstance(cliente, Cliente):
                            self.banco.clientes.remove(cliente)
                            print(f"Cliente {cliente.cpf} removido.")
                        else:
                            print("Cliente não existe na base de dados.")
                    else:
                        print("Sem clientes")
        else:
            print('Não há clientes para remover.')

    def menu_alterar_cliente(self):
        if len(self.banco.clientes) > 0:
            opt = '-1'
            while opt != '0':
                men = ("\n"
                       ",_________________________,\n"
                       "|__Menu Alterar Cliente___|\n"
                       "| 0 - Sair do Menu        |\n"
                       "| 1 - Listar Clientes     |\n"
                       "| 2 - Escolher por CPF    |\n"
                       "| 3 - Escolher por nome   |\n"
                       "|-------------------------|")
                print(men)
                opt = input("Escolha uma das opções acima: ")
                if opt == '0':
                    print("Saindo do menu!")
                elif opt == '1':
                    print(self.listagem_simples_clientes(), end='')
                elif opt == '2':
                    cp = Cliente.ajusta_cpf(input("Informe só os nºs do cpf: "))
                    if cp != '000.000.000-00':
                        cli = self.pegar_cliente(cp)
                        if isinstance(cli, Cliente):
                            print(f"Cliente do CPF nº {cli.cpf} encontrado.\nAjuste no menu abaixo:")
                            cliente_interface = ClienteUI(self.banco, cli)
                            cliente_interface.menu()
                        else:
                            print("Cliente não existe na base de dados.")
                    else:
                        print("Digite o cpf corretamente.")
                elif opt == '3':
                    nome = input("Digite o nome exato do Cliente: ").upper()
                    cliente = self.pegar_cliente(nome)
                    if isinstance(cliente, Cliente):
                        print(f"Cliente do CPF nº {cliente.cpf} encontrado.\nAjuste no menu abaixo:")
                        cliente_interface = ClienteUI(self, cliente)
                        cliente_interface.menu()
                    else:
                        print("Cliente não existe na base de dados.")
        else:
            print('Não há clientes para alterar.')

    def adicionar_agencia(self, agencia):
        isinstance(agencia, Agencia)
        self.banco.agencias.append(agencia)

    def listar_agencias(self):
        if len(self.banco.agencias) > 0:
            print('Banco ' + self.banco.nome)
            for a in self.banco.agencias:
                print(a)
        else:
            print('Não há agências para exibir')

    def pegar_agencia(self, code_agencia: str):
        for a in self.banco.agencias:
            if a.numero == code_agencia:
                return a
        return

    def pegar_agenciaUI(self, code_agencia: str):
        for a in self.banco.agencias:
            if a.numero == code_agencia:
                return AgenciaUI(self, a)
        return

    def adicionar_cliente(self, client):
        self.banco.clientes.append(client)

    def pegar_cliente(self, valor: str):
        positions = []
        for cl in range(len(self.banco.clientes)):
            if valor == self.banco.clientes[cl].nome or valor == self.banco.clientes[cl].cpf:
                positions.append(cl)
        if len(positions) > 1:
            for li in range(len(positions)):
                print(
                    f'{li + 1}º Cliente: {self.banco.clientes[positions[li]].nome} CPF: {self.banco.clientes[positions[li]].cpf}')

            escolha = int(input('Escolha o número correspondente acima: '))

            while 0 >= escolha or escolha > len(positions):
                escolha = int(input('Escolha o número correspondente acima: '))

            cliente_de_retorno = self.banco.clientes[positions[escolha - 1]]
            cliente_de_retorno = cliente_de_retorno
            return cliente_de_retorno
        elif len(positions) == 1:
            # Retorna o cliente em questão
            return self.banco.clientes[positions[0]]
        else:
            return

    def listar_clientes(self):
        info = ''
        for f in range(len(self.banco.clientes)):
            info += self.banco.clientes[f].__str__()
            if f < len(self.banco.clientes) - 1:
                info += '\n' + ('-' * 30) + '\n'
        return info

    def listagem_simples_clientes(self):
        if len(self.banco.clientes) > 0:
            info = ''
            for f in range(len(self.banco.clientes)):
                info += f'Cliente: {self.banco.clientes[f].nome}'
                info += f'\nCPF: {self.banco.clientes[f].cpf}'
                if f < len(self.banco.clientes) - 1:
                    info += '\n' + ('-' * 20) + '\n'
            return info
        else:
            return ''
