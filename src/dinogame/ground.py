import pygame
from dinogame import speed_manager

from dinogame.speed_manager import SpeedManager

from .constants import BLACK, SCREEN_HEIGHT
from .sprite import Sprite


class Ground(pygame.sprite.Sprite):
    def __init__(self, sprite: Sprite, speed_manager: SpeedManager):
        super().__init__()

        # create a double image to scroll
        surface = pygame.Surface((4800, 26))
        surface.blit(sprite.get(2, 104, 2400, 26), (0, 0))
        surface.blit(sprite.get(2, 104, 2400, 26), (2400, 0))

        self.speed_manager = speed_manager
        self.image = surface
        self.image.set_colorkey(BLACK)  # Set the background color as transparent
        self.rect = self.image.get_rect()
        self.rect.y = SCREEN_HEIGHT - self.rect.height

    def update(self, *args, **kwargs) -> None:
        self.rect.x -= self.speed_manager.get_speed()
        if self.rect.x <= -(self.rect.width // 2):
            self.rect.x = 0
