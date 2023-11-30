from typing import Any
import pygame
from .constants import MAXIMUM_SCORE_DIGIT, SCORE_FACTOR, SCREEN_WIDTH, WHITE

from .sprite import Sprite


SCORE_BEGIN_X = 1294
SCORE_BEGIN_Y = 2
SCORE_WIDTH = 20
SCORE_HEIGHT = 20


class Score(pygame.sprite.Sprite):
    def __init__(self, sprite: Sprite):
        super().__init__()

        self.sprite = sprite
        self.scores = [  # 0 - 9
            self.sprite.get(SCORE_BEGIN_X + SCORE_WIDTH * i, SCORE_BEGIN_Y, SCORE_WIDTH, SCORE_HEIGHT)
            for i in range(0, 10)
        ]
        self.extra_score = 0
        self.previous_score = 0

        self.image = self._get_score_surface(self.get_score())
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.y = 10


    def get_score(self) -> int:
        # Score is based on the time.
        t = pygame.time.get_ticks() // SCORE_FACTOR

        return t + self.extra_score - self.previous_score

    def reset(self) -> None:
        self.previous_score += self.get_score()

    def _get_score_surface(self, score: int) -> pygame.Surface:
        score_surface = pygame.Surface((MAXIMUM_SCORE_DIGIT * SCORE_WIDTH, SCORE_HEIGHT))
        score_surface.fill(WHITE)

        score_str = f"{score:06d}"

        for i, digit in enumerate(score_str):
            score_surface.blit(self.scores[int(digit)], (i * SCORE_WIDTH, 0))

        return score_surface

    def add_extra_score(self, score: int):
        self.extra_score += score

    def update(self, *args: Any, **kwargs: Any) -> None:
        self.image = self._get_score_surface(self.get_score())
