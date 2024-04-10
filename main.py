# Example file showing a circle moving on screen
import pygame


def draw_grid():
    grid_size = 40  # size of the grid cells
    num_cells = 10  # number of cells in each direction
    size = num_cells * grid_size

    # Calculate the starting point to center the grid
    start_x = (screen.get_width() - size) // 2
    start_y = (screen.get_height() - size) // 2

    # Draw the vertical lines
    for x in range(num_cells + 1):
        pygame.draw.line(screen, "white", (start_x + x * grid_size, start_y), (start_x + x * grid_size, start_y + size))

    # Draw the horizontal lines
    for y in range(num_cells + 1):
        pygame.draw.line(screen, "white", (start_x, start_y + y * grid_size), (start_x + size, start_y + y * grid_size))
    
    font = pygame.font.Font(None, 24)  # Choose the font for the letters and numbers
    for i in range(num_cells):
        letter = chr(65 + i)  # Convert number to ASCII character, starting from 'A'
        number = str(i + 1)  # Convert number to string, starting from '1'
        letter_surface = font.render(letter, True, "white")
        number_surface = font.render(number, True, "white")
        screen.blit(letter_surface, (start_x + i * grid_size + 12, start_y - grid_size // 2 - 5))
        screen.blit(number_surface, (start_x - grid_size // 2 - 5, start_y + i * grid_size + 12))

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("darkblue")

    draw_grid()

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()


