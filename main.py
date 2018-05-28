import pygame
from config import width, height
import gamestate
pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
state = gamestate.GameState()

while running:
    # 1. Process input
    state.process_input()

    # 2. Update game
    state.update()
    # 3. Render screen (draw things)

    # Draw things here
    state.draw(screen)

    #b.draw(screen)
    pygame.display.update()
    # 4. Wait some time
    clock.tick(60)
