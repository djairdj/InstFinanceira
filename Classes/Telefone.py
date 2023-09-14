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
        def isDDD(d: int) -> bool:
            siglasDDD = {
                # Norte
                "AC": 68,
                "AP": 96,
                "AM": [92, 97],
                "PA": [91, 93, 94],
                "RO": 69,
                "RR": 95,
                "TO": 63,

                # Nordeste
                "AL": 82,
                "BA": [71, 72, 73, 74, 75, 77],
                "CE": [85, 88],
                "MA": [98, 99],
                "PB": 83,
                "PE": [81, 87],
                "PI": [86, 89],
                "RN": 84,
                "SE": 79,

                # Centro-Oeste
                "DF": 61,
                "GO": [62, 64],
                "MT": [65, 66],
                "MS": 67,

                # Sudeste
                "ES": [27, 28],
                "MG": [31, 32, 33, 34, 35, 37, 38],
                "RJ": [21, 22, 24],
                "SP": [11, 12, 13, 14, 15, 16, 17, 18, 19],

                # Sul
                "PR": [41, 42, 43, 44, 45, 46],
                "RS": [51, 53, 54, 55],
                "SC": [47, 48, 49]
            }
            
            for item in siglasDDD:
                if isinstance (siglasDDD[item], list):
                    for n in siglasDDD[item]:
                        if d == n: return True
                if d == siglasDDD[item]: return True
            return False

        if isinstance(ddd, str):
            novo_ddd = int(''.join([i for i in ddd if i.isdigit()]))
            if novo_ddd >= 100:
                return '000'
            else:
                if isDDD(novo_ddd):
                    return str(novo_ddd)
                return '000'
        return '000'
