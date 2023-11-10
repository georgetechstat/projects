import pygame
import sys
import random

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        player_walk_1 = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
        player_walk_2 = pygame.image.load("graphics/player/player_walk_2.png").convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_idx = 0
        self.player_jump = pygame.image.load("graphics/player/jump.png").convert_alpha()

        self.image = self.player_walk[self.player_idx]
        self.rect = self.image.get_rect(midbottom=(80, 300))
        self.gravity = 0
        self.jump_sound = pygame.mixer.Sound("audio/jump.mp3")
        self.jump_sound.set_volume(0.5)
    
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()
    
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        
        if self.rect.bottom >= 300:
            self.rect.bottom = 300
    
    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_idx += 0.1
            if self.player_idx >= len(self.player_walk):
                self.player_idx = 0
            self.image = self.player_walk[int(self.player_idx)]
    
    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == "fly":
            fly_1 = pygame.image.load("graphics/fly/fly1.png").convert_alpha()
            fly_2 = pygame.image.load("graphics/fly/fly2.png").convert_alpha()
            self.frames = [fly_1, fly_2]
            y_pos = 210 # y level for fly
        else:
            snail_1 = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
            snail_2 = pygame.image.load("graphics/snail/snail2.png").convert_alpha()
            self.frames = [snail_1, snail_2]
            y_pos = 300 # y level for snail
        
        self.animation_idx = 0
        self.image = self.frames[self.animation_idx]
        self.rect = self.image.get_rect(midbottom=(random.randint(900, 1100), y_pos))

    def animation_state(self):
        self.animation_idx += 0.1
        if self.animation_idx >= len(self.frames):
            self.animation_idx = 0
        self.image = self.frames[int(self.animation_idx)]
    
    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()
    
    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f'Score: {current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)
    return current_time

def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        return False
    else:
        return True

pygame.init()

screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
pygame.display.set_caption("Runner")

# Create a font
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)
game_active = False
start_time = 0
score = 0
bg_music = pygame.mixer.Sound("audio/music.wav")
bg_music.play(loops=-1)

player = pygame.sprite.GroupSingle(Player())

obstacle_group = pygame.sprite.Group()

sky_surface = pygame.image.load("graphics/Sky.png").convert() # .convert() makes blitting faster
ground_surface = pygame.image.load("graphics/ground.png").convert()

player_stand = pygame.image.load("graphics/player/player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))

game_name = test_font.render("Pixel Runner", False, (255, 255, 255))
game_name_rect = game_name.get_rect(center=(400, 50))

instruction_title = test_font.render("Press space to begin.", False, (255, 255, 255))
instruction_title_rect = instruction_title.get_rect(center=(400, 350))

#* Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(random.choice(['fly', 'snail', 'snail', 'snail'])))
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: 
                    game_active = True
                    start_time = int(pygame.time.get_ticks() / 1000)

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))

        score = display_score()

        #* player
        player.update()
        player.draw(screen)

        obstacle_group.update()
        obstacle_group.draw(screen)

        game_active = collision_sprite()
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)

        score_message = test_font.render(f"Your score: {score}", False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center=(400, 330))

        if score:
            screen.blit(score_message, score_message_rect)
        else:
            screen.blit(instruction_title, instruction_title_rect)
            
        screen.blit(game_name, game_name_rect)

    pygame.display.update()
    clock.tick(60)