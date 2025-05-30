from package.transacao import Transacao
from package.receita import Receita
from package.despesa import Despesa
from collections import defaultdict

class RelatorioFinanceiro:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao: Transacao):
        self.transacoes.append(transacao)

    def gerar_saldo(self):
        saldo = 0
        for t in self.transacoes:
            if isinstance(t, Receita):
                saldo += t.valor
            elif isinstance(t, Despesa):
                saldo -= t.valor
        return saldo

    def listar_transacoes(self):
        return [t.exibir_resumo() for t in self.transacoes]

    def agrupar_por_categoria(self):
        categorias = defaultdict(float)
        for t in self.transacoes:
            if isinstance(t, Receita):
                categorias[t.categoria] += t.valor
            elif isinstance(t, Despesa):
                categorias[t.categoria] -= t.valor
        return dict(categorias)
