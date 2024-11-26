import requests

class Leitor:
    @staticmethod
    def leArquivoHTTP(url):
        try:
            arquivo = requests.get(url).text
            lista = arquivo.split() # Distribui cada elemento do arquivo numa lista
            n_palavras = int(lista.pop(0)) # Separa o número de palavras (primeira linha do arquivo)

            palavras = []
            for i in range(n_palavras):
                palavra = lista[i]
                palavras.append(palavra)

            dados = [n_palavras]
            dados.append(palavras)
            return dados

        except requests.exceptions.RequestException:
            return []

    @staticmethod
    def leArquivo(origem):
        try:
            with open(origem, 'r', encoding='utf-8') as arquivo:
                n_palavras = int(arquivo.readline()) # Recupera o número de palavras (primeira linha do arquivo)

                palavras = []
                for i in range(n_palavras):
                    palavra = arquivo.readline().strip()
                    palavras.append(palavra)

            dados = [n_palavras]
            dados.append(palavras)
            return dados

        except FileNotFoundError:
            return []

    @staticmethod
    def gravaDados(n_palavras, palavras):
        with open("grafo.txt", "w") as arquivo:
            arquivo.write(str(n_palavras)+"\n")

            for i in range(n_palavras):
                arquivo.write(palavras[i]+"\n")