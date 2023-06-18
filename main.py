import pygame
import sys
from constantes import *
from player import Player

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.init()
clock = pygame.time.Clock()

imagen_fondo = pygame.image.load("images/locations/forest/all.png")
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
player_1 = Player(x=30,y=400,speed_walk=4,speed_run=8,gravity=8,jumping=16, frame_rate_ms=30,move_rate_ms=30,jump_height=200)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
                
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
            player_1.walk(DIRECTION_R)
        if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            player_1.walk(DIRECTION_L)
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]and not keys[pygame.K_SPACE]:
            player_1.stay()
        if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]:
            player_1.stay()
        if keys[pygame.K_SPACE]:
            player_1.jump() 
        
        
    delta_ms = clock.tick(FPS)
    screen.blit(imagen_fondo,imagen_fondo.get_rect())
   
    player_1.update(delta_ms)
    player_1.draw(screen)
    
    # enemigos update
    # player dibujarlo
    # dibujar todo el nivel

    pygame.display.flip()
    
 



    






