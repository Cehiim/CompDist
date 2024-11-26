class Utilitarios:
    
    @staticmethod
    def buscaIndice(n_palavras, vertices, palavra):
        for i in range(n_palavras):
            if(vertices[i] == palavra):
                return i
        return -1
    
    @staticmethod
    def buscaPalavra(n_palavras, vertices, indice):
        if(indice >= n_palavras or indice < 0):
            return "erro"
        for i in range(n_palavras):
            if(i == indice):
                return vertices[i]
        return "erro"