import pygame
import json, os
pygame.init()

width, height = 800, 600
tile_color = (0, 255, 0)
tile_size = 40

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

TILEMAP = {
    "tile_pos": []
}

# nested array of pos=tuple(x, y)
TILE_TOPLEFT_POS = set()

tile = pygame.Surface((tile_size, tile_size))
tile.fill(tile_color)

# A rect which is created only once, isn't copied and shared among all tiles
rct = pygame.rect.Rect(0, 0, tile_size, tile_size)

while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            TILEMAP["tile_pos"] = list(TILE_TOPLEFT_POS)
            with open(os.path.join(os.getcwd(), "shooter/map.json"), "w") as f:
                f.write(json.dumps(TILEMAP))
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mx, my = pygame.mouse.get_pos()
                c = (mx // tile_size) * tile_size
                r = (my // tile_size) * tile_size
                TILE_TOPLEFT_POS.add((c, r))

    for c in range(width // tile_size):
        pygame.draw.line(screen, (0, 255, 0), (c * tile_size, 0), (c * tile_size, height))
    
    for r in range(height // tile_size):
        pygame.draw.line(screen, (0, 255, 0), (0, r * tile_size), (width, r * tile_size))

    for pos in TILE_TOPLEFT_POS:
        rct.topleft = pos
        screen.blit(tile, rct)

    pygame.display.update()
    clock.tick(60)
