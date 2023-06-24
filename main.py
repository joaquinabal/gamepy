import pygame
import sys
from constantes import *
from player import Player
from plataforma import Platform
from enemigo import Enemy
from proyectile import Proyectile 

unpressed_flag = True
contador_charge = 0

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.init()
clock = pygame.time.Clock()

imagen_fondo = pygame.image.load("images/locations/forest/forest.png")
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
player_1 = Player(x=30,y=GROUND_LEVEL,speed_walk=10,speed_run=10,gravity=20,jumping=40, frame_rate_ms=100,move_rate_ms=45,jump_height=100)

platform_list = []
platform_list.append(Platform(400,570,50,200,"images/tiles/0.png"))
platform_list.append(Platform(800,570,50,200,"images/tiles/1.png"))

enemy_list = []
enemy_list.append(Enemy(x=870,y=500,speed_walk=1.5,speed_run=8,gravity=8,frame_rate_ms=80,move_rate_ms=80,x_length=60))
enemy_list.append(Enemy(x=630,y=GROUND_LEVEL+20,speed_walk=1.5,speed_run=8,gravity=8,frame_rate_ms=80,move_rate_ms=80,x_length=120))

proyectile_list = []

loot_list = []



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
                
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
            if not player_1.is_jump:
                player_1.walk(DIRECTION_R)
        if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            if not player_1.is_jump:
                player_1.walk(DIRECTION_L)
        if keys[pygame.K_SPACE] and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
             player_1.jump_vertical()
        if keys[pygame.K_SPACE]:
            player_1.jump()
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]and not keys[pygame.K_SPACE]:
            player_1.stay()
        if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]:
            player_1.stay()           
            
        if keys[pygame.K_q]:
            player_1.atk_stance()
            if player_1.timer(500):
                unpressed_flag = False
                player_1.charge_attack() 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_q:   
                print(player_1.atk_stance_flag)       
                if not unpressed_flag:   
                    player_1.attack()
                    if player_1.direction == DIRECTION_R:
                        player_1.create_proyectile(proyectile_list,player_1.rect.right,player_1.rect.centery)
                    else:
                        player_1.create_proyectile(proyectile_list,player_1.rect.left,player_1.rect.centery)    
                    unpressed_flag = True
                player_1.atk_stance_flag = False

        
        
    delta_ms = clock.tick(FPS)
    screen.blit(imagen_fondo,imagen_fondo.get_rect())
   
    for platform in platform_list:
        platform.draw(screen)

    for enemy in enemy_list:
        enemy.draw(screen)
        enemy.update(delta_ms)
        
    player_1.update(delta_ms, platform_list,enemy_list)
    player_1.draw(screen)

    for proyectile in proyectile_list:
        proyectile.draw(screen)
        proyectile.update(enemy_list,loot_list)
    
    for loot in loot_list:
        loot.draw(screen)
        loot.update()

    
    # enemigos update
    # player dibujarlo
    # dibujar todo el nivel

    pygame.display.flip()
    
    

 



    






