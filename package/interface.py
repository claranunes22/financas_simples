import tkinter as tk
from tkinter import simpledialog, messagebox
from package.relatorio import RelatorioFinanceiro
from package.meta import MetaFinanceira
from package.receita import Receita
from package.despesa import Despesa
from package.grafico import gerar_grafico_por_categoria

relatorio = RelatorioFinanceiro()
meta = MetaFinanceira("2025-05", 1500)

# Dados de exemplo iniciais
relatorio.adicionar_transacao(Receita(3000, '2025-05-01', 'Salário', 'Salário do mês'))
relatorio.adicionar_transacao(Despesa(800, '2025-05-05', 'Aluguel', 'Pagamento do aluguel'))
relatorio.adicionar_transacao(Despesa(300, '2025-05-06', 'Supermercado', 'Compras do mês'))

def atualizar_interface(label_saldo, label_meta, lista_transacoes):
    saldo = relatorio.gerar_saldo()
    meta.atualizar_valor_atual(saldo)
    label_saldo.config(text=f"Saldo Atual: R$ {saldo:.2f}")
    label_meta.config(text=meta.exibir_meta())

    lista_transacoes.delete(0, tk.END)
    for resumo in relatorio.listar_transacoes():
        lista_transacoes.insert(tk.END, resumo)

def adicionar_receita(label_saldo, label_meta, lista_transacoes):
    valor = simpledialog.askfloat("Nova Receita", "Valor da receita:")
    if valor is not None:
        data = simpledialog.askstring("Nova Receita", "Data (AAAA-MM-DD):")
        categoria = simpledialog.askstring("Nova Receita", "Categoria:")
        descricao = simpledialog.askstring("Nova Receita", "Descrição:")
        if data and categoria and descricao:
            r = Receita(valor, data, categoria, descricao)
            relatorio.adicionar_transacao(r)
            atualizar_interface(label_saldo, label_meta, lista_transacoes)

def adicionar_despesa(label_saldo, label_meta, lista_transacoes):
    valor = simpledialog.askfloat("Nova Despesa", "Valor da despesa:")
    if valor is not None:
        data = simpledialog.askstring("Nova Despesa", "Data (AAAA-MM-DD):")
        categoria = simpledialog.askstring("Nova Despesa", "Categoria:")
        descricao = simpledialog.askstring("Nova Despesa", "Descrição:")
        if data and categoria and descricao:
            d = Despesa(valor, data, categoria, descricao)
            relatorio.adicionar_transacao(d)
            atualizar_interface(label_saldo, label_meta, lista_transacoes)

def iniciar_interface():
    janela = tk.Tk()
    janela.title("Finanças Simples")
    janela.geometry("550x500")
    janela.configure(bg="#f1f1f1")

    tk.Label(janela, text="Gestor Financeiro Pessoal", font=("Arial", 16, "bold"), bg="#f1f1f1").pack(pady=10)

    saldo = relatorio.gerar_saldo()
    meta.atualizar_valor_atual(saldo)

    label_saldo = tk.Label(janela, text=f"Saldo Atual: R$ {saldo:.2f}", font=("Arial", 14), fg="green", bg="#f1f1f1")
    label_saldo.pack(pady=5)

    label_meta = tk.Label(janela, text=meta.exibir_meta(), font=("Arial", 12), bg="#f1f1f1")
    label_meta.pack(pady=5)

    frame_botoes = tk.Frame(janela, bg="#f1f1f1")
    frame_botoes.pack(pady=10)

    tk.Button(frame_botoes, text="Adicionar Receita", command=lambda: adicionar_receita(label_saldo, label_meta, lista_transacoes)).grid(row=0, column=0, padx=5)
    tk.Button(frame_botoes, text="Adicionar Despesa", command=lambda: adicionar_despesa(label_saldo, label_meta, lista_transacoes)).grid(row=0, column=1, padx=5)
    tk.Button(frame_botoes, text="Exibir Gráfico", command=lambda: gerar_grafico_por_categoria(relatorio)).grid(row=0, column=2, padx=5)

    # Lista visual de transações
    tk.Label(janela, text="Transações Registradas:", font=("Arial", 12, "bold"), bg="#f1f1f1").pack(pady=5)
    lista_transacoes = tk.Listbox(janela, width=75, height=10)
    lista_transacoes.pack()

    atualizar_interface(label_saldo, label_meta, lista_transacoes)

    tk.Button(janela, text="Fechar", command=janela.destroy).pack(pady=10)

    janela.mainloop()
