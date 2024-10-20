import os
from time import sleep
from Carrinho import Carrinho
from Catalogo import Catalogo

def menu():
    catalogo = Catalogo()
    while(True):
        catalogo.mostrarCatalogo()
        print(
            '''
1) Adicionar produto no carrinho de compras
2) Acessar carrinho de compras
3) Realizar pedido
4) Sair
            '''
            )
        
        try:
            opcao = int(input("Escolha uma opção: "))

            if opcao == 1:
                try:
                    indice = int(input("Digite o índice do produto: "))
                    if(indice < 0 or indice >= catalogo.qtde):
                        print("Índice inválido.")
                    else:
                        carrinho = Carrinho()
                        carrinho.adicionarProduto(catalogo.produtos[indice])
                except ValueError:
                    print("Índice inválido.")
                    

            elif opcao == 2:
                while(True):
                    try:
                        carrinho.mostrarCarrinho()
                        print(
                            '''
1) Remover um produto
2) Esvaziar carrinho de compras
3) Voltar
                            '''
                        )
                        try:
                            opcao2 = int(input("Escolha uma opção: "))

                            if opcao2 == 1:
                                try:
                                    indice = int(input("Digite o índice do produto: "))
                                    carrinho.removerProduto(indice)
                                except ValueError:
                                    print("Índice inválido.")

                            if opcao2 == 2:
                                carrinho.removerTudo()

                            if opcao2 == 3:
                                break

                            else:
                                print("Opção inválida.")
                        except ValueError:
                            print("Opção inválida.")
                    except NameError:
                        print("Carrinho vazio.")

            elif opcao == 3:
                carrinho.removerTudo
                print("Pedido realizado.")
            
            elif opcao == 4:
                print("Encerrando programa...")
                exit()

            else:
                print("Opção inválida.")
        except ValueError:
            print("Opção inválida.")

        sleep(2)
        if os.name == 'nt': # Limpa o terminal caso o OS seja Windows
            os.system('cls')
        else:
            os.system('clear') # Limpa o terminal caso o OS seja Linux ou MacOS

menu()