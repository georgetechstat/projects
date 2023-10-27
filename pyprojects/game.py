import pygame as pg
import numpy as np

pg.init()

WIDTH, HEIGHT = 800, 600

screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

running: bool = True
dt: float = 0

class Body(pg.sprite.Sprite):
    def __init__(self, size: tuple = None, color: tuple = None) -> None:
        pg.sprite.Sprite.__init__(self)

        self.image = pg.surface.Surface(size if size else (50, 50))
        self.image.fill(color if color else (255, 0, 0))
        self.rect = self.image.get_rect()

        self.vel = np.zeros(2, dtype=float)
        self.acc = np.zeros(2, dtype=float)

    def update_pos(self, dt: float) -> None:
        self.rect.centerx = self.rect.centerx + self.vel[0] * dt
        self.rect.centery = self.rect.centery + self.vel[1] * dt
        self.vel[1] = self.vel[1] + self.acc[1]

    def update(self, dt: float) -> None:
        self.update_pos(dt)

plr = pg.sprite.GroupSingle(Body((50, 50)))
plr.sprite.rect.bottom = HEIGHT
plr.sprite.rect.centerx = WIDTH // 2

while running:
    screen.fill((0, 0, 0))
    for event in pg.event.get():
        match event.type:
            case pg.QUIT:
                pg.quit()
                exit()

    plr.update(dt=dt)
    plr.draw(screen)

    pg.display.flip()
    dt = clock.tick(60) * 0.01
