import pygame, json

pygame.init()

WIDTH, HEIGHT = 800, 600
tile_x, tile_y = 50, 50
active_map = "map_1"

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption("Map maker")

with open("result.json", "r") as f:
    tile_map: dict = json.loads(f.read())
    
    # Convert each subarray to tuple (To make it hashable)
    # Convert the endire nested list of tuples to a set (To prevent same coordinates being written twice)
    tile_map_pos = set(tuple(pos) for pos in tile_map[active_map])

col_total = WIDTH // tile_x
row_total = HEIGHT // tile_y

active_tile_img = pygame.Surface((tile_x, tile_y))
active_tile_img.fill((0, 255, 0))

while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open("result.json", "w") as f:
                tile_map[active_map] = list(tile_map_pos)
                f.write(json.dumps(tile_map, indent=2))
            pygame.quit()
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mx, my = pygame.mouse.get_pos()
                tx = mx // tile_x
                ty = my // tile_y
                tile_map_pos.add((tx * tile_x, ty * tile_y))
            
            if event.button == 3:
                mx, my = pygame.mouse.get_pos()
                tx = mx // tile_x
                ty = my // tile_y
                tile_map_pos.remove((tx * tile_x, ty * tile_y))

    for c in range(col_total):
        pygame.draw.line(screen, (0, 255, 0), (c * tile_x, 0), (c * tile_x, HEIGHT))
    
    for r in range(row_total):
        pygame.draw.line(screen, (0, 255, 0), (0, r * tile_y), (WIDTH, r * tile_y))
    
    for tl in tile_map_pos:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(*tl, tile_x, tile_y))

    pygame.display.update()
    clock.tick(60)
