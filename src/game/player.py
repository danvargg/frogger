"""Player Sprite."""
import os
import pygame as pg

from game import PLAYER_GRAPHS_PATH


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
        self.status = 'down'
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center=pos)

        # Float based movement
        self.pos = pg.math.Vector2(self.rect.center)
        self.direction = pg.math.Vector2(0, 0)
        self.speed = 200

    def import_assets(self) -> None:  # TODO: property or constructor?
        """Import player assets."""
        self.animations = {}
        for index, folder in enumerate(os.walk(PLAYER_GRAPHS_PATH)):
            if index == 0:
                for name in folder[1]:
                    self.animations[name] = []
            else:
                for file_name in folder[2]:
                    path = folder[0].replace('\\', '/') + '/' + file_name  # TODO: are the slashes ok?
                    surf = pg.image.load(path).convert_alpha()
                    key = folder[0].split('\\')[1]
                    self.animations[key].append(surf)

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
            self.status = 'right'
        elif keys[pg.K_LEFT]:
            self.direction.x = -1
            self.status = 'left'
        else:
            self.direction.x = 0

        # Horizontal input
        if keys[pg.K_UP]:
            self.direction.y = -1
            self.status = 'up'
        elif keys[pg.K_DOWN]:
            self.direction.y = 1
            self.status = 'down'
        else:
            self.direction.y = 0

    def animate(self, dt: float):
        """Animate the player.

        Args:
            dt (float): delta time
        """
        current_animation = self.animations[self.status]
        if self.direction.magnitude() != 0:
            self.frame_index += 10 * dt
            if self.frame_index >= len(current_animation):
                self.frame_index = 0
        else:
            self.frame_index = 0

        self.image = current_animation[int(self.frame_index)]

    def update(self, dt: float) -> None:
        """Update player.

        Args:
            dt (float): delta time
        """  # TODO: docs
        self.input()
        self.move(dt)
        self.animate(dt)
