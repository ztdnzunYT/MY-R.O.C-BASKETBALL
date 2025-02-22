import pygame
import math

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Start and end points
start_pos = (100, 100)
end_pos = (400, 400)
total_time = 2.0  # Move in 2 seconds

# Calculate distance and speed
dx = end_pos[0] - start_pos[0]
dy = end_pos[1] - start_pos[1]
distance = math.sqrt(dx**2 + dy**2)

# Velocity per frame (assuming 60 FPS)
speed = distance / (total_time * 60)
velocity_x = (dx / distance) * speed
velocity_y = (dy / distance) * speed

# Object properties
pos_x, pos_y = start_pos
running = True

while running:
    screen.fill((0, 0, 0))  # Clear screen
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the object
    pos_x += velocity_x
    pos_y += velocity_y

    # Draw moving object
    pygame.draw.circle(screen, (0, 255, 0), (int(pos_x), int(pos_y)), 10)

    # Stop movement when reaching the target
    if abs(pos_x - end_pos[0]) < abs(velocity_x) and abs(pos_y - end_pos[1]) < abs(velocity_y):
        pos_x, pos_y = end_pos

    pygame.display.flip()
    clock.tick(60)  # Limit FPS to 60

pygame.quit()
