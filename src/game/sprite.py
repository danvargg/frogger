"""Objects sprites."""
import pygame as pg


class SimpleSprite(pg.sprite.Sprite):
    """Simple sprite class."""

    def __init__(self, surf, pos, groups) -> None:
        """_summary_

        Args:
            surf (_type_): _description_
            pos (_type_): _description_
            groups (_type_): _description_
        """
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)


class LongSprite(pg.sprite.Sprite):
    """Simple sprite class."""

    def __init__(self, surf, pos, groups) -> None:
        """_summary_

        Args:
            surf (_type_): _description_
            pos (_type_): _description_
            groups (_type_): _description_
        """
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)
