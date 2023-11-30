import pygame

from dinogame.speed_manager import SpeedManager

from .constants import GRAVITY, JUMP_SPEED_FACTOR, SCREEN_HEIGHT
from .sprite import Sprite


class Dino(pygame.sprite.Sprite):
    def __init__(self, sprite: Sprite, speed_manager: SpeedManager):
        super().__init__()

        self.speed_manager = speed_manager
        self.frame = [sprite.get(1854, 0, 88, 94), sprite.get(1942, 0, 88, 94)]

        self.image = self.frame[0]
        self.rect = self.image.get_rect()
        self.rect.x = 80
        self.rect.y = SCREEN_HEIGHT - self.rect.height - self.speed_manager.get_speed()

        self.vel_y = 0
        self.jumping = False

    def jump(self) -> None:
        if self.jumping:
            return

        self.jumping = True
        self.vel_y = -JUMP_SPEED_FACTOR * max(self.speed_manager.get_speed() // 4, 10)

    def update(self, *args, **kwargs) -> None:
        self.image = self.frame[pygame.time.get_ticks() // 200 % 2]

        self.vel_y += GRAVITY * max(self.speed_manager.get_speed() // 10, 1)
        print(self.vel_y)
        self.rect.y += self.vel_y

        edge = SCREEN_HEIGHT - self.rect.height - self.speed_manager.get_speed()

        if self.rect.y > edge:
            self.rect.y = edge
            self.jumping = False
