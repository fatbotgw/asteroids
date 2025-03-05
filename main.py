import pygame

from constants import *  # noqa: F403
from player import Player


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")  # noqa: F405
    print(f"Screen height: {SCREEN_HEIGHT}")  # noqa: F405
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # noqa: F405

    game_clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color='black')
        player.draw(screen)
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000

        




if __name__ == "__main__":
    main()
