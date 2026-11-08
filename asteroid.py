import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        # a circle, because rocks don't do triangles.
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        # big rocks become two smaller arguments.
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        first = self.velocity.rotate(angle)
        second = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        one = Asteroid(self.position.x, self.position.y, new_radius)
        two = Asteroid(self.position.x, self.position.y, new_radius)
        one.velocity = first * 1.2
        two.velocity = second * 1.2

