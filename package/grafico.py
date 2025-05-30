import matplotlib.pyplot as plt
from package.relatorio import RelatorioFinanceiro

def gerar_grafico_por_categoria(relatorio: RelatorioFinanceiro):
    dados = relatorio.agrupar_por_categoria()

    categorias = list(dados.keys())
    valores = [abs(v) for v in dados.values()]  # <-- correção: garantir valores positivos

    if not categorias or all(v == 0 for v in valores):
        print("Nenhum dado disponível para exibir o gráfico.")
        return

    plt.figure(figsize=(6, 6))
    plt.pie(valores, labels=categorias, autopct='%1.1f%%', startangle=90)
    plt.title('Distribuição por Categoria')
    plt.axis('equal')
    plt.tight_layout()
    plt.show()
