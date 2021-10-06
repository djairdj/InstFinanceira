from Classes.Banco import Banco
from Interfaces.BancoUI import BancoUI

nome = input("Informe um nome pro banco: ")
bank = Banco(nome)
instFin = BancoUI(bank)
instFin.menu()
