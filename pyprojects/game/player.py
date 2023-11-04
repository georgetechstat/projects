import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, size: tuple, color: tuple = None, initial_coordinates: tuple = None) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface(size)
        self.image.fill(color if color else (255, 60, 0))
        
        if initial_coordinates:
            self.rect = self.image.get_rect(topleft=initial_coordinates)
        else:
            self.rect = self.image.get_rect()
        
        self.vel = [0, 0]

    def update(self) -> None:
        self.rect.centerx += self.vel[0]
        self.rect.centery += self.vel[1]