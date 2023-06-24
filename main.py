import pygame
import sys
from constantes import *
from player import Player
from plataforma import Platform
from enemigo import Enemy
from proyectile import Proyectile 

def is_jumping_anim(player):
    if player.animation == player.jump_r:
        print("salta R")
    elif player.animation == player.jump_l:
        print("salta L")
    else:
        print("wtf")

unpressed_flag = True

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.init()
clock = pygame.time.Clock()

imagen_fondo = pygame.image.load("images/locations/forest/forest.png")
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
player_1 = Player(x=30,y=GROUND_LEVEL,speed_walk=8,speed_run=8,gravity=8,jumping=27, frame_rate_ms=100,move_rate_ms=80,jump_height=120)

platform_list = []
platform_list.append(Platform(400,570,50,200,"images/tiles/0.png"))
platform_list.append(Platform(800,570,50,200,"images/tiles/1.png"))

enemy_list = []
enemy_list.append(Enemy(x=630,y=GROUND_LEVEL,speed_walk=1.5,speed_run=8,gravity=8,frame_rate_ms=30,move_rate_ms=30,x_length=120))

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
        if keys[pygame.K_SPACE]:
            player_1.jump()
            is_jumping_anim(player_1)
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]and not keys[pygame.K_SPACE]:
            player_1.stay()
        if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]:
            player_1.stay()
            
            
        if keys[pygame.K_q]:
            player_1.atk_stance()
            if player_1.timer(500):
                unpressed_flag = False
                player_1.charge_attack()
        if not unpressed_flag:    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_q:          
                    player_1.attack()
                    player_1.create_proyectile(proyectile_list,player_1.rect.centerx,player_1.rect.centery)
                    unpressed_flag = True

        
        '''if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                player_1.create_proyectile(proyectile_list,player_1.rect.centerx,player_1.rect.centery)
                print(proyectile_list)
'''
        
        
    delta_ms = clock.tick(FPS)
    screen.blit(imagen_fondo,imagen_fondo.get_rect())
   
    for platform in platform_list:
        platform.draw(screen)

    for enemy in enemy_list:
        enemy.draw(screen)
        enemy.update(delta_ms)
        
    player_1.update(delta_ms, platform_list)
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
    
    

 



    






