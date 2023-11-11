import pygame, random
import numpy as np

class Target(pygame.sprite.Sprite):
    def __init__(self, pos, size=50, min_alive_time=2, max_alive_time=5, random_alive_time: bool = False, target_img=None):
        super().__init__()
        self.size = size
        if target_img:
            self.image = pygame.transform.scale(target_img, (size, size))
        else:
            self.image = pygame.Surface((size, size))
            self.image.fill("Red")
        self.rect = self.image.get_rect(center=pos)

        self.creation_time = pygame.time.get_ticks()
        self.min_alive_time = min_alive_time # seconds
        self.max_alive_time = max_alive_time # seconds
        self.random_alive_time = random_alive_time

        self.min_alive_time_ticks = self.min_alive_time * 1000
        self.max_alive_time_ticks = self.max_alive_time * 1000

    def timer(self):
        """If the object is alive for more than n seconds, remove self"""

        # alive: amount of ticks the object has been alive for
        currently_alive_time = pygame.time.get_ticks() - self.creation_time
        
        if self.random_alive_time:
            if currently_alive_time >= random.randint(self.min_alive_time_ticks, self.max_alive_time_ticks):
                self.kill()
        else:
            if self.max_alive_time_ticks <= currently_alive_time:
                self.kill()

    def update(self):
        self.timer()

    def destroy(self):
        self.kill()

class TargetManager:
    def __init__(self, surface) -> None:
        self.surface: pygame.Surface = surface
        self.surface_rect = self.surface.get_rect()
        self.targets = pygame.sprite.Group()
        self.target_img = pygame.image.load("images/target.png").convert_alpha()
        self._population_size: int = 5
        self.__max_population_size: int = 20

    @property
    def population_size(self) -> int:
        return self._population_size

    @population_size.setter
    def population_size(self, size: int) -> None:
        if isinstance(size, int):
            if size <= self.__max_population_size:
                self._population_size = size
            else:
                print(f"Population size must be below or equal to {self.__max_population_size}")
        else:
            print(f"population size must be of type int, not {type(size)}")

    def target_mouse_response(self):
        pos = pygame.mouse.get_pos()
        for sprite in self.targets.sprites():
            if sprite.rect.collidepoint(pos):
                sprite.destroy()

    def __random_pos(self):
        random_x = random.randint(self.surface_rect.left, self.surface_rect.right)
        random_y = random.randint(self.surface_rect.top, self.surface_rect.bottom)
        return (random_x, random_y)

    def create_target(self, pos=None, size=100, min_alive_time:float=2, max_alive_time:float=5, random_alive_time:bool=False) -> None:
        if pos:
            self.targets.add( Target(pos, size, min_alive_time, max_alive_time, random_alive_time, self.target_img) )
        else:
            taken_area = size**2 * self.targets.__len__()
            surface_size = self.surface.get_size()

            if taken_area + size ** 2 >= surface_size[0] * surface_size[1]:
                print("Area exceeded")
                return
            
            target = Target(self.__random_pos(), size, min_alive_time, max_alive_time, random_alive_time, self.target_img)

            while pygame.sprite.spritecollide(target, self.targets, False):
                target.rect.center = self.__random_pos()

            self.targets.add(target)
    
    def update(self):
        if self.targets.__len__() < self.population_size:
            self.create_target()
