# noinspection SpellCheckingInspection,PyPep8Naming
class Endereco:
    # noinspection PyMethodParameters
    def ajusta_cep(cep: str) -> str:
        # noinspection PyMethodFirstArgAssignment
        cep = ''.join([i for i in cep if i.isdigit()])
        resultado = '00.000-000'
        if len(cep) > 2:
            resultado = cep[:2] + '.' + cep[2:]
        if len(cep) > 5:
            resultado = resultado[:6] + '-' + (cep[5:8] if len(cep) >= 8 else cep[5:])
        return resultado

    def __init__(self, rua: str, numero: str, complemento: str, CEP: str, cidade: str, UF: str):
        self.rua = rua.capitalize()
        self.numero = numero
        self.complemento = complemento.capitalize()
        self.CEP = Endereco.ajusta_cep(CEP)
        self.cidade = cidade.upper()
        self.UF = UF.upper()

    def __str__(self) -> str:
        info = ''
        info += 'Rua: ' + self.rua
        info += ', ' + self.numero
        info += ', ' + self.complemento
        info += '. ' + self.CEP
        info += '. ' + self.cidade
        info += '-' + self.UF
        return info
