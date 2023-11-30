from math import ceil
import pygame

from dinogame.constants import MESSAGE_SECOND, MESSAGE_WIDTH, SCREEN_WIDTH, TEXT_PX, WHITE
from dinogame.score import SCORE_HEIGHT


class Message(pygame.sprite.Sprite):
    message: str | None = None
    last_update_tick: int | None = None

    def __init__(self) -> None:
        super().__init__()

        self.image = pygame.Surface((MESSAGE_WIDTH, ceil(TEXT_PX * 1.2)))
        self.reset()

        self.rect = self.image.get_rect()
        self.font = pygame.font.SysFont("Arial", TEXT_PX)

        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.y = SCORE_HEIGHT + 20


    def show_message(self, message: str) -> None:
        self.message = message
        self.last_update_tick = pygame.time.get_ticks()

    def reset(self) -> None:
        self.image.fill(WHITE)
        self.last_update_tick = None

    def update(self) -> None:
        if self.message:
            rendered_font = self.font.render(self.message, True, (0, 0, 0))
            self.image.blit(rendered_font, (MESSAGE_WIDTH // 2 - rendered_font.get_width() // 2, 0))
            self.message = None

        if self.last_update_tick:
            if pygame.time.get_ticks() - self.last_update_tick > MESSAGE_SECOND * 1000:
                self.reset()
