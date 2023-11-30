import importlib.resources
from tempfile import NamedTemporaryFile
import pygame

sprite_sheet = importlib.resources.open_binary("dinogame", "sprite_sheet.png")


class Sprite:
    def __init__(self):
        # create a temporary file to store the sprite sheet
        with NamedTemporaryFile("wb") as f:
            f.write(sprite_sheet.read())
            self.image = pygame.image.load(f.name)

    def get(self, x: int, y: int, width: int, height: int) -> pygame.Surface:
        return self.image.subsurface((x, y, width, height))
