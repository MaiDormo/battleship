from grid import Grid
from events import handle_click


class Player:
    def __init__(self, pygame, screen, offset):
        self.grid = Grid(pygame, screen)
        self.total_health = sum(ship.health for ship in self.grid.ships)
        self.offset = offset

    def place_ships(self):
        self.grid.place_ships()

    def draw(self):
        self.grid.draw(self.offset)

    def handle_click(self, pygame, screen, offset):
        return handle_click(self.grid.grid, pygame, screen, offset)