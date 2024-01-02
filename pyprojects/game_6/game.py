import pygame
import obj

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

plr = pygame.sprite.GroupSingle(obj.Player((400, 300), (50, 50), (255, 255, 0)))
gun = pygame.sprite.GroupSingle(obj.Weapon((50, 20), (60, 0)))
plr.sprite.gun = gun.sprite

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

    gun.update()
    gun.draw(screen)

    pygame.display.flip()
    clock.tick(60)
