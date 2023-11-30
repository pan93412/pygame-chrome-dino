import pygame
from dinogame.constants import SCREEN_HEIGHT, SCREEN_WIDTH
from dinogame.speed_manager import SpeedManager
from dinogame.sprite import Sprite


class Cactus(pygame.sprite.Sprite):
    def __init__(self, sprite: Sprite, speed_manager: SpeedManager):
        super().__init__()
        self.sprite = sprite
        self.image = self.sprite.get(446, 2, 33, 70)
        self.rect = self.image.get_rect()
        self.speed_manager = speed_manager

        self.reset()

    def reset(self) -> None:
        self.rect.x = SCREEN_WIDTH
        self.rect.y = SCREEN_HEIGHT - self.rect.height - self.speed_manager.get_speed()

    def update(self):
        self.rect.x -= self.speed_manager.get_speed()
        if self.rect.x < -self.rect.width:
            self.reset()
