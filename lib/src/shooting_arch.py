import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Arch")
# Create a clock object
clock = pygame.time.Clock()

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)

class My_roc_gym():

    class Jumpshot():

        shot_time = 10
    
        x = 300
        y = 400

        startpoint1_x = x
        startpoint1_y = y + 20
        
        startpoint2_x = x
        startpoint2_y = y -300

        start_point_1 = pygame.Rect(startpoint1_x,startpoint1_y,20,20)
        start_point_2 = pygame.Rect(startpoint2_x,startpoint2_y,20,20)

        #goal endpoint
        endpoint1_x = 100
        endpoint1_y = 250

        #goal height endpoint
        endpoint2_x = 200
        endpoint2_y = startpoint2_y

        def draw_rects():
            pygame.draw.rect(screen,(255,0,0),(My_roc_gym.Jumpshot.start_point_1),1)
            pygame.draw.rect(screen,(255,0,0),(My_roc_gym.Jumpshot.start_point_2),1)
            pygame.draw.rect(screen,(0,255,0),(My_roc_gym.Jumpshot.endpoint1_x,My_roc_gym.Jumpshot.endpoint1_y,20,20),1)
            pygame.draw.rect(screen,(255,0,0),(My_roc_gym.Jumpshot.endpoint2_x,My_roc_gym.Jumpshot.endpoint2_y,20,20),1)       

        
        def draw_lines():
            pygame.draw.line(screen,(255,255,255),(My_roc_gym.Jumpshot.startpoint1_x+20,My_roc_gym.Jumpshot.startpoint1_y),(My_roc_gym.Jumpshot.startpoint2_x+20,My_roc_gym.Jumpshot.startpoint2_y))
            pygame.draw.line(screen,(255,255,255),(My_roc_gym.Jumpshot.startpoint2_x,My_roc_gym.Jumpshot.startpoint2_y),(My_roc_gym.Jumpshot.endpoint2_x,My_roc_gym.Jumpshot.endpoint2_y))
            pygame.draw.line(screen,(255,255,255),(My_roc_gym.Jumpshot.endpoint1_x,My_roc_gym.Jumpshot.endpoint1_y),(My_roc_gym.Jumpshot.endpoint2_x,My_roc_gym.Jumpshot.endpoint2_y))


        def get_sp_distance(x1,x2,y1,y2):
            return (math.sqrt((x2 - x1)**2 + (y2-y1)**2)) 

        

        class Sps():

            def __init__(self,x,y,distance,dx,dy,shot_time):
                self.x = x
                self.y = y
                self.dx = dx
                self.dy = dy
                self.distance = distance
                self.radius = 10
                self.shot_time = shot_time
                self.speed = (distance / (self.shot_time*120))
                self.vel_x = (dx/self.distance * self.speed)
                self.vel_y = (dy/self.distance * self.speed)
            
            def shoot():
            
                
                My_roc_gym.Jumpshot.sp1.vel_x = (My_roc_gym.Jumpshot.sp1.dx/My_roc_gym.Jumpshot.sp1.distance * My_roc_gym.Jumpshot.sp1.speed)
                My_roc_gym.Jumpshot.sp1.y += My_roc_gym.Jumpshot.sp1.vel_y

                My_roc_gym.Jumpshot.sp2.x += My_roc_gym.Jumpshot.sp2.vel_x
            
                My_roc_gym.Jumpshot.sp3.x += My_roc_gym.Jumpshot.sp3.vel_x
                My_roc_gym.Jumpshot.sp3.y += My_roc_gym.Jumpshot.sp3.vel_y

                My_roc_gym.Jumpshot.sp4.dx = My_roc_gym.Jumpshot.sp2.x-My_roc_gym.Jumpshot.sp1.x
                My_roc_gym.Jumpshot.sp4.dy = My_roc_gym.Jumpshot.sp2.y-My_roc_gym.Jumpshot.sp1.y
                My_roc_gym.Jumpshot.sp4.speed = (My_roc_gym.Jumpshot.sp4.distance/(My_roc_gym.Jumpshot.shot_time*120))
                My_roc_gym.Jumpshot.sp4.vel_x = (My_roc_gym.Jumpshot.sp4.dx/My_roc_gym.Jumpshot.sp4.distance * My_roc_gym.Jumpshot.sp4.speed)
                My_roc_gym.Jumpshot.sp4.vel_y = (My_roc_gym.Jumpshot.sp4.dy/My_roc_gym.Jumpshot.sp4.distance * My_roc_gym.Jumpshot.sp4.speed)
                My_roc_gym.Jumpshot.sp4.x += My_roc_gym.Jumpshot.sp4.vel_x *2
                My_roc_gym.Jumpshot.sp4.y += My_roc_gym.Jumpshot.sp4.vel_y*2
            
                My_roc_gym.Jumpshot.sp5.dx = My_roc_gym.Jumpshot.sp3.x-My_roc_gym.Jumpshot.sp2.x
                My_roc_gym.Jumpshot.sp5.dy = My_roc_gym.Jumpshot.sp3.y-My_roc_gym.Jumpshot.sp2.y
                My_roc_gym.Jumpshot.sp5.distance = My_roc_gym.Jumpshot.get_sp_distance(My_roc_gym.Jumpshot.sp2.x,My_roc_gym.Jumpshot.sp3.x,My_roc_gym.Jumpshot.sp2.y,My_roc_gym.Jumpshot.sp3.y)
                My_roc_gym.Jumpshot.sp5.speed = (My_roc_gym.Jumpshot.sp5.distance/(My_roc_gym.Jumpshot.shot_time*120))
                My_roc_gym.Jumpshot.sp5.vel_x = (My_roc_gym.Jumpshot.sp5.dx/My_roc_gym.Jumpshot.sp5.distance * My_roc_gym.Jumpshot.sp5.speed)
                My_roc_gym.Jumpshot.sp5.vel_y = (My_roc_gym.Jumpshot.sp5.dy/My_roc_gym.Jumpshot.sp5.distance * My_roc_gym.Jumpshot.sp5.speed)
                My_roc_gym.Jumpshot.sp5.x += My_roc_gym.Jumpshot.sp5.vel_x *2
                My_roc_gym.Jumpshot.sp5.y += My_roc_gym.Jumpshot.sp5.vel_y*2

                My_roc_gym.Jumpshot.sp6.dx = My_roc_gym.Jumpshot.sp5.x-My_roc_gym.Jumpshot.sp4.x
                My_roc_gym.Jumpshot.sp6.dy = My_roc_gym.Jumpshot.sp5.y-My_roc_gym.Jumpshot.sp4.y
                My_roc_gym.Jumpshot.sp6.distance = My_roc_gym.Jumpshot.get_sp_distance(My_roc_gym.Jumpshot.sp4.x,My_roc_gym.Jumpshot.sp5.x,My_roc_gym.Jumpshot.sp4.y,My_roc_gym.Jumpshot.sp5.y)
                My_roc_gym.Jumpshot.sp6.speed = (My_roc_gym.Jumpshot.sp6.distance/(My_roc_gym.Jumpshot.shot_time*120))
                My_roc_gym.Jumpshot.sp6.vel_x = (My_roc_gym.Jumpshot.sp6.dx/My_roc_gym.Jumpshot.sp6.distance * My_roc_gym.Jumpshot.sp6.speed)
                My_roc_gym.Jumpshot.sp6.vel_y = (My_roc_gym.Jumpshot.sp6.dy/My_roc_gym.Jumpshot.sp6.distance * My_roc_gym.Jumpshot.sp6.speed)
                My_roc_gym.Jumpshot.sp6.x += My_roc_gym.Jumpshot.sp6.vel_x * 3
                My_roc_gym.Jumpshot.sp6.y += My_roc_gym.Jumpshot.sp6.vel_y * 3.2

                for sp in My_roc_gym.Jumpshot.shot_points:
                    pygame.draw.circle(screen,(255,255,0,),(sp.x,sp.y),sp.radius,1)
                    


        sp1 = Sps(startpoint1_x,startpoint1_y,get_sp_distance(startpoint1_x,startpoint1_y,startpoint2_x,startpoint2_y),(startpoint2_x-startpoint1_x),(startpoint2_y-startpoint1_y),shot_time)
        sp2 = Sps(startpoint2_x,startpoint2_y,get_sp_distance(startpoint2_x,startpoint2_y,endpoint2_x,endpoint2_y),(endpoint2_x-startpoint2_x),(endpoint2_y-startpoint2_y),shot_time)
        sp3 = Sps(endpoint2_x,endpoint2_y,get_sp_distance(endpoint1_x,endpoint1_y,endpoint2_x,endpoint2_y),(endpoint1_x-endpoint2_x),(endpoint1_y-endpoint2_y),shot_time)
        sp4 = Sps(sp1.x,sp1.y,get_sp_distance(sp2.x,sp1.x,sp2.y,sp1.y),(sp2.x-sp1.x),(sp2.y-sp1.y),shot_time)
        sp5 = Sps(sp2.x,sp2.y,get_sp_distance(sp3.x,sp2.x,sp3.y,sp2.y),(sp3.x-sp2.x),(sp3.y-sp2.y),shot_time)
        sp6 = Sps(sp4.x,sp4.y,get_sp_distance(sp5.x,sp4.x,sp5.y,sp4.y),(sp5.x-sp4.x),(sp5.y-sp5.y),shot_time)

        shot_points = [sp1,sp2,sp3,sp4,sp5,sp6]

        def reset():
            print("My_roc_gym.Jumpshot.shot_time reset")
            My_roc_gym.Jumpshot.shot_time = 2
            
            My_roc_gym.Jumpshot.startpoint1_x = My_roc_gym.Jumpshot.x
            startpoint1_y = My_roc_gym.Jumpshot.y + 20
            My_roc_gym.Jumpshot.startpoint2_x = My_roc_gym.Jumpshot.x
            My_roc_gym.Jumpshot.startpoint2_y = My_roc_gym.Jumpshot.y -300

            My_roc_gym.Jumpshot.endpoint1_x = 100
            My_roc_gym.Jumpshot.endpoint1_y = 250

            #goal height endpoint
            My_roc_gym.Jumpshot.endpoint2_x = 200
            My_roc_gym.Jumpshot.endpoint2_y = My_roc_gym.Jumpshot.startpoint2_y

            My_roc_gym.Jumpshot.sp1.x = My_roc_gym.Jumpshot.startpoint1_x
            My_roc_gym.Jumpshot.sp1.y = startpoint1_y

            My_roc_gym.Jumpshot.sp2.x = My_roc_gym.Jumpshot.startpoint2_x
            My_roc_gym.Jumpshot.sp2.y = My_roc_gym.Jumpshot.startpoint2_y

            My_roc_gym.Jumpshot.sp3.x = My_roc_gym.Jumpshot.endpoint2_x
            My_roc_gym.Jumpshot.sp3.y = My_roc_gym.Jumpshot.endpoint2_y

            My_roc_gym.Jumpshot.sp4.x = My_roc_gym.Jumpshot.sp1.x
            My_roc_gym.Jumpshot.sp4.y = My_roc_gym.Jumpshot.sp1.y

            My_roc_gym.Jumpshot.sp5.x = My_roc_gym.Jumpshot.sp2.x
            My_roc_gym.Jumpshot.sp5.y = My_roc_gym.Jumpshot.sp2.y

            My_roc_gym.Jumpshot.sp6.x = My_roc_gym.Jumpshot.sp4.x
            My_roc_gym.Jumpshot.sp6.y = My_roc_gym.Jumpshot.sp4.y

            # Recalculate distances and velocities
            My_roc_gym.Jumpshot.sp4.dx = My_roc_gym.Jumpshot.sp2.x - My_roc_gym.Jumpshot.sp1.x
            My_roc_gym.Jumpshot.sp4.dy = My_roc_gym.Jumpshot.sp2.y - My_roc_gym.Jumpshot.sp1.y
            My_roc_gym.Jumpshot.sp4.distance = My_roc_gym.Jumpshot.get_sp_distance(My_roc_gym.Jumpshot.sp1.x, My_roc_gym.Jumpshot.sp2.x, My_roc_gym.Jumpshot.sp1.y, My_roc_gym.Jumpshot.sp2.y)
            My_roc_gym.Jumpshot.sp4.speed = (My_roc_gym.Jumpshot.sp4.distance / (My_roc_gym.Jumpshot.shot_time * 120))
            My_roc_gym.Jumpshot.sp4.vel_x = (My_roc_gym.Jumpshot.sp4.dx / My_roc_gym.Jumpshot.sp4.distance * My_roc_gym.Jumpshot.sp4.speed)
            My_roc_gym.Jumpshot.sp4.vel_y = (My_roc_gym.Jumpshot.sp4.dy / My_roc_gym.Jumpshot.sp4.distance * My_roc_gym.Jumpshot.sp4.speed)

            My_roc_gym.Jumpshot.sp5.dx = My_roc_gym.Jumpshot.sp3.x - My_roc_gym.Jumpshot.sp2.x
            My_roc_gym.Jumpshot.sp5.dy = My_roc_gym.Jumpshot.sp3.y - My_roc_gym.Jumpshot.sp2.y
            My_roc_gym.Jumpshot.sp5.distance = My_roc_gym.Jumpshot.get_sp_distance(My_roc_gym.Jumpshot.sp2.x, My_roc_gym.Jumpshot.sp3.x, My_roc_gym.Jumpshot.sp2.y, My_roc_gym.Jumpshot.sp3.y)
            My_roc_gym.Jumpshot.sp5.speed = (My_roc_gym.Jumpshot.sp5.distance / (My_roc_gym.Jumpshot.shot_time * 120))
            My_roc_gym.Jumpshot.sp5.vel_x = (My_roc_gym.Jumpshot.sp5.dx / My_roc_gym.Jumpshot.sp5.distance * My_roc_gym.Jumpshot.sp5.speed)
            My_roc_gym.Jumpshot.sp5.vel_y = (My_roc_gym.Jumpshot.sp5.dy / My_roc_gym.Jumpshot.sp5.distance * My_roc_gym.Jumpshot.sp5.speed)

            My_roc_gym.Jumpshot.sp6.dx = My_roc_gym.Jumpshot.sp5.x - My_roc_gym.Jumpshot.sp4.x
            My_roc_gym.Jumpshot.sp6.dy = My_roc_gym.Jumpshot.sp5.y - My_roc_gym.Jumpshot.sp4.y

            My_roc_gym.Jumpshot.sp6.distance = My_roc_gym.Jumpshot.get_sp_distance(My_roc_gym.Jumpshot.sp4.x, My_roc_gym.Jumpshot.sp5.x, My_roc_gym.Jumpshot.sp4.y, My_roc_gym.Jumpshot.sp5.y)
            My_roc_gym.Jumpshot.sp6.speed = (My_roc_gym.Jumpshot.sp6.distance / (My_roc_gym.Jumpshot.shot_time * 120))
            My_roc_gym.Jumpshot.sp6.vel_x = (My_roc_gym.Jumpshot.sp6.dx / My_roc_gym.Jumpshot.sp6.distance * My_roc_gym.Jumpshot.sp6.speed)
            My_roc_gym.Jumpshot.sp6.vel_y = (My_roc_gym.Jumpshot.sp6.dy / My_roc_gym.Jumpshot.sp6.distance * My_roc_gym.Jumpshot.sp6.speed)





# Game loop
running = True
while running:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                My_roc_gym.Jumpshot.reset()
            

 


  
    

    My_roc_gym.Jumpshot.draw_rects()
    My_roc_gym.Jumpshot.draw_lines()
    My_roc_gym.Jumpshot.Sps.shoot()
    


    # Clear the screen
   

   
    # Update the display
    pygame.display.flip()

    # Cap the frame rate to 60 FPS
    clock.tick(120)

# Quit Pygame
pygame.quit()
sys.exit()
