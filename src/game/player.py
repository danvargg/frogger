"""Player Sprite."""
import os
import pygame as pg

from game import PLAYER_GRAPHS_PATH  # FIXME: use for paths


class Player(pg.sprite.Sprite):  # TODO: sprites have pos, dir and speed
    """Player class."""

    def __init__(self, pos: tuple, groups: pg.sprite.Group) -> None:  # TODO: add type hints
        """_summary_

        Args:
            pos (_type_): _description_
            groups (_type_): _description_
        """
        super().__init__(groups)
        self.import_assets()  # TODO: is this good?
        self.frame_index = 0
        self.image = self.animation[self.frame_index]
        self.rect = self.image.get_rect(center=pos)

        # Float based movement
        self.pos = pg.math.Vector2(self.rect.center)
        self.direction = pg.math.Vector2(0, 0)
        self.speed = 200

    def import_assets(self) -> None:  # TODO: property or constructor?
        """Import player assets."""
        # TODO: refactor range(4)
        self.animation = [pg.image.load(f'{PLAYER_GRAPHS_PATH}/{frame}.png').convert_alpha() for frame in range(4)]

    def move(self, dt: float) -> None:
        """Move player.

        Args:
            dt (float): delta time
        """
        # Normalize vector (direction)
        if self.direction.length_squared() != 0:
            self.direction = self.direction.normalize()

        self.pos += self.direction * self.speed * dt
        self.rect.center = (round(self.pos.x), round(self.pos.y))

    def input(self) -> None:  # TODO: refator!
        """Player inputs."""
        keys = pg.key.get_pressed()

        # Horizontal input
        if keys[pg.K_RIGHT]:
            self.direction.x = 1
        elif keys[pg.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        # Horizontal input
        if keys[pg.K_UP]:
            self.direction.y = -1
        elif keys[pg.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

    def animate(self, dt: float):
        """Animate the player.

        Args:
            dt (float): delta time
        """
        self.frame_index += 10 * dt
        if self.frame_index >= len(self.animation):
            self.frame_index = 0
        self.image = self.animation[int(self.frame_index)]

    def update(self, dt: float) -> None:
        """Update player.

        Args:
            dt (float): delta time
        """  # TODO: docs
        self.input()
        self.move(dt)
        self.animate(dt)
