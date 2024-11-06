import pygame
from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.SHOT_RADIUS = 5
        
    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, 0)

    def update(self, dt):
        self.position += self.velocity * dt