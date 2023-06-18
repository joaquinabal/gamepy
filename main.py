import pygame
import sys
from constantes import *
from player import Player
from plataforma import Platform
from enemigo import Enemy


screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.init()
clock = pygame.time.Clock()

imagen_fondo = pygame.image.load("images/locations/forest/all.png")
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
player_1 = Player(x=30,y=500,speed_walk=4,speed_run=8,gravity=8,jumping=16, frame_rate_ms=30,move_rate_ms=30,jump_height=200)

platform_list = []
platform_list.append(Platform(400,450,80,80,1))
platform_list.append(Platform(800,450,80,400,2))

enemy_list = []
enemy_list.append(Enemy(x=630,y=500,speed_walk=2,speed_run=8,gravity=8,frame_rate_ms=30,move_rate_ms=30,x_length=50))

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
        if keys[pygame.K_SPACE]:
            player_1.jump()
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]and not keys[pygame.K_SPACE]:
            player_1.stay()
        if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]:
            player_1.stay()

        
        
    delta_ms = clock.tick(FPS)
    screen.blit(imagen_fondo,imagen_fondo.get_rect())
   
    for platform in platform_list:
        platform.draw(screen)

    for enemy in enemy_list:
        enemy.draw(screen)
        enemy.update(delta_ms)
        
    player_1.update(delta_ms, platform_list)
    player_1.draw(screen)
    
    # enemigos update
    # player dibujarlo
    # dibujar todo el nivel

    pygame.display.flip()
    
 



    






