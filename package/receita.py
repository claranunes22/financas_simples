from package.transacao import Transacao

class Receita(Transacao):
    def exibir_resumo(self):
        return f"[RECEITA] {super().exibir_resumo()}"
