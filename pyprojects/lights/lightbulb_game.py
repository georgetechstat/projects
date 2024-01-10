import pygame
from bulbs import LightBulb as LB

class Game:
    def __init__(self) -> None:
        pygame.init()

        self.SIZE = (800, 600)
        self.screen = pygame.display.set_mode(self.SIZE)
        self.clock = pygame.time.Clock()
        self.FPS: int = 60
        self.running: bool = True

        self.run(self.FPS)
    
    def run(self, fps: int=60) -> None:
        line1_counter = 0
        line2_counter = 0

        line1 = pygame.sprite.Group()
        for r in range(2):
            for _ in range(15): LB(line1, (_ * 60, r*50))

        line2 = pygame.sprite.Group()
        for r in range(2):
            for _ in range(13): LB(line2, (_ * 60 + 30, r * 50 + 25)).color_state = True
        
        speed_ratio = 1

        while self.running:
            self.screen.fill((0, 0, 0)) # Black (0, 0, 0)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            if line1_counter == 60:
                line1.update()
                line1_counter = 0
                
            if line2_counter == 60 * speed_ratio:
                line2.update()
                line2_counter = 0
                
            line1_counter += 1
            line2_counter += 1

            line1.draw(self.screen)
            line2.draw(self.screen)

            pygame.display.update()
            self.clock.tick(fps)

if __name__ == "__main__":
    game = Game()
