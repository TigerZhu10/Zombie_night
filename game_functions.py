import pygame, sys
from slash import Slash

def Key_up(event, my_hero):
    if event.key == pygame.K_RIGHT:
        my_hero.moving_right = False
    elif event.key == pygame.K_LEFT:
        my_hero.moving_left = False
    elif event.key == pygame.K_SPACE:
        my_hero.moving_up = False
    elif event.key == pygame.K_x:
        my_hero.attacking = False

    
def Key_down(event, my_hero, screen):
    if event.key == pygame.K_RIGHT:
        my_hero.moving_right = True
    elif event.key == pygame.K_LEFT:
        my_hero.moving_left = True 
    elif event.key == pygame.K_SPACE:
        my_hero.moving_up = True
    elif event.key == pygame.K_x:
        my_hero.attacking = True
        attack_slash = Slash(screen, my_hero)

def check_mouse_key_events(my_hero, screen):
    for ev in pygame.event.get():
        # print(ev)
        if ev.type == pygame.QUIT:
            sys.exit()
        
        elif ev.type == pygame.KEYDOWN:
            Key_down(ev,my_hero, screen)
        elif ev.type == pygame.KEYUP:
            Key_up(ev,my_hero)
        

def update_screen(game_settings,screen,background,tile_map, my_hero, attack_slash):
    screen.fill(game_settings.bg_color)
    
    screen.blit(background, (0,0))

    tile_map.draw_tile_map()
    
    my_hero.display_hero()
    my_hero.hit_floor()
    my_hero.moving_hero()
    my_hero.attack()

    attack_slash.draw()


    pygame.display.flip()
