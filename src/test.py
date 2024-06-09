import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Smooth Animation Example")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)

# Define the ball's properties
ball_pos = [50, height // 2]
ball_radius = 20
ball_speed = 5

# Create a clock object
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the ball's position
    ball_pos[0] += ball_speed
    if ball_pos[0] > width + ball_radius:
        ball_pos[0] = -ball_radius

    # Clear the screen
    screen.fill(black)

    # Draw the ball
    pygame.draw.circle(screen, white, ball_pos, ball_radius)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate to 60 FPS
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
