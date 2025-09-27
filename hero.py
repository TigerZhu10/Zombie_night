import pygame, random

vector = pygame.math.Vector2

class Hero():
    def __init__(self,screen, game_settings, tile_map):
        self.screen = screen
        self.game_settings = game_settings
        self.tile_map = tile_map
        self.image = pygame.image.load("./assets/images/player/jump/idle/idle (1).png")
        self.image = pygame.transform.scale(pygame.image.load("./assets/images/player/jump/idle/idle (1).png"), (58,70))
        self.rect = self.image.get_rect()
        self.x = random.randint(440,770)
        self.y = random.randint(310, 450)

        self.moving_right = False
        self.moving_left = False

        self.position = vector(self.x, self.y)
        self.velocity = vector(0, 0)
        self.acceleration = vector(0, 0)

        self.HORIZONTAL_ACCELERATION = 1
        self.HORIZONTAL_FRICTION = 0.15
        self.VERTICAL_JUMP_SPEED = 15
        self.GRAVITY = 0.05  

    def moving_hero(self):
        self.acceleration = vector(0, self.GRAVITY)

        # HORIZONTAL_ACCELERATION change the sign, not the value
        # When keyup the if statement is false, so acceleration is always zero 
        if self.moving_right and self.rect.right <= self.game_settings.WINDOW_WIDTH:
            self.acceleration.x = self.HORIZONTAL_ACCELERATION
        if self.moving_left and self.rect.left >= 0:
            self.acceleration.x = -self.HORIZONTAL_ACCELERATION

        # You get a nagative number for acceleration when it's zero
        self.acceleration.x = self.acceleration.x - self.velocity.x * self.HORIZONTAL_FRICTION

        #Don't need to know now, it's about physics 11
        # The velocity decrease when velocity adds the acceleration which is a nagtive number
        self.velocity = self.velocity + self.acceleration
        self.position = self.position + self.velocity + 0.5 * self.acceleration

        self.rect.topleft = self.position
    
    def hit_floor(self):
        self.on_ground = False  

        for tile in self.tile_map.all_tiles:
            if self.rect.colliderect(tile):
                if self.velocity.y > 0 and self.rect.bottom <= tile.bottom:
                    self.rect.bottom = tile.top 
                    # self.position.y = self.rect.bottom
                    self.velocity.y = 0
                    self.on_ground = True



        
    def display_hero(self): 
        self.screen.blit(self.image,self.rect)
