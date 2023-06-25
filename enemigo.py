from doctest import FAIL_FAST
import pygame
from constantes import *
from auxiliar import Auxiliar
from player import Player
from loot import Loot

class Enemy():
    def __init__(self,x,y,speed_walk,speed_run,gravity,frame_rate_ms,move_rate_ms, x_length, enemy_type):
        self.enemy_type = enemy_type
        
        if enemy_type == 0: #MUSHROOM
            self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("images/enemies/mushroom_walk_r.png",7,1,scale=DEFAULT_ENEMY_SIZE)
            self.walk_l =  Auxiliar.getSurfaceFromSpriteSheet("images/enemies/mushroom_walk_l.png",7,1,scale=DEFAULT_ENEMY_SIZE)
            self.stay_r = Auxiliar.getSurfaceFromSpriteSheet("images/enemies/mushroom_walk_l.png",7,1,scale=DEFAULT_ENEMY_SIZE)
            self.stay_l = Auxiliar.getSurfaceFromSpriteSheet("images/enemies/mushroom_walk_r.png",7,1,scale=DEFAULT_ENEMY_SIZE)
            
        elif enemy_type == 1: #ONEYE
            self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("images/enemies/oneye_walk_r.png",8,1,scale=DEFAULT_ENEMY_SIZE)
            self.walk_l =  Auxiliar.getSurfaceFromSpriteSheet("images/enemies/oneye_walk_l.png",8,1,scale=DEFAULT_ENEMY_SIZE)
            self.stay_r = Auxiliar.getSurfaceFromSpriteSheet("images/enemies/oneye_walk_l.png",8,1,scale=DEFAULT_ENEMY_SIZE)
            self.stay_l = Auxiliar.getSurfaceFromSpriteSheet("images/enemies/oneye_walk_r.png",8,1,scale=DEFAULT_ENEMY_SIZE)                    
        #self.jump_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/jump.png",33,1,False,2,scale=DEFAULT_ENEMY_SIZE)
        #self.jump_l = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/jump.png",33,1,True,2,scale=DEFAULT_ENEMY_SIZE)
        self.frame = 0
        self.move_x = 0
        self.move_y = 0
        self.x_length = x_length
        self.initial_x = x
        self.movement_right = True
        self.speed_walk =  speed_walk
        self.speed_run =  speed_run
        self.gravity = gravity
        self.y_start_jump = 0
        self.animation = self.stay_r
        self.direction = DIRECTION_R
        self.image = self.animation[self.frame]
        #self.jump_height = (self.image.get_rect().top - self.image.get_rect().bottom) * 2 
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y
        self.rect.h = self.rect.h / 1.3
        self.rect.w = self.rect.w 
        self.transcurred_time_move = 0
        self.transcurred_time_animation = 0
        self.frame_rate_ms = frame_rate_ms
        self.move_rate_ms = move_rate_ms
        self.mask = pygame.mask.from_surface(self.image)
        self.rect_ground_col = pygame.Rect(self.rect.x + self.rect.w / 4, self.rect.y + self.rect.h - GROUND_RECT_H, self.rect.w / 2, GROUND_RECT_H)
       
       
    def draw(self,screen):
        if(DEBUG): 
            pygame.draw.rect(screen,RED, self.rect)      
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)
        
    def animate(self, delta_ms):
        self.transcurred_time_animation += delta_ms
        if (self.transcurred_time_animation >= self.frame_rate_ms):
            self.transcurred_time_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
            else: 
                self.frame = 0          

    def update(self,delta_ms):
        self.animate(delta_ms)
        self.move()    
        
    def increment_x(self,delta_x):
        self.rect.x += delta_x

    def increment_y(self,delta_y):
        self.rect.y += delta_y
        
    def move(self):
        if self.movement_right:
            self.increment_x(self.speed_walk)
            self.animation = self.walk_r
            if self.rect.x > self.initial_x + self.x_length:
                self.movement_right = False
        else:
            self.increment_x(-self.speed_walk)
            self.animation = self.walk_l
            if self.rect.x < self.initial_x - self.x_length:
                self.movement_right = True

