from doctest import FAIL_FAST
import pygame
from constantes import *
from auxiliar import Auxiliar
from proyectile import Proyectile

class Player:
    def __init__(self,x,y,speed_walk,speed_run,gravity,jumping,frame_rate_ms,move_rate_ms,jump_height) -> None:
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/adventurer/adv_walk_r.png",6,1,scale=3)
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/adventurer/adv_walk_l.png",6,1,scale=3)  
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/adventurer/adv_stay_r.png",3,1,scale=3)
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/adventurer/adv_stay_l.png",3,1,scale=3)  
        self.jump_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/adventurer/adv_jump_r.png",15,1,scale=3)  
        self.jump_l = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/adventurer/adv_jump_l.png",15,1,scale=3)  
        self.atk_stance_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/adventurer/adv_atk_stance_r.png",5,1,scale=3)  
        self.atk_stance_l = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/adventurer/adv_atk_stance_l.png",5,1,scale=3) 
        self.charge_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/adventurer/adv_charge_r.png",1,1,scale=3)  
        self.charge_l = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/adventurer/adv_charge_l.png",1,1,scale=3)   
        self.atk_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/adventurer/adv_atk_r.png",2,1,scale=3)  
        self.atk_l = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/adventurer/adv_atk_l.png",2,1,scale=3)    
        self.hurt_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/adventurer/adv_hurt_r.png",3,1,scale=3)  
        self.hurt_l = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/adventurer/adv_hurt_l.png",3,1,scale=3) 
        self.colliding_enemy_flag = False
        self.frame = 0
        self.lives = 5
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk =  speed_walk
        self.speed_run =  speed_run
        #self.speed_hurted = 100
        self.gravity = gravity
        self.jumping = jumping 
        self.jump_height = jump_height
        self.y_start_jump = 0
        self.animation = self.stay_r
        self.direction = DIRECTION_R
        self.image = self.animation[self.frame]
        #self.jump_height = (self.image.get_rect().top - self.image.get_rect().bottom) * 2 
        self.rect = self.image.get_rect(center=(100, 100))
        self.rect.x = x
        self.rect.y = y
        self.transcurred_time_move = 0
        self.transcurred_time_animation = 0
        self.frame_rate_ms = frame_rate_ms
        self.move_rate_ms = move_rate_ms
        self.is_jump = False
        self.rect_ground_col = pygame.Rect(self.rect.x + self.rect.w / 4, self.rect.y + self.rect.h - GROUND_RECT_H, self.rect.w / 2, GROUND_RECT_H)
        self.tiempo_objetivo = 500
        self.atk_stance_flag = False
        self.tiempo_transcurrido = 0
        self.lives_font = pygame.font.Font(None, 32)

    def walk(self, direction):
        if self.direction != direction or (self.animation != self.walk_r and self.animation != self.walk_l):
            self.frame = 0
        self.direction = direction
        if direction == DIRECTION_R:
            self.move_x = self.speed_walk
            if self.is_jump:
                self.animation = self.jump_r
            else:
                self.animation = self.walk_r
        else:
            self.move_x = -self.speed_walk
            if self.is_jump:
                self.animation = self.jump_l
            else:
                self.animation = self.walk_l
            
    def jump_vertical(self,on_off = True):
        if on_off and self.is_jump == False:
            self.y_start_jump = self.rect.y
            if self.direction == DIRECTION_R:
                self.animation = self.jump_r
            else:
                self.animation = self.jump_l
            self.move_y = -self.jumping
            self.frame = 0
            self.is_jump = True      
        if on_off == False:
            self.is_jump = False
            self.stay(True)                   
            
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
            self.stay(True)     

    def stay(self,post_jump = False):
        if self.animation != self.stay_r and self.animation != self.stay_l:
            if self.direction == DIRECTION_R:
                self.animation = self.stay_r
            else:
                self.animation = self.stay_l
            if not post_jump:
                self.move_x = 0
            self.move_y = 0
            self.frame = 0
            
    def move(self, delta_ms,platform_list):
        self.transcurred_time_move += delta_ms
        if (self.transcurred_time_move >= self.move_rate_ms):
            if(abs(self.y_start_jump) - abs(self.rect.y) > self.jump_height and self.is_jump):
                self.move_y = 0
            self.transcurred_time_move = 0
            self.increment_x(self.move_x)
            self.increment_y(self.move_y)  
            if(not self.collide_platform(platform_list)):
                self.increment_y(self.gravity)
            elif self.is_jump: #sacar
                self.jump(False)

    def collide_platform(self, platform_list): 
        retorno = False
        if(self.rect.y >= GROUND_LEVEL): 
            retorno = True
        else:
            for platform in platform_list:
                if (self.rect_ground_col.colliderect(platform.rect_ground_col)):
                    retorno = True
                    break
        return retorno
    
    def colllide_enemy(self, enemy_list):
        collision_detected = False  # Bandera para indicar si se detectó una colisión con algún enemigo   
        for enemy in enemy_list:
            if self.rect.colliderect(enemy.rect):
                collision_detected = True
                break  # Si hay una colisión, no es necesario verificar los otros enemigos
        if collision_detected:
            if not self.colliding_enemy_flag:  # Verifica si ya estás colisionando con un enemigo
                self.be_hurted()
                self.lives -= 1
                print(self.lives)
                self.colliding_enemy_flag = True  # Establece la bandera para indicar que estás colisionando con un enemigo
        else:
            self.colliding_enemy_flag = False
            
            
    def increment_x(self,delta_x):
        self.rect.x += delta_x
        self.rect_ground_col.x += delta_x

    def increment_y(self,delta_y):
        self.rect.y += delta_y
        self.rect_ground_col.y += delta_y

    def animate(self, delta_ms):
        self.transcurred_time_animation += delta_ms
        if (self.transcurred_time_animation >= self.frame_rate_ms):
            self.transcurred_time_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
            else: 
                self.frame = 0          

    def update(self,delta_ms,platform_list,enemy_list):
        self.move(delta_ms,platform_list)
        self.animate(delta_ms)
        self.colllide_enemy(enemy_list)
        if (self.animation == self.atk_l or self.animation == self.atk_r) and self.timer(100):
            self.stay()
        
    def draw(self,screen):
        if(DEBUG): 
            pygame.draw.rect(screen,RED, self.rect)     
            pygame.draw.rect(screen,GREEN, self.rect_ground_col)    
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)
        screen.blit(self.show_lives(), LIVES_POSITION)

    def atk_stance(self):
        if self.direction == DIRECTION_R:
            self.animation = self.atk_stance_r
        else:
            self.animation = self.atk_stance_l

    def create_proyectile(self, proyectile_list,x,y):
        proyectile = Proyectile(5,x,y,self.direction) 
        proyectile_list.append(proyectile)
       # tiempo_actual = pygame.time.get_ticks()
        
    def timer(self, tiempo_obj):
            if self.atk_stance_flag == False:
                self.tiempo_transcurrido = pygame.time.get_ticks()
                self.atk_stance_flag = True
            print(self.atk_stance_flag)
            tiempo_actual = pygame.time.get_ticks()
            if tiempo_actual - self.tiempo_transcurrido >= tiempo_obj:
                return True
            else:
                return False

    def show_lives(self):
        lives_count = self.lives_font.render('LIVES: {0}'.format(self.lives), True, TEXTCOLOUR, None)
        return lives_count

    def charge_attack(self):
        if self.direction == DIRECTION_R:
            self.animation = self.charge_r
        else:
            self.animation = self.charge_l        

    def attack(self):
        if self.direction == DIRECTION_R:
            self.animation = self.atk_r
        else:
            self.animation = self.atk_l

    def be_hurted(self):
        pass
        '''CHEQUEAR 
        if self.direction == DIRECTION_R:
            self.animation = self.hurt_r
        else:
            self.animation = self.hurt_l'''