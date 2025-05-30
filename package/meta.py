class MetaFinanceira:
    def __init__(self, mes: str, valor_alvo: float):
        self.mes = mes  # formato: '2025-05'
        self.valor_alvo = valor_alvo
        self.valor_atual = 0.0

    def atualizar_valor_atual(self, saldo: float):
        self.valor_atual = saldo

    def calcular_progresso(self):
        if self.valor_alvo == 0:
            return 0.0
        return min((self.valor_atual / self.valor_alvo) * 100, 100.0)

    def exibir_meta(self):
        progresso = self.calcular_progresso()
        return f"Meta para {self.mes}: R$ {self.valor_alvo:.2f} - Progresso: {progresso:.2f}%"
