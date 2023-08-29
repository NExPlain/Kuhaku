import pygame
from player import Player
from zombie import Zombie
from obstacle import Obstacle
from missile import Missile
import random


class Game:
    def __init__(self, player: Player):
        self.score = 0
        self.player = player
        self.zombies = []
        self.obstacles = []
        self.missiles = []
        self.font = pygame.font.Font(None, 24)
        self.game_over = False

    def add_zombie(self, zombie: Zombie):
        self.zombies.append(zombie)

    def add_obstacle(self, obstacle: Obstacle):
        self.obstacles.append(obstacle)

    def add_missile(self, missile: Missile):
        self.missiles.append(missile)

    def update(self):
        for zombie in self.zombies:
            zombie.move()
        for missile in self.missiles:
            missile.move()

    def draw(self, screen):
        for zombie in self.zombies:
            zombie.draw(screen)
        for obstacle in self.obstacles:
            obstacle.draw(screen)
        for missile in self.missiles:
            missile.draw(screen)
        self.player.draw(screen)
        score_text = self.font.render(
            "Score: " + str(self.score), True, (255, 255, 255)
        )
        screen.blit(score_text, (10, 10))

    def check_collision(self):
        for zombie in self.zombies:
            if self.player.rect.colliderect(zombie.rect):
                self.game_over = True
        for missile in self.missiles:
            for zombie in self.zombies:
                if missile.rect.colliderect(zombie.rect):
                    self.zombies.remove(zombie)
                    if missile in self.missiles:
                        self.missiles.remove(missile)
                    self.score += 1
            for obstacle in self.obstacles:
                if missile.rect.colliderect(obstacle.rect):
                    if missile in self.missiles:
                        self.missiles.remove(missile)
                    if obstacle.decrease_life():
                        self.obstacles.remove(obstacle)
                        self.player.increase_missile_speed()

    def spawn_zombies_and_obstacles(self):
        if random.randint(0, 100) < 5:  # 10% chance to spawn a zombie
            self.add_zombie(Zombie(random.randint(0, 800), 0, 2))
        if random.randint(0, 100) < 1:  # 5% chance to spawn an obstacle
            self.add_obstacle(
                Obstacle(random.randint(0, 800), 0, random.randint(10, 20))
            )
