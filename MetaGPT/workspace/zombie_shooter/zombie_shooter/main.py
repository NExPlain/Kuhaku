import pygame
from player import Player
from game import Game

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    player = Player(400, 550, 5)
    game = Game(player)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move('left')
        if keys[pygame.K_RIGHT]:
            player.move('right')

        missile = player.shoot()
        if missile:
            game.add_missile(missile)

        game.spawn_zombies_and_obstacles()
        game.update()
        game.check_collision()

        screen.fill((0, 0, 0))
        game.draw(screen)
        pygame.display.flip()

        if game.game_over:
            print("Game Over! Your score is: ", game.score)
            running = False

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
