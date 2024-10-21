class Carrinho:

    def __init__(self):
        self.produtos = []
        self.qtde = 0
        self.custo = 0.0

    def mostrarCarrinho(self):
        print("Carrinho de compras:\n")
        if(self.qtde > 0):
            print("Indíce\tTítulo\tPreço")
            for i in range(self.qtde):
                nome = self.produtos[i].nome
                preco = self.produtos[i].preco
                print(f"{i}\t{nome}\t{preco:.2f}")
            print(f"\nTotal: {self.custo:.2f}")
        else:
            print("Carrinho vazio.")
    
    def adicionarProduto(self, produto):
        if produto not in self.produtos:
            self.produtos.append(produto)
            self.custo += produto.preco
            self.qtde += 1
            print("Produto adicionado.")
        else:
            print("Produto já está no carrinho.")
    
    def removerProduto(self, indice):
        if(indice >= self.qtde or indice < 0):
            print("Índice inválido.")
        else:
            preco_produto = self.produtos[indice].preco
            self.qtde -= 1
            self.custo -= preco_produto
            self.produtos.pop(indice)
            print("Produto removido.")

    def removerTudo(self):
        self.produtos = []
        self.qtde = 0
        self.custo = 0.0