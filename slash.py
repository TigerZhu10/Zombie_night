import pygame
from pygame.sprite import Sprite

class Slash(Sprite):
    def __init__(self, screen, my_hero, game_settings):
        super().__init__()
        self.screen = screen
        self.my_hero = my_hero
        self.game_settings = game_settings
        self.image_right = pygame.image.load("./assets/images/player/slash.png") 
        self.image_right = pygame.transform.scale(self.image_right, (64, 64))
        self.rect_right = self.image_right.get_rect()
        self.rect_right.x = my_hero.rect.x
        self.rect_right.y = my_hero.rect.y
        
        self.image_left = [pygame.transform.flip(self.rect_right, True, False)]
        self.image_left = pygame.transform.scale(self.image_left, (64, 64))
        self.rect_left = self.image_left.get_rect()
        self.rect_left.x = my_hero.rect.x
        self.rect_left.y = my_hero.rect.y
        

    # def attack_animate(self):
    #     if self.hero_attack:
    #         if self.my_hero.facing_right:
    #             self.my_hero.animate(self.my_hero.attack_right_sprites, 0.2)
    #         else:
    #             self.my_hero.animate(self.my_hero.attack_left_sprites, 0.2)

    def display_slash(self):
        if self.my_hero.facing_right:
            self.rect_right.x += self.game_settings.slash_speed
        else:
            self.rect_left.x -= self.game_settings.slash_speed

    def draw_slash(self):
        self.screen.blit(self.image_right, self.rect_right)
        self.screen.blit(self.image_left, self.rect_left)
