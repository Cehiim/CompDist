import pygame
import random
import math

# Inicialização do Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Asteroids")

# Variáveis globais e configurações
player_x, player_y = 400, 300
player_angle = 0
player_speed = 0
bullets = []
asteroids = []
score = 0
font = pygame.font.SysFont(None, 36)

# Função para desenhar o jogador
def draw_player():
    points = [
        (player_x + 15 * math.cos(math.radians(player_angle)), player_y - 15 * math.sin(math.radians(player_angle))),
        (player_x + 15 * math.cos(math.radians(player_angle + 120)), player_y - 15 * math.sin(math.radians(player_angle + 120))),
        (player_x + 15 * math.cos(math.radians(player_angle + 240)), player_y - 15 * math.sin(math.radians(player_angle + 240)))
    ]
    pygame.draw.polygon(screen, (255, 255, 255), points)

# Função para desenhar asteroides
def draw_asteroids():
    for asteroid in asteroids:
        pygame.draw.circle(screen, (255, 255, 255), (int(asteroid[0]), int(asteroid[1])), asteroid[2])

# Função para desenhar balas
def draw_bullets():
    for bullet in bullets:
        pygame.draw.circle(screen, (255, 255, 255), (int(bullet[0]), int(bullet[1])), 3)

# Função para movimentar o jogador
def move_player():
    global player_x, player_y, player_speed
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        global player_angle
        player_angle += 5  # Gira a nave no sentido horário
    if keys[pygame.K_RIGHT]:
        player_angle -= 5  # Gira a nave no sentido anti-horário
    if keys[pygame.K_UP]:
        player_speed = 5  # Acelera a nave para frente
    elif keys[pygame.K_DOWN]:
        player_speed = -3  # Move a nave para trás
    else:
        player_speed = 0  # Parar a nave se nenhuma tecla for pressionada

    # Atualiza a posição da nave com base na velocidade e ângulo
    player_x += player_speed * math.cos(math.radians(player_angle))
    player_y -= player_speed * math.sin(math.radians(player_angle))

    # Verifica os limites da tela para criar o efeito de "loop" de borda a borda
    if player_x < 0: player_x = 800
    if player_x > 800: player_x = 0
    if player_y < 0: player_y = 600
    if player_y > 600: player_y = 0

# Função para atirar balas
def shoot():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        bullets.append([player_x, player_y, player_angle])

# Função para mover balas
def move_bullets():
    global bullets
    for bullet in bullets:
        bullet[0] += 10 * math.cos(math.radians(bullet[2]))
        bullet[1] -= 10 * math.sin(math.radians(bullet[2]))
    bullets = [bullet for bullet in bullets if 0 < bullet[0] < 800 and 0 < bullet[1] < 600]

# Função para criar asteroides
def create_asteroids():
    if len(asteroids) < 5:
        for _ in range(5 - len(asteroids)):
            x = random.randint(0, 800)
            y = random.randint(0, 600)
            size = random.randint(20, 50)
            angle = random.randint(0, 360)
            speed = random.random() * 2 + 1
            asteroids.append([x, y, size, angle, speed])

# Função para mover asteroides
def move_asteroids():
    for asteroid in asteroids:
        asteroid[0] += asteroid[4] * math.cos(math.radians(asteroid[3]))
        asteroid[1] -= asteroid[4] * math.sin(math.radians(asteroid[3]))
        if asteroid[0] < 0: asteroid[0] = 800
        if asteroid[0] > 800: asteroid[0] = 0
        if asteroid[1] < 0: asteroid[1] = 600
        if asteroid[1] > 600: asteroid[1] = 0

# Função de detecção de colisão corrigida
def check_collisions():
    global score, asteroids, bullets
    bullets_to_remove = []
    asteroids_to_remove = []
    
    for bullet in bullets:
        for asteroid in asteroids:
            # Cálculo da distância entre a bala e o asteroide
            distance = math.hypot(bullet[0] - asteroid[0], bullet[1] - asteroid[1])
            if distance < asteroid[2]:  # Se a distância for menor que o raio do asteroide
                asteroids_to_remove.append(asteroid)
                bullets_to_remove.append(bullet)
                score += 10

    # Remover asteroides e balas após colisão
    for bullet in bullets_to_remove:
        if bullet in bullets:
            bullets.remove(bullet)
    
    for asteroid in asteroids_to_remove:
        if asteroid in asteroids:
            asteroids.remove(asteroid)

# Função principal do jogo
def game_loop():
    global asteroids
    running = True
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        move_player()
        shoot()
        move_bullets()
        create_asteroids()
        move_asteroids()
        check_collisions()

        draw_player()
        draw_bullets()
        draw_asteroids()

        score_text = font.render(f'Score: {score}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        pygame.time.delay(30)

    pygame.quit()

# Executando o jogo
game_loop()