import pygame
import cmath
from config import BLACK
from math import radians
from config import width, height


class Bullet:

    def __init__(self, pos, velocity, direction):
        self.pos = pos
        self.velocity = velocity
        self.direction = direction
        self.radius = 10

    def draw(self, surfing_surface):
        pygame.draw.circle(surfing_surface, BLACK, (int(self.pos.real), int(self.pos.imag)), self.radius)


    def surfing_updating(self):
        step = cmath.rect(self.velocity, radians(self.direction))

        self.pos += step

    def colides_with_other_player(self, other_player):
        a = self
        b = other_player
        d = self.pos - b.pos
        distance = abs(d)
        #print(distance)
        if distance < a.radius + b.radius:
            return True
        else:
            return False


