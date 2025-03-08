import pygame
from pygame.draw import polygon

from circleshape import CircleShape
from constants import *  # noqa: F403


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)  # noqa: F405
        self.rotation = 0
        self.shot_timer = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        # sub-classes must override
        # polygon(surface, color, points) -> Rect
        polygon(screen, color="white", points=self.triangle(), width=2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt  # noqa: F405

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if self.shot_timer > 0:
            self.shot_timer -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_SPACE]:
            self.shoot(self.position)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt  # noqa: F405

    def shoot(self, shot_position):
        if self.shot_timer <= 0:
            bullet = Shot(shot_position.x, shot_position.y, SHOT_RADIUS)  # noqa: F405
            bullet.velocity = pygame.Vector2(0, 1).rotate(self.rotation)
            bullet.velocity *= PLAYER_SHOOT_SPEED  # noqa: F405
            self.shot_timer = PLAYER_SHOOT_COOLDOWN  # noqa: F405


class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen, color="white", center=(self.position), radius=SHOT_RADIUS, width=2
        )  # noqa: F405

    def update(self, dt):
        self.position += self.velocity * dt
