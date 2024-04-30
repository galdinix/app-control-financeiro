from Transacao import*

class Despesa(Transacao):
    def __init__(self, valor, categoria, descricao='Não informada'):
        super().__init__(valor, descricao)
        self.categoria = categoria

    def __str__(self) -> str:
        if self.descricao:
            return f'Valor: {self.valor}, Categoria: {self.categoria}, Descrição: {self.descricao}'
        return f'Valor: {self.valor}, Categoria: {self.categoria}'