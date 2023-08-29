import pygame

class Zombie:
    def __init__(self, x: int, y: int, speed: int):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = pygame.image.load('zombie.png')
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def move(self):
        self.y += self.speed
        self.rect.center = (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
