import pygame, sys, random

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption("Pong")
active = False
score = [0, 0]

class Bar_1(pygame.sprite.Sprite):
    def __init__(self, pos: tuple, size: tuple=None) -> None:
        super().__init__()

        self.image = pygame.Surface((20, 100) if not size else size)
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(topleft=pos)
        self.directiony = 0
    
    def movement(self) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_DOWN]:
            self.rect.y += 5
            self.directiony = 1
        
        if keys[pygame.K_UP]:
            self.rect.y -= 5
            self.directiony = -1
        
        if not (keys[pygame.K_DOWN] or keys[pygame.K_UP]):
            self.directiony = 0
    
    def update(self):
        self.movement()

class Bar_2(Bar_1):
    def movement(self) -> None:
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_s]:
            self.rect.y += 5
            self.directiony = 1

        if keys[pygame.K_w]:
            self.rect.y -= 5
            self.directiony = -1
        
        if not (keys[pygame.K_s] or keys[pygame.K_w]):
            self.directiony = 0

class Ball(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        global width, height
        self.directionx = 0
        self.directiony = 0
        self.vel = 5

        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=(width / 2, height / 2))

    def update(self):
        global active, score, score_left, score_right, font

        if self.rect.top <= 0:
            self.directiony = 1
        
        if self.rect.bottom >= 600:
            self.directiony = -1

        if self.rect.left <= 0:
            active = False
            score[1] += 1
            score_right = font.render(f"{score[1]}", False, (255, 255, 255))
        
        if self.rect.right >= 800:
            active = False
            score[0] += 1
            score_left = font.render(f"{score[0]}", False, (255, 255, 255))
        
        self.rect.x += self.directionx * self.vel
        self.rect.y += self.directiony * self.vel

bars = pygame.sprite.Group(Bar_1((760, 250)), Bar_2((20, 250)))
ball = pygame.sprite.GroupSingle(Ball())

font = pygame.font.Font(None, 40)
score_left = font.render(f"{score[0]}", False, (255, 255, 255))
score_right = font.render(f"{score[1]}", False, (255, 255, 255))
score_left_rect = score_left.get_rect(center=(200, 50))
score_right_rect = score_right.get_rect(center=(600, 50))

start_text = font.render("PRESS SPACE TO START", False, (255, 255, 255))
start_text_rect = start_text.get_rect(center=(400, 100))

while True:
    screen.fill((0, 0, 0))
    screen.blit(score_left, score_left_rect)
    screen.blit(score_right, score_right_rect)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if not active and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                active = True
                ball.sprite.directionx = random.choice((-1, 1))
                ball.sprite.directiony = random.choice((-1, 1))
    
    if active:
        hits = pygame.sprite.spritecollide(ball.sprite, bars, False)
        bars.update()

        if hits:
            ball.sprite.directiony = hits[0].directiony
            ball.sprite.directionx = -ball.sprite.directionx

        ball.update()
        bars.draw(screen)
        ball.draw(screen)
    else:
        ball.sprite.directionx = 0
        ball.sprite.directiony = 0
        ball.sprite.rect.center = (400, 300)
        
        for bar in bars.sprites():
            bar.directiony = 0
            bar.rect.top = 250

        bars.draw(screen)
        ball.draw(screen)
        ball.update()
        bars.update()

        screen.blit(start_text, start_text_rect)

    pygame.display.flip()
    clock.tick(60)
