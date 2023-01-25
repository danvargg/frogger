"""Car sprite."""
import os
from random import choice

import pygame as pg

from game import CAR_GRAPHS_PATH


class Car(pg.sprite.Sprite):  # FIXME: remove magic numbers
    """Car sprite."""

    def __init__(self, pos, groups) -> None:
        super().__init__(groups)

        for _, _, image_list in os.walk(CAR_GRAPHS_PATH):  # TODO: refactor
            car_name = choice(image_list)

        self.image = pg.image.load(CAR_GRAPHS_PATH + '/' + car_name).convert_alpha()  # TODO: refactor
        self.rect = self.image.get_rect(center=pos)

        # Float based movement
        self.pos = pg.math.Vector2(self.rect.center)

        if pos[0] < 200:
            self.direction = pg.math.Vector2(1, 0)
        else:
            self.direction = pg.math.Vector2(-1, 0)
            self.image = pg.transform.flip(self.image, True, False)

        self.speed = 300

    def update(self, dt: float):
        """_summary_

        Args:
            dt (float): _description_
        """
        self.pos += self.direction * self.speed * dt
        self.rect.center = (round(self.pos.x), round(self.pos.y))

        if not -200 < self.rect.x < 3400:
            self.kill()
