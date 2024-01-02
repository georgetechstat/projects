import pygame
import math
from pygame import Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, size, color) -> None:
        super().__init__()

        self.original = pygame.Surface(size, pygame.SRCALPHA)
        self.original.fill(color)

        self.image = self.original
        self.rect = self.image.get_rect(center=pos)

        self.gun = None
        
        self.vel = Vector2((0, 0))
        self.acc = Vector2((0, 1))

    def update_inv(self):
        self.gun.rect.x += self.vel[0]
        self.gun.rect.y += self.vel[1]
        self.gun.pivot.update(self.rect.center)

    def update_pos(self):
        self.vel += self.acc
        self.rect.centery += self.vel.y

        if self.rect.bottom > 600:
            self.rect.bottom = 600
            self.vel[1] = 0

    def update(self) -> None:
        self.update_pos()
        self.update_inv()

class Weapon(pygame.sprite.Sprite):
    def __init__(self, size, offset) -> None:
        super().__init__()

        self.original = pygame.Surface(size, pygame.SRCALPHA)
        self.original.fill((100, 100, 100))

        self.pivot = Vector2((400, 300))

        self.image = self.original
        self.rect = self.image.get_rect(center=self.pivot + offset)

    def mouse_rotation(self) -> None:
        mx, my = pygame.mouse.get_pos()
        angle_rad = math.atan2(my - self.pivot.y, mx - self.pivot.x)
        radius = self.pivot.distance_to(self.rect.center)

        self.rect.centerx = self.pivot.x + radius * math.cos(angle_rad)
        self.rect.centery = self.pivot.y + radius * math.sin(angle_rad)

        self.image = pygame.transform.rotate(self.original, -math.degrees(angle_rad))
        self.rect = self.image.get_rect(center=self.rect.center)
    
    def update(self):
        self.mouse_rotation()
