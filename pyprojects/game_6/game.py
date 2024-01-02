import pygame
import obj

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

plr = obj.PlayerSingle(obj.Player((400, 300), (50, 50), (255, 255, 0)))

while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                plr.sprite.vel[1] = -20
    
    plr.update()
    plr.draw(screen)

    pygame.display.flip()
    clock.tick(60)
