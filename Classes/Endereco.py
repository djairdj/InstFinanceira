import requests

class Endereco:
    # noinspection PyMethodParameters
    @staticmethod
    def ajusta_cep(cep: str) -> str:
        # noinspection PyMethodFirstArgAssignment
        cep = ''.join([i for i in cep if i.isdigit()])
        resultado = '00.000-000'
        if len(cep) != 8: return resultado
        cep = cep[:2] + '.' + cep[2:5] + '-' + cep[5:]
        return cep

    @staticmethod
    def isUF(uf: str) -> bool:
        ufs = [
            # Norte
            "AC",
            "AP",
            "AM",
            "PA",
            "RO",
            "RR",
            "TO",

            # Nordeste
            "AL",
            "BA",
            "CE",
            "MA",
            "PB",
            "PE",
            "PI",
            "RN",
            "SE",

            # Centro-Oeste
            "DF",
            "GO",
            "MT",
            "MS",

            # Sudeste
            "ES",
            "MG",
            "RJ",
            "SP",

            # Sul
            "PR",
            "RS",
            "SC"
        ]
        return ufs.count(uf.upper()) == 1

    @staticmethod
    def uf_cidade_bairro(cep: str) -> list:
        cep = ''.join([i for i in cep if i.isdigit()])
        if len(cep) != 8: return []
        link = f'https://viacep.com.br/ws/{cep}/json/'
        requisicao = requests.get(link)
        # print(requisicao)
        dic_requisicao = requisicao.json()
        return [
            dic_requisicao['uf'],
            dic_requisicao['localidade'],
            dic_requisicao['bairro']
        ]

    def __init__(self, rua: str, numero: str, complemento: str, CEP: str):
        CEP = Endereco.ajusta_cep(CEP)
        listagemViaCep = self.uf_cidade_bairro(CEP)
        if len(listagemViaCep) > 0:
            self.UF = listagemViaCep[0]
            self.cidade = listagemViaCep[1]
        else:
            self.cidade = ""
            self.UF = 'XX'
        self.rua = rua.capitalize()
        self.numero = numero
        self.complemento = complemento.capitalize()
        self.CEP = CEP

    def __str__(self) -> str:
        info = ''
        info += 'Rua: ' + self.rua
        info += ', ' + self.numero
        info += ', ' + self.complemento
        info += '. ' + self.CEP
        info += '. ' + self.cidade
        info += '-' + self.UF
        return info
