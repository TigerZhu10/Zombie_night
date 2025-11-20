import pygame, random
from pygame.sprite import Sprite
vector = pygame.math.Vector2

class Zombies(Sprite):
    def __init__(self, screen, game_settings):
        super().__init__()
        self.screen = screen
        self.game_settings = game_settings

        base = pygame.image.load("./assets/images/zombie/boy/walk/Walk (1).png").convert_alpha()
        self.image_right = pygame.transform.scale(base, (80, 80))

        self.move_left = False
        self.move_right = False
        self.flag = random.randint(0,1) # 0 = left; 1 = right
        if self.flag == 0:
            self.move_left = True
        if self.flag == 1:
            self.move_right = True

        self.rect_right = self.image_right.get_rect()
        self.rect_right.x = random.randint(0, self.game_settings.WINDOW_WIDTH)
        self.rect_right.y = random.randint(0,10)

        self.image_left = pygame.transform.flip(self.image_right, True, False)
        self.image_left = pygame.transform.scale(self.image_left, (80, 80))
        self.rect_left = self.image_left.get_rect()
        self.rect_left.topleft = (random.randint(0, self.game_settings.WINDOW_WIDTH), random.randint(0,10))

    def update(self):
        if self.move_right:
            self.rect_right.x += self.game_settings.zombie_speed
            if self.rect_right.right >= self.game_settings.WINDOW_WIDTH:
                self.rect_right.x = 0
        else:
            self.rect_left.x -= self.game_settings.zombie_speed
            if self.rect_left.left <= 0:
                self.rect_left.left = self.game_settings.WINDOW_WIDTH

    def display_zombies(self):
        if self.move_left:
            self.screen.blit(self.image_left, self.rect_left)
        else:
            self.screen.blit(self.image_right, self.rect_right)
        
