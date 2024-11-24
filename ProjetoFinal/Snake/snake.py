import pygame
import time
import random

pygame.init()

# Definindo cores
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (213, 50, 80)
verde = (0, 255, 0)
azul = (50, 153, 213)

# Definindo tamanho da tela
largura_tela = 1280
altura_tela = 720

# Inicializando a tela do jogo
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Snake Game')

# Definindo a velocidade e o tamanho do cubo (segmento da cobra)
relogio = pygame.time.Clock()
velocidade_cobra = 15
tamanho_cubo = 10

# Função para mostrar a pontuação na tela
def mostrar_pontuacao(score):
    fonte = pygame.font.SysFont(None, 35)
    valor_pontuacao = fonte.render("Pontuação: " + str(score), True, preto)
    tela.blit(valor_pontuacao, [0, 0])

# Função principal do jogo
def jogo():
    game_over = False
    game_close = False

    x_cobra = largura_tela / 2
    y_cobra = altura_tela / 2

    x_cobra_mudanca = 0
    y_cobra_mudanca = 0

    segmentos_cobra = []
    comprimento_cobra = 1

    x_comida = round(random.randrange(0, largura_tela - tamanho_cubo) / 10.0) * 10.0
    y_comida = round(random.randrange(0, altura_tela - tamanho_cubo) / 10.0) * 10.0

    while not game_over:

        while game_close:
            tela.fill(branco)
            fonte = pygame.font.SysFont(None, 50)
            mensagem = fonte.render("Você perdeu! Pressione Q-Quit ou C-Continuar", True, vermelho)
            tela.blit(mensagem, [largura_tela / 6, altura_tela / 3])
            mostrar_pontuacao(comprimento_cobra - 1)
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if evento.key == pygame.K_c:
                        jogo()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x_cobra_mudanca = -tamanho_cubo
                    y_cobra_mudanca = 0
                elif evento.key == pygame.K_RIGHT:
                    x_cobra_mudanca = tamanho_cubo
                    y_cobra_mudanca = 0
                elif evento.key == pygame.K_UP:
                    y_cobra_mudanca = -tamanho_cubo
                    x_cobra_mudanca = 0
                elif evento.key == pygame.K_DOWN:
                    y_cobra_mudanca = tamanho_cubo
                    x_cobra_mudanca = 0

        if x_cobra >= largura_tela or x_cobra < 0 or y_cobra >= altura_tela or y_cobra < 0:
            game_close = True
        x_cobra += x_cobra_mudanca
        y_cobra += y_cobra_mudanca
        tela.fill(azul)
        pygame.draw.rect(tela, verde, [x_comida, y_comida, tamanho_cubo, tamanho_cubo])
        corpo_cobra = []
        corpo_cobra.append(x_cobra)
        corpo_cobra.append(y_cobra)
        segmentos_cobra.append(corpo_cobra)
        if len(segmentos_cobra) > comprimento_cobra:
            del segmentos_cobra[0]

        for segmento in segmentos_cobra[:-1]:
            if segmento == corpo_cobra:
                game_close = True

        for segmento in segmentos_cobra:
            pygame.draw.rect(tela, preto, [segmento[0], segmento[1], tamanho_cubo, tamanho_cubo])

        mostrar_pontuacao(comprimento_cobra - 1)

        pygame.display.update()

        if x_cobra == x_comida and y_cobra == y_comida:
            x_comida = round(random.randrange(0, largura_tela - tamanho_cubo) / 10.0) * 10.0
            y_comida = round(random.randrange(0, altura_tela - tamanho_cubo) / 10.0) * 10.0
            comprimento_cobra += 1

        relogio.tick(velocidade_cobra)

    pygame.quit()
    quit()

jogo()
