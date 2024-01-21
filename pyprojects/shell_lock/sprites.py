import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, gp):
        super().__init__(gp)
        self.original = pygame.Surface((50, 50), pygame.SRCALPHA)
        self.original.fill((255, 0, 0))

        self.image = self.original
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
    
        self.acc = pygame.Vector2((0, 0))
        self.vel = pygame.Vector2((0, 0))

    def update(self) -> None:
        self.vel += self.acc
        self.rect.center += self.vel

class Tile(pygame.sprite.Sprite):
    def __init__(self, gp, src_img, pos):
        super().__init__(gp)

        self.original = src_img
        self.image = self.original
        self.rect = self.image.get_rect(topleft=pos)
