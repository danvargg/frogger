import sys
from random import choice, randint

import pygame as pg

from game import (
    WINDOW_WIDTH, WINDOW_HEIGHT, CLOCK, CAR_START_POSITIONS, SIMPLE_OBJECTS, LONG_OBJECTS, DISPLAY_SURFACE,
    BACKGROUND_GRAPH_PATH, OVERLAY_GRAPH_PATH
)
from game.player import Player
from game.car import Car


class AllSprites(pg.sprite.Group):  # TODO: refactor
    """Group of all sprites."""

    def __init__(self):
        """Iniiate sprites group."""
        super().__init__()
        self.offset = pg.math.Vector2()
        self.bg = pg.image.load(BACKGROUND_GRAPH_PATH).convert_alpha()
        self.fg = pg.image.load(OVERLAY_GRAPH_PATH).convert_alpha()

    def customize_draw(self):
        """Customize draw method."""
        # Change offset vector
        self.offset.x = player.rect.centerx - WINDOW_WIDTH / 2
        self.offset.y = player.rect.centery - WINDOW_HEIGHT / 2

        # Blit background
        DISPLAY_SURFACE.blit(self.bg, -self.offset)

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            DISPLAY_SURFACE.blit(sprite.image, offset_pos)

        # Blit overlay
        DISPLAY_SURFACE.blit(self.fg, -self.offset)


# Groups
all_sprites = AllSprites()

# Sprites
player = Player(pos=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2), groups=all_sprites)
car_timer = pg.event.custom_type()
pg.time.set_timer(car_timer, 50)
pos_list = []

# game loop
while True:

    # event loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        if event.type == car_timer:
            random_pos = choice(CAR_START_POSITIONS)
            if random_pos not in pos_list:
                pos_list.append(random_pos)
                pos = (random_pos[0], 200, random_pos[1] + randint(-10, 10))
                Car(pos=random_pos, groups=all_sprites)
            if len(pos_list) > 5:
                pos_list.pop(0)

    # delta time
    dt = CLOCK.tick() / 1000

    # Draw a background
    DISPLAY_SURFACE.fill('black')

    # Update
    all_sprites.update(dt=dt)

    # Draw
    # all_sprites.draw(DISPLAY_SURFACE)
    all_sprites.customize_draw()

    # update the display surface -> drawing the frame
    pg.display.update()
