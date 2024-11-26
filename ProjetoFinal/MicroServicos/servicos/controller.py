from servicos.codificador import Codificador
from servicos.grafo import Grafo
from servicos.leitor import Leitor
from servicos.tela import Tela
from servicos.utilitarios import Utilitarios
import time

class Controller:
    def __init__(self):
        self.n_palavras = -1
        self.palavras = []
        self.embeddings = []
        self.codificador = Codificador()
        self.grafo = set()

    def lerDados(self):
        #dados = Leitor.leArquivoHTTP("https://raw.githubusercontent.com/Cehiim/TeoriaDosGrafos/refs/heads/main/ProjetoFinal/teste.txt")
        dados = Leitor.leArquivo("teste.txt")

        if(dados == []):
            print("[Erro: Não foi possível ler o arquivo]")

        else:
            self.n_palavras = dados[0] # Número de palavras
            self.palavras = dados[1] # Lista de palavras
            self.embeddings = self.codificador.geraEmbeddings(self.palavras) # Lista dos embeddings das palavras
            self.grafo = Grafo(self.n_palavras)
            n_vizinhos = 4 # Número desejado + 1, pois considera a própria palavra como o vizinho mais próximo

            for i in range(self.n_palavras):
                busca = self.codificador.buscaVetorial(self.embeddings, n_vizinhos, self.palavras[i])

                for j in range(1, n_vizinhos):
                    vizinho = busca[0][j]["corpus_id"]
                    peso = busca[0][j]["score"]
                    self.grafo.insereA(i, vizinho, peso)

            print("Grafo criado com sucesso")
        time.sleep(1)

    def gravarDados(self):
        if(self.n_palavras != -1):
            Leitor.gravaDados(self.n_palavras, self.palavras)
            print("Os dados foram salvos no arquivo 'grafo.txt'")
        else:
            print("[Erro: Grafo não criado]")
        time.sleep(1)

    def inserirVertice(self):
        if(self.n_palavras != -1):
            palavra = input("Palavra a ser inserida: ")

            if(Utilitarios.buscaIndice(self.n_palavras, self.palavras, palavra) == -1):
                self.grafo.insereV()
                self.palavras.append(palavra)
                self.n_palavras += 1
                print("Vértice inserido com sucesso")
            else:
                print("[Erro: palavra já existe]")

        else:
            print("[Erro: Grafo não criado]")
        time.sleep(1)

    def inserirAresta(self):
        if(self.n_palavras != -1):
            try:
                origem = int(input("Insira o índice de origem: "))
                destino = int(input("Insira o índice de destino: "))
                peso = float(input("Insira o peso: "))

                if(origem >= self.n_palavras or origem < 0):
                    print("[Erro: origem não existe]")

                elif(destino >= self.n_palavras or destino < 0):
                    print("[Erro: destino não existe]")

                else:
                    self.grafo.insereA(origem, destino, peso)
                    print("Aresta inserida com sucesso")

            except ValueError:
                print("[Erro: a entrada não é do tipo int]")
        else:
            print("[Erro: Grafo não criado]")
        time.sleep(1)

    def removerArestaAux(self, origem, destino): # Função auxiliar
        if(origem >= self.n_palavras or origem < 0):
            return False
        elif(destino >= self.n_palavras or destino < 0):
            return False
        else:
            self.grafo.removeA(origem, destino)
            return True

    def removerAresta(self):
        if(self.n_palavras != -1):
            try:
                origem = int(input("Insira o índice de origem: "))
                destino = int(input("Insira o índice de destino: "))
                
                if(self.removerArestaAux(origem, destino)):
                    print("Aresta removida com sucesso")
                else:
                    print("[Erro: vértice não existe]")

            except ValueError:
                print("[Erro: a entrada não é do tipo int]")
        else:
            print("[Erro: Grafo não criado]")
        time.sleep(1)

    def removerVertice(self):
        try:
            if(self.n_palavras != -1):
                removido = int(input("Insira o índice do vértice: "))

                if(removido >= self.n_palavras or removido < 0):
                    print("[Erro: vértice não existe]")

                else:
                    for i in range(self.n_palavras - 1):
                        if(i >= removido):
                            self.palavras[i] = self.palavras[i+1]

                        if(self.grafo.adj[i][removido] != 0):
                            origem = i
                            destino = removido
                            self.removerArestaAux(origem, destino)

                    self.grafo.removeV(removido)
                    self.palavras.pop()
                    self.n_palavras -= 1
                    print("Vértice removido com sucesso!")
                
            else:
                print("[Erro: Grafo não criado]")

        except ValueError:
            print("[Erro: a entrada não é do tipo int]")
        time.sleep(1)

    def exibirGrafo(self):
        if(self.n_palavras != -1):
            Tela.imprimeGrafo(self.n_palavras, self.palavras, self.grafo)
            print(f"\nGrafo não-direcionado rotulado com {self.grafo.n} vértices e {self.grafo.m} arestas\n")
            print("O grafo visual foi criado no arquivo 'grafo.html'.")
        else:
            print("[Erro: Grafo não criado]")
        time.sleep(3)

    def exibirMatriz(self):
        if(self.n_palavras != -1):
            self.grafo.showMin()
            print(("\nAperte ENTER para continuar "))
            ok = input()
        else:
            print("[Erro: Grafo não criado]")

    def apresentarConexidade(self):
        if(self.n_palavras != -1):
            if(self.grafo.conexidade()):
                print("O grafo é conexo.")
            else:
                print("O grafo não é conexo.")
            print(("\nAperte ENTER para continuar "))
            ok = input()
        else:
            print("[Erro: Grafo não criado]")
        time.sleep(1)

    def buscarIndice(self):
        if(self.n_palavras != -1):
            palavra = input("Palavra a ser consultada: ")
            indice = Utilitarios.buscaIndice(self.n_palavras, self.palavras, palavra)
            if(indice == -1):
                print("[Erro: palavra não encontrada]")
            else:
                print(f"Índice de {palavra}: {indice}")
                print(("\nAperte ENTER para continuar "))
                ok = input()
        else:
            print("[Erro: Grafo não criado]")
        time.sleep(1)

    def buscarPalavra(self):
        if(self.n_palavras != -1):
            try:
                indice = int(input("Índice a ser consultado: "))
                palavra = Utilitarios.buscaPalavra(self.n_palavras, self.palavras, indice)
                if(palavra == "erro"):
                    print("[Erro: palavra não encontrada]")
                else:
                    print(f"Palavra do índice {indice}: {palavra}")
                    print(("\nAperte ENTER para continuar "))
                    ok = input()
            except ValueError:
                print("[Erro: a entrada não é do tipo int]")
        else:
            print("[Erro: Grafo não criado]")
        time.sleep(1)

    def BuscaVetorial(self):
        if(self.n_palavras != -1):
            busca = input("Insira uma palavra: ")
            n_buscas = int(input("Insira o número de buscas: "))
            resultado = self.codificador.buscaVetorial(self.embeddings, n_buscas, busca)

            print("\nPalavra consultada: ", busca)
            for i in range(n_buscas):
                id_vizinho = resultado[0][i]["corpus_id"]
                peso = resultado[0][i]["score"]
                print(f"{self.palavras[id_vizinho]} - {peso:.2f}")

            print(("\nAperte ENTER para continuar "))
            ok = input()
        else:
            print("[Erro: Grafo não criado]")

    def grafoColorido(self):
        if(self.n_palavras != -1):
            lista_colorida = self.grafo.coloreV()
            n_cores = lista_colorida[0]
            cores = lista_colorida[1]
            Tela.imprimeGrafoColorido(self.n_palavras, self.palavras, self.grafo, n_cores, cores)
            print(f"\nGrafo não-direcionado rotulado com {self.grafo.n} vértices, {self.grafo.m} arestas e {n_cores} cores\n")
            print("O grafo visual foi criado no arquivo 'grafo_colorido.html'.")
        else:
            print("[Erro: Grafo não criado]")
        time.sleep(3)

    def ArvoreParcial(self):
        if(self.n_palavras != -1):
            Tela.imprimeAPCM(self.n_palavras, self.palavras, self.grafo)
            print("O grafo visual foi criado no arquivo 'apcm.html'.")
        else:
            print("[Erro: Grafo não criado]")
        time.sleep(3)
        
    def caminhoHamiltoniano(self):
        if(self.n_palavras != -1):
            Tela.imprimeCaminhoHamiltoniano(self.grafo, self.n_palavras, self.palavras)
            print("O grafo visual foi criado no arquivo 'caminho_hamiltoniano.html'.")
        else:
            print("[Erro: Grafo não criado]")
        time.sleep(3)