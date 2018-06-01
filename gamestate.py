import pygame
from player import Player
import config
RED = (255, 0, 0)
GREEN = (0, 225, 0)
BLUE = (0, 0, 255)



class GameState:

    def __init__(self):
        self.player_1 = Player(20, 20, BLUE)
        self.player_2 = Player(780, 580, RED)

    def process_input(self):


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                config.running = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s:
                     self.player_1.surfing_stoping_moving()
                if event.key == pygame.K_UP:
                    self.player_2.surfing_stoping_moving()
                if event.key == pygame.K_w:
                    self.player_1.surfing_stoping_moving()
                if event.key == pygame.K_DOWN:
                    self.player_2.surfing_stoping_moving()
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.player_2.stop_rotating()
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    self.player_1.stop_rotating()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.player_2.surfing_starting_moving()
                if event.key == pygame.K_w:
                    self.player_1.surfing_starting_moving()
                if event.key == pygame.K_LEFT:
                    self.player_2.start_rotating_left()
                if event.key == pygame.K_RIGHT:
                    self.player_2.start_rotating_right()
                if event.key == pygame.K_a:
                    self.player_1.start_rotating_left()
                if event.key == pygame.K_d:
                    self.player_1.start_rotating_right()
                if event.key == pygame.K_DOWN:
                    self.player_2.surfing_moving_backwards()
                if event.key == pygame.K_s:
                    self.player_1.surfing_moving_backwards()
                if event.key == pygame.K_f:
                    self.player_1.fire_bullet()
                if event.key == pygame.K_COMMA:
                    self.player_2.fire_bullet()
                if event.key == pygame.K_g:
                    self.player_1.place_mine()
                if event.key == pygame.K_m:
                    self.player_2.place_mine()

    def update(self):
        self.player_1.surfing_updating(self.player_2)
        self.player_2.surfing_updating(self.player_1)

        for b in self.player_1.bullets:
            b.surfing_updating()
        for b in self.player_2.bullets:
            b.surfing_updating()

        if self.player_1.health <= 0 or self.player_2.health <= 0:
            config.running = False

    def draw(self, screen):
        screen.fill(GREEN)
        self.player_2.draw(screen)
        self.player_1.draw(screen)
        for b in self.player_1.bullets:
            b.draw(screen)
        for b in self.player_2.bullets:
            b.draw(screen)




