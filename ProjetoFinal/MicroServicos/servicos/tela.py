import os
from pyvis.network import Network

class Tela:

    @staticmethod
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

    @staticmethod
    def limpaTerminal():
        # Verifica se o sistema operacional é Windows ou Linux (Linux/Mac)
        if os.name == 'nt':  # Windows
            os.system('cls')
        else:  # Unix-based (Linux/Mac)
            os.system('clear')

    def imprimeVertices(network, n_palavras, vertices):
        for i in range(n_palavras):
            network.add_node( # Adiciona vértices
                i, # Índice
                label=vertices[i], # Descrição do vértice
                color="yellow"
            )

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

    @staticmethod
    def imprimeGrafo(n_palavras, vertices, grafo):
        net = Network(cdn_resources='local', directed=False, height="1200px", width="100%", bgcolor="black", font_color="white")
        Tela.imprimeVertices(net, n_palavras, vertices)
        Tela.imprimeArestas(net, n_palavras, vertices, grafo)

        net.barnes_hut() # Dispersa melhor os vértices
        net.write_html("grafo.html", open_browser=True, notebook=False)
        

    def imprimeVerticesColoridos(network, n_palavras, vertices, cores, grupos):
        for i in range(n_palavras):
            num = grupos[i]
            network.add_node( # Adiciona vértices
                i, # Índice
                label=vertices[i], # Descrição do vértice
                color=cores[num - 1]
            )

    @staticmethod
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
            net = Network(cdn_resources='local', directed=False, height="1200px", width="100%", bgcolor="black", font_color="white")
            Tela.imprimeVerticesColoridos(net, n_palavras, vertices, cores, grupos)
            Tela.imprimeArestas(net, n_palavras, vertices, grafo)
            net.barnes_hut() # Dispersa melhor os vértices
            net.write_html("grafo_colorido.html", open_browser=True, notebook=False)

    @staticmethod
    def imprimeAPCM(n_palavras, vertices, grafo):
        net = Network(cdn_resources='local', directed=False, height="1200px", width="100%", bgcolor="black", font_color="white")
        Tela.imprimeVertices(net, n_palavras, vertices)

        arvore_parcial = grafo.kruskal()

        for i in range(len(arvore_parcial)):
            indice1 = arvore_parcial[i][0] - 1
            indice2 = arvore_parcial[i][1] - 1
            vertice1 = vertices[indice1]
            vertice2 = vertices[indice2]


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
        net.write_html("apcm.html", open_browser=True, notebook=False)

    @staticmethod
    def imprimeCaminhoHamiltoniano(grafo, n_palavras, vertices):
        path = grafo.caminhoHamiltoniano(n_palavras, vertices)
        net = Network(cdn_resources='local', directed=False, height="1200px", width="100%", bgcolor="black", font_color="white")
        Tela.imprimeVertices(net, n_palavras, vertices)
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
        net.write_html("caminho_hamiltoniano.html", open_browser=True, notebook=False)