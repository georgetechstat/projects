import pygame

class LightBulb(pygame.sprite.Sprite):
    def __init__(self, gp, tl) -> None:
        super().__init__(gp)

        self.image = pygame.Surface((20, 20))
        self.rect = self.image.get_rect(topleft=tl)

        self.color_state: bool = False # 0 or 1, used for index in self.colors
        self.colors = [(255, 0, 0), (255, 255, 0)]
        
        self.image.fill((255, 0, 0)) # Red-inactive

    def update(self):
        self.color_state = not self.color_state
        self.image.fill(self.colors[self.color_state])
