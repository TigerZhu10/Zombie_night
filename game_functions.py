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
        my_hero.hero_attack = False
    
def Key_down(event, my_hero, screen, slash_group, game_settings):
    if event.key == pygame.K_RIGHT:
        my_hero.moving_right = True
    elif event.key == pygame.K_LEFT:
        my_hero.moving_left = True 
    elif event.key == pygame.K_SPACE:
        my_hero.moving_up = True
    elif event.key == pygame.K_x:
        current_time = pygame.time.get_ticks()
        if current_time - game_settings.last_attack_time >= game_settings.attack_cooldown:
            slash_group.add(Slash(screen, my_hero, game_settings))
            my_hero.hero_attack = True
            game_settings.last_attack_time = current_time
        

def update_slash(slash_group, game_settings):
    for slash in slash_group.sprites():
        # slash.draw_slash()
        slash.display_slash()

    # delete the slash when it's out of the screen
    for slash in slash_group.copy():
        if slash.rect_right.x >= game_settings.WINDOW_WIDTH or slash.rect_left.x <= 0:
            slash_group.remove(slash)
        # print(len(slash_group))

def check_zombie_slash_collisions(slash_group, walker_zombies):
    for slash in slash_group.copy():
        if slash.frozen_facing_right:
            slash_rect = slash.rect_right
        else:
            slash_rect = slash.rect_left

        for z in walker_zombies.zombies.copy():
            if slash_rect.colliderect(z["rect"]):
                walker_zombies.zombies.remove(z)
                slash_group.remove(slash)


def check_mouse_key_events(game_settings, my_hero, screen, slash_group):
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            sys.exit()
        
        elif ev.type == pygame.KEYDOWN:
            Key_down(ev,my_hero, screen, slash_group, game_settings)
        elif ev.type == pygame.KEYUP:
            Key_up(ev,my_hero)
        

def update_screen(game_settings,screen,background,tile_map, my_hero, slash_group, walker_zombies):
    screen.fill(game_settings.bg_color)
    
    screen.blit(background, (0,0))

    tile_map.draw_tile_map()
    
    my_hero.display_hero()
    my_hero.hit_floor()
    my_hero.moving_hero()
    my_hero.attack_animate()

    walker_zombies.update()
    walker_zombies.display_zombies()

    check_zombie_slash_collisions(slash_group, walker_zombies)

    update_slash(slash_group, game_settings)



    pygame.display.flip()

