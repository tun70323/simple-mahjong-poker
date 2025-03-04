import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mahjong Poker Demo")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 50, 50)
BLUE = (50, 50, 200)
GREEN = (34, 139, 34)  # Green table color

table_lines = [
    ((50, HEIGHT // 3), (WIDTH - 50, HEIGHT // 3)),  # Top line
    ((50, 2 * HEIGHT // 3), (WIDTH - 50, 2 * HEIGHT // 3))  # Bottom line
]

# Tile settings
TILE_WIDTH, TILE_HEIGHT = 80, 120
TILE_GAP = 20

def generate_hand():
    """Generate a hand of 5 random Mahjong tiles (numbers 1-6)."""
    return [random.randint(1, 6) for _ in range(5)]

# Initial player hand
tiles = generate_hand()

# Game loop
running = True
while running:
    screen.fill(GREEN)  # Set background to green (table color)
    
    # Draw white table lines
    for line in table_lines:
        pygame.draw.line(screen, WHITE, line[0], line[1], 5)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for i, tile in enumerate(tiles):
                tile_x = 150 + i * (TILE_WIDTH + TILE_GAP)
                tile_y = 2 * HEIGHT // 3 + 10  # Position inside the bottom section
                if tile_x <= mouse_x <= tile_x + TILE_WIDTH and tile_y <= mouse_y <= tile_y + TILE_HEIGHT:
                    tiles[i] = random.randint(1, 6)  # Replace with a new tile
                    
    # Draw tiles
    for i, tile in enumerate(tiles):
        tile_x = 150 + i * (TILE_WIDTH + TILE_GAP)
        tile_y = 2 * HEIGHT // 3 + 10  # Align within bottom section
        pygame.draw.rect(screen, RED if tile % 2 == 0 else BLUE, (tile_x, tile_y, TILE_WIDTH, TILE_HEIGHT))
        font = pygame.font.Font(None, 48)
        text = font.render(str(tile), True, WHITE)
        screen.blit(text, (tile_x + 25, tile_y + 40))
    
    pygame.display.flip()
    
pygame.quit()
