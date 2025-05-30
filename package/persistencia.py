import pickle

class PersistenciaMixin:
    def salvar_em_arquivo(self, dados, nome_arquivo):
        with open(nome_arquivo, 'wb') as f:
            pickle.dump(dados, f)

    def carregar_de_arquivo(self, nome_arquivo):
        try:
            with open(nome_arquivo, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            return []
