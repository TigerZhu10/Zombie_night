import pygame, random

class Hero():
    def __init__(self,screen, game_settings):
        self.screen = screen
        self.game_settings = game_settings
        self.image = pygame.image.load("./assets/images/player/jump/idle/idle (1).png")
        self.image = pygame.transform.scale(pygame.image.load("./assets/images/player/jump/idle/idle (1).png"), (58,70))
        self.rect = self.image.get_rect()
        self.rect.topleft = (random.randint(0,game_settings.WINDOW_WIDTH - 58),random.randint(0,game_settings.WINDOW_HEIGHT - 166))

        self.moving_right = False
        self.moving_left = False

        self.position = 0

    def moving_hero(self):
        if self.moving_right and self.rect.right <= self.game_settings.WINDOW_WIDTH:
            self.position += self.game_settings.hero_velocity
        if self.moving_left and self.rect.left >= 0:
            self.position -= self.game_settings.hero_velocity

        self.rect = self.position
        
    def display_hero(self): 
        self.screen.blit(self.image,self.rect)
