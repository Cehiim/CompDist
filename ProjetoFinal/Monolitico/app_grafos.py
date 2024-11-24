# -*- coding: utf-8 -*-
"""ProjetoFinal.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/github/Cehiim/TeoriaDosGrafos/blob/main/ProjetoFinal/ProjetoFinal.ipynb

# Informações gerais

## Tema
* Aplicação com busca semântica para representação de grafos.

## Integrantes
* Cesar Hideki Imai - 10402758.
* João Victor Dallapé Madeira - 10400725.
* David Varão Lima Bentes Pessoa - 10402647.
* André Franco Ranieri - 10390470.

# Setup

## Integração dos pacotes
"""

# Commented out IPython magic to ensure Python compatibility.
# %pip install sentence-transformers
# %pip install requests
# %pip install networkx pyvis

"""## Importação das bibliotecas"""

from sentence_transformers import SentenceTransformer, util
import requests
from pyvis.network import Network
import time
#from ipywidgets import widgets
#from IPython.display import display, clear_output
import os

"""## Importação do modelo codificador"""

nome = "neuralmind/bert-large-portuguese-cased" # Modelo BERTimbau
modelo = SentenceTransformer(nome)

"""## Definição da classe do grafo não-direcionado rotulado"""

# Grafo como uma matriz de adjacência não-direcionado rotulado
class GrafoNDR(): # Ex 8
    TAM_MAX_DEFAULT = 100 # qtde de vértices máxima default
    # construtor da classe grafo
    def __init__(self, n=TAM_MAX_DEFAULT):
        self.n = n # número de vértices
        self.m = 0 # número de arestas
        # matriz de adjacência
        self.adj = [[0 for i in range(n)] for j in range(n)]

    def insereA(self, v, w, p):
        if(v == w or self.adj[v][w] != 0):
            return

        else:
            self.adj[v][w] = p
            self.adj[w][v] = p
            self.m += 1  # atualiza qtd arestas

# remove uma aresta v->w do Grafo
    def removeA(self, v, w):
        if(v == w or self.adj[v][w] == 0):
            return
        # testa se temos a aresta
        else:
            self.adj[v][w] = 0
            self.adj[w][v] = 0
            self.m -= 1  # atualiza qtd arestas

    def show(self):
        print(f"\n n: {self.n:2d} ", end="")
        print(f"m: {self.m:2d}\n")
        for i in range(self.n):
            for w in range(self.n):
                print(f"Adj[{i:2d},{w:2d}] = {self.adj[i][w]:.2f} ", end="")
            print("\n")
        print("\nfim da impressao do grafo." )


	# Apresenta o Grafo contendo
	# número de vértices, arestas
	# e a matriz de adjacência obtida
    # Apresentando apenas os valores 0 ou 1
    def showMin(self):
        print(f"\n n: {self.n:2d} ", end="")
        print(f"m: {self.m:2d}\n")
        for i in range(self.n):
            for w in range(self.n):
                print(f" {self.adj[i][w]:.2f} ", end="")
            print("\n")
        print("\nfim da impressao do grafo." )

    def insereV(self):
        for i in range(self.n):
            self.adj[i].append(0)
        self.n += 1
        self.adj.append([0]*self.n)

    def removeV(self, vertice):
        if(vertice >= self.n or vertice < 0):
            return False

        for i in range(self.n - 1):
            if(i >= vertice and i != self.n-1): # Substitui as conexões do vértice a ser retirado e
                self.adj[i] = self.adj[i+1]     # os vértices posteriores a ele com as conexões do próximo vértice

            self.removeA(i,vertice)
            self.adj[i].pop(vertice) # Remove o vértice escolhido da linha da matriz
        self.adj.pop() # Remove a última linha da matriz
        self.n -= 1
        return True

    def dfs(self, visitados, vertice): # Depth First Search
        visitados[vertice] = True
        for i in range(self.n):
            if(self.adj[vertice][i] != 0 and visitados[i] == False): # Caso haja acesso para um próximo vértice que não foi visitado
                self.dfs(visitados, i)

    def conexidade(self):
        for i in range(self.n):
            visitados = [False] * self.n
            self.dfs(visitados, i)
            if(all(visitados)): # Caso todos tenham sido visitados
                return "O grafo é conexo"
        return "O grafo não é conexo"

    def EhAdjacente(self, v, x): #verifica se o vértice v é adjacente a x
        if self.adj[v][x] != 0:
            return True
        else:
            return False

    def coloreV(self):
        lista_colorida = self.n * [0]
        n_cores = 0
        for i in range(self.n):
            other_colors = []
            for j in range(self.n):
                if self.EhAdjacente(i, j) and lista_colorida[j] != 0:
                    other_colors.append(lista_colorida[j])

            if other_colors == []:
                lista_colorida[i] = 1

            elif other_colors != []:
                for k in range(1, self.n):
                    if k not in other_colors:
                        if(k > n_cores):
                            n_cores = k

                        lista_colorida[i] = k
                        break

        info = [n_cores,lista_colorida]

        return info

    def _find(self, parent, i):
        if parent[i] == i:
            return i
        return self._find(parent, parent[i])

    # Função para unir dois subconjuntos no Union-Find
    def _union(self, parent, rank, x, y):
        root_x = self._find(parent, x)
        root_y = self._find(parent, y)

        # Anexar a árvore de menor rank sob a árvore de maior rank
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    # Implementação do Algoritmo de Kruskal
    def kruskal(self):
        arestas = [] #Obtém as arestas do grafo
        for i in range(self.n):
            for j in range(i, self.n):
                if self.adj[i][j] > 0:
                    aresta = (i, j, self.adj[i][j])
                    arestas.append(aresta)

        # Ordenar as arestas por peso
        arestas.sort(key=lambda x: x[2])

        # Inicializar a estrutura Union-Find
        parent = []
        rank = []

        for node in range(self.n):
            parent.append(node)
            rank.append(0)

        # Lista para armazenar a árvore geradora mínima (MST)
        arvore_parcial = []

        # Número de arestas na MST
        e = 0
        i = 0

        # Iterar pelas arestas em ordem de peso
        while e < self.n - 1 and i < len(arestas):
            # Escolher a menor aresta
            u, v, peso = arestas[i]
            i += 1

            # Encontrar os representantes (subconjuntos) dos vértices u e v
            x = self._find(parent, u)
            y = self._find(parent, v)

            # Se u e v não pertencem ao mesmo subconjunto, adicionar a aresta à MST
            if x != y:
                e += 1
                arvore_parcial.append([u, v, peso])
                self._union(parent, rank, x, y)

        for i in range(len(arvore_parcial)): #Ajusta índice dos vértices
            arvore_parcial[i][0] += 1
            arvore_parcial[i][1] += 1

        return arvore_parcial

"""# Métodos

## Funções auxiliares

### Busca índice

Busca um índice através da palavra dentro da lista de vértices.
"""

def buscaIndice(n_palavras, vertices, palavra):
  for i in range(n_palavras):
    if(vertices[i] == palavra):
      return i
  return -1

"""### Busca palavra

Busca uma palavra através do índice dentro da lista de vértices.
"""

def buscaPalavra(n_palavras, vertices, indice):
  if(indice >= n_palavras or indice < 0):
    return "[Erro: índice inválido]"
  for i in range(n_palavras):
    if(i == indice):
      return vertices[i]
  return "[Erro: índice não encontrado]"

"""### Busca vetorial"""

def buscaVetorial(modelo, embeddings, vertices, busca):
  consulta_embedding = modelo.encode(busca)
  resultado = util.semantic_search(consulta_embedding, embeddings, top_k=3)
  print(f"\n\nBusca: {busca}\n")
  for i in range(3):
      id = resultado[0][i]["corpus_id"] # Índice do vizinho
      score = resultado[0][i]["score"] # Peso do vizinho
      palavra = vertices[id]
      print(f"Palavra: {palavra}\nPeso: {score:.2f}\n")

"""## Arquivo

### Lê arquivo

Os dados do documento são importados e guardados na variável `dados`.
"""

def leArquivoHTTP(url):
  try:
    arquivo = requests.get(url).text

    lista = arquivo.split() # Distribui cada elemento do arquivo numa lista
    n_palavras = int(lista.pop(0)) # Separa o número de palavras (primeira linha do arquivo)
    vertices = []
    for i in range(n_palavras):
      vertice = lista[i]
      vertices.append(vertice)

    dados = [n_palavras]
    dados.append(vertices)

    return dados

  except requests.exceptions.RequestException:
    print("[Erro: URL não encontrada]")

def leArquivo(origem):
  try:
    with open(origem, 'r', encoding='utf-8') as arquivo:
      n_palavras = int(arquivo.readline()) # Recupera o número de palavras (primeira linha do arquivo)

      vertices = []
      for i in range(n_palavras):
        vertice = arquivo.readline().strip()
        vertices.append(vertice)

    dados = [n_palavras]
    dados.append(vertices)

    return dados

  except FileNotFoundError:
    print("[Erro: Arquivo não encontrado]")

"""### Grava dados"""

def gravaDados(n_palavras, vertices):
  with open("grafo.txt", "w") as arquivo:
    for i in range(n_palavras):
      palavra = vertices[i]
      arquivo.write(palavra+"\n")

  print("Os dados foram salvos no arquivo 'grafo.txt'.")

"""## Grafo

### Insere vértice
"""

def insereVertice(grafo, n_palavras, vertices, palavra):
  if(buscaIndice(n_palavras, vertices, palavra) == -1):
    grafo.insereV()
    vertices.append(palavra)
    return True
  else:
    #print("[Erro: palavra já existe]")
    return False

"""### Insere aresta"""

def insereAresta(grafo, n_palavras, origem, destino, peso):
  if(origem >= n_palavras or origem < 0):
    #print("[Erro: origem não existe]")
    return False

  elif(destino >= n_palavras or destino < 0):
    #print("[Erro: destino não existe]")
    return False

  else:
    grafo.insereA(origem, destino, peso)
    return True

"""### Integra grafo

A palavra mais próxima armazenada na memória é ela mesma, portanto para encontrar as outras três palavras mais próximas foram recuperadas as palavras de índice 1 até 4.
"""

def integraGrafo(modelo, embeddings, n_palavras, vertices):
  grafo = GrafoNDR(n_palavras) # Cria o grafo

  for i in range(n_palavras):
    consulta_embedding = modelo.encode(vertices[i])
    busca = util.semantic_search(consulta_embedding, embeddings, top_k=4)

    for j in range(1,4):
      vizinho = busca[0][j]["corpus_id"]
      peso = busca[0][j]["score"]
      grafo.insereA(i, vizinho, peso)

  print("Grafo criado com sucesso!")
  return grafo

"""### Remove aresta"""

def removeAresta(grafo, n_palavras, origem, destino):
  if(origem >= n_palavras or origem < 0):
    #print("[Erro: origem não existe]")
    return False

  elif(destino >= n_palavras or destino < 0):
    #print("[Erro: destino não existe]")
    return False

  else:
      grafo.removeA(origem, destino)
      return True

"""### Remove vértice"""

def removeVertice(grafo, n_palavras, vertices, removido):
  if(removido >= n_palavras or removido < 0):
    #print("[Erro: vértice não existe]")
    return False

  else:
    for i in range(n_palavras - 1):
      if(i >= removido):
        vertices[i] = vertices[i+1]

      if(grafo.adj[i][removido] != 0):
        origem = i
        destino = removido
        removeAresta(grafo, n_palavras, origem, destino)

    grafo.removeV(removido)
    vertices.pop()
    return True

"""## Network

### Imprime vértices
"""

def imprimeVertices(network, n_palavras, vertices):
  for i in range(n_palavras):
    network.add_node( # Adiciona vértices
        i, # Índice
        label=vertices[i], # Descrição do vértice
        color="yellow"
    )

"""### Imprime arestas"""

def imprimeArestas(network, n_palavras, vertices, grafo):
  for i in range(n_palavras):
    for j in range(n_palavras):
      peso = grafo.adj[i][j]

      if(peso != 0):
        network.add_edge( # Adiciona as arestas
            i, # Origem
            j, # Destino
            value=peso, # Peso
            title=f'''
            {vertices[i]}
            {vertices[j]}
            Peso: {peso:.2f}
                          ''', # Descrição
            color="gray"
        )

"""### Imprime grafo"""

def imprimeGrafo(n_palavras, vertices, grafo):
  net = Network(notebook=True, cdn_resources='remote', directed=False, height="1200px", width="100%", bgcolor="black", font_color="white")
  imprimeVertices(net, n_palavras, vertices)
  imprimeArestas(net, n_palavras, vertices, grafo)

  net.barnes_hut() # Dispersa melhor os vértices
  net.show("grafo.html") # Salva o grafo

  print(f"\nGrafo não-direcionado rotulado com {grafo.n} vértices e {grafo.m} arestas\n")
  print("O grafo visual foi criado no arquivo 'grafo.html'.")

"""### Imprime vértices coloridos"""

def imprimeVerticesColoridos(network, n_palavras, vertices, cores, grupos):
  for i in range(n_palavras):
    num = grupos[i]
    network.add_node( # Adiciona vértices
        i, # Índice
        label=vertices[i], # Descrição do vértice
        color=cores[num - 1]
    )

"""### Imprime grafo colorido"""

def imprimeGrafoColorido(n_palavras, vertices, grafo, n_grupos, grupos):
  cores = [
      "blue",
      "green",
      "yellow",
      "red",
      "purple",
      "coral",
      "turquoise",
      "magenta",
      "caramel",
      "beige",
  ]
  n_cores = 10

  if(n_grupos > n_cores):
    print("[Erro: Não é possível exibir um grafo com mais de 10 cores]")

  else:
    net = Network(notebook=True, cdn_resources='remote', directed=False, height="1200px", width="100%", bgcolor="black", font_color="white")
    imprimeVerticesColoridos(net, n_palavras, vertices, cores, grupos)
    imprimeArestas(net, n_palavras, vertices, grafo)
    net.barnes_hut() # Dispersa melhor os vértices
    net.show("grafo_colorido.html") # Salva o grafo

    print(f"\nGrafo não-direcionado rotulado com {grafo.n} vértices, {grafo.m} arestas e {n_grupos} cores\n")
    print("O grafo visual foi criado no arquivo 'grafo_colorido.html'.")

"""### Imprime APCM (Árvore Parcial de Custo Mínimo)"""

def imprimeAPCM(n_palavras, vertices, grafo):
    net = Network(notebook=True, cdn_resources='remote', directed=False, height="1200px", width="100%", bgcolor="black", font_color="white")
    imprimeVertices(net, n_palavras, vertices)

    arvore_parcial = grafo.kruskal()
    #print("Árvore Parcial de Custo mínimo gerada:")
    for i in range(len(arvore_parcial)):
        indice1 = arvore_parcial[i][0] - 1
        indice2 = arvore_parcial[i][1] - 1
        vertice1 = vertices[indice1]
        vertice2 = vertices[indice2]
        #print(f"[{indice1}, {indice2}] --> [{vertice1}, {vertice2}]")

        peso = grafo.adj[indice1][indice2]

        net.add_edge( # Adiciona a aresta
            indice1, # Origem
            indice2, # Destino
            value=peso, # Peso
            title=f'''
            {vertice1}
            {vertice2}
            Peso: {peso:.2f}
                          ''', # Descrição
            color="gray"
        )

    net.barnes_hut() # Dispersa melhor os vértices
    net.show("apcm.html") # Salva o grafo

    print("O grafo visual foi criado no arquivo 'apcm.html'.")

"""### Imprime caminho hamiltoniano"""

def isSafe(grafo, v, path, pos):
    # Verifica se o vértice atual é um vértice adjacente do último vértice no caminho
    if grafo.adj[path[pos - 1]][v] == 0:
        return False

    # Verifica se o vértice já foi incluído no caminho
    if v in path:
        return False
    return True

def hamiltonianPathUtil(grafo, path, pos):
    # Se todos os vértices são incluídos no caminho
    if pos == grafo.n:
        return True

    # Tenta diferentes vértices como próximo candidato no caminho hamiltoniano
    for v in range(1, grafo.n):
        if isSafe(grafo, v, path, pos):
            path[pos] = v
            if hamiltonianPathUtil(grafo, path, pos + 1):
                return True
            path[pos] = -1
    return False

def caminhoHamiltoniano(grafo, n_palavras, vertices):

    path = [-1] * grafo.n
    path[0] = 0  # Começa do primeiro vértice
    if not hamiltonianPathUtil(grafo, path, 1):
        print("Não existe caminho hamiltoniano.")

    net = Network(notebook=True, cdn_resources='remote', directed=False, height="1200px", width="100%", bgcolor="black", font_color="white")
    imprimeVertices(net, n_palavras, vertices)
    for i in range(n_palavras-1):
        indice1 = path[i]
        indice2 = path[i+1]
        vertice1 = vertices[indice1]
        vertice2 = vertices[indice2]
        #print(f"[{indice1}, {indice2}] --> [{vertice1}, {vertice2}]")

        peso = grafo.adj[indice1][indice2]

        net.add_edge( # Adiciona a aresta
            indice1, # Origem
            indice2, # Destino
            value=peso, # Peso
            title=f'''
            {vertice1}
            {vertice2}
            Peso: {peso:.2f}
                          ''', # Descrição
            color="gray"
        )
    net.barnes_hut() # Dispersa melhor os vértices
    net.show("caminho_hamiltoniano.html") # Salva o grafo
    print("O grafo visual foi criado no arquivo 'caminho_hamiltoniano.html'.")
    #print("Caminho hamiltoniano encontrado:", path)

"""# Aplicação

## Código

### Front
"""

'''
def mostraMenu():
    menu_text = widgets.HTML(value="""
    <h1>Menu:</h1>
    <ol>
        <li>Ler dados do arquivo</li>
        <li>Gravar dados no arquivo grafo.txt</li>
        <li>Inserir vértice</li>
        <li>Inserir aresta</li>
        <li>Remover vértice</li>
        <li>Remover aresta</li>
        <li>Exibir grafo</li>
        <li>Exibir matriz</li>
        <li>Apresentar a conexidade do grafo</li>
        <li>Encerrar a aplicação</li>
        <li>Buscar um índice pela palavra</li>
        <li>Buscar uma palavra pelo índice</li>
        <li>Fazer busca vetorial</li>
        <li>Exibir grafo colorido</li>
        <li>Exibir árvore parcial de custo mínimo</li>
        <li>Apresentar caminho hamiltoniano</li>
    </ol>
    """)
    display(menu_text)
'''

def mostraMenu():
    print('''
    Menu:
        1. Ler dados do arquivo
        2. Gravar dados no arquivo grafo.txt
        3. Inserir vértice
        4. Inserir aresta
        5. Remover vértice
        6. Remover aresta
        7. Exibir grafo
        8. Exibir matriz
        9. Apresentar a conexidade do grafo
        10. Encerrar a aplicação
        11. Buscar um índice pela palavra
        12. Buscar uma palavra pelo índice
        13. Fazer busca vetorial
        14. Exibir grafo colorido
        15. Exibir árvore parcial de custo mínimo
        16. Apresentar caminho hamiltoniano
    ''')

def limpaTerminal():
    # Verifica se o sistema operacional é Windows ou Linux (Linux/Mac)
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix-based (Linux/Mac)
        os.system('clear')

"""### Back"""

def menu(modelo):

    fim = False
    n_palavras = -1
    vertices = []
    embeddings = []
    grafo = set()

    while(fim == False):
        time.sleep(1)
        #clear_output(wait = True) # Limpa o terminal no Jupyter Notebook
        limpaTerminal()
        mostraMenu()
        choice = input()

        try:
            choice = int(choice)
            if choice == 1: # Cria grafo
                #dados = leArquivoHTTP("https://raw.githubusercontent.com/Cehiim/TeoriaDosGrafos/refs/heads/main/ProjetoFinal/teste.txt")
                dados = leArquivo("palavras.txt")
                try:
                    n_palavras = dados[0] # Número de palavras
                    vertices = dados[1] # Lista de palavras
                    embeddings = modelo.encode(vertices) # Lista dos embeddings das palavras
                    grafo = integraGrafo(modelo, embeddings, n_palavras, vertices)
                except TypeError:
                    fim = True
                    print("Interrompendo programa...")

            elif choice == 2: # Grava dados no arquivo .txt
                if(n_palavras != -1):
                    gravaDados(n_palavras, vertices)
                else:
                    print("[Erro: Grafo não criado]")

            elif choice == 3: # Insere vértice
                palavra = input("Palavra a ser inserida: ")
                if(n_palavras != -1):
                    if(insereVertice(grafo, n_palavras, vertices, palavra)):
                        n_palavras += 1
                        print("Vértice inserido com sucesso!")
                    else:
                        print("[Erro: vértice já existe]")
                else:
                    print("[Erro: Grafo não criado]")

            elif choice == 4: # Insere aresta
                try:
                    origem = int(input("Insira o índice de origem: "))
                    destino = int(input("Insira o índice de destino: "))
                    peso = float(input("Insira o peso: "))
                    if(n_palavras != -1):
                        if(insereAresta(grafo, n_palavras, origem, destino, peso)):
                          print("Aresta inserida com sucesso!")
                        else:
                          print("[Erro: vértice não existe]")
                    else:
                        print("[Erro: Grafo não criado]")
                except ValueError:
                    print("[Erro: a entrada não é do tipo int]")

            elif choice == 5: # Remove vértice
                try:
                    indice = int(input("Insira o índice do vértice: "))
                    if(n_palavras != -1):
                        if(removeVertice(grafo, n_palavras, vertices, indice)):
                            n_palavras -= 1
                            print("Vértice removido com sucesso!")
                        else:
                            print("[Erro: vértice não existe]")
                    else:
                        print("[Erro: Grafo não criado]")
                except ValueError:
                    print("[Erro: a entrada não é do tipo int]")

            elif choice == 6: # Remove aresta
                try:
                    origem = int(input("Insira o índice de origem: "))
                    destino = int(input("Insira o índice de destino: "))
                    if(n_palavras != -1):
                        if(removeAresta(grafo, n_palavras, origem, destino)):
                            print("Aresta removida com sucesso!")
                        else:
                            print("[Erro: vértice não existe]")
                    else:
                        print("[Erro: Grafo não criado]")
                except ValueError:
                    print("[Erro: a entrada não é do tipo int]")

            elif choice == 7: # Exibe grafo
                if(n_palavras != -1):
                    imprimeGrafo(n_palavras, vertices, grafo)
                    time.sleep(5)
                else:
                    print("[Erro: Grafo não criado]")

            elif choice == 8: # Exibe matriz
                if(n_palavras != -1):
                    grafo.showMin()
                    print(("\nAperte ENTER para continuar "))
                    ok = input()
                else:
                    print("[Erro: Grafo não criado]")

            elif choice == 9: # Apresenta a conexidade do grafo
                if(n_palavras != -1):
                    if(grafo.conexidade()):
                        print("O grafo é conexo.")
                    else:
                        print("O grafo não é conexo.")
                    time.sleep(5)
                else:
                    print("[Erro: Grafo não criado]")

            elif choice == 10: # Encerra
                fim = True
                print("Encerrando programa...")

            elif choice == 11: # Busca um índice pela palavra
                palavra = input("Palavra a ser consultada: ")
                if(n_palavras != -1):
                    indice = buscaIndice(n_palavras, vertices, palavra)
                    if(indice == -1):
                        print("[Erro: palavra não encontrada]")
                    else:
                        print(f"Índice de {palavra}: {indice}")
                        time.sleep(5)
                else:
                    print("[Erro: Grafo não criado]")

            elif choice == 12: # Busca um índice pela palavra
                try:
                    indice = int(input("Índice a ser consultado: "))
                    if(n_palavras != -1):
                        palavra = buscaPalavra(n_palavras, vertices, indice)
                        if(indice == -1):
                            print("[Erro: palavra não encontrada]")
                        else:
                            print(f"Palavra do índice {indice}: {palavra}")
                            time.sleep(5)
                    else:
                      print("[Erro: Grafo não criado]")
                except ValueError:
                    print("[Erro: a entrada não é do tipo int]")

            elif choice == 13: # Fazer busca vetorial de uma palavra
                busca = input("Insira uma palavra: ")
                if(n_palavras != -1):
                    buscaVetorial(modelo, embeddings, vertices, busca)
                    print(("\nAperte ENTER para continuar "))
                    ok = input()
                else:
                    print("[Erro: Grafo não criado]")

            elif choice == 14: # Exibir árvore parcial de custo mínimo
                if(n_palavras != -1):
                    lista_colorida = grafo.coloreV()
                    n_cores = lista_colorida[0]
                    cores = lista_colorida[1]
                    imprimeGrafoColorido(n_palavras, vertices, grafo, n_cores, cores)
                    time.sleep(5)
                else:
                    print("[Erro: Grafo não criado]")

            elif choice == 15: # Exibir árvore parcial de custo mínimo
                if(n_palavras != -1):
                    imprimeAPCM(n_palavras, vertices, grafo)
                    time.sleep(5)
                else:
                    print("[Erro: Grafo não criado]")

            elif choice == 16: # Apresentar o caminho hamiltoniano
                if(n_palavras != -1):
                    caminhoHamiltoniano(grafo, n_palavras, vertices)
                    time.sleep(5)
                else:
                    print("[Erro: Grafo não criado]")

            else:
                print("Opção inválida.")

        except ValueError:
            #print("[Erro: a entrada não é do tipo int]")
            pass

"""## Menu"""

menu(modelo)