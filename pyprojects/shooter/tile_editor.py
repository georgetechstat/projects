import pygame
import json, os
pygame.init()

width, height = 800, 600
tile_color = (0, 255, 0)
tile_size = 40
MAP_PATH = os.path.join(os.getcwd(), "shooter/map.json") # Default path, you can change to other map path

with open(MAP_PATH, "r") as f:
    TILEMAP = json.loads(f.read())

    #*EXPLANATION OF THE LINE BELOW:
    # Inside the json file, TILEMAP["tile_pos"] is a nested list list[list[int, int]]
    #*This project uses the ability of a set to store unique coordinates.
    #!However, a set cannot identify list's "uniqueness" because of its unhashability, so, to fix this:
    # Convert each sublist into a tuple (An immutable hashable iterable)
    # and then convert the list[tuple[int, int]] into a set set[tuple[int, int]]

    TILE_TOPLEFT_POS = set([tuple(sublist) for sublist in TILEMAP["tile_pos"]])

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

tile = pygame.Surface((tile_size, tile_size))
tile.fill(tile_color)

# A rect which is created only once, isn't copied and shared among all tiles
rct = pygame.rect.Rect(0, 0, tile_size, tile_size)

def draw_rows():
    global screen, height, tile_size
    for r in range(height // tile_size):
        pygame.draw.line(screen, (0, 255, 0), (0, r * tile_size), (width, r * tile_size))

def draw_cols():
    global screen, width, tile_size
    for c in range(width // tile_size):
        pygame.draw.line(screen, (0, 255, 0), (c * tile_size, 0), (c * tile_size, height))

def draw_rects():
    global TILE_TOPLEFT_POS, rct, screen
    for pos in TILE_TOPLEFT_POS:
        rct.topleft = pos
        screen.blit(tile, rct)

def quit_map():
    global TILEMAP, TILE_TOPLEFT_POS
    TILEMAP["tile_pos"] = list(TILE_TOPLEFT_POS)
    with open(os.path.join(os.getcwd(), "shooter/map.json"), "w") as f:
        f.write(json.dumps(TILEMAP))

def get_tile_tl_pos():
    """
    Returns topleft of a tile (col, row) || (x, y)
    """
    mx, my = pygame.mouse.get_pos()
    c = (mx // tile_size) * tile_size
    r = (my // tile_size) * tile_size
    return (c, r)

while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit_map()
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                TILE_TOPLEFT_POS.add(get_tile_tl_pos())
            
            if event.button == 3:
                tile_tl_pos = get_tile_tl_pos()
                if tile_tl_pos in TILE_TOPLEFT_POS:
                    TILE_TOPLEFT_POS.remove(tile_tl_pos)

    draw_cols()
    draw_rows()
    draw_rects()

    pygame.display.update()
    clock.tick(60)
