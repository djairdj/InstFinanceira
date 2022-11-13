from Interfaces.BancoUI import BancoUI
from Classes.Banco import Banco

nome = input("Informe um nome pro banco: ")
bank = Banco(nome)
instFin = BancoUI(bank)
instFin.menu()
