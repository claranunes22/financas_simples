# Finanças Simples

**Finanças Simples** é Aplicativo de controle financeiro pessoal com interface em Python. Projeto da disciplina de Orientação a Objetos – UnB Gama.
---

## ✅ Casos de Uso

1. **Cadastrar nova transação (receita ou despesa)**
2. **Visualizar saldo atual**
3. **Editar informações de saldo e meta (autoatualização)**
4. **Visualizar lista de transações registradas**
5. **Visualizar gráfico de distribuição por categoria**
6. **Fechar o sistema com botão dedicado**

---

## 📦 Estrutura de Arquivos

```
financas_simples/
├── main.py
├── README.md
└── package/
    ├── __init__.py
    ├── transacao.py
    ├── receita.py
    ├── despesa.py
    ├── categoria.py
    ├── meta.py
    ├── relatorio.py
    ├── persistencia.py
    ├── interface.py
    └── grafico.py
```

---

## 🧠 Conceitos de POO Aplicados

- ✔ **Encapsulamento:** todas as classes com atributos e métodos organizados.
- ✔ **Herança:** `Receita` e `Despesa` herdam de `Transacao`.
- ✔ **Polimorfismo:** método `exibir_resumo()` se comporta de forma diferente em cada tipo de transação.
- ✔ **Mixin:** `PersistenciaMixin` implementa métodos reutilizáveis de serialização (ainda opcional de ser usado).
- ✔ **Composição:** `RelatorioFinanceiro` contém e manipula uma lista de `Transacao`.
- ✔ **Associação Fraca:** `Transacao` está associada à `Categoria` como texto livre.

---

## 💻 Tecnologias

- Python 3.10+
- Tkinter (interface gráfica)
- Matplotlib (gráficos)
- Programação Orientada a Objetos

---

## ▶️ Como Executar

1. Certifique-se de ter Python 3 instalado.
2. Instale a biblioteca `matplotlib` com o comando:

```
pip install matplotlib
```

3. Rode o sistema com:

```
python main.py
```

---

## 📈 Funcionalidades Visuais

- Interface com título, saldo e meta atual
- Botões para:
  - Adicionar Receita
  - Adicionar Despesa
  - Exibir Gráfico de Categoria
  - Fechar o app
- Lista visual com todas as transações registradas

---

## 📚 Autor

Clara dos Santos Oliveira Nunes  
Projeto Livre – Disciplina de Orientação a Objetos  
Faculdade UnB Gama – 2025

