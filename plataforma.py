import pygame
from constantes import *
from auxiliar import Auxiliar


class Platform:
    def __init__(self,x,y,height,width,image,type=0):
        self.image = Auxiliar.getSurfaceFromSpriteSheet(image,1,1)[type]
        self.image = pygame.transform.scale(self.image, (width, height))
        self.height = height
        self.width = width
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect_ground_col = pygame.Rect(self.rect.x, self.rect.y, self.rect.w, GROUND_RECT_H)


    def draw(self,screen):
        screen.blit(self.image, self.rect)
        if(DEBUG): 
            pygame.draw.rect(screen,RED, self.rect)
            pygame.draw.rect(screen,GREEN,self.rect_ground_col)


