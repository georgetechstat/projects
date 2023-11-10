import pygame, sys, random
from sprites import Target
import numpy as np

# TODO: add Target spawn logic: if generated_target collides with others: create new spawn (repeat until not colliding)

class Game:
    def __init__(self, screensize: tuple | list) -> None:
        self.width = screensize[0]
        self.height = screensize[1]
        self.fps = 60
        
        pygame.init()

        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Target practice")

        self.active: bool = True
        self.targets = pygame.sprite.Group()
        self.bg_color = np.array([135, 206, 235])

    def run(self):
        self.targets.add(Target((200, 300)))
        while True:
            self.screen.fill(self.bg_color)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if self.active:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        for target in self.targets:
                            if target.rect.collidepoint(event.pos):
                                target.destroy()

            if self.active:
                self.targets.update()
                self.targets.draw(self.screen)
            else:
                pass

            pygame.display.update()
            self.clock.tick(60)

if __name__ == "__main__":
    game = Game((800, 600))
    game.run()
