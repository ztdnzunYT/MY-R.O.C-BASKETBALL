import pygame
import sys
import os 
import math
import random
import pygame.examples
import pygame.macosx




# Initialize Pygame
pygame.init()
pygame.joystick.init()
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
game_state = "My Gym"
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

class Transition_screen():
    transition_surface = pygame.Surface((WIDTH,HEIGHT),pygame.SRCALPHA)
    clicked = False
    transpacrency = 0

    def draw_screen():
        global game_state

        if Transition_screen.transpacrency < 255:
            Transition_screen.transpacrency +=1
        pygame.draw.rect(Transition_screen.transition_surface,(0,0,0,Transition_screen.transpacrency),(0,0,WIDTH,HEIGHT))
        screen.blit(Transition_screen.transition_surface,(0,0))

        if Transition_screen.transpacrency == 255 and Transition_screen.clicked == True:
            if game_state == "Main menu":
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
                    
        if keys[pygame.K_SPACE] or controller1.get_button(0):
            Loadup_screen.key_space_pressed = True
         
            
        if Loadup_screen.key_space_pressed == True:
            Main_menu.Ui_sounds.startup_sound.play()
            Loadup_screen.transparency +=1
           
            if Loadup_screen.transparency == 255:
                Transition_screen.clicked = False
                game_state = "Main menu"


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
        menu_slide = pygame.mixer.Sound("lib/assets/ui_sounds/menu_slide.mp3")

    def menu_select():
        Main_menu.Ui_sounds.ui_select.play()
        Main_menu.Ui_sounds.ui_select.set_volume(0.3)
        Transition_screen.clicked = True

    class Windows():
        select_windows = []
        delay_time = 150
        timer = 0
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
            My_roc_gym.Controller.get_button()
            
            if (keys[pygame.K_d] or My_roc_gym.Controller.get_button() == "right"):
                if current_time > Main_menu.Windows.timer: 
                    Main_menu.Ui_sounds.ui_slide.play()
                    

                    if Main_menu.Windows.current_window_num > len(Main_menu.Windows.select_windows)-2:
                        Main_menu.Windows.current_window_num = 0
                    else: 
                        Main_menu.Windows.current_window_num +=1
                    
                    Main_menu.Windows.timer = current_time + Main_menu.Windows.delay_time

            elif (keys[pygame.K_a] or My_roc_gym.Controller.get_button() == "left"):
                if current_time > Main_menu.Windows.timer:
                    Main_menu.Ui_sounds.ui_slide.play()
                    Main_menu.Windows.timer = current_time + Main_menu.Windows.delay_time
                    

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

class Pause_menu():

    options_pressed = False
    options_background_surface = pygame.Surface((WIDTH,HEIGHT),pygame.SRCALPHA)
    options_background_screen = pygame.Rect(0,0,WIDTH,HEIGHT)
    options_backgorund_sidemenu = pygame.Rect(-170,0,170,HEIGHT)
    options_background_transparency = 0
    default_transparency = 170
    item_selected = 0

    def draw_pause_menu():
        global game_state
        pygame.draw.rect(Pause_menu.options_background_surface,(0,0,0,Pause_menu.options_background_transparency),Pause_menu.options_background_screen)
        pygame.draw.rect(Pause_menu.options_background_surface,(0,0,0,Pause_menu.options_background_transparency+30),Pause_menu.options_backgorund_sidemenu)
        screen.blit(Pause_menu.options_background_surface,(0,0))

        if Pause_menu.options_pressed == False:
            Pause_menu.item_selected = 0

        for num,item in enumerate(Pause_menu.pause_menu_items):
            
            item.rect.y = (60 * num) + 50
            screen.blit(item.surface,item.rect) 
            transparency = item.surface.get_alpha()
            pygame.draw.rect(screen,(255,255,255),(item.rect.x,item.rect.y+25,40,1))

            if Pause_menu.item_selected == num:
                item.surface.set_alpha(min(transparency+5,255))
            else:
                item.surface.set_alpha(max(transparency-5,150))

        if Pause_menu.options_pressed:
            Pause_menu.options_background_transparency = min(Pause_menu.options_background_transparency+5,Pause_menu.default_transparency)
            Pause_menu.options_backgorund_sidemenu.x = min(Pause_menu.options_backgorund_sidemenu.x+5,0)
        else:
            Pause_menu.options_background_transparency = max(Pause_menu.options_background_transparency-5,0)
            Pause_menu.options_backgorund_sidemenu.x = max(Pause_menu.options_backgorund_sidemenu.x-5,-Pause_menu.options_backgorund_sidemenu.width)
        
        if Pause_menu.options_pressed:
            for num,item in enumerate(Pause_menu.pause_menu_items):
                item.rect.x = min(item.rect.x+5,25)
        else:
            for num,item in enumerate(Pause_menu.pause_menu_items):
                item.rect.x = max(item.rect.x-5,-150)
    

        if Transition_screen.clicked == True:
            Transition_screen.draw_screen()
        
        if Transition_screen.transpacrency == 254:
            Transition_screen.clicked = False
            Transition_screen.transpacrency = 0
            game_state = "Main menu"
    
    def next_selected(val):
        global game_state
    
        if val != None:
            Main_menu.Ui_sounds.ui_slide.play()
            Pause_menu.item_selected += val

        if Pause_menu.item_selected > len(Pause_menu.pause_menu_items)-1:
            Pause_menu.item_selected = 0
        elif Pause_menu.item_selected < 0:
            Pause_menu.item_selected = len(Pause_menu.pause_menu_items)-1
        
        if val == None:
            if Pause_menu.item_selected == 0:
                Transition_screen.clicked = True
                Main_menu.Ui_sounds.ui_select.play()
                

    def check_paused():
        Main_menu.Ui_sounds.menu_slide.set_volume(0.3)
        if Pause_menu.options_pressed == False:
            Pause_menu.options_pressed = True
            Main_menu.Ui_sounds.menu_slide.play()
        else:
            Pause_menu.options_pressed = False
            Main_menu.Ui_sounds.menu_slide.play()
    
    class Pause_items():
        def __init__(self,item_name,color,transparency):
            self.font = pygame.font.Font(None,25)
            self.item_name = item_name
            self.color = color
            self.transparency = transparency
            self.surface = self.font.render(self.item_name,True,(self.color))
            self.rect = self.surface.get_rect(center=(self.surface.get_width()/2,self.surface.get_height()/2))
            self.rect.x = -150

    main_menu_item = Pause_items("Main menu",(255,255,255),155)
    start_game_menu_item = Pause_items("Start game",(255,255,255),155)
    settings_menu_item = Pause_items("Settings",(255,255,255),155)

    pause_menu_items = [main_menu_item,start_game_menu_item,settings_menu_item]

class My_roc_gym():

    scale = 1.2
    delay_time = 5
    timer = pygame.time.get_ticks()
    x_start_pos = 300
    y_start_pos = 150
    x_offset = 0

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

    paint_rect1 = pygame.Rect(55,200,415,210)
    paint_rect2 = pygame.Rect(470,215,50,180)
    paint_rect3 = pygame.Rect(520,230,40,140)
    paint_rect4 = pygame.Rect(560,260,25,80)
    paint_rect5 = pygame.Rect(80,230,230,140)

    paint_rects = [paint_rect1,paint_rect2,paint_rect3,paint_rect4,paint_rect5]

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
        screen.blit(my_roc_gym_background.background_image,my_roc_gym_background.background_rect)
        screen.blit(My_roc_gym.goal,My_roc_gym.goal_rect)
        screen.blit(My_roc_gym.front_goal,My_roc_gym.front_goal_rect)    
        screen.blit(My_roc_gym.basket_rack,My_roc_gym.basket_rack_rect)

    
    def draw_detection_areas():
        
        for paint in My_roc_gym.paint_rects:
            pygame.draw.rect(screen,(0,0,0),paint,width=-1)

       
        if pygame.Rect.colliderect(pygame.Rect(My_roc_gym.paint_rect1),pygame.Rect(My_roc_gym.Player.Animaitons.shadow_x+5,My_roc_gym.Player.Animaitons.shadow_y,5,5)) or pygame.Rect.colliderect(pygame.Rect(My_roc_gym.paint_rect2),pygame.Rect(My_roc_gym.Player.Animaitons.shadow_x+5,My_roc_gym.Player.Animaitons.shadow_y,5,5)) or pygame.Rect.colliderect(pygame.Rect(My_roc_gym.paint_rect3),pygame.Rect(My_roc_gym.Player.Animaitons.shadow_x+5,My_roc_gym.Player.Animaitons.shadow_y,5,5)) or pygame.Rect.colliderect(pygame.Rect(My_roc_gym.paint_rect4),pygame.Rect(My_roc_gym.Player.Animaitons.shadow_x+5,My_roc_gym.Player.Animaitons.shadow_y,5,5)):
            player.in_paint = True
        else:
            player.in_paint = False
        
        if pygame.Rect.colliderect(pygame.Rect(My_roc_gym.paint_rect5),pygame.Rect(My_roc_gym.Player.Animaitons.shadow_x+5,My_roc_gym.Player.Animaitons.shadow_y,5,5)):
            player.layup_range = True
        else:
            player.layup_range = False

    class Player():
        
        def __init__(self,build,rect,animation,player_speed):
            self.build = build
            self.surface = pygame.Surface((50,50),pygame.SRCALPHA)
            self.rect_size = None
            self.rect = rect
            self.x = self.rect[0]
            self.y = self.rect[1]
            self.y_min = 70
            self.y_max = 300
            self.animation_number = None
            self.scale = My_roc_gym.scale 
            self.x_direction = -1
            self.y_direction = -1
            self.grounded = True
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
            self.animation_playing = False
            self.frame = pygame.Rect(self.animation_frame_x,self.animation_frame_y,self.animation_wh,self.animation_wh)
            self.hand = "right"
            self.in_paint = False
            self.layup_range = False
        
            self.animation = pygame.image.load(animation).convert_alpha()
            self.animation = pygame.transform.smoothscale(self.animation,(self.animation.get_size()[0]/My_roc_gym.Player.Animaitons.animation_scale,self.animation.get_size()[1]/My_roc_gym.Player.Animaitons.animation_scale)).convert_alpha()

        class Animaitons():

            animation_scale = 1
            animation_sheet = pygame.image.load("lib/assets/player_model/l_player_animation_sheet2.png").convert_alpha()
            scaled_animation_sheet = pygame.transform.smoothscale(animation_sheet,(animation_sheet.get_size()[0]/animation_scale,animation_sheet.get_size()[1]/animation_scale)).convert_alpha()
            
            shadow_x = 0
            shadow_y = 0
            
            timer = pygame.time.get_ticks()
            animation_delay = 0
            button_hold = 0
            dribble_pressed = False
            animation_overlap = 1
            stepback_hold = 0
            animation_speed = 10
        
            animaiton_dict = {
                #column, #num animations , delay
                "idle" : [0, 2,350],  #no buttons pressed w/o ball
                "dribble" : [1,7,70], #no buttons pressed w ball
                "run" : [2,6,120], #wasd buttons
                "side jumpshot" : [3,16,85], #e button
                "between legs" : [4,12,75-animation_speed], #no wasd n button | r2 and down on right stick
                "spin move" : [5,10,70-animation_speed], #bnm buttons  | 
                "behind the back" : [6,8,70-animation_speed],#no wasd bm
                "snatch back" : [7,10,70-animation_speed], #no wasd 
                "moving crossover" : [8,11,60-animation_speed], #shift wasd and b or m 
                "l standing crossover" : [9,11,50-animation_speed], #wasd and b button
                "r standing crossover" : [10,11,50-animation_speed], #wasd and m button
                "l hezi" : [11,10,70-animation_speed],
                "r hezi" : [12,10,70-animation_speed],
                "stepback" : [13,13,60],
                "chest pass" : [14,15,60], #number buttons 1,2
                "layup" : [15,15,90], #wasd and e in paint 
                "one hand dunk" : [16,13,120], #shift wasd and e in paint
            }

            def animation_playing_check():
                if player.animation_playing == False:
                    return False

            def run_animation():
                player.current_anmimation = player.animation_list[2]
           
        def draw():
        
            My_roc_gym.Player.Animaitons.animation_delay = My_roc_gym.Player.Animaitons.animaiton_dict[player.current_anmimation][2]
            
            player.animation_wh = My_roc_gym.Player.Animaitons.scaled_animation_sheet.get_width()/16
            player.animation_frame_x = player.animation_wh * player.animation_frame_num
            player.animation_frame_y = player.animation_wh * My_roc_gym.Player.Animaitons.animaiton_dict[player.current_anmimation][0]
            player.frame = pygame.Rect(player.animation_frame_x,player.animation_frame_y,player.animation_wh,player.animation_wh)

            player.next_animation = My_roc_gym.Player.Animaitons.scaled_animation_sheet.subsurface(player.frame).convert_alpha()
            
            pygame.draw.ellipse(player.surface,(0,0,0,130),(0,0,37,23))
            
            if My_roc_gym.Player.Animaitons.button_hold < 3:
                My_roc_gym.Player.Animaitons.shadow_y = player.y+player.animation.get_size()[1]-97
            My_roc_gym.Player.Animaitons.shadow_x = player.x+player.animation.get_size()[0]-185
            screen.blit(player.surface,(My_roc_gym.Player.Animaitons.shadow_x,My_roc_gym.Player.Animaitons.shadow_y))
            screen.blit(player.next_animation,(int(player.x),int(player.y)))

          
        def move():

            keys = pygame.key.get_pressed()
   
            if (keys[pygame.K_LSHIFT] or round(My_roc_gym.Controller.get_r_trigger()) == 1):
                player.player_speed = min(player.player_speed + .002,player.max_speed)
            else:
                player.player_speed = max(player.player_speed - .002,1)

            if (keys[pygame.K_d] or My_roc_gym.Controller.get_x_left_stick() == 1) and player.x < My_roc_gym.Camera.x_max :
                player.x_direction = 1
                if player.animation_playing == False : 
                    My_roc_gym.Player.Animaitons.run_animation()
                player.x += player.player_speed 
                player.x_velocity = 1
            elif (keys[pygame.K_a] or My_roc_gym.Controller.get_x_left_stick() == -1) and player.x > My_roc_gym.Camera.x_min :
                player.x_direction = -1 
                if player.animation_playing == False : 
                    My_roc_gym.Player.Animaitons.run_animation()
                if My_roc_gym.Camera.x_offset <= 0:
                    player.x -= player.player_speed
                player.x_velocity = 1
            else:
                if player.x < My_roc_gym.Camera.x_max:
                    player.x += player.x_velocity * player.x_direction
                    player.x_velocity = max(player.x_velocity-0.03,0)
            
            if player.animation_playing == False:
                    
                if (keys[pygame.K_w] or My_roc_gym.Controller.get_y_left_stick() == -1 and My_roc_gym.Player.Animaitons.button_hold == 0):
                    if player.y > player.y_min:
                        player.y_direction = -1
                        if player.animation_playing == False : 
                            My_roc_gym.Player.Animaitons.run_animation()
                        player.y -= player.player_speed
                        player.y_velocity = 1
                elif (keys[pygame.K_s] or My_roc_gym.Controller.get_y_left_stick() == 1 and My_roc_gym.Player.Animaitons.button_hold == 0):
                    if player.y < player.y_max:
                        player.y_direction = 1
                        if player.animation_playing == False : 
                            My_roc_gym.Player.Animaitons.run_animation()
                        player.y += player.player_speed 
                        player.y_velocity = 1
                else:
                        if My_roc_gym.Player.Animaitons.button_hold < 3:
                            player.y += player.y_velocity * player.y_direction
                            player.y_velocity = max(player.y_velocity-0.05,0)
            
            
            move_keys = [(keys[pygame.K_w] or My_roc_gym.Controller.get_y_left_stick() == -1),
                         (keys[pygame.K_s] or My_roc_gym.Controller.get_y_left_stick() == 1),
                         (keys[pygame.K_a] or My_roc_gym.Controller.get_x_left_stick() == -1),
                         (keys[pygame.K_d] or My_roc_gym.Controller.get_x_left_stick() == 1),
                         (keys[pygame.K_e] or My_roc_gym.Controller.get_button() == "e"), player.animation_playing]
            
            dribble_keys = [My_roc_gym.Controller.get_x_left_stick(),My_roc_gym.Controller.get_y_right_stick()]
            
            if True in move_keys:
                pass
            else:
                if player.animation_playing == False:
                    player.current_anmimation = player.animation_list[1]
        
        def animation_check(animation_num):
            if player.current_anmimation == player.animation_list[animation_num]:
                return bool

            
        def animation_move():
        
            
            keys = pygame.key.get_pressed()
            move_keys = [(keys[pygame.K_w] or My_roc_gym.Controller.get_y_left_stick() == -1),
                        (keys[pygame.K_s] or My_roc_gym.Controller.get_y_left_stick() == 1),
                        (keys[pygame.K_a] or My_roc_gym.Controller.get_x_left_stick() == -1),
                        (keys[pygame.K_d] or My_roc_gym.Controller.get_x_left_stick() == 1),
                        (keys[pygame.K_e] or My_roc_gym.Controller.get_button() == "e"), player.animation_playing]
            

            
            #JUMPSHOT ------
            if My_roc_gym.Player.animation_check(3) and player.animation_frame_num > 4 and player.animation_frame_num < 8:
                if My_roc_gym.Player.Animaitons.button_hold < 40:
                    My_roc_gym.Player.Animaitons.button_hold +=2
                    player.y -=1.3
                    if My_roc_gym.Player.Animaitons.button_hold > 40:
                        player.grounded = False
                
            elif player.animation_frame_num >= 8 or player.grounded == False:
                if My_roc_gym.Player.Animaitons.button_hold > 0:
                    My_roc_gym.Player.Animaitons.button_hold = max(My_roc_gym.Player.Animaitons.button_hold-2,0)
                    player.y +=1.3
                else:
                    player.grounded = True


            if My_roc_gym.Player.animation_check(4) or player.current_anmimation == player.animation_list[6]:
                player.x += random.uniform(-1.2,1)

            if My_roc_gym.Controller.get_x_left_stick() != 1:
                
                if My_roc_gym.Player.animation_check(5):
                        player.x += 1
                        if player.y_direction == 1:
                            player.y += .8
                        elif player.y_direction == -1:
                            player.y -= .8

                if My_roc_gym.Player.animation_check(7):
                    player.x += 1

                #time delay 

            if My_roc_gym.Player.animation_check(8):
                player.x -= .5
                player.y += .2 * player.y_direction

            
            if My_roc_gym.Player.animation_check(9):
                player.y -= random.uniform(0.8,1)
            elif My_roc_gym.Player.animation_check(10):
                player.y -= (random.uniform(-0.8,-1))

            if player.animation_frame_num > 3:
                if My_roc_gym.Player.animation_check(11):
                    player.y += 1.5
                if My_roc_gym.Player.animation_check(12):
                    player.y -= 1.5

            if My_roc_gym.Player.animation_check(13):
                player.x += .5

            if My_roc_gym.Player.animation_check(15):
                if My_roc_gym.Controller.get_x_left_stick() == 0:
                    player.x -= .5
                if pygame.Rect.colliderect(pygame.Rect(My_roc_gym.Player.Animaitons.shadow_x,My_roc_gym.Player.Animaitons.shadow_y,20,20),My_roc_gym.paint_rect5):
                    if My_roc_gym.Controller.get_y_left_stick() == 0:
                        player.y += .2 * player.y_direction
                    else:
                        player.y += .2 * My_roc_gym.Controller.get_y_left_stick() 

            if player.y <= player.y_min and player.current_anmimation != player.animation_list[3]:
                player.y +=1 
            if player.y >= player.y_max and player.current_anmimation != player.animation_list[3]:
                player.y -=1
        
            
            
        def set_animation(animation):
            player.animation_frame_num = 0
            player.current_anmimation = player.animation_list[animation]
            player.animation_playing = True
            My_roc_gym.Player.Animaitons.dribble_pressed = True


        def animate():
            current_time = pygame.time.get_ticks()
        
            if current_time > My_roc_gym.Player.Animaitons.timer:
                player.animation_frame_num +=1 
                My_roc_gym.Player.Animaitons.timer = current_time + My_roc_gym.Player.Animaitons.animation_delay

            if player.current_anmimation != player.animation_list[1]:
                if player.animation_frame_num >= int(My_roc_gym.Player.Animaitons.animaiton_dict[player.current_anmimation][1]) - My_roc_gym.Player.Animaitons.animation_overlap:
                    player.animation_playing = False
                    player.animation_frame_num = 0
            else:
                if player.animation_frame_num >= int(My_roc_gym.Player.Animaitons.animaiton_dict[player.current_anmimation][1]):
                    player.animation_playing = False
                    player.animation_frame_num = 0

            keys = pygame.key.get_pressed()
            dribble_keys = [My_roc_gym.Controller.get_x_right_stick(),My_roc_gym.Controller.get_y_right_stick()]
            
            multicheck = 0


            if (keys[pygame.K_e] or My_roc_gym.Controller.get_button() == "e"):
                if player.current_anmimation != player.animation_list[3] and player.current_anmimation != player.animation_list[14]:
                    if player.layup_range == False:
                        My_roc_gym.Player.Animaitons.y_delay = 10
                        My_roc_gym.Player.set_animation(3)
                        player.hand = "right"
                    else:
                        if My_roc_gym.Controller.get_x_left_stick() != -1:
                            My_roc_gym.Player.Animaitons.y_delay = 10
                            My_roc_gym.Player.set_animation(3)
                            player.hand = "right"
                        
            if player.current_anmimation == player.animation_list[0]:
                My_roc_gym.Player.Animaitons.dribble_pressed = False
            elif dribble_keys == [0,0] and player.animation_frame_num == 0 or player.animation_frame_num == player.current_anmimation[1] :
                My_roc_gym.Player.Animaitons.dribble_pressed = False
  

            if player.animation_playing == False and player.grounded and My_roc_gym.Player.Animaitons.dribble_pressed == False:

                if My_roc_gym.Controller.get_r_trigger() == -1:
                        
                    #BETWEEN LEGS -------
                    if My_roc_gym.Controller.get_y_right_stick() == -1 and My_roc_gym.Controller.get_x_left_stick() == 0 and My_roc_gym.Controller.get_y_left_stick() == 0:
                        if multicheck == 0:
                            My_roc_gym.Player.set_animation(4)    

                    #BEHIND THE BACK -------
                    if My_roc_gym.Controller.get_x_right_stick() == 1:
                        My_roc_gym.Player.set_animation(6)

                #BACK SPIN ---------
                if My_roc_gym.Controller.get_x_right_stick() == -1:
                    multicheck +=1
                if My_roc_gym.Controller.get_y_right_stick() == 1:
                    multicheck +=1 
                if multicheck == 2:
                    My_roc_gym.Player.set_animation(5)
                    
                #SNATCHBACK -------
                if My_roc_gym.Controller.get_x_left_stick() == 1 and My_roc_gym.Controller.get_y_right_stick() == 1 and multicheck != 2:
                    My_roc_gym.Player.set_animation(7)
                        
                #MOVING CROSSOVER ------
                if My_roc_gym.Controller.get_x_left_stick() == -1 and My_roc_gym.Controller.get_r_trigger() == 1 and My_roc_gym.Controller.get_y_right_stick() == -1:
                    My_roc_gym.Player.set_animation(8)    
                       
                if My_roc_gym.Controller.get_r_trigger() == 1:
                    #RIGHT HAND CROSSOVER -------

                    if My_roc_gym.Controller.get_y_right_stick() == -1 and player.hand == "right" :
                        My_roc_gym.Player.set_animation(9)
                        player.hand = "left"
                    elif My_roc_gym.Controller.get_y_right_stick() == -1 and My_roc_gym.Controller.get_x_left_stick() != -1:
                        My_roc_gym.Player.set_animation(12)
                 
                    if My_roc_gym.Controller.get_y_right_stick() == 1 and player.hand == "left":
                        My_roc_gym.Player.set_animation(10)
                        player.hand = "right"
                    elif My_roc_gym.Controller.get_y_right_stick() == 1 and My_roc_gym.Controller.get_x_left_stick() != -1:
                        My_roc_gym.Player.set_animation(11)
                
                    if My_roc_gym.Controller.get_x_right_stick() == 1 and My_roc_gym.Controller.get_x_left_stick() != 1:
                        My_roc_gym.Player.set_animation(13)



            if player.layup_range == True and player.current_anmimation != player.animation_list[15] and player.current_anmimation != player.animation_list[3]:
                if My_roc_gym.Controller.get_button() == "e" and My_roc_gym.Controller.get_x_left_stick() == -1:
                    My_roc_gym.Player.set_animation(15)
                    player.layup_range = False        


            

            
            """
           
            if player.current_anmimation == player.animation_list[3]: 
                if player.animation_frame_num  > 4 and player.animation_frame_num < 7:
                    player.y -=1 
                if player.animation_frame_num > 8 and player.animation_frame_num < 11:
                    player.y  +=1
            """
            
    class Controller():
        def get_x_left_stick():
            return round(controller1.get_axis(0))
        def get_y_left_stick():
            return round(controller1.get_axis(1))
        
        def get_x_right_stick():
            return round(controller1.get_axis(2))
        
        def get_y_right_stick():
            return round(controller1.get_axis(3))
        
        
        def get_button():
            for i in range(controller1.get_numbuttons()):
                button = round(controller1.get_button(i))
                if i == 14 and button == True:
                    return "right"
                if i == 13 and button == True:
                    return "left"
                if i == 2 and button  == True:
                    return "e"

        def get_r_trigger():
            return round(controller1.get_axis(5))
        

    class Camera():

        camera_rect = pygame.Rect(WIDTH/2,HEIGHT/2,20,20)

        x_position = WIDTH/2 
        y_position = HEIGHT/2
        fov = 100
        offset_amount = 0.3
        x_offset = 0 
        y_offset = 0  
        y_distance = 0
        size = 20
        x_max = 600
        x_min = -40
        y_max = -180
        y_min = -100
        cam_y_max = -65
        cam_y_min = -170
        x_direction = 0
        y_direction = 0
        camera_moving = bool

        #rect = pygame.Rect(x_offset)

        time_delay = 10
        timer = pygame.time.get_ticks()

        def offset_stage():
           
            pygame.draw.rect(screen,(0,0,0),(player.x,player.y,My_roc_gym.Camera.camera_rect[2],My_roc_gym.Camera.camera_rect[3]),1)
            keys = pygame.key.get_pressed()
            My_roc_gym.Camera.y_distance = player.y - HEIGHT/2

            if (keys[pygame.K_d] or My_roc_gym.Controller.get_x_left_stick() == 1) and player.x > My_roc_gym.Camera.x_max and My_roc_gym.Camera.x_offset < 150:
                My_roc_gym.Camera.x_direction =-1
                My_roc_gym.Camera.x_offset +=1 
                for _ in stage_rects[:len(stage_rects)-1]:
                    _.x += My_roc_gym.Camera.x_direction

            elif (keys[pygame.K_a] or My_roc_gym.Controller.get_x_left_stick() == -1):
                My_roc_gym.Camera.x_direction = 1
                if My_roc_gym.Camera.x_offset > 0:
                    My_roc_gym.Camera.x_offset -=1
                    for _ in stage_rects[:len(stage_rects)-1]:
                        _.x += My_roc_gym.Camera.x_direction
                    
            if (keys[pygame.K_w] or My_roc_gym.Controller.get_y_left_stick() == -1) :
                if My_roc_gym.Camera.y_distance < My_roc_gym.Camera.y_max:
                    My_roc_gym.Camera.y_direction = 1
                    My_roc_gym.Camera.camera_moving = True
                    
                    if my_roc_gym_background.background_rect.y < My_roc_gym.Camera.cam_y_max:

                        for _ in stage_rects[:len(stage_rects)-1]:
                            _.y += My_roc_gym.Camera.y_direction 
                        
            elif (keys[pygame.K_s] or My_roc_gym.Controller.get_y_left_stick() == 1) or My_roc_gym.Player.animation_check(11) or My_roc_gym.Player.animation_check(12):
                if My_roc_gym.Camera.y_distance > My_roc_gym.Camera.y_min:
                    My_roc_gym.Camera.y_direction = -1
                    My_roc_gym.Camera.camera_moving = True
                    
                    if my_roc_gym_background.background_rect.y > My_roc_gym.Camera.cam_y_min:

                        for _ in stage_rects[:len(stage_rects)-1]:
                            _.y += My_roc_gym.Camera.y_direction

            elif My_roc_gym.Camera.y_distance < My_roc_gym.Camera.y_max == False and  My_roc_gym.Camera.y_distance > My_roc_gym.Camera.y_min == False:
                My_roc_gym.Camera.camera_moving = False
        
        def get_offset():

            current_time = pygame.time.get_ticks()

            if current_time > My_roc_gym.Camera.timer :
                My_roc_gym.Camera.timer = current_time + My_roc_gym.Camera.time_delay
             
'''
region = pygame.Rect(0,0,320,110)
square1 = my_roc_gym.scaled_surf.subsurface(region)

basket_image = pygame.image.load("lib/assets/my_roc_gym/basket.png").convert_alpha()
basket_size = basket_image.get_size()
basket = pygame.transform.smoothscale(basket_image,(basket_size[0]/4,basket_size[1]/4))
basket_rect = basket.get_rect()
'''

Enviornment_sounds.park_ambience.set_volume(0.5)
Enviornment_sounds.park_ambience.play(loops=-1)

#song = random.choice(Music.songs)
song = Music.hate_it_or_love_it
#print(song.__getattribute__)
song.set_volume(0.1)
#song.play() 

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
stage_rects = [my_roc_gym_background.background_rect,My_roc_gym.goal_rect,My_roc_gym.front_goal_rect,
               My_roc_gym.basket_rack_rect,*My_roc_gym.paint_rects,player.x]



# Game loop

controller1 = pygame.joystick.Joystick(0)

running = True
while running:

    screen.fill(gray_cement)

    #screen.blit(my_roc_gym.scaled_surf,(-270,-110))
   
    #screen.blit(square1,(0,0))
    #pygame.draw.rect(screen,(0,0,0),rect,2)
    #screen.blit(basket,(-660,-200))

    if game_state == "Loadup screen":
        Loadup_screen.draw_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                pass

    if game_state == "Main menu":
        Main_menu.Windows.draw_menu()
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    Main_menu.menu_select()

            elif event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0:
                    Main_menu.menu_select()
        

    if game_state == "My Gym":
        My_roc_gym.draw_gym()
        My_roc_gym.draw_detection_areas()
        My_roc_gym.Camera.offset_stage()
        My_roc_gym.Player.animate()
        My_roc_gym.Player.animation_move()
        My_roc_gym.Player.draw()
        My_roc_gym.Player.move()
        Pause_menu.draw_pause_menu()
    

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    Pause_menu.next_selected(-1)
                if event.key == pygame.K_DOWN:
                    Pause_menu.next_selected(1)
                if event.key == pygame.K_RETURN:
                    Pause_menu.next_selected(None)
                if event.key == pygame.K_ESCAPE:
                    Pause_menu.check_paused()
            

            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 6:
                    Pause_menu.check_paused()
                if Pause_menu.options_pressed == True:
                    if event.button == 11:
                        Pause_menu.next_selected(-1)
                    if event.button == 12:
                        Pause_menu.next_selected(1)
                    if event.button == 0:
                        Pause_menu.next_selected(None)
    else:
        Pause_menu.options_pressed = False
                
                    
  
    
    pygame.display.flip()

    clock.tick(FPS)/ 1000.0
    

    

# Quit Pygame
pygame.quit()
sys.exit()
