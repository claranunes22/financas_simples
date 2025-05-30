class Transacao:
    def __init__(self, valor, data, categoria, descricao):
        self.valor = valor
        self.data = data
        self.categoria = categoria
        self.descricao = descricao

    def exibir_resumo(self):
        return f"{self.data} - {self.descricao}: R$ {self.valor:.2f} ({self.categoria})"
