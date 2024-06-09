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
    court_size = (800,800)
    court_png = pygame.transform.smoothscale(pygame.image.load("lib/assets/court/court png/sprite_0.png"),(court_size))
    court_rect = court_png.get_rect(center=(0,0))
    court_rect.center = (SCREEN.get_width()/2,SCREEN.get_height()/2)
    
class Players(pygame.sprite.Sprite):

    def __init__(self,ball_hand,speed):
        super(Players,self).__init__()
        self.image = pygame.image.load("lib/assets/player model/animations/base animations/player model-/sprite_2.png") 
        self.surface = self.image
        self.rect = self.surface.get_rect(center=(self.surface.get_width()/2,self.surface.get_height()/2))
        self.ball_hand = "right hand"
        self.animation_state = None
        self.speed = speed
        self.velocity = 0

class Animations:

    standing_dribble = {
        "path" : "lib/assets/player model/animations/right hand/r standing dribble-",
        "right hand": "lib/assets/player model/animations/right hand/r standing dribble-",
        "left hand" : listdir("lib/assets/player model/animations/left hand/l standing dribble-"),
        "animation_length" : len(listdir("lib/assets/player model/animations/right hand/r standing dribble-"))
        }
    
    walking_dribble = {
        
    }
   



class Main_menu:
 
    def play():
        pygame.display.set_caption("My Gym")
        player1 = Players("r",1)
        player1.rect.x = My_gym.court_rect.width/2 - 150
        player1.rect.y = SCREEN.get_height()/2

        animation_num = 0
        last_key_pressed = []

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

 
        def test(key):

            if True not in movement_keys and player1.velocity == 0 :
                print("False in side")
                for animation_num in range(len(Animations.idle["right hand"])):
                    png = "lib/assets/player model/animations/right hand/r standing dribble-/" + str(Animations.standing_dribble["right hand"][animation_num])
                    player1.surface = pygame.image.load(png).convert_alpha()
                    pygame.display.update()
        

        def change_animation(png):
            player1.surface = png

        def animate(animation_num):
           
            if player1.ball_hand == "right hand":
                if True not in movement_keys and player1.velocity == 0:
                    player1.animation_state = Animations.standing_dribble
                    if player1.animation_state == Animations.standing_dribble:
                        animation_num +=1
                        if animation_num +1 > Animations.standing_dribble["animation_length"]:
                            animation_num = 0
                        png = pygame.image.load(str(Animations.standing_dribble[player1.ball_hand] + "/" + listdir(Animations.standing_dribble[player1.ball_hand])[animation_num]))
                        player1.surface = png
                        return animation_num 
                elif True in movement_keys:
                    
                    return 0 
                else:
                    return 0 
        print(Animations.standing_dribble)
           


        while True:

            clock.tick(fps)
            mouse_pointer = pygame.mouse.get_pos()

            SCREEN.blit(My_gym.court_png,My_gym.court_rect)
            SCREEN.blit(player1.surface,player1.rect)

            keys = pygame.key.get_pressed()
            movement_keys = [keys[pygame.K_w],keys[pygame.K_s],keys[pygame.K_a],keys[pygame.K_d]]

            if keys[pygame.K_w]:
                move("w")
                #animate("w")
            if keys[pygame.K_s]:
                move("s")
            if keys[pygame.K_a]:
                move("a")
            if keys[pygame.K_d]:
                move("d")

            animation_num = animate(animation_num)
            

        
            
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