import pygame
from player import Player
from config import width, height
pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
player_1 = Player(20, 20)
player_2 = Player(780, 580)

while running:
    # 1. Process input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:

            if event.key == pygame.K_d:
                player_2.surfing_stoping_moving()
            if event.key == pygame.K_LEFT:
                player_1.surfing_stoping_moving()
            if event.key == pygame.K_a:
                player_2.surfing_stoping_moving()
            if event.key == pygame.K_RIGHT:
                player_1.surfing_stoping_moving()
            if event.key == pygame.K_RIGHT:
                player_2.surfing_stoping_moving()
            if event.key == pygame.K_n or event.key == pygame.K_m:
                player_1.stop_rotating()
            if event.key == pygame.K_f or event.key == pygame.K_g:
                player_2.stop_rotating()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:

                player_1.surfing_starting_moving()
            if event.key == pygame.K_d:
                player_2.surfing_starting_moving()
            if event.key == pygame.K_n:
                player_1.start_rotating_left()
            if event.key == pygame.K_m:
                player_1.start_rotating_right()
            if event.key == pygame.K_f:
                player_2.start_rotating_left()
            if event.key == pygame.K_g:
                player_2.start_rotating_right()
            if event.key == pygame.K_LEFT:
                player_1.surfing_moving_backwards()
            if event.key == pygame.K_a:
                player_2.surfing_moving_backwards()
            if event.key == pygame.K_h:
                player_2.fire_bullet()
            if event.key == pygame.K_COMMA:
                player_1.fire_bullet()
            if event.key == pygame.K_j:
                player_2.place_mine()
            if event.key == pygame.K_b:
                player_1.place_mine()

    # 2. Update game
    player_1.surfing_updating(player_2)
    player_2.surfing_updating(player_1)

    for b in player_1.bullets:
        b.surfing_updating()
    for b in player_2.bullets:
        b.surfing_updating()
    for m in player_1.mines:
        m.surfing_updating()
    for m in player_2.mines:
        m.surfing_updating()

    if player_1.health <= 0 or player_2.health <= 0:
        running = False
    # 3. Render screen (draw things)
    screen.fill(GREEN)
    # Draw things here
    player_2.draw(screen)
    player_1.draw(screen)
    for b in player_1.bullets:
        b.draw(screen)
    for b in player_2.bullets:
        b.draw(screen)
    for m in player_1.mines:
        m.draw(screen)
    for m in player_2.mines:
        m.draw(screen)
    #b.draw(screen)
    pygame.display.update()
    # 4. Wait some time
    clock.tick(60)
