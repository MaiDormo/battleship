import random
from constants import EMPTY, GRID_SIZE, HIT, MISS, NUM_CELLS, SHIP, DEBUG, SIZE

#Implementation of the grid class
"""The idea behind this class is to have the ability to store the player grid"""
class Grid:

    def __init__(self, pygame, screen):
        self.grid = [[EMPTY for x in range(NUM_CELLS)] for y in range(NUM_CELLS)]
        self.pygame = pygame
        self.screen = screen

    def generate_random_coordinates(self):
        return random.randint(0, NUM_CELLS - 1), random.randint(0, NUM_CELLS - 1)

    def place_ships(self):
        # Place 5 ships
        for _ in range(5):
            # Randomly place the ship
            x, y = self.generate_random_coordinates()

            # Check if the cell is already occupied by a ship
            while self.grid[x][y] == SHIP:
                # If the cell is occupied, generate new random coordinates
                x, y = self.generate_random_coordinates()

            # Place the ship
            self.grid[x][y] = SHIP
            if DEBUG:
                print(f"Ship placed at ({chr(65 + x)}, {y + 1})")

    def draw_line(self, color, start, end):
        self.pygame.draw.line(self.screen, color, start, end)

    def draw(self,offset):
        # Calculate the starting point to center the grid
        start_x = (self.screen.get_width() - SIZE*offset) // 2
        start_y = (self.screen.get_height() - SIZE) // 2

        # Draw the vertical lines
        for x in range(NUM_CELLS + 1):
            self.draw_line("white", (start_x + x * GRID_SIZE, start_y), (start_x + x * GRID_SIZE, start_y + SIZE))

        # Draw the horizontal lines
        for y in range(NUM_CELLS + 1):
            self.draw_line("white", (start_x, start_y + y * GRID_SIZE), (start_x + SIZE, start_y + y * GRID_SIZE))
        
        # Draw the hits and misses
        for x in range(NUM_CELLS):
            for y in range(NUM_CELLS):
                if self.grid[x][y] == MISS:
                    self.pygame.draw.circle(self.screen, "blue", (start_x + x * GRID_SIZE + GRID_SIZE // 2, start_y + y * GRID_SIZE + GRID_SIZE // 2), GRID_SIZE // 4)
                elif self.grid[x][y] == HIT: 
                    self.pygame.draw.circle(self.screen, "red", (start_x + x * GRID_SIZE + GRID_SIZE // 2, start_y + y * GRID_SIZE + GRID_SIZE // 2), GRID_SIZE // 4)
                elif self.grid[x][y] == SHIP:
                    self.pygame.draw.rect(self.screen, "red", (start_x + x * GRID_SIZE, start_y + y * GRID_SIZE, GRID_SIZE, GRID_SIZE))
                
        # Draw the labels
        font = self.pygame.font.Font(None, 24)
        for x in range(NUM_CELLS):
            label = font.render(chr(65 + x), 1, (255, 255, 255))
            self.screen.blit(label, (start_x + x * GRID_SIZE + GRID_SIZE // 2, start_y - GRID_SIZE))
        for y in range(NUM_CELLS):
            label = font.render(str(y + 1), 1, (255, 255, 255))
            self.screen.blit(label, (start_x - GRID_SIZE, start_y + y * GRID_SIZE + GRID_SIZE // 2))