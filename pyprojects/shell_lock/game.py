import pygame
from sprites import Player, Tile

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Shell Lock")
dt: float = 0

tiles = pygame.sprite.Group()

while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    tiles.draw(screen)

    pygame.display.update()
    dt = clock.tick(60) / 1000
