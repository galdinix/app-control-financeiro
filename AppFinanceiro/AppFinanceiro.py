from Conta import Conta
from Despesa import Despesa
from Receita import Receita
from Utils import receberValor, receberDescricao, receberDespesaEDescricao, receberCategoria, comparar_despesa

class AppFinanceiro:
    def adicionarConta(self, conta):
        saldo = receberValor('o saldo') #função presente em Utils
        conta = Conta(saldo)
        return conta
        
    def adicionarReceita(self, conta):
        valor_receita = receberValor('o valor da receita ') #função presente em Utils
        descricao_receita = receberDescricao('descrição da receita') #função presente em Utils
        receita = Receita(valor_receita, descricao_receita)
        conta.receita(receita)
        
    def adicionarDespesa(self, conta):
        valor_despesa, descricao = receberDespesaEDescricao()    
        categoria = receberCategoria() 
        if descricao == None:
            despesa = Despesa(float(valor_despesa), categoria)
        else:
            despesa = Despesa(float(valor_despesa), categoria, descricao)
        conta.despesa(despesa)

    def extratoReceitas(self, conta):
        for i in range(len(conta.extrato_receitas)):
            print(f'**********Receitas {i+1}**********')
            print(f"Valor da receita: R${conta.extrato_receitas[i]['Valor']}\nDescrição: {conta.extrato_receitas[i]['Descrição']}\nSaldo Final: {conta.extrato_receitas[i]['Saldo']}")
            print('*****************************')

    def extratoDespesas(self, conta):
        for i in range(len(conta.extrato_despesas)):
            print(f'**********Despesas {i+1}**********')
            print(f"Saldo inicial: R${conta.extrato_despesas[i]['SaldoAtual']}\nValor da despesa: R${conta.extrato_despesas[i]['Despesa']}\nCategoria: {conta.extrato_despesas[i]['Categoria']}\nDescrição: {conta.extrato_despesas[i]['Descrição']}\nSaldo final: R${conta.extrato_despesas[i]['Saldo']}")
            print('*****************************')
        
    def extratoDespesaOrdenada(self, conta):
        extrato_despesas_ordenado = sorted(conta.extrato_despesas, key=comparar_despesa)
        for i in range(len(extrato_despesas_ordenado)):
            print(f'**********{i+1}° Despesaa Ordenada por valor dos gastos por categoria**********')
            print(f"Saldo inicial: R${extrato_despesas_ordenado[i]['SaldoAtual']}\nValor da despesa: R${extrato_despesas_ordenado[i]['Despesa']}\nCategoria: {extrato_despesas_ordenado[i]['Categoria']}\nDescrição: {extrato_despesas_ordenado[i]['Descrição']}\nSaldo final: R${extrato_despesas_ordenado[i]['Saldo']}")
            print('*****************************')
