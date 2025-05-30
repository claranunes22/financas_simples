from package.transacao import Transacao

class Despesa(Transacao):
    def exibir_resumo(self):
        return f"[DESPESA] {super().exibir_resumo()}"
