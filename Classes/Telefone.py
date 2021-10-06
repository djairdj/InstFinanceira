class Telefone:
    def __init__(self, ddd: str, telefone: str):
        self.telefone = self.formata_numero(telefone)
        self.ddd = ddd

    def __str__(self):
        return f'({self.ddd}) {self.telefone}'

    @staticmethod
    def formata_numero(num: str) -> str:
        if isinstance(num, str):
            num = ''.join([i for i in num if i.isdigit()])
            t = int(len(num) / 2)
            num = num[:t] + '-' + num[t:]
            return num
        return '00000-0000'

    @staticmethod
    def formata_ddd(ddd: str) -> str:
        if isinstance(ddd, str):
            novo_ddd = ''.join([i for i in ddd if i.isdigit()])
            if len(novo_ddd) > 3:
                return '000'
            else:
                for a in range(3 - len(novo_ddd)):
                    novo_ddd = '0' + novo_ddd
                return novo_ddd
