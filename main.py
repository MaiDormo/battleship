# main.py
import pygame
from constants import *
from events import handle_click
from player import Player

def game_logic(opponent, pygame, screen, offset):
    valid_click, health_lost = handle_click(opponent.grid.grid, pygame, screen, offset)
    if valid_click:
        opponent.total_health -= health_lost
        return True
    return False

def switch_player(current_player):
    return 1 if current_player == 0 else 0

def update_game_state(players, current_player, pygame, screen, offset):
    if game_logic(players[switch_player(current_player)], pygame, screen, offset):
        current_player = switch_player(current_player)
    return current_player

def draw(players, screen):
    screen.fill("black")
    players[0].draw()
    players[1].draw()
    pygame.display.flip()

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    clock = pygame.time.Clock()
    running = True

    players = [
        Player(pygame, screen, OFFSET_PLAYER_ONE),
        Player(pygame, screen, OFFSET_PLAYER_TWO)
    ]

    players[0].place_ships()
    players[1].place_ships()

    current_player = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                current_player = update_game_state(players, current_player, pygame, screen, OFFSET_PLAYER_TWO if current_player == 0 else OFFSET_PLAYER_ONE)

        if players[0].total_health == 0 or players[1].total_health == 0:
            print(f"Player {switch_player(current_player) + 1} won!!")
            running = False

        draw(players, screen)
        clock.tick(FPS_LIMIT)

    pygame.quit()

if __name__ == "__main__":
    main()