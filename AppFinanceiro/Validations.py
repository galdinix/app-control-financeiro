def isSaldoValid(saldo):
    return saldo >= 0

def isCategoriaValid(categoria):
    categorias_validas = ['alimentação', 'transporte', 'lazer', 'contas']
    return categoria in categorias_validas

def isValorDespesaValid(valor_despesa):
    if valor_despesa.isdigit() and float(valor_despesa) > 0:
        return True
    return False
    
def isOpcValid(opc):
    if opc >= 0 and opc <= 6:
        return True
    return False



