import math

class Bullets:
    def __init__(self):
        self.lista = []

    # Função para mover balas
    def move_bullets(self):
        for bullet in self.lista:
            bullet[0] += 10 * math.cos(math.radians(bullet[2]))
            bullet[1] -= 10 * math.sin(math.radians(bullet[2]))
        self.lista = [bullet for bullet in self.lista if 0 < bullet[0] < 800 and 0 < bullet[1] < 600]