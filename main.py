# main.py
import pygame
from constants import *
from grid import Grid
from events import handle_click


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

# Initialize the grid
personalGrid = Grid()
ships_sunk = 0

personalGrid.place_ships()

# game loop
while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            ships_sunk = handle_click(personalGrid.grid,ships_sunk,pygame,screen)
            
    # Check if all ships have been sunk
    if ships_sunk == 5:
        print("All ships have been sunk!")
        running = False  # End the game


    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    personalGrid.draw(pygame,screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()


