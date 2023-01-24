import sys

import pygame as pg

from game import (
    WINDOW_WIDTH, WINDOW_HEIGHT, CLOCK, CAR_START_POSITIONS, SIMPLE_OBJECTS, LONG_OBJECTS, DISPLAY_SURFACE
)
from game.player import Player

# Groups
all_sprites = pg.sprite.Group()

# Sprites
player = Player(pos=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2), groups=all_sprites)

# game loop
while True:

    # event loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    # delta time
    dt = CLOCK.tick() / 1000

    # Draw a background
    DISPLAY_SURFACE.fill('black')

    # Update
    all_sprites.update(dt=dt)

    # Draw
    all_sprites.draw(DISPLAY_SURFACE)

    # update the display surface -> drawing the frame
    pg.display.update()
