import random
import math

class Asteroids:
    def __init__(self):
        self.lista = []

    # Função para criar asteroides
    def create_asteroids(self):
        if len(self.lista) < 5:
            for _ in range(5 - len(self.lista)):
                x = random.randint(0, 800)
                y = random.randint(0, 600)
                size = random.randint(20, 50)
                angle = random.randint(0, 360)
                speed = random.random() * 2 + 1
                self.lista.append([x, y, size, angle, speed])

    # Função para mover asteroides
    def move_asteroids(self):
        for asteroid in self.lista:
            asteroid[0] += asteroid[4] * math.cos(math.radians(asteroid[3]))
            asteroid[1] -= asteroid[4] * math.sin(math.radians(asteroid[3]))
            if asteroid[0] < 0: asteroid[0] = 800
            if asteroid[0] > 800: asteroid[0] = 0
            if asteroid[1] < 0: asteroid[1] = 600
            if asteroid[1] > 600: asteroid[1] = 0