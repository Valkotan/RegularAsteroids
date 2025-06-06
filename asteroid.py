from circleshape import *
from constants import *
import random

# Asteroid class representing an asteroid in the game, inheriting from CircleShape
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2) #or (self.position.x, self.position.y) for coordinates

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)

        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = a * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = b * 1.2

        #my implementation
        #angle = random.uniform(20, 50)
        #random_angle = self.velocity.rotate(angle)
        #neg_random_angle = self.velocity.rotate(-angle)
        #self.radius -= ASTEROID_MIN_RADIUS
        #A1 = Asteroid(self.position.x, self.position.y, self.radius)
        #A2 = Asteroid(self.position.x, self.position.y, self.radius)
        #A1.velocity = random_angle * 1.2
        #A2.velocity = neg_random_angle * 2
