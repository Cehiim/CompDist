from sentence_transformers import SentenceTransformer, util
import numpy as np

class Codificador:
    def __init__(self):
        self.modelo = SentenceTransformer("neuralmind/bert-large-portuguese-cased") # BERTimbau: modelo de linguagem especializado em português

    def geraEmbeddings(self, palavras):
        return self.modelo.encode(palavras)
        
    def buscaVetorial(self, embeddings, n_buscas, palavra):
        embedding = self.modelo.encode(palavra) # Gera embedding da palavra
        busca = util.semantic_search(embedding, embeddings, top_k=n_buscas) # Busca semântica por cosseno
        return busca
'''
    def geraEmbeddings(self, n_palavras, palavras):
        embeddings = []
        for i in range(n_palavras):
            embedding = self.modelo.encode(palavras[i]) # Gera embewdding da palavra
            embeddings.append(embedding)
        return np.array(embeddings)
'''
