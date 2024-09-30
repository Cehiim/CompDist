import pygame
import math
from player import Player
from controller import Controller

class Screen:
    def __init__(self):
        self.display = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Asteroids")
        
    # Função para desenhar o jogador
    def draw_player(self, player):
        points = [
            (player.player_x + 15 * math.cos(math.radians(player.player_angle)), player.player_y - 15 * math.sin(math.radians(player.player_angle))),
            (player.player_x + 15 * math.cos(math.radians(player.player_angle + 120)), player.player_y - 15 * math.sin(math.radians(player.player_angle + 120))),
            (player.player_x + 15 * math.cos(math.radians(player.player_angle + 240)), player.player_y - 15 * math.sin(math.radians(player.player_angle + 240)))
        ]
        pygame.draw.polygon(self.display, (255, 255, 255), points)

    # Função para desenhar asteroides
    def draw_asteroids(self, asteroids):
        for asteroid in asteroids.lista:
            pygame.draw.circle(self.display, (255, 255, 255), (int(asteroid[0]), int(asteroid[1])), asteroid[2])

    # Função para desenhar balas
    def draw_bullets(self, bullets):
        for bullet in bullets.lista:
            pygame.draw.circle(self.display, (255, 255, 255), (int(bullet[0]), int(bullet[1])), 3)