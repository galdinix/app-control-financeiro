from Utils import imprimirErro, verificarSeExisteReceita, verificarSeExisteDespesa

def adicionarConta(conta, app):
    if conta is None:
        conta = app.adicionarConta(conta)
        return conta
    imprimirErro('Se deseja aumentar saldo, selecione a opção [2]', 0.8)
  
def adicionarReceita(app, conta):
    if conta is None:
        imprimirErro('Conta não existe')
        return
    app.adicionarReceita(conta)
    
def adicionarDespesa(app, conta):
    if conta is None:
        imprimirErro('Conta não existe')
        return
    app.adicionarDespesa(conta)

def extratoReceitas(conta, app):
    if conta is None:
        imprimirErro('Conta não existe')
        return
    if verificarSeExisteReceita(conta):
        app.extratoReceitas(conta)
        return
    imprimirErro('Nenhuma receita encontrada!')

def extratoDespesas(conta, app):
    if conta is None:
        imprimirErro('Conta não existe')
        return
    if verificarSeExisteDespesa(conta):
        app.extratoDespesas(conta)
        return
    imprimirErro('Nenhuma Despesa encontrada!')

def extratoDespesaOrdenada(conta, app):
    if conta is None:
        imprimirErro('Conta não existe')
        return
    if verificarSeExisteDespesa(conta):
        app.extratoDespesaOrdenada(conta)
        return
    imprimirErro('Nenhuma Despesa encontrada!')


                
                
             