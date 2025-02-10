import pygame
import sys
import os 
import math
import random
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
FPS = 120

class Music():
    
    souls_of_mischief = pygame.mixer.Sound("lib/assets/music/Souls Of Mischief - 93 'Til Infinity.mp3")
    whatever_you_like = pygame.mixer.Sound("lib/assets/music/Whatever You Like.mp3")
    rocketeer = pygame.mixer.Sound("lib/assets/music/Far_East_Movement_Ryan_Tedder_-_Rocketeer_Lyrics_128kbps.mp3")
    hood_gone_love_it = pygame.mixer.Sound("lib/assets/music/Hood_Gone_Love_It_feat._Kendrick_Lamar_128kbps.mp3")
    hate_it_or_love_it = pygame.mixer.Sound("lib/assets/music/The_Game_50_Cent_-_Hate_It_Or_Love_It_Official_Music_Video_128kbps.mp3")
    hardway = pygame.mixer.Sound("lib/assets/music/Derez_Deshon_-_Hardaway_Official_Lyric_Video_128kbps.mp3")
    wanna_be_a_baller = pygame.mixer.Sound("lib/assets/music/Wanna_Be_A_Baller_128kbps.mp3")
    starships = pygame.mixer.Sound("lib/assets/music/Nicki_Minaj_-_Starships_Clean_-_Lyrics_128kbps.mp3")
    young_ma = pygame.mixer.Sound("lib/assets/music/OOOUUU_128kbps.mp3")
    i_choose_you = pygame.mixer.Sound("lib/assets/music/UGK_ft._Outkast_-_Int_l_Players_Anthem_I_Choose_You_Official_Audio_128kbps.mp3")

    songs = [souls_of_mischief,whatever_you_like,rocketeer,hood_gone_love_it,hate_it_or_love_it,hardway,wanna_be_a_baller]


class Enviornment_sounds():
    sound_length = None
    channel1 = pygame.mixer.Channel(1)
    channel1.set_volume(0.1)

    park_ambience = pygame.mixer.Sound("lib/assets/enviornment_sounds/Afternoon_in_Suburban_Backyard_2 (mp3cut.net).mp3")
    ac_ambience = pygame.mixer.Sound("lib/assets/enviornment_sounds/Virtual_Air_Conditioner_1_Hour_128kbps (mp3cut.net).mp3")

    all_sounds = [park_ambience,ac_ambience]

Enviornment_sounds.park_ambience.set_volume(0.5)
Enviornment_sounds.park_ambience.play(loops=-1)

#song = random.choice(Music.songs)
song = Music.souls_of_mischief
#print(song.__getattribute__)
song.set_volume(0.1)
song.play()


class Transition_screen():
    transition_surface = pygame.Surface((WIDTH,HEIGHT),pygame.SRCALPHA)
    clicked = False
    transpacrency = 0

    def draw_screen():
        global game_state
        Transition_screen.transpacrency +=1
        pygame.draw.rect(Transition_screen.transition_surface,(0,0,0,Transition_screen.transpacrency),(0,0,WIDTH,HEIGHT))
        screen.blit(Transition_screen.transition_surface,(0,0))

        if Transition_screen.transpacrency == 255:
            for num,window in enumerate(Main_menu.Windows.select_windows):
                if num == Main_menu.Windows.current_window_num:
                    game_state = window.text
            Transition_screen.clicked = False
            Transition_screen.transpacrency = 0
            
class Loadup_screen():
    direction = -1
    delay_time = 60
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

        button_prompt = font2.render("Press x or space to continue",True,(255,255,255,255))
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

        Loadup_screen.loop +=0.01
        x = round (120 * (math.sin(Loadup_screen.loop)*2))
        Loadup_screen.prompt_transparency = x + 200

class Main_menu():

    class Ui_sounds():
        clicked = False
        ui_slide = pygame.mixer.Sound("lib/assets/ui_sounds/ui_slide.mp3")
        ui_select = pygame.mixer.Sound("lib/assets/ui_sounds/button-124476 (mp3cut.net).mp3")
        startup_sound = pygame.mixer.Sound("lib/assets/ui_sounds/soft-startup-sound-269291.mp3")

    class Windows():
        select_windows = []
        delay_time = 100
        timer = pygame.time.get_ticks()
        current_window_num = 0
        
        background_surf = pygame.Surface((WIDTH,HEIGHT),pygame.SRCALPHA)
        background_surf_rect = background_surf.get_rect(topleft=(0,0))

        transition_surface = pygame.Surface((WIDTH,HEIGHT),pygame.SRCALPHA)
        transparency = 0
        clicked = False

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
                
                elif keys[pygame.K_a]:
                    Main_menu.Ui_sounds.ui_slide.play()
                    
                    if Main_menu.Windows.current_window_num < 1:
                        Main_menu.Windows.current_window_num = 4
                    else:
                        Main_menu.Windows.current_window_num -=1
                    

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

            pygame.draw.rect(Main_menu.Windows.transition_surface,(0,0,0,Main_menu.Windows.transparency),(0,0,WIDTH,HEIGHT))
            screen.blit(Main_menu.Windows.transition_surface,(0,0))
        
            if Transition_screen.clicked == True:
                Transition_screen.draw_screen()

        '''
        def menu_select():
            global game_state
            keys = pygame.key.get_pressed()
            for num,window in enumerate(Main_menu.Windows.select_windows):
                if Main_menu.Windows.current_window_num == num and keys[pygame.K_SPACE]:
                    Main_menu.Windows.clicked = True
            
                game_state = window.text
        '''

class My_roc_gym():

    scale = 1.2
    
    delay_time = 10
    timer = pygame.time.get_ticks()
    x_start_pos = 300
    y_start_pos = 150

    court_sections = []

    background_surf = pygame.Surface((WIDTH,HEIGHT),pygame.SRCALPHA)
    background_surf_rect = background_surf.get_rect(topleft=(0,0))

    goal_image = pygame.image.load("lib/assets/my_roc_gym/my_gym_goal.png").convert_alpha()
    goal = pygame.transform.smoothscale(goal_image,(goal_image.get_size()[0]/scale,goal_image.get_size()[1]/scale))
    goal_rect = goal.get_rect(topleft=(-x_start_pos,-y_start_pos))

    front_goal_image = pygame.image.load("lib/assets/my_roc_gym/my_gym_front_rim.png").convert_alpha()
    front_goal = pygame.transform.smoothscale(front_goal_image,(front_goal_image.get_size()[0]/scale,front_goal_image.get_size()[1]/scale))
    front_goal_rect = front_goal.get_rect(topleft=(-x_start_pos,-y_start_pos-1))

    basket_rack_image = pygame.image.load("lib/assets/my_roc_gym/basket_rack.png").convert_alpha()
    basket_rack = pygame.transform.smoothscale(basket_rack_image,(basket_rack_image.get_size()[0]/2,basket_rack_image.get_size()[1]/2))
    basket_rack_rect = basket_rack.get_rect(topleft=(-x_start_pos+90,-y_start_pos+20))
   
    def __init__(self,background_image,court_image,scale,fov):
        super(My_roc_gym,self).__init__()
        self.scale = scale
        self.fov = fov
        self.original_image = pygame.image.load(background_image)
        self.background_image = pygame.image.load(background_image)
        self.background_image = pygame.transform.smoothscale(pygame.image.load(background_image).convert_alpha(),
            (self.background_image.get_size()[0]/self.scale,self.background_image.get_size()[1]/self.scale))
        self.court_image = court_image
        self.background_rect = self.background_image.get_rect(topleft=(-My_roc_gym.x_start_pos,-My_roc_gym.y_start_pos))

    def draw_gym():
        current_time = pygame.time.get_ticks()
        
        screen.blit(my_roc_gym_background.background_image,my_roc_gym_background.background_rect)
        
        screen.blit(My_roc_gym.goal,My_roc_gym.goal_rect)
        
        screen.blit(My_roc_gym.front_goal,My_roc_gym.front_goal_rect)    
        screen.blit(My_roc_gym.basket_rack,My_roc_gym.basket_rack_rect)
        
        if current_time > My_roc_gym.timer:
            #my_roc_gym_background.background_rect.x -=1
            My_roc_gym.timer = current_time + My_roc_gym.delay_time

        #pygame.draw.rect(screen,(255,0,0),(200,250,20,20))
    
    class Player():
        
        def __init__(self,build,rect,animation,player_speed):
            self.build = build
            self.surface = pygame.Surface((50,50),pygame.SRCALPHA)
            self.rect_size = None
            self.rect = rect
            self.x = self.rect[0]
            self.y = self.rect[1]
            self.animation_number = None
            self.scale = My_roc_gym.scale
            self.x_direction = -1
            self.y_direction = -1
            self.player_speed = player_speed
            self.x_velocity = 0
            self.y_velocity = 0
            self.max_speed = 1.4
            self.acceleration = 0
            self.current_anmimation = list(My_roc_gym.Player.Animaitons.animaiton_dict)[4]
            self.animation_list = list(My_roc_gym.Player.Animaitons.animaiton_dict)
            self.animation_wh = My_roc_gym.Player.Animaitons.scaled_animation_sheet.get_width()/16
            self.animation_frame_num = 0
            self.animation_col = 1
            self.animation_frame_x = self.animation_wh * self.animation_frame_num
            self.animation_frame_y = self.animation_wh * My_roc_gym.Player.Animaitons.animaiton_dict[self.current_anmimation][0]
            self.next_animation = None
            self.frame = pygame.Rect(self.animation_frame_x,self.animation_frame_y,self.animation_wh,self.animation_wh)
            
        
            self.animation = pygame.image.load(animation).convert_alpha()
            self.animation = pygame.transform.smoothscale(self.animation,(self.animation.get_size()[0]/My_roc_gym.Player.Animaitons.animation_scale,self.animation.get_size()[1]/My_roc_gym.Player.Animaitons.animation_scale)).convert_alpha()

        class Animaitons():

            animation_scale = 1
            animation_sheet = pygame.image.load("lib/assets/player_model/l_player_animation_sheet.png").convert_alpha()
            scaled_animation_sheet = pygame.transform.smoothscale(animation_sheet,(animation_sheet.get_size()[0]/animation_scale,animation_sheet.get_size()[1]/animation_scale)).convert_alpha()

            
            timer = pygame.time.get_ticks()
            animation_delay = None

            animaiton_dict = {
                #column, #num animations , delay
                "idle" : [0, 2,350],
                "dribble" : [1,7,70],
                "run" : [2,6,120],
                "side jumpshot" : [3,16,85],
                "between legs" : [4,12,75],
                "spin move" : [5,10,80],
                "behind the back" : [6,8,100],
                "snatch back" : [7,10,70],
                "moving crossover" : [8,11,100],
                "l standing crossover" : [9,11,60],
                "r standing crossover" : [10,11,60],
                "chest pass" : [11,15,60],
                "layup" : [12,15,80],
                "one hand dunk" : [13,13,120],
            }

           
        def draw():
            

            current_time = pygame.time.get_ticks()
            My_roc_gym.Player.Animaitons.animation_delay = My_roc_gym.Player.Animaitons.animaiton_dict[player.current_anmimation][2]
            
            player.animation_wh = My_roc_gym.Player.Animaitons.scaled_animation_sheet.get_width()/16
            player.animation_frame_x = player.animation_wh * player.animation_frame_num
            player.animation_frame_y = player.animation_wh * My_roc_gym.Player.Animaitons.animaiton_dict[player.current_anmimation][0]
            player.frame = pygame.Rect(player.animation_frame_x,player.animation_frame_y,player.animation_wh,player.animation_wh)

            player.next_animation = My_roc_gym.Player.Animaitons.scaled_animation_sheet.subsurface(player.frame).convert_alpha()
            
            pygame.draw.ellipse(player.surface,(0,0,0,130),(0,0,37,23))
            screen.blit(player.surface,(player.x+player.animation.get_size()[0]-185,player.y+player.animation.get_size()[1]-97))
            screen.blit(player.next_animation,(int(player.x),int(player.y)))


            if current_time > My_roc_gym.Player.Animaitons.timer:
                if player.animation_frame_num != My_roc_gym.Player.Animaitons.animaiton_dict[player.current_anmimation][1]:
                    player.animation_frame_num +=1 
                My_roc_gym.Player.Animaitons.timer = current_time + My_roc_gym.Player.Animaitons.animation_delay

            if player.animation_frame_num >= My_roc_gym.Player.Animaitons.animaiton_dict[player.current_anmimation][1] :
                player.animation_frame_num = 0
            
            #print(player.animation_frame_num)

        def move():

            keys = pygame.key.get_pressed()
            
            #print(keys)

            if keys[pygame.K_LSHIFT]:
                player.player_speed = min(player.player_speed + .001,player.max_speed)
            else:
                player.player_speed = max(player.player_speed - .001,1)

            if keys[pygame.K_d]:
                player.x_direction = 1
                player.current_anmimation = player.animation_list[2]
                player.x += player.player_speed 
                player.x_velocity = 1
            elif keys[pygame.K_a]:
                player.x_direction = -1 
                player.current_anmimation = player.animation_list[2]
                player.x -= player.player_speed
                player.x_velocity = 1
            else:
                player.x_velocity = max(player.x_velocity-0.03,0)
                player.x += player.x_velocity * player.x_direction
            
            #print(player.x_velocity)
            
            if keys[pygame.K_w]:
                player.y_direction = -1
                player.current_anmimation = player.animation_list[2]
                player.y -= player.player_speed
                player.y_velocity = 1
            elif keys[pygame.K_s]:
                player.y_direction = 1
                player.current_anmimation = player.animation_list[2]
                player.y += player.player_speed
                player.y_velocity = 1
            else:
                player.y_velocity = max(player.y_velocity-0.05,0)
                player.y += player.y_velocity * player.y_direction

            move_keys = [keys[pygame.K_w],keys[pygame.K_s],keys[pygame.K_a],keys[pygame.K_d]]
            
            if True in move_keys:
                pass
            else:
                player.current_anmimation = player.animation_list[1]
           
            
            

            
            
            

            #print(player.player_speed)
        
        
            
    

    class Camera():
        fov = 100
        offset = 0 
        distance = 0
        center = WIDTH/2 

        time_delay = 400
        timer = pygame.time.get_ticks()

        def get_offset():
            keys = pygame.key.get_pressed()
            current_time = pygame.time.get_ticks()

            if current_time > My_roc_gym.Camera.timer :
                My_roc_gym.Camera.timer = current_time + My_roc_gym.Camera.time_delay

                My_roc_gym.Camera.distance = (int(player.x - My_roc_gym.Camera.center))
                if My_roc_gym.Camera.offset < My_roc_gym.Camera.distance:
                    My_roc_gym.Camera.offset -=2
                if My_roc_gym.Camera.offset > My_roc_gym.Camera.distance:
                    My_roc_gym.Camera.offset +=2
                    
            
'''
region = pygame.Rect(0,0,320,110)
square1 = my_roc_gym.scaled_surf.subsurface(region)

basket_image = pygame.image.load("lib/assets/my_roc_gym/basket.png").convert_alpha()
basket_size = basket_image.get_size()
basket = pygame.transform.smoothscale(basket_image,(basket_size[0]/4,basket_size[1]/4))
basket_rect = basket.get_rect()
'''

rect = pygame.Rect(My_roc_gym.x_start_pos+235,My_roc_gym.y_start_pos-30,20,20)

loadup_screen = Loadup_screen("lib/assets/menu_backgrounds/loadup_background.png")
my_roc_text = font.render("My Roc",True,(255,255,255))
my_roc_rect = my_roc_text.get_rect(center=(0,0))
settings_window = Main_menu.Windows(20,80,170,160,"Settings","lib/assets/menu_backgrounds/gear_background.png",(1300,700))
roster_window = Main_menu.Windows(210,80,170,160,"Roster","lib/assets/menu_backgrounds/roster_background.png" ,(1300,700))
my_roc_window = Main_menu.Windows(20,260,360,150,"My Gym","lib/assets/menu_backgrounds/my_roc_background.png",(1300,700))
my_season_window = Main_menu.Windows(400,80,180,330,"My Season","lib/assets/menu_backgrounds/my_season_background.png",(1300,700))
the_roc_window = Main_menu.Windows(600,80,180,330,"The Roc","lib/assets/menu_backgrounds/the_roc_background.png",(1300,700))

Main_menu.Windows.select_windows = [settings_window,roster_window,my_roc_window,my_season_window,the_roc_window,]

my_roc_gym_background = My_roc_gym("lib/assets/my_roc_gym/my_gym_background.png",None,My_roc_gym.scale,My_roc_gym.Camera.fov)

player = My_roc_gym.Player(None,(My_roc_gym.x_start_pos-200,My_roc_gym.y_start_pos,20,20),"lib/assets/my_roc_gym/player_example.png",1)


# Game loop
running = True
while running:

    screen.fill(gray_cement)

    #screen.blit(my_roc_gym.scaled_surf,(-270,-110))
   
    #screen.blit(square1,(0,0))
    #pygame.draw.rect(screen,(0,0,0),rect,2)
    #screen.blit(basket,(-660,-200))

    if game_state == "loadup_screen":
        Loadup_screen.draw_screen()

    if game_state == "main_menu":
        Main_menu.Windows.draw_menu()
       
    if game_state == "My Gym":
        My_roc_gym.draw_gym()
        pygame.draw.rect(screen,(0,0,0),rect,width=2)
        #My_roc_gym.Player.set_animation()
        My_roc_gym.Player.draw()
        
        My_roc_gym.Player.move()
        My_roc_gym.Camera.get_offset()
        
    

    pygame.display.flip()

    clock.tick(FPS)/ 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if game_state == "main_menu":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    Main_menu.Ui_sounds.ui_select.set_volume(0.3)
                    Main_menu.Ui_sounds.ui_select.play()
                    Transition_screen.clicked = True

    

# Quit Pygame
pygame.quit()
sys.exit()
