import pygame
import json
import os
from sprites import Tile

pygame.init()

with open(os.path.join(os.getcwd(), "shooter/settings.json"), "r") as f:
    global SETTINGS
    SETTINGS = json.loads(f.read())

with open(os.path.join(os.getcwd(), "shooter/map.json"), "r") as f:
    global TILEMAP
    TILEMAP = json.loads(f.read())["tile_pos"]

# initial definitions
WIDTH = SETTINGS["GAME_SETTINGS"]["width"]
HEIGHT = SETTINGS["GAME_SETTINGS"]["height"]
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
###

tilegp = pygame.sprite.Group()
for pos in TILEMAP:
    tilegp.add(Tile(pos))

while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    tilegp.draw(screen)

    pygame.display.update()
    clock.tick(60)
