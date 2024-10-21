import os
from time import sleep
from Controller import Controller

def menu():
    controller = Controller()
    while(True):
        controller.mostrarCatalogo()
        print(
            '''
1) Adicionar produto no carrinho de compras
2) Acessar carrinho de compras
3) Sair do programa
            '''
            )
        
        try:
            opcao = int(input("Escolha uma opção: "))

            if opcao == 1:
                controller.adicionarProduto()
                    
            elif opcao == 2:
                controller.acessarCarrinho()
            
            elif opcao == 3:
                print("Encerrando programa...")
                break

            else:
                print("Opção inválida.")
        except ValueError:
            print("Opção inválida.")

        sleep(1)
        if os.name == 'nt': # Limpa o terminal caso o OS seja Windows
            os.system('cls')
        else:
            os.system('clear') # Limpa o terminal caso o OS seja Linux ou MacOS

menu()