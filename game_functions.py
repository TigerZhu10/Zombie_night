import pygame, sys

def Key_up(event, my_hero):
    if event.key == pygame.K_RIGHT:
        my_hero.moving_right = False
    elif event.key == pygame.K_LEFT:
        my_hero.moving_left = False
    
def Key_down(event, my_hero):
    if event.key == pygame.K_RIGHT:
        my_hero.moving_right = True
    elif event.key == pygame.K_LEFT:
        my_hero.moving_left = True 

def check_mouse_key_events(my_hero):
    for ev in pygame.event.get():
        # print(ev)
        if ev.type == pygame.QUIT:
            sys.exit()
        
        elif ev.type == pygame.KEYDOWN:
            Key_down(ev,my_hero)
        elif ev.type == pygame.KEYUP:
            Key_up(ev,my_hero)
        

def update_screen(game_settings,screen,background,tile_map, my_hero):
    screen.fill(game_settings.bg_color)
    
    screen.blit(background, (0,0))

    tile_map.draw_tile_map()

    my_hero.display_hero()

    my_hero.moving_hero()

    my_hero.hit_floor()


    

    pygame.display.flip()
