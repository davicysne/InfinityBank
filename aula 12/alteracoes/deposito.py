from banco import banco, obterConta

def depositar(conta:int, valor:float) -> bool:
    cliente = obterConta(conta)
    if cliente:
        cliente['saldo'] += valor
        print("Depósito realizado com sucesso!")
    else: 
        print("Cliente não encontrado")

depositar(1,500)
print(banco)