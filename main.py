import pygame
from settings import Settings
import game_functions
from create_background import Background

pygame.init()

game_settings = Settings()

screen = pygame.display.set_mode((game_settings.WINDOW_WIDTH, game_settings.WINDOW_HEIGHT))
pygame.display.set_caption("Zombie Night!")

background = pygame.image.load("./assets/images/background.png")
background = pygame.transform.scale(background, (game_settings.WINDOW_WIDTH, game_settings.WINDOW_HEIGHT))

tile_map = Background(game_settings,screen)


def Game_runner():
    game_running = True
    while game_running: 
        game_functions.check_mouse_key_events()
        game_functions.update_screen(game_settings,screen,background,tile_map)
Game_runner()