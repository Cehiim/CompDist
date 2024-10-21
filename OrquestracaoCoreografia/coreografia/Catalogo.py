from Produto import Produto
import csv

class Catalogo:
    def __init__(self):
        self.produtos = []
        self.qtde = 0
        with open("games.csv", "r", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)
            next(leitor)  # Pular o cabeçalho
            for linha in leitor:
                nome, preco = linha
                try:
                    preco = float(preco)
                except ValueError:
                    print(f"Erro ao converter o preço '{preco}' para float.")
                    continue
                produto = Produto(nome, preco)
                self.produtos.append(produto)
                self.qtde += 1
    
    def mostrarCatalogo(self):
        print("Catálogo:\n")
        if(self.qtde > 0):
            print("Indíce\tTítulo\tPreço")
            for i in range(self.qtde):
                nome = self.produtos[i].nome
                preco = self.produtos[i].preco
                print(f"{i}\t{nome}\t{preco:.2f}")
        else:
            print("Catálogo vazio.")