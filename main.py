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
playerOneGrid = Grid(pygame, screen)
playerTwoGrid = Grid(pygame, screen)
shipsSunkPlayerOne = 0
shipsSunkPlayerTwo = 0

offsetPlayerOne = 2.5
offsetPlayerTwo = 0.1

playerOneGrid.place_ships()
playerTwoGrid.place_ships()

# game loop
while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            shipsSunkPlayerOne = handle_click(playerOneGrid.grid,shipsSunkPlayerOne,pygame,screen,offsetPlayerOne)
            shipsSunkPlayerTwo = handle_click(playerTwoGrid.grid,shipsSunkPlayerTwo,pygame,screen,offsetPlayerTwo)
            
    # Check if all ships have been sunk
    if shipsSunkPlayerOne == 5:
        print("Player Two won!!")
        running = False  # End the game
    if shipsSunkPlayerTwo == 5:
        print("Player One won!!")
        running = False  # End the game


    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    playerOneGrid.draw(offsetPlayerOne)
    playerTwoGrid.draw(offsetPlayerTwo)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()


