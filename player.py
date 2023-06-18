from doctest import FAIL_FAST
import pygame
from constantes import *
from auxiliar import Auxiliar

class Player:
    def __init__(self,x,y,speed_walk,speed_run,gravity,jumping,frame_rate_ms,move_rate_ms,jump_height) -> None:
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/walk.png",15,1)[:12]
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/walk.png",15,1,True)[:12]
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/idle.png",16,1)
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/idle.png",16,1, True)     
        self.jump_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/jump.png",33,1,False,2)
        self.jump_l = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/jump.png",33,1,True,2)
        self.frame = 0
        self.lives = 5
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk =  speed_walk
        self.speed_run =  speed_run
        self.gravity = gravity
        self.jumping = jumping 
        self.jump_height = jump_height
        self.y_start_jump = 0
        self.animation = self.stay_r
        self.direction = DIRECTION_R
        self.image = self.animation[self.frame]
        #self.jump_height = (self.image.get_rect().top - self.image.get_rect().bottom) * 2 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.transcurred_time_move = 0
        self.transcurred_time_animation = 0
        self.frame_rate_ms = frame_rate_ms
        self.move_rate_ms = move_rate_ms
        self.is_jump = False

    def walk(self, direction):
        if self.direction != direction or (self.animation != self.walk_r and self.animation != self.walk_l):
            self.frame = 0
        self.direction = direction
        if direction == DIRECTION_R:
            self.move_x = self.speed_walk
            self.animation = self.walk_r
        else:
            self.move_x = -self.speed_walk
            self.animation = self.walk_l
            
    def jump(self,on_off = True):
        if on_off and self.is_jump == False:
            self.y_start_jump = self.rect.y
            if self.direction == DIRECTION_R:
                self.move_x = self.speed_walk
                self.animation = self.jump_r
            else:
                self.move_x = -self.speed_walk
                self.animation = self.jump_l
            self.move_y = -self.jumping
            self.frame = 0
            self.is_jump = True      
        if on_off == False:
            self.is_jump = False
            self.stay()     

    def stay(self):
        if self.animation != self.stay_r and self.animation != self.stay_l:
            if self.direction == DIRECTION_R:
                self.animation = self.stay_r
            else:
                self.animation = self.stay_l
            self.move_x = 0
            self.move_y = 0
            self.frame = 0
            
    def move(self, delta_ms):
        self.transcurred_time_move += delta_ms
        if (self.transcurred_time_move >= self.move_rate_ms):
            if(abs(self.y_start_jump) - abs(self.rect.y) > self.jump_height and self.is_jump):
                self.move_y = 0
            self.transcurred_time_move = 0
            self.rect.x += self.move_x
            self.rect.y += self.move_y  
            if(self.rect.y < 500):
                self.rect.y += self.gravity
            elif self.is_jump: #sacar
                self.jump(False)
                
    
        
    def animate(self, delta_ms):
        self.transcurred_time_animation += delta_ms
        if (self.transcurred_time_animation >= self.frame_rate_ms):
            self.transcurred_time_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
            else: 
                self.frame = 0
        
        


    def update(self,delta_ms):
        self.move(delta_ms)
        self.animate(delta_ms)
        
    def draw(self,screen):
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)
        

