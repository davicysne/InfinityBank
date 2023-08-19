from banco import *
from alteracoes.deposito import depositar
from alteracoes.consulta import consultarSaldo
from alteracoes.saque import sacar
from alteracoes.transferencia import transferir

def menu():
    while True:
        print("---- Sistema Bancário ----")
        print("1 - Adicionar Conta")
        print("2 - Editar Conta")
        print("3 - Consultar Conta")
        print("4 - Apagar Conta")
        print("5 - Listar Contas")
        print("6 - Atualizar Nome")
        print("7 - Atualizar Saldo")
        print("8 - Realizar Saque")
        print("9 - Realizar Depósito")
        print("10 - Consultar Saldo")
        print("11 - Transferencia")
        print("12 - Sair")
        opcao = input("Selecione uma opção: ")
