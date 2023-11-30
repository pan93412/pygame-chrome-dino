import pygame

from .constants import BLACK
from .sprite import Sprite

class Ground(pygame.sprite.Sprite):
    def __init__(self, sprite: Sprite):
        super().__init__()

        self.sprite = sprite
        self.image = self.sprite.get(2, 104, 2400, 26)
        self.image.set_colorkey(BLACK)  # Set the background color as transparent
        self.rect = self.image.get_rect()

    def update(self, *args, **kwargs) -> None:
        self.rect.x -= 5
        if self.rect.x <= -2400:
            self.rect.x = 0
