from typing import Any
import pygame
import pygame.ftfont
import sys
import time
import random
import os
from os import listdir
import pathlib
from pygame.sprite import Group
pygame.init()
pygame.font.init()

SCREEN = pygame.display.set_mode((700,450))
pygame.display.set_caption("MY R.O.C BASKETBALL")
clock = pygame.time.Clock()
fps = 50


class Colors:
    BLACK = (0,0,0)
    GREY = (128,128,128)
    WHITE = (255,255,255)
    HOVER_WHITE = (200,200,200)

class Buttons(pygame.sprite.Sprite):
    def __init__(self,text_size,text,text_color,pos,hover_color):
        super(Buttons,self).__init__()
        self.surface = Buttons.font_render(text_size,text,text_color)
        self.rect = self.surface.get_rect(center=(0,0))
        self.rect.center = (self.surface.get_width()/2,self.surface.get_height()/2)
        self.rect.centerx = pos[0]
        self.rect.centery = pos[1]  
        self.text_size = text_size
        self.text = text
        self.text_color = text_color
        self.hover_color = hover_color
        
    def font_render(size,text,col):
        font = pygame.font.Font("lib/ARIALBD 1.TTF",size)
        return font.render(text,True,col)
            
class My_gym:
    court_size = (800,720)
    court_png = pygame.transform.smoothscale(pygame.image.load("lib/assets/court/court png/sprite_0.png"),(court_size))
    court_rect = court_png.get_rect(center=(0,0))
    court_rect.center = (SCREEN.get_width()/2,SCREEN.get_height()/2-10)
    
class Players(pygame.sprite.Sprite):

    def __init__(self,ball_hand,speed):
        super(Players,self).__init__()
        self.image = pygame.image.load("lib/assets/player model/animations/base animations/player model-/sprite_2.png") 
        self.surface = self.image
        self.rect = self.surface.get_rect(center=(self.surface.get_width()/2,self.surface.get_height()/2))
        self.ball_hand = "right hand"
        self.animation_state = Animations.standing_dribble
        self.dribble_ready = True
        self.speed = speed
        self.acceleration_speed = 2
        self.velocity = 0



class Animations:

    standing_dribble = {
        "right hand": "lib/assets/player model/animations/right hand/standing dribble-",
        "left hand" : "lib/assets/player model/animations/left hand/standing dribble-",
        "animation_length" : len(listdir("lib/assets/player model/animations/right hand/standing dribble-"))
        }
    
    walking_dribble = {
        "right hand": "lib/assets/player model/animations/right hand/walking dribble-",
        "left hand" : "lib/assets/player model/animations/left hand/walking dribble-",
        "animation_length" : len(listdir("lib/assets/player model/animations/right hand/walking dribble-"))
        }
    
    squated_dribble = {
        "right hand": "lib/assets/player model/animations/right hand/r squated dribble-",
        "left hand" : "lib/assets/player model/animations/left hand/r squated dribble-",
        "animation_length" : len(listdir("lib/assets/player model/animations/right hand/r squated dribble-"))
    }

    hezi = {
        "right hand": "lib/assets/player model/animations/right hand/r hezi-",
        "left hand" : "lib/assets/player model/animations/left hand/r hezi-",
        "animation_length" : len(listdir("lib/assets/player model/animations/right hand/r hezi-"))
    }
    

    

class Main_menu:

 
    def play():
        player1 = Players("r",1)
        player1.rect.x = My_gym.court_rect.width/2 - 150
        player1.rect.y = SCREEN.get_height()/2

        animation_num = 0
        last_key_pressed = []
        dribble_move = False

        def move(direction):
            player1.velocity = random.randint(13,15)
            if direction == "a":
                player1.rect.x -= player1.speed
            if direction == "d":
                player1.rect.x += player1.speed
            if direction == "w":
                player1.rect.y -= player1.speed
            if direction == "s":
                player1.rect.y += player1.speed
            
            
        def decelerate():
            print(last_key_pressed)
            if player1.velocity > .5 and "a" in last_key_pressed:
                player1.velocity -=1
                player1.rect.x -=1
            if player1.velocity > .5 and "d" in last_key_pressed:
                player1.velocity -=1
                player1.rect.x +=1    
            if player1.velocity > .5 and "w" in last_key_pressed:
                player1.velocity -=1
                player1.rect.y -=1
            if player1.velocity > .5 and "s" in last_key_pressed:
                player1.velocity -=1
                player1.rect.y +=1
            if keys[pygame.K_m] and "m" not in last_key_pressed and player1.acceleration_speed < 1:
                player1.acceleration_speed = 1
            if player1.acceleration_speed > 0.5 and "m" in last_key_pressed:
                player1.rect.x +=2
                player1.acceleration_speed -=.05
            print(player1.acceleration_speed)    
        
                
        def play_animation(animation_num,pngs):
            animation_num +=1  
            if animation_num == pngs["animation_length"]:
                player1.dribble_ready == True
            else:
                player1.dribble_ready == False
            if animation_num +1 > pngs["animation_length"]:
                animation_num = 0
          
                
            
            player1.surface = pygame.transform.smoothscale(pygame.image.load(str(pngs[player1.ball_hand]) + "/" + listdir(pngs[player1.ball_hand])[animation_num]),(200,200))
            return animation_num
        
        def animate(animation_num):
            if player1.ball_hand == "right hand": 
                if True not in movement_keys and player1.velocity == 0 and keys[pygame.K_LSHIFT] == False :
                    if player1.dribble_ready == True:
                        player1.animation_state = Animations.standing_dribble
                elif True not in movement_keys and keys[pygame.K_LSHIFT]:
                    if player1.dribble_ready == True:
                        if keys[pygame.K_LSHIFT] == True:
                            player1.animation_state = Animations.squated_dribble
                elif True in movement_keys and keys[pygame.K_w] or keys[pygame.K_s]:
                    if player1.dribble_ready == True:
                        player1.animation_state = Animations.walking_dribble
                

            return play_animation(animation_num,player1.animation_state)

          

        while True:

            clock.tick(fps)
            mouse_pointer = pygame.mouse.get_pos()

            SCREEN.blit(My_gym.court_png,My_gym.court_rect)
            SCREEN.blit(player1.surface,player1.rect)

            keys = pygame.key.get_pressed()
            movement_keys = [keys[pygame.K_w],keys[pygame.K_s],keys[pygame.K_a],keys[pygame.K_d]]
            dribble_move_keys = [keys[pygame.K_m]]

            if keys[pygame.K_w]:
                move("w")
            if keys[pygame.K_s]:
                move("s")
            if keys[pygame.K_a]:
                move("a")
            if keys[pygame.K_d]:
                move("d")

    
            decelerate()

            animation_num = animate(animation_num)
            
            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    key=pygame.key.name(event.key)
                    last_key_pressed.clear()
                if event.type == pygame.KEYUP:
                    key=pygame.key.name(event.key)
                    last_key_pressed.append(key)
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                        pygame.quit()
                        sys.exit()    

            pygame.display.update()



    def main_menu():
        game_state = "main_menu"
        play_button = Buttons(25,"My Gym",Colors.WHITE,(100,50),Colors.HOVER_WHITE)

        while True:
            
            mouse_pointer = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                        pygame.quit()
                        sys.exit()    
                if game_state == "main_menu":
                    SCREEN.fill(Colors.BLACK)
                    SCREEN.blit(play_button.surface,play_button.rect)
                    if play_button.rect.collidepoint(mouse_pointer):
                        play_button.surface = Buttons.font_render(play_button.text_size,play_button.text,play_button.hover_color)
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            time.sleep(.1)
                            Main_menu.play()
                            game_state = "Play"
                            
                    else:
                        play_button.surface = Buttons.font_render(play_button.text_size,play_button.text,play_button.text_color)

            
            pygame.display.update()

















Main_menu.main_menu()