import pygame
import math

class Controller:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.SysFont(None, 36)

    # Função de detecção de colisão corrigida
    def check_collisions(self, asteroids, bullets):
        bullets_to_remove = []
        asteroids_to_remove = []
        
        for bullet in bullets.lista:
            for asteroid in asteroids.lista:
                # Cálculo da distância entre a bala e o asteroide
                distance = math.hypot(bullet[0] - asteroid[0], bullet[1] - asteroid[1])
                if distance < asteroid[2]:  # Se a distância for menor que o raio do asteroide
                    asteroids_to_remove.append(asteroid)
                    bullets_to_remove.append(bullet)
                    self.score += 10

        # Remover asteroides e balas após colisão
        for bullet in bullets_to_remove:
            if bullet in bullets.lista:
                bullets.lista.remove(bullet)
        
        for asteroid in asteroids_to_remove:
            if asteroid in asteroids.lista:
                asteroids.lista.remove(asteroid)

    # Função de detecção de colisão asteroide-player
    def player_hit(self, asteroids, player):
        for asteroid in asteroids.lista:
            distance = math.hypot(player.player_x - asteroid[0], player.player_y - asteroid[1])
            if distance < asteroid[2]:  # Se a distância for menor que o raio do asteroide
                return True
        return False

    # Função principal do jogo
    def game_loop(self, screen, player, bullets, asteroids):
        running = True
        while running:
            screen.display.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            player.move_player()
            player.shoot(bullets)
            bullets.move_bullets()
            asteroids.create_asteroids()
            asteroids.move_asteroids()
            self.check_collisions(asteroids, bullets)
            if(self.player_hit(asteroids, player)):
                running = False

            screen.draw_player(player)
            screen.draw_bullets(bullets)
            screen.draw_asteroids(asteroids)

            score_text = self.font.render(f'Score: {self.score}', True, (255, 255, 255))
            screen.display.blit(score_text, (10, 10))

            pygame.display.flip()
            pygame.time.delay(30)