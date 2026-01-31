import pygame, random

vector = pygame.math.Vector2

class Hero():
    def __init__(self,screen, game_settings, tile_map):
        self.screen = screen
        self.game_settings = game_settings
        self.tile_map = tile_map


        self.idle_right_sprites = self.load_images("./assets/images/player/jump/idle/", "idle",  9)
        self.idle_left_sprites = [pygame.transform.flip(s, True, False) for s in self.idle_right_sprites]

        self.moving_right_sprites = self.load_images("./assets/images/player/run/", "Run", 9)
        self.moving_left_sprites = [pygame.transform.flip(s, True, False) for s in self.moving_right_sprites]

        self.jump_right_sprites = self.load_images("./assets/images/player/jump/", "Jump", 9)
        self.jump_left_sprites = [pygame.transform.flip(s, True, False) for s in self.jump_right_sprites]

        self.attack_right_sprites = self.load_images("./assets/images/player/attack/", "Attack", 9)
        self.attack_left_sprites = [pygame.transform.flip(s, True, False) for s in self.attack_right_sprites]
        
        
        # starting image
        self.image = self.idle_right_sprites[0]
        self.rect = self.image.get_rect()
        self.facing_right = True
        self.current_sprite = 0

        self.x = random.randint(440,770)
        self.y = random.randint(310, 450)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.hero_attack = False

        self.position = vector(self.x, self.y)
        # Ensure initial draw/spawn uses the randomized position
        self.rect.topleft = self.position
        self.velocity = vector(0, 0)
        self.acceleration = vector(0, 0)

        self.HORIZONTAL_ACCELERATION = 1
        self.HORIZONTAL_FRICTION = 0.15
        self.VERTICAL_JUMP_SPEED = 12
        self.GRAVITY = 0.45

        self.on_ground = False

    def moving_hero(self):
        self.acceleration = vector(0, self.GRAVITY)
        # HORIZONTAL_ACCELERATION change the sign, not the value
        # When keyup the if statement is false, so acceleration is always zero 
        if self.moving_right and self.rect.right <= self.game_settings.WINDOW_WIDTH:
            self.acceleration.x = self.HORIZONTAL_ACCELERATION
            self.facing_right = True
            if self.on_ground and self.moving_up:
                self.jump_right()

            elif not self.on_ground:
                self.animate(self.jump_right_sprites, 0.2)
            else: 
                self.animate(self.moving_right_sprites, 0.3)
        
        elif self.moving_left and self.rect.left >= 0:
            self.acceleration.x = -self.HORIZONTAL_ACCELERATION
            self.facing_right = False
            if self.on_ground and self.moving_up:
                self.jump_left()
            elif not self.on_ground:
                self.animate(self.jump_left_sprites, 0.2)
            else:
                self.animate(self.moving_left_sprites, 0.3)
                
        elif self.facing_right:
            if self.on_ground and self.moving_up:
                self.jump_right()
            elif not self.on_ground:
                self.animate(self.jump_right_sprites, 0.2)
            else:
                self.animate(self.idle_right_sprites, 0.2)

        else:
            if self.on_ground and self.moving_up:
                self.jump_left()
            elif not self.on_ground:
                self.animate(self.jump_left_sprites, 0.2)
            else:
                self.animate(self.idle_left_sprites, 0.2)

        # You get a nagative number for acceleration when it's zero
        self.acceleration.x = self.acceleration.x - self.velocity.x * self.HORIZONTAL_FRICTION

        # Don't need to know now, it's about physics 11
        # The velocity decrease when velocity adds the acceleration which is a nagtive number
        self.velocity = self.velocity + self.acceleration
        self.position = self.position + self.velocity + 0.5 * self.acceleration

        self.rect.topleft = self.position

    def load_images(self, folder, prefix, count):
        """
        批量加载并缩放动画帧
        folder: 子文件夹名 (如 "boy")
        prefix: 文件名前缀 (如 "Run")
        count: 帧数量
        """
        return [
            pygame.transform.scale(
                pygame.image.load(f"{folder}/{prefix} ({i}).png"), (64, 64)
            ) 
            for i in range(1, count + 1)# count is 8 so the range is from 1 to (8+1) and you will get a value from 1 to 8
        ]   
    
    def hit_floor(self):
        # self.on_ground = False

        for tile in self.tile_map.all_tiles_rect:
            if self.rect.colliderect(tile):
                if self.velocity.y > 0 and self.rect.bottom <= tile.bottom:
                    self.rect.bottom = tile.top 
                    self.position.y = self.rect.top
                    self.velocity.y = 0
                    self.on_ground = True                        

    def animate(self, sprite_list, speed):
        """
        播放指定动画帧列表
        sprite_list: 图像帧序列
        speed: 帧切换速度（建议 0.1 ~ 0.3)
        """
        self.current_sprite = (self.current_sprite + speed) % len(sprite_list)
        self.image = sprite_list[int(self.current_sprite)]

    def jump_left(self):
        self.velocity.y = -self.VERTICAL_JUMP_SPEED
        self.animate(self.jump_left_sprites, 0.2)
        self.on_ground = False

    def jump_right(self):
        self.velocity.y = -self.VERTICAL_JUMP_SPEED
        self.animate(self.jump_right_sprites, 0.2)
        self.on_ground = False
    
    def attack_animate(self):
        if self.hero_attack:
            if self.facing_right:
                self.animate(self.attack_right_sprites, 0.2)
            else:
                self.animate(self.attack_left_sprites, 0.2)
        
    def display_hero(self): 
        self.screen.blit(self.image,self.rect)
