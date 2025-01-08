import pygame
import sys
import os 
import math

import pygame.macosx
# Initialize Pygame
pygame.init()
pygame.mixer.init()
# Set up the display
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Roc Basketball")

white = (255, 255, 255)
gray_cement = (129,129,129)
blue = (20,30,120)
clock = pygame.time.Clock()
font =  pygame.font.Font("lib/assets/fonts/pixellari/Pixellari.ttf",20)
game_state = "loadup_screen"

class Music():
    souls_of_mischief = pygame.mixer.Sound("lib/assets/music/Souls Of Mischief - 93 'Til Infinity.mp3")
    whatever_you_like = pygame.mixer.Sound("lib/assets/music/Whatever You Like.mp3")
    rocketeer = pygame.mixer.Sound("lib/assets/music/Far_East_Movement_Ryan_Tedder_-_Rocketeer_Lyrics_128kbps.mp3")
    hood_gone_love_it = pygame.mixer.Sound("lib/assets/music/Hood_Gone_Love_It_feat._Kendrick_Lamar_128kbps.mp3")
    hate_it_or_love_it =pygame.mixer.Sound("lib/assets/music/The_Game_50_Cent_-_Hate_It_Or_Love_It_Official_Music_Video_128kbps.mp3")

Music.souls_of_mischief.set_volume(0.2)
#Music.souls_of_mischief.play()
Music.whatever_you_like.set_volume(0.1)
#Music.whatever_you_like.play()
Music.rocketeer.set_volume(0.1)
#Music.rocketeer.play()
Music.hood_gone_love_it.set_volume(0.1)
#Music.hood_gone_love_it.play()
Music.hate_it_or_love_it.set_volume(0.1)
Music.hate_it_or_love_it.play()

class Loadup_screen():
    direction = -1
    delay_time = 50
    timer = pygame.time.get_ticks()
    loop = 0

    transparency = 0
    key_space_pressed = False
    prompt_transparency = 255

    background_surface = pygame.Surface((WIDTH,HEIGHT),pygame.SRCALPHA)
    transition_surface = pygame.Surface((WIDTH,HEIGHT),pygame.SRCALPHA)

    def __init__(self,background_image):
        self.background_image = pygame.transform.smoothscale(pygame.image.load(background_image).convert_alpha(),(1600,800))
        self.background_rect = self.background_image.get_rect(topleft=(0,-230))
        
    def draw_screen():
        global game_state
        keys = pygame.key.get_pressed()
        screen.blit(loadup_screen.background_image,loadup_screen.background_rect)
        pygame.draw.rect(Loadup_screen.background_surface,(0,0,0,120),(0,0,WIDTH,HEIGHT))
        screen.blit(Loadup_screen.background_surface,(0,0))

        font1 = pygame.font.Font("lib/assets/fonts/pixellari/Pixellari.ttf",80)
        font2 = pygame.font.Font("lib/assets/fonts/pixellari/Pixellari.ttf",30)
        title_text = font1.render("Roc Basketball",True,(255,255,255))
        title_rect = title_text.get_rect(center=(WIDTH/2,HEIGHT/2-25))

        button_prompt = font2.render("Press X or space to continue",True,(255,255,255,255))
        button_prompt_rect = button_prompt.get_rect(center=(WIDTH/2,HEIGHT/1.5-25))

        button_alpha_surface = pygame.Surface((button_prompt.get_size()),pygame.SRCALPHA)
        button_alpha_surface.fill((0,0,0,0))
        
        pygame.draw.rect(screen,(255,255,255),(title_rect.left,HEIGHT/1.80-25,title_rect.size[0],2))

        screen.blit(title_text,title_rect)
        
        button_alpha_surface.blit(button_prompt,(0,0))
        button_alpha_surface.set_alpha(Loadup_screen.prompt_transparency)
        screen.blit(button_alpha_surface,(button_prompt_rect))

        current_time = pygame.time.get_ticks()

        if current_time > Loadup_screen.timer:
            Loadup_screen.timer = current_time + Loadup_screen.delay_time

            if Loadup_screen.direction == -1:
                if loadup_screen.background_rect.x > -800:
                    loadup_screen.background_rect.x -=1

                if loadup_screen.background_rect.x  == -800:
                    Loadup_screen.direction = 1 

            if Loadup_screen.direction == 1:
                if loadup_screen.background_rect.x < 0:
                    loadup_screen.background_rect.x +=1
                
                if loadup_screen.background_rect.x  == 0:
                    Loadup_screen.direction = -1 
                    
         
        
        if keys[pygame.K_SPACE]:
            Loadup_screen.key_space_pressed = True
            
        if Loadup_screen.key_space_pressed == True:
            Main_menu.Ui_sounds.startup_sound.play()
            Loadup_screen.transparency +=1
            if Loadup_screen.transparency == 255:
                
                game_state = "main_menu"

        pygame.draw.rect(Loadup_screen.transition_surface,(0,0,0,Loadup_screen.transparency),(0,0,WIDTH,HEIGHT))
        screen.blit(Loadup_screen.transition_surface,(0,0))

        

            
            


      

class Main_menu():

    class Ui_sounds():
        ui_slide = pygame.mixer.Sound("lib/assets/ui_sounds/ui_slide.mp3")
        startup_sound = pygame.mixer.Sound("lib/assets/ui_sounds/soft-startup-sound-269291.mp3")

    class Windows():

        delay_time = 100
        timer = pygame.time.get_ticks()

        current_window_num = 0 

        def __init__(self,x,y,width,length,text,background_image,scale):
            super(Main_menu.Windows,self).__init__()
            self.rect = pygame.Rect(x,y,width,length)
            self.text = text
            self.font_size = 30
            self.transparency = 120
            self.font = pygame.font.Font("lib/assets/fonts/pixellari/Pixellari.ttf",self.font_size)
            self.text_surf = self.font.render(text,(255,255,255),(255,255,255))
            self.text_rect = self.text_surf.get_rect()
            self.scale = scale
            self.background_image = pygame.transform.smoothscale(pygame.image.load(background_image).convert_alpha(),(scale))
            self.background_rect = self.background_image.get_rect()

        background_surf = pygame.Surface((WIDTH,HEIGHT),pygame.SRCALPHA)
        background_surf_rect = background_surf.get_rect(topleft=(0,0))

        def draw_menu():
            current_time = pygame.time.get_ticks()
            keys = pygame.key.get_pressed()

            
            if current_time > Main_menu.Windows.timer:
                Main_menu.Windows.timer = current_time + Main_menu.Windows.delay_time 

                if keys[pygame.K_d]:
                    Main_menu.Ui_sounds.ui_slide.play()

                    if Main_menu.Windows.current_window_num > len(Main_menu.Windows.select_windows)-2:
                        Main_menu.Windows.current_window_num = 0
                    else:
                        
                        Main_menu.Windows.current_window_num +=1


            #pygame.draw.rect(Main_menu.Windows.background_surf,(0,0,0,0),(0,0,WIDTH,HEIGHT))

            for num,window in enumerate(Main_menu.Windows.select_windows):
                if Main_menu.Windows.current_window_num == num:
                    screen.blit(window.background_image,window.background_rect)

                pygame.draw.rect(Main_menu.Windows.background_surf,(0,0,0,window.transparency),window,border_radius=3)

                if Main_menu.Windows.current_window_num == num:
                    Main_menu.Windows.select_windows[num].transparency = min(Main_menu.Windows.select_windows[num].transparency+2,150)
                else:
                    Main_menu.Windows.select_windows[num].transparency = max(Main_menu.Windows.select_windows[num].transparency-2,110)
            pygame.draw.rect(Main_menu.Windows.background_surf,(0,0,0,150),(23,65,WIDTH-50,2),border_radius=3)
            screen.blit(Main_menu.Windows.background_surf,Main_menu.Windows.background_surf_rect)

            for window in Main_menu.Windows.select_windows:
                screen.blit(window.text_surf,(window.rect[0]+10,window.rect[1]+10))
            screen.blit(my_roc_text,(25,40))
            
           

        select_windows = []

class My_roc_gym():
    def __init__(self,image):
        super(My_roc_gym,self).__init__()
        self.court_png = image
        self.surf = pygame.image.load(image).convert_alpha()
        self.size = self.surf.get_size()
        self.scale_size = 4
        self.scaled_surf = pygame.transform.smoothscale(self.surf,(self.size[0]/self.scale_size,self.size[1]/self.scale_size))
        self.scaled_surf_size = self.scaled_surf.get_size()
        self.rect = self.surf.get_rect(center=(0,0))

    def split_court():
        pass

    
    court_sections = []

my_roc_gym = My_roc_gym("lib/assets/my_roc_gym/surface_court.png")

region = pygame.Rect(0,0,320,110)
square1 = my_roc_gym.scaled_surf.subsurface(region)

basket_image = pygame.image.load("lib/assets/my_roc_gym/basket.png").convert_alpha()
basket_size = basket_image.get_size()
basket = pygame.transform.smoothscale(basket_image,(basket_size[0]/4,basket_size[1]/4))
basket_rect = basket.get_rect()

move=0

rect = pygame.Rect(200,200,20,20)




loadup_screen = Loadup_screen("lib/assets/menu_backgrounds/loadup_background.png")

my_roc_text = font.render("Roc Basketball",True,(255,255,255))
my_roc_rect = my_roc_text.get_rect(center=(0,0))
settings_window = Main_menu.Windows(20,80,170,160,"Settings","lib/assets/menu_backgrounds/gear_background.png",(1300,700))
roster_window = Main_menu.Windows(210,80,170,160,"Roster","lib/assets/menu_backgrounds/roster_background.png" ,(1300,700))
my_roc_window = Main_menu.Windows(20,260,360,150,"My Roc","lib/assets/menu_backgrounds/my_roc_background.png",(1300,700))
my_season_window = Main_menu.Windows(400,80,180,330,"My Season","lib/assets/menu_backgrounds/my_season_background.png",(1300,700))
the_roc_window = Main_menu.Windows(600,80,180,330,"The Roc","lib/assets/menu_backgrounds/the_roc_background.png",(1300,700))

Main_menu.Windows.select_windows = [settings_window,roster_window,my_roc_window,my_season_window,the_roc_window,]

# Game loop
running = True
while running:

    screen.fill(gray_cement)

    #screen.blit(my_roc_gym.scaled_surf,(-270,-110))
   
    #screen.blit(square1,(0,0))
    #pygame.draw.rect(screen,(0,0,0),rect,2)
    #screen.blit(basket,(-660,-200))

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        rect.x +=1
    if keys[pygame.K_a]:
        rect.x -=1


    if game_state == "loadup_screen":
        Loadup_screen.loop +=0.01
        x = round (120 * (math.sin(Loadup_screen.loop)*2))
        Loadup_screen.prompt_transparency = x + 200
        Loadup_screen.draw_screen()

    if game_state == "main_menu":
        Main_menu.Windows.draw_menu()


    pygame.display.flip()

    clock.tick(120)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    

# Quit Pygame
pygame.quit()
sys.exit()
