import random

import pygame

from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,
                           "white",
                           self.position,
                           self.radius,
                           LINE_WIDTH)
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        new_angle = random.uniform(20, 50)
        new_velocity1 = self.velocity.rotate(new_angle)
        new_velocity2 = self.velocity.rotate(-new_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        a1 = Asteroid(*self.position, new_radius)
        a2 = Asteroid(*self.position, new_radius)

        a1.velocity = new_velocity1 * 1.2
        a2.velocity = new_velocity2 * 1.2

