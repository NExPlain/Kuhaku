import pygame
from missile import Missile


class Player:
    def __init__(self, x: int, y: int, speed: int):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = pygame.image.load("player.png")
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.missile_speed = 10
        self.missile_timer = pygame.time.get_ticks()

    def move(self, direction: str):
        if direction == "left":
            self.x -= self.speed
        elif direction == "right":
            self.x += self.speed
        self.rect.center = (self.x, self.y)

    def shoot(self):
        current_time = pygame.time.get_ticks()
        if (
            current_time - self.missile_timer > 1000 / self.missile_speed
        ):  # 20 missiles per second
            self.missile_timer = current_time
            return Missile(self.x, self.y, self.missile_speed)
        return None

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def increase_missile_speed(self):
        self.missile_speed *= 1.1
