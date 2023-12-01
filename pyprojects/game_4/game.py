import pygame
from obj import EventManager

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running: bool = True

sprites = pygame.sprite.Group()

while running:
    EventManager.update_events(pygame.event.get())    
    for event in EventManager.get_events():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    pygame.display.update()
    clock.tick(60)
