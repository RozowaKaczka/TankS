import pygame
from math import radians
import cmath
from config import width, height, BLACK
from bullet import Bullet
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)




class Player:
    def __init__(self, x, y):
        self.pos = x + y * 1j
        self.direction = 45
        self.radius = 20
        self.vel_rot = 0
        self.velocity = 0
        self.bullets = []
        self.health = 100
        self.mines = []
    def draw(self, surfing_surface):
        c = self.pos + cmath.rect(self.radius / 2, radians(self.direction))
        d = self.pos + cmath.rect(1.5*self.radius, radians(self.direction))
        pygame.draw.line(surfing_surface, BLACK, (int(c.real), int(c.imag)), (int(d.real),int(d.imag)), 3)
        pygame.draw.circle(surfing_surface, BLUE, (int(self.pos.real), int(self.pos.imag)), self.radius)

        v = -50 - (self.radius + 40) * 1j

        if (int(self.pos.imag)) < 60:
             v = -50-(self.radius-60)*1j

        health_bar_pos = self.pos + v
        pygame.draw.rect(surfing_surface, BLACK, (int(health_bar_pos.real), int(health_bar_pos.imag), 100, 20))
        pygame.draw.rect(surfing_surface, RED, (int(health_bar_pos.real ), int(health_bar_pos.imag  ), self.health  , 20))
    def surfing_starting_moving(self):
        self.velocity = 7

    def surfing_moving_backwards(self):
        self.velocity = -7

    def surfing_stoping_moving(self):
        self.velocity = 0

    def is_outside_screen(self):
        return self.pos.real > width - self.radius or \
               self.pos.imag > height - self.radius or \
               self.pos.real < 0 + self.radius or \
               self.pos.imag < 0 + self.radius




    def colides_with_other_player(self, other_player):
        a = self
        b = other_player
        d = a.pos - b.pos
        distance = abs(d)
        #print(distance)
        if distance < a.radius + b.radius:
            return True
        else:
            return False
    def surfing_updating(self, other_player):
        self.direction = self.direction + self.vel_rot
        self.pos = self.pos + cmath.rect(self.velocity, radians(self.direction))
        if self.is_outside_screen():
            self.pos = self.pos - cmath.rect(self.velocity, radians(self.direction))
        if self.colides_with_other_player(other_player):
            self.pos = self.pos - cmath.rect(self.velocity, radians(self.direction))
        for b in self.bullets:
            if b.colides_with_other_player(other_player):
                other_player.health -= 10
                b = None
        for m in self.mines:
            if m.colides_with_other_player(other_player):
                other_player.health -= 20
                m = None

    def start_rotating_left(self):
        self.vel_rot = -3
        #self.direction -= 10
    def start_rotating_right(self):
        self.vel_rot = 3
        #self.directiond += 10
    def stop_rotating(self):
        self.vel_rot = 0
    def fire_bullet(self):
        b = Bullet(self.pos, 10, self.direction)
        self.bullets.append(b)
    def place_mine(self):
        m = Bullet(self.pos, 0, self.direction)
        self.mines.append(m)



