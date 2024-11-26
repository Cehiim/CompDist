from servicos.tela import Tela
from servicos.controller import Controller

def menu():

    fim = False
    controller = Controller()

    while(fim == False):
        Tela.limpaTerminal()
        Tela.mostraMenu()
        choice = input("Selecione uma opção: ")

        try:
            choice = int(choice)
            if choice == 1: # Cria grafo
                controller.lerDados()

            elif choice == 2: # Grava dados no arquivo .txt
                controller.gravarDados()

            elif choice == 3: # Insere vértice
                controller.inserirVertice()

            elif choice == 4: # Insere aresta
                controller.inserirAresta()

            elif choice == 5: # Remove vértice
                controller.removerVertice()

            elif choice == 6: # Remove aresta
                controller.removerAresta()

            elif choice == 7: # Exibe grafo
                controller.exibirGrafo()

            elif choice == 8: # Exibe matriz
                controller.exibirMatriz()

            elif choice == 9: # Apresenta a conexidade do grafo
                controller.apresentarConexidade()

            elif choice == 10: # Encerra
                fim = True
                print("Encerrando programa...")

            elif choice == 11: # Busca um índice pela palavra
                controller.buscarIndice()

            elif choice == 12: # Busca uma palavra pelo índice
                controller.buscarPalavra()

            elif choice == 13: # Fazer busca vetorial de uma palavra
                controller.BuscaVetorial()

            elif choice == 14: # Exibir grafo colorido
                controller.grafoColorido()

            elif choice == 15: # Exibir árvore parcial de custo mínimo
                controller.ArvoreParcial()

            elif choice == 16: # Apresentar o caminho hamiltoniano
                controller.caminhoHamiltoniano()

            else:
                print("Opção inválida.")

        except ValueError:
            print("[Erro: a entrada não é do tipo int]")

menu()