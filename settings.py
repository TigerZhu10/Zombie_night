import pygame, random

class Settings():
    def __init__(self):
        self.WINDOW_WIDTH = 1280
        self.WINDOW_HEIGHT = 768

        self.bg_color = (0,0,0)

        self.tile_size = 32

        self.slash_speed = 10

        self.boy_zombie_speed = random.randint(1,6)
        self.girl_zombie_speed = random.randint(1,6)

        self.zombie_random_spawn_time = random.randint(3000,6000)
        self.zombie_random_spawn_number = random.randint(2,5)
        self.zombie_spawned_count = 0
        self.max_zombies_round = 10

        self.round = 1

        self.GRAVITY = 0.45
        self.SIZE = (80, 80)