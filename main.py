import pygame
from settings import Settings
import game_functions

pygame.init()

game_settings = Settings()

screen = pygame.display.set_mode((game_settings.WINDOW_WIDTH, game_settings.WINDOW_HEIGHT))
pygame.display.set_caption("Zombie Night!")


def Game_runner():
    game_running = True
    while game_running:
        game_functions.check_mouse_key_events()
        game_functions.update_screen(game_settings,screen)
Game_runner()