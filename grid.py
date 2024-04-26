import random
from constants import EMPTY, GRID_SIZE, HIT, MISS, NUM_CELLS, SHIP, DEBUG, SIZE


class Grid:

    def __init__(self):
        self.grid = [[EMPTY for x in range(NUM_CELLS)] for y in range(NUM_CELLS)]

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

    def draw_line(self, pygame, screen, color, start, end):
        pygame.draw.line(screen, color, start, end)

    def draw(self, pygame, screen):
        # Calculate the starting point to center the grid
        start_x = (screen.get_width() - SIZE) // 2
        start_y = (screen.get_height() - SIZE) // 2

        # Draw the vertical lines
        for x in range(NUM_CELLS + 1):
            self.draw_line(pygame, screen, "white", (start_x + x * GRID_SIZE, start_y), (start_x + x * GRID_SIZE, start_y + SIZE))

        # Draw the horizontal lines
        for y in range(NUM_CELLS + 1):
            self.draw_line(pygame, screen, "white", (start_x, start_y + y * GRID_SIZE), (start_x + SIZE, start_y + y * GRID_SIZE))
        
        # Draw the hits and misses
        for x in range(NUM_CELLS):
            for y in range(NUM_CELLS):
                if self.grid[x][y] == MISS:
                    pygame.draw.circle(screen, "blue", (start_x + x * GRID_SIZE + GRID_SIZE // 2, start_y + y * GRID_SIZE + GRID_SIZE // 2), GRID_SIZE // 4)
                elif self.grid[x][y] == HIT: 
                    pygame.draw.circle(screen, "red", (start_x + x * GRID_SIZE + GRID_SIZE // 2, start_y + y * GRID_SIZE + GRID_SIZE // 2), GRID_SIZE // 4)
                elif self.grid[x][y] == SHIP:
                    pygame.draw.rect(screen, "red", (start_x + x * GRID_SIZE, start_y + y * GRID_SIZE, GRID_SIZE, GRID_SIZE))
                
        # Draw the labels
        font = pygame.font.Font(None, 24)
        for x in range(NUM_CELLS):
            label = font.render(chr(65 + x), 1, (255, 255, 255))
            screen.blit(label, (start_x + x * GRID_SIZE + GRID_SIZE // 2, start_y - GRID_SIZE))
        for y in range(NUM_CELLS):
            label = font.render(str(y + 1), 1, (255, 255, 255))
            screen.blit(label, (start_x - GRID_SIZE, start_y + y * GRID_SIZE + GRID_SIZE // 2))