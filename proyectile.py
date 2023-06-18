from doctest import FAIL_FAST
import pygame
from constantes import *
from auxiliar import Auxiliar

class Proyectile:
    def __init__(self,speed,x,y,direction) -> None:
        self.sprite_left = Auxiliar.getSurfaceFromSpriteSheet("images/bullet01_l.png",1,1)[0]
        self.sprite_right = Auxiliar.getSurfaceFromSpriteSheet("images/bullet01_r.png",1,1)[0]
        self.image = self.sprite_right
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.direction = direction

    def draw(self,screen):
        if(DEBUG): 
            pygame.draw.rect(screen,RED, self.rect)     
            pygame.draw.rect(screen,GREEN, self.rect_ground_col)
        if self.direction == DIRECTION_L:
                self.image = self.sprite_left
        screen.blit(self.image,self.rect)

    def update(self,enemy_list):
        if self.direction == DIRECTION_L:
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
        self.collide(enemy_list)

    def collide(self,enemy_list):
        for enemy in enemy_list:
            if self.rect.colliderect(enemy.rect):
                enemy_list.remove(enemy)