from math import floor
from dinogame.constants import SPEED_UP_FACTOR
from dinogame.score import Score


class SpeedManager:
    def __init__(self, score: Score):
        self.score = score
        self.speed = 10

    def update(self) -> None:
        self.speed = 10 + floor(self.score.get_score() // SPEED_UP_FACTOR)

    def get_speed(self) -> int:
        print(self.speed)
        return self.speed
