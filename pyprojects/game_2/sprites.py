import pygame

class Target(pygame.sprite.Sprite):
    def __init__(self, pos, size=50):
        super().__init__()
        self.size = size
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill("Red")
        self.rect = self.image.get_rect(center=pos)

        self.creation_time = pygame.time.get_ticks()
        self.max_alive_time = 5 # seconds

        self.__max_alive_time_ticks = self.max_alive_time * 1000

    def timer(self):
        """If the object is alive for more than n seconds, remove self"""
        if self.__max_alive_time_ticks <= pygame.time.get_ticks():
            self.kill()

    def update(self):
        self.timer()

    def destroy(self):
        self.kill()
