import sys

import pygame
from pygame.display import update

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *  # noqa: F403
from player import Player, Shot


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")  # noqa: F405
    print(f"Screen height: {SCREEN_HEIGHT}")  # noqa: F405
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # noqa: F405

    game_clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH / 2  # noqa: F405
    y = SCREEN_HEIGHT / 2  # noqa: F405

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    player = Player(x, y)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color="black")
        updatable.update(dt)
        for thing in drawable:
            thing.draw(screen)

        for asteroid in asteroids:
            if player.collision(asteroid):
                sys.exit("Game over!")

        pygame.display.flip()
        dt = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
