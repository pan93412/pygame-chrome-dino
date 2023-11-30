from pathlib import Path
import pygame

sprite_sheet_path = Path(__file__).parent / 'sprite_sheet.png'

class Sprite:
    def __init__(self):
        self.image = pygame.image.load(sprite_sheet_path)

    def get(self, x: int, y: int, width: int, height: int) -> pygame.Surface:
        return self.image.subsurface((x, y, width, height))
