# noinspection SpellCheckingInspection
class Cliente:
    def __init__(self, nome: str, endereco, phone, cpf: str):
        self.address: list = []
        self.telefones: list = []
        self.contas: list = []
        self.nome: str = nome.upper()
        self.cpf: str = Cliente.ajusta_cpf(cpf)
        self.email: str = ''
        self.address.append(endereco)
        self.telefones.append(phone)

    def __str__(self):
        result = f'Cliente: {self.nome}'
        result += f"\nCPF: {self.cpf}"
        result += ('\nE-mail: ' + self.email) if self.email != '' else ""
        if len(self.telefones) > 0:
            result += '\nTelefone(s): '
            for h in range(len(self.telefones)):
                result += self.telefones[h].__str__()
                if h < len(self.telefones) - 1:
                    result += " / "
        if len(self.address) > 0:
            result += "\nEndereço(s):\n"
            for y in range(len(self.address)):
                result += self.address[y].__str__()
                if y < len(self.address) - 1:
                    result += "\n"
        if len(self.contas) > 0:
            result += '\nContas:\n'
            for f in range(len(self.contas)):
                result += self.contas[f].__str__()
                if f < len(self.contas) - 1:
                    result += '\n'
        return result

    @staticmethod
    def ajusta_cpf(cp_efi: str):
        if isinstance(cp_efi, str):
            cp_ef = ''.join([i for i in cp_efi if i.isdigit()])
            if len(cp_ef) == 11:
                cp = cp_ef[:3] + '.' + cp_ef[3:6] + '.' + cp_ef[6:9] + '-' + cp_ef[9:]
                return cp
            else:
                return '000.000.000-00'
        else:
            return cp_efi

    @staticmethod
    def ajustar_email_cliente():
        mail = input("Informe o novo email do cliente: ")
        tem_arroba: bool = '@' in mail
        tem_ponto: bool = "." in mail
        sem_ponto_extremos: bool = (mail[0] != '.' and mail[-1] != '.')

        while not (tem_arroba and sem_ponto_extremos and tem_ponto):
            print("e-mail inválido!")
            mail = input("Informe o novo email do cliente: ")
            tem_arroba: bool = '@' in mail
            sem_ponto_extremos: bool = (mail[0] != '.' and mail[-1] != '.')
            tem_ponto: bool = "." in mail
        return mail.lower()
