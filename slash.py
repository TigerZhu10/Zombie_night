import pygame


class Slash:
    def __init__(self, screen, my_hero):
        self.screen = screen
        self.image = pygame.image.load("./assets/images/player/slash.png") 
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.rect.x = my_hero.rect.x
        self.rect.y = my_hero.rect.y

    def draw(self):
        self.screen.blit(self.image, self.rect)
