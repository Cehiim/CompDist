import pygame
from asteroids import Asteroids
from bullets import Bullets
from controller import Controller
from player import Player
from screen import Screen

pygame.init()

asteroids = Asteroids()
bullets = Bullets()
player = Player()

screen = Screen()
controller = Controller()
controller.game_loop(screen, player, bullets, asteroids)

pygame.quit()