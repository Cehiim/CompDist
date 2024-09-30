import pygame
import math

class Player:
    def __init__(self):
        self.player_x, self.player_y = 400, 300
        self.player_angle = 0
        self.player_speed = 0

    # Função para movimentar o jogador
    def move_player(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            self.player_angle += 5  # Gira a nave no sentido horário
        if keys[pygame.K_RIGHT]:
            self.player_angle -= 5  # Gira a nave no sentido anti-horário
        if keys[pygame.K_UP]:
            self.player_speed = 5  # Acelera a nave para frente
        elif keys[pygame.K_DOWN]:
            self.player_speed = -3  # Move a nave para trás
        else:
            self.player_speed = 0  # Parar a nave se nenhuma tecla for pressionada

        # Atualiza a posição da nave com base na velocidade e ângulo
        self.player_x += self.player_speed * math.cos(math.radians(self.player_angle))
        self.player_y -= self.player_speed * math.sin(math.radians(self.player_angle))

        # Verifica os limites da tela para criar o efeito de "loop" de borda a borda
        if self.player_x < 0: self.player_x = 800
        if self.player_x > 800: self.player_x = 0
        if self.player_y < 0: self.player_y = 600
        if self.player_y > 600: self.player_y = 0

    # Função para atirar balas
    def shoot(self, bullets):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            bullets.lista.append([self.player_x, self.player_y, self.player_angle])