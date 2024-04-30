class Transacao:
    def __init__(self, valor, descricao=None):
        self.valor = valor
        self.descricao = descricao

    def __str__(self) -> str:
            return f'Valor: {self.valor}, Descrição: {self.descricao}'
        