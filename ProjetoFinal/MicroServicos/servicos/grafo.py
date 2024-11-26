# Grafo como uma matriz de adjacência não-direcionado rotulado
class Grafo: # Ex 8
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
    
    def isSafe(self, v, path, pos):
        # Verifica se o vértice atual é um vértice adjacente do último vértice no caminho
        if self.adj[path[pos - 1]][v] == 0:
            return False

        # Verifica se o vértice já foi incluído no caminho
        if v in path:
            return False
        return True

    def hamiltonianPathUtil(self, path, pos):
        # Se todos os vértices são incluídos no caminho
        if pos == self.n:
            return True

        # Tenta diferentes vértices como próximo candidato no caminho hamiltoniano
        for v in range(1, self.n):
            if self.isSafe(v, path, pos):
                path[pos] = v
                if self.hamiltonianPathUtil(path, pos + 1):
                    return True
                path[pos] = -1
        return False

    def caminhoHamiltoniano(self, n_palavras, vertices):

        path = [-1] * self.n
        path[0] = 0  # Começa do primeiro vértice
        if not self.hamiltonianPathUtil(path, 1):
            return []
        else:
            return path