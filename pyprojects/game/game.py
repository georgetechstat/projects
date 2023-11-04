import pygame
import settings
import level
from player import *

# TODO 1: change the way the level updates (instead of clearing layout, move the Tile objects to different cells and add more tiles if needed)
# TODO 2: create proper movement (based on acceleration, velocity)

pygame.init()

screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
pygame.display.set_caption("Shooter")
clock = pygame.time.Clock()

# initial level setup
lvl = level.Level(level.level_1)
lvl.fill_level_tiles()

plr = pygame.sprite.GroupSingle( Player((40, 40)) )
pplr = plr.sprite

keys = None

def key_handler(keys) -> None:
    if keys[pygame.K_DOWN]:
        pplr.vel[1] = 5
    
    if keys[pygame.K_RIGHT]:
        pplr.vel[0] = 5
    
    if keys[pygame.K_LEFT]:
        pplr.vel[0] = -5
    
    if keys[pygame.K_UP]:
        pplr.vel[1] = -5

def collision_handler(sp, gp) -> None:
    for tile in gp:
        if abs(tile.rect.top - pplr.rect.bottom) < 10:
            sp.rect.centery -= abs(tile.rect.top - sp.rect.bottom)
        if abs(tile.rect.bottom - sp.rect.top) < 10:
            sp.rect.centery += abs(tile.rect.bottom - sp.rect.top)
        if abs(tile.rect.right - sp.rect.left) < 10:
            sp.rect.centerx += abs(tile.rect.right - sp.rect.left)
        if abs(tile.rect.left - sp.rect.right) < 10:
            sp.rect.centerx -= abs(tile.rect.left - sp.rect.right)

while True:
    screen.fill((0, 0, 0))
    lvl.tiles.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    key_handler(pygame.key.get_pressed())
    tile_hitlist = pygame.sprite.spritecollide(pplr, lvl.tiles, False)
    if (tile_hitlist):
        collision_handler(pplr, tile_hitlist)

    plr.draw(screen)

    pygame.display.update()
    clock.tick(60)