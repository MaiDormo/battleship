import random
from constants import EMPTY, GRID_SIZE, HIT, MISS, NUM_CELLS, SHIP, DEBUG, SIZE
from ships import Ship, ShipType

class Grid:
    def __init__(self, pygame, screen):
        self.grid = [[EMPTY for _ in range(NUM_CELLS)] for _ in range(NUM_CELLS)]
        self.pygame = pygame
        self.screen = screen
        self.ships = [Ship(ship_type) for ship_type in ShipType]

    def generate_random_coordinates(self):
        return random.randint(0, NUM_CELLS - 1), random.randint(0, NUM_CELLS - 1), random.choice([True,False])

    def is_valid_position(self, x: int, y: int) -> bool:
        return 0 <= x < NUM_CELLS and 0 <= y < NUM_CELLS and self.grid[x][y] != SHIP

    def place_ships(self):
        for ship in self.ships:
            self.place_ship(ship)

    def place_ship(self, ship):
        while True:
            x, y, is_horizontal = self.generate_random_coordinates()
            if self.can_be_placed(x, y, is_horizontal, ship):
                for i in range(ship.health):
                    if is_horizontal:
                        self.grid[x+i][y] = SHIP
                    else:
                        self.grid[x][y+i] = SHIP
                break

    def can_be_placed(self, x: int, y: int, is_horizontal: bool, ship: Ship) -> bool:
        for i in range(ship.health):
            if not self.is_valid_position(x+i, y) if is_horizontal else not self.is_valid_position(x, y+i):
                return False
        return True

    def draw(self, offset):
        start_x = (self.screen.get_width() - SIZE*offset) // 2
        start_y = (self.screen.get_height() - SIZE) // 2

        for x in range(NUM_CELLS + 1):
            self.draw_line("white", (start_x + x * GRID_SIZE, start_y), (start_x + x * GRID_SIZE, start_y + SIZE))

        for y in range(NUM_CELLS + 1):
            self.draw_line("white", (start_x, start_y + y * GRID_SIZE), (start_x + SIZE, start_y + y * GRID_SIZE))

        draw_methods = {
            MISS: self.draw_miss,
            HIT: self.draw_hit,
            SHIP: self.draw_ship
        }

        for x in range(NUM_CELLS):
            for y in range(NUM_CELLS):
                draw_method = draw_methods.get(self.grid[x][y])
                if draw_method:
                    draw_method(start_x, start_y, x, y)

        self.draw_labels(start_x, start_y)

    def draw_line(self, color, start, end):
        self.pygame.draw.line(self.screen, color, start, end)

    def draw_miss(self, start_x, start_y, x, y):
        self.pygame.draw.circle(self.screen, "blue", (start_x + x * GRID_SIZE + GRID_SIZE // 2, start_y + y * GRID_SIZE + GRID_SIZE // 2), GRID_SIZE // 4)

    def draw_hit(self, start_x, start_y, x, y):
        self.pygame.draw.circle(self.screen, "red", (start_x + x * GRID_SIZE + GRID_SIZE // 2, start_y + y * GRID_SIZE + GRID_SIZE // 2), GRID_SIZE // 4)

    def draw_ship(self, start_x, start_y, x, y):
        self.pygame.draw.rect(self.screen, "red", (start_x + x * GRID_SIZE, start_y + y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    def draw_labels(self, start_x, start_y):
        font = self.pygame.font.Font(None, 24)
        for x in range(NUM_CELLS):
            label = font.render(chr(65 + x), 1, (255, 255, 255))
            self.screen.blit(label, (start_x + x * GRID_SIZE + GRID_SIZE // 2, start_y - GRID_SIZE))
        for y in range(NUM_CELLS):
            label = font.render(str(y + 1), 1, (255, 255, 255))
            self.screen.blit(label, (start_x - GRID_SIZE, start_y + y * GRID_SIZE + GRID_SIZE // 2))