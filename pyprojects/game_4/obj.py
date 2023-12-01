import pygame
import numpy as np
from copy import deepcopy

class EventManager:
    # Class variable to store events shared among all instances
    _events = []

    @classmethod
    def get_events(cls):
        return cls._events

    @classmethod
    def update_events(cls, new_events):
        cls._events = new_events

#* custom sprite with an automatic access to EventManager
class CSprite(pygame.sprite.Sprite):
    def __init__(self, pos=None, surface=None, size=None):
        super().__init__()

        if surface:
            self.image = surface
        else:
            self.image = pygame.Surface(size if size else (50, 50))
            self.image.fill((255, 0, 0))
        
        self.rect = self.image.get_rect(pos if pos else None)
        self.EventManager = EventManager

class Player(CSprite):
    def __init__(self):
        super().__init__()

        self.v = pygame.Vector2(0, 0)
        self.a = pygame.Vector2(0, 0)
        self.p = pygame.Vector2(*deepcopy(self.rect.center))
