import time
from Validations import*

def receberValor(acao):
    while True:
        try:
            saldo = float(input(f'Informe {acao}: '))
            if isSaldoValid(saldo):
                return saldo
            imprimirErro('Erro, tente novamente')
        except ValueError:
            imprimirErro('Erro, insira um número')

def imprimirErro(acao='carregando', tempo = 0.3):
    for i in range(5):  # Define a quantidade de pontos
        print(acao, '.' * i, end='\r')  # Imprime os pontos
        time.sleep(tempo)

def receberDescricao(acao):
     while True:
        try:
            descricao = input(f'Informe {acao}: ')
            return descricao
        except Exception:
            imprimirErro('Erro, insira um número')

def receberCategoria():
    while True:
        try:
            categoria = input('Informe a categoria da despesa (alimentação, transporte, lazer, contas): ').lower().strip() 
            if isCategoriaValid(categoria):
                return categoria
            imprimirErro('Informe uma categoria válida!')
        except Exception:
            imprimirErro('erro ao procesar, tente novamente!')

def receberDespesaEDescricao():
    while True:
        try:
            despesa = input('Informe o valor da despesa e, opcionalmente, uma descrição separada por ; do valor: ')
            if despesaPossuiDescricao(despesa):
                valor_despesa, descricao = separarDespesaDaDescricao(despesa)
                if isValorDespesaValid(valor_despesa):
                    return valor_despesa, descricao
                imprimirErro('Informe um número > 0')
            else:
                if isValorDespesaValid(despesa):
                    return despesa, None
        except Exception as e:
            imprimirErro('Erro ao processar: ' + str(e))

def despesaPossuiDescricao(despesa):
    lista_despesa = despesa.split(';')
    return len(lista_despesa) > 1

def separarDespesaDaDescricao(despesa):
    string_despesa = despesa.split('; ')
    valor_despesa = string_despesa[0]
    descricao = string_despesa[1]
    return valor_despesa, descricao
    
def comparar_despesa(item):
    return (item['Categoria'], item['Despesa'])

def receberOpcMenu():
    while True:
        try:
            opc = int(input('Informe a opção: '))
            if isOpcValid(opc):
                return opc
        except ValueError:
            imprimirErro('Erro, informe um inteiro')

def verificarSeContaExiste(conta):
    if conta:
        return True
    False

def verificarSeExisteReceita(conta):
    if len(conta.extrato_receitas) == 0:
        return False
    return True

def verificarSeExisteDespesa(conta):
    if len(conta.extrato_despesas) == 0:
        return False
    return True

