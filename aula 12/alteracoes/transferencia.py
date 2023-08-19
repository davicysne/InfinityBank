from banco import obterConta

def transferir(contaOri: int, contaDes:int, valor:float) -> None:
    contaOrigem = obterConta(contaOri)
    contaDestino = obterConta(contaDes)
    if contaOrigem and contaDestino:
        if contaOrigem['saldo'] >= valor:
            contaDestino['saldo'] += valor
            contaOrigem['saldo'] -= valor
            print("Trasnferencia realizada com sucesso!")
        else:
            print("Saldo insuficiente para transferencia")
    else:
        print("Uma das contas não existem")

transferir(1,3,100)