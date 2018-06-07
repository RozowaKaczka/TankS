import pygame
import config
from gamestate import GameState
import state
RED = (255, 0, 0)
GREEN = (0, 225, 0)
BLUE = (0, 0, 255)
WHITE = [255, 255, 255]

class TitleState:

    def __init__(self):
        pass

    def process_input(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                config.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    state.state = GameState()
                if event.key == pygame.K_q:
                    config.running = False
    def update(self):

        pass

    def draw(self, screen):

        screen.fill(BLUE)
        myfont = pygame.font.SysFont("Calibri", 40)
        biggerfont = pygame.font.SysFont("Calibri", 70)
        label = biggerfont.render("Tanks", 1, WHITE)
        lubel = myfont.render("press SPACE to continue", 1, WHITE)
        lebel = myfont.render("press Q to exit", 1, WHITE)
        screen.blit(label, (100, 100))
        screen.blit(lubel, (100, 170))
        screen.blit(lebel, (100, 220))