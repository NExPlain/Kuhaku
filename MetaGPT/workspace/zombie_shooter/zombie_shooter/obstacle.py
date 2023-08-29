import pygame


class Obstacle:
    def __init__(self, x: int, y: int, life_points: int, speed: int):
        self.x = x
        self.y = y
        self.life_points = life_points
        self.image = pygame.image.load("obstacle.png")
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.speed = speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        font = pygame.font.Font(None, 100)
        text = font.render(str(self.life_points), True, (255, 255, 255))
        screen.blit(text, (self.x, self.y))

    def move(self):
        self.y += self.speed
        self.rect.center = (self.x, self.y)

    def decrease_life(self):
        self.life_points -= 1
        if self.life_points <= 0:
            return True
        return False
