class Conta():
    def __init__(self,saldo) -> None:
        self.saldo = saldo
        self.extrato_receitas = []
        self.extrato_despesas = []
        

    def __str__(self) -> str:
        return f'Saldo atual: {self.saldo}'

    def receita(self, receita):
        self.saldo += receita.valor
        self.extrato_receitas.append(({'Valor': receita.valor, 'Descrição': receita.descricao, 'Saldo': self.saldo}))

    def despesa(self, despesa):
        self.saldo -= despesa.valor
        self.extrato_despesas.append(({'SaldoAtual': self.saldo+despesa.valor,'Despesa': despesa.valor, 'Categoria': despesa.categoria,'Descrição': despesa.descricao, 'Saldo': self.saldo}))
    


    

