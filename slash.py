import pygame
from pygame.sprite import Sprite

class Slash(Sprite):
    def __init__(self, screen, my_hero):
        super().__init__()
        self.screen = screen
        self.my_hero = my_hero
        self.image = pygame.image.load("./assets/images/player/slash.png") 
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.rect.x = my_hero.rect.x
        self.rect.y = my_hero.rect.y
        

    def attack_animate(self):
        if self.hero_attack:
            if self.my_hero.facing_right:
                self.my_hero.animate(self.my_hero.attack_right_sprites, 0.2)
            else:
                self.my_hero.animate(self.my_hero.attack_left_sprites, 0.2)

    def display_slash(self):
        if self.my_hero.facing_right:
            self.rect.x += 10

    def draw_slash(self):
        self.screen.blit(self.image, self.rect)
