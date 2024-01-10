import pygame
import json
import os
from typing import Iterable

tile_img = pygame.Surface((40, 40))
tile_img.fill((0, 255, 0))

class Tile(pygame.sprite.Sprite):
    def __init__(self, topleft):
        super().__init__()

        self.image = tile_img
        self.rect = self.image.get_rect(topleft=topleft)
