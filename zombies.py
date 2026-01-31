import random
import pygame
from pygame.sprite import Sprite

vector = pygame.math.Vector2


class Zombies(Sprite):

    def __init__(self, screen, game_settings, tile_map):
        super().__init__()
        self.screen = screen
        self.game_settings = game_settings
        self.tile_map = tile_map


        # 0 = left, 1 = right
        self.move_right = bool(random.randint(0, 1))

        # Load images once
        self.images = self._load_images()

        # Create zombies (each has: pos, vel, rect, kind)
        self.zombies = []

        self.next_spawn_time = pygame.time.get_ticks()

        self.randomize_round_settings()
        


    def randomize_round_settings(self):
        self.boy_zombie_speed = random.randint(1,6)
        self.girl_zombie_speed = random.randint(1,6)
        self.zombie_random_spawn_time = random.randint(3000,6000)
        self.zombie_random_spawn_number = random.randint(2,5)

    def _load_images(self):
        def load_pair(path):
            img_r = pygame.image.load(path).convert_alpha()
            img_r = pygame.transform.scale(img_r, self.game_settings.SIZE)
            img_l = pygame.transform.flip(img_r, True, False)
            return {"right": img_r, "left": img_l}

        return {
            "boy": load_pair("./assets/images/zombie/boy/walk/Walk (1).png"),
            "girl": load_pair("./assets/images/zombie/girl/walk/Walk (1).png"),
        }

    def _random_spawn(self):
        x = random.randint(0, self.game_settings.WINDOW_WIDTH)
        y = random.randint(0, 10)
        return vector(x, y)

    def _create_zombie(self, kind: str):
        pos = self._random_spawn()
        rect = self.images[kind]["right"].get_rect(topleft=pos)
        if kind == "boy":
            speed = self.boy_zombie_speed
        else:
            speed = self.girl_zombie_speed

        return {
            "kind": kind,
            "pos": pos,
            "vel": vector(0, 0),
            "rect": rect,
            "on_ground": False,
            "speed" : speed,
        }
    
    def spawn_one_zombie(self):
        zombie_random_spawn_number = random.randint(2,5)
        for _ in range(zombie_random_spawn_number):
            kind = random.choice(["boy", "girl"])
            self.zombies.append(self._create_zombie(kind))
            self.game_settings.zombie_spawned_count += 1


        self.zombie_random_spawn_time = random.randint(3000,6000)
        self.next_spawn_time = pygame.time.get_ticks() + self.zombie_random_spawn_time


    def update(self):
        self.zombie_spawn_rounds()
        self._move_horizontal()
        self._apply_gravity_and_fall()
        self._sync_rects()
        self._hit_floor()

    def zombie_spawn_rounds(self):

        now = pygame.time.get_ticks()

        if self.game_settings.zombie_spawned_count < self.game_settings.max_zombies_round and now >= self.next_spawn_time:
            self.spawn_one_zombie()

    def _move_horizontal(self):
        for z in self.zombies:
            speed = z["speed"]
            dx = speed if self.move_right else -speed
            z["pos"].x += dx

            if self.move_right and z["rect"].left >= self.game_settings.WINDOW_WIDTH:
                z["pos"].x = 0
            elif (not self.move_right) and z["rect"].right <= 0:
                z["pos"].x = self.game_settings.WINDOW_WIDTH


    def _apply_gravity_and_fall(self):
        for z in self.zombies:
            z["on_ground"] = False
            acc = vector(0, self.game_settings.GRAVITY)

            z["vel"] += acc
            z["pos"] += z["vel"] + 0.5 * acc
    
    def _sync_rects(self):
        for z in self.zombies:
            z["rect"].topleft = (z["pos"].x, z["pos"].y)

    def _hit_floor(self):
        tiles = self.tile_map.all_tiles_rect

        for z in self.zombies:
            for tile in tiles:
                if z["rect"].colliderect(tile):
                    if z["rect"].bottom <= tile.bottom:
                        z["rect"].bottom = tile.top
                        z["pos"].y = z["rect"].top
                        z["vel"].y = 0
                        z["on_ground"] = True


    def display_zombies(self):
        direction = "right" if self.move_right else "left"
        for z in self.zombies:
            img = self.images[z["kind"]][direction]
            self.screen.blit(img, z["rect"])
