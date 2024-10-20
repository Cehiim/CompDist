class Produto:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    @property # Getter para nome
    def nome(self):
        return self._nome

    @nome.setter # Setter para nome
    def nome(self, valor):
        if isinstance(valor, str) and valor.strip():
            self._nome = valor
        else:
            raise ValueError("O nome deve ser uma string não vazia.")

    @property # Getter para preço
    def preco(self):
        return self._preco

    @preco.setter # Setter para preço
    def preco(self, valor):
        if valor >= 0:
            self._preco = valor
        else:
            raise ValueError("O preço deve ser maior ou igual a zero.")