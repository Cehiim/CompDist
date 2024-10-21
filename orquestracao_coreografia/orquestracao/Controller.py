from Carrinho import Carrinho
from Catalogo import Catalogo
from time import sleep
import os

class Controller:
    def __init__(self):
        self.catalogo = Catalogo()
        self.carrinho = Carrinho()

    def mostrarCatalogo(self):
        self.catalogo.mostrarCatalogo()

    def adicionarProduto(self):
        try:
            indice = int(input("Digite o índice do produto: "))
            if(indice < 0 or indice >= self.catalogo.qtde):
                print("Índice inválido.")
            else:
                self.carrinho.adicionarProduto(self.catalogo.produtos[indice])
        except ValueError:
            print("Índice inválido.")

    def acessarCarrinho(self):
        while(True):
            try:
                self.carrinho.mostrarCarrinho()
                print(
                    '''
    1) Remover um produto
    2) Esvaziar carrinho de compras
    3) Realizar pedido
    4) Voltar ao catálogo
                    '''
                    )
                try:
                    opcao2 = int(input("Escolha uma opção: "))

                    if opcao2 == 1:
                        try:
                            indice = int(input("Digite o índice do produto: "))
                            self.carrinho.removerProduto(indice)
                        except ValueError:
                            print("Índice inválido.")

                    elif opcao2 == 2:
                        self.carrinho.removerTudo()

                    elif opcao2 == 3:
                        # Lógica de pagamento...
                        # Lógica de notificação...
                        print("Realizando pagamento...")
                        sleep(4)
                        self.carrinho.removerTudo()
                        print("Pedido realizado.")

                    elif opcao2 == 4:
                        break

                    else:
                        print("Opção inválida.")
                except ValueError:
                    print("Opção inválida.")

            except NameError:
                print("Carrinho vazio.")
            sleep(1)
            if os.name == 'nt': # Limpa o terminal caso o OS seja Windows
                os.system('cls')
            else:
                os.system('clear') # Limpa o terminal caso o OS seja Linux ou MacOS"