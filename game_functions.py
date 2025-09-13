import pygame, sys

def check_mouse_key_events():
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            sys.exit()

def update_screen(game_settings,screen,background,tile_map):
    screen.fill(game_settings.bg_color)
    
    screen.blit(background, (0,0))

    tile_map.draw_tile_map()

    

    pygame.display.flip()
