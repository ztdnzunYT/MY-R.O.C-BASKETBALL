import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Increase Speed with Shift Key")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)

# Define the rectangle's properties
rect_pos = [width // 2, height // 2]
rect_size = [50, 50]
normal_speed = 5
fast_speed = 10

# Create a clock object
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the keys pressed
    keys = pygame.key.get_pressed()

    # Determine speed
    speed = fast_speed if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT] else normal_speed

    # Update the rectangle's position based on arrow keys
    if keys[pygame.K_LEFT]:
        rect_pos[0] -= speed
    if keys[pygame.K_RIGHT]:
        rect_pos[0] += speed
    if keys[pygame.K_UP]:
        rect_pos[1] -= speed
    if keys[pygame.K_DOWN]:
        rect_pos[1] += speed

    # Clear the screen
    screen.fill(black)

    # Draw the rectangle
    pygame.draw.rect(screen, white, (*rect_pos, *rect_size))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate to 60 FPS
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
