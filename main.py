import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
FPS = 60
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pacman Lite")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Player
player_size = 30
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 5

# Ghost
ghost_size = 30
ghost_x = random.randint(0, WIDTH - ghost_size)
ghost_y = random.randint(0, HEIGHT - ghost_size)
ghost_speed = 3

# Score and level
score = 0
level = 1

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < HEIGHT - player_size:
        player_y += player_speed

    # Move the ghost
    ghost_x += ghost_speed
    if ghost_x > WIDTH or ghost_x < 0:
        ghost_speed = -ghost_speed

    # Check for collision with the ghost
    if (
        player_x < ghost_x + ghost_size
        and player_x + player_size > ghost_x
        and player_y < ghost_y + ghost_size
        and player_y + player_size > ghost_y
    ):
        print("Game Over!")
        pygame.quit()
        sys.exit()

    # Check for collision with the border (wrap around)
    if player_x > WIDTH:
        player_x = 0
    elif player_x < 0:
        player_x = WIDTH - player_size

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, YELLOW, (player_x, player_y, player_size, player_size))
    pygame.draw.rect(screen, BLUE, (ghost_x, ghost_y, ghost_size, ghost_size))

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(FPS)

# Clean up
pygame.quit()
sys.exit()