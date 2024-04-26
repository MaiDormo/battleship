# Function to handle the click event
from constants import EMPTY, GRID_SIZE, HIT, MISS, NUM_CELLS, DEBUG, OUTSIDE_GRID, SHIP, SIZE


def cell_clicked(pygame,screen, offset: float):
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Calculate the starting point to center the grid
    start_x = int((screen.get_width() - SIZE * offset) // 2)
    start_y = (screen.get_height() - SIZE) // 2

    # Calculate the cell coordinates
    cell_x = (mouse_x - start_x) // GRID_SIZE
    cell_y = (mouse_y - start_y) // GRID_SIZE

    # Check if the click was inside the grid
    if 0 <= cell_x < NUM_CELLS and 0 <= cell_y < NUM_CELLS:
        if DEBUG:
            print(f"Cell ({chr(65 + cell_x)}, {cell_y + 1}) was clicked.")
        return cell_x, cell_y
    else:
        if DEBUG:
            print("Click was outside the grid.")
        return OUTSIDE_GRID
    

def handle_click(grid, ships_sunk, pygame, screen, offset: float):
    cell_x, cell_y = cell_clicked(pygame, screen, offset)

    # check if the cell is already hit
    if (cell_x, cell_y) == OUTSIDE_GRID:
        if DEBUG:
            print("Click outside grid")
    elif grid[cell_x][cell_y] == EMPTY:
        grid[cell_x][cell_y] = MISS
    elif grid[cell_x][cell_y] == SHIP:
        grid[cell_x][cell_y] = HIT
        ships_sunk += 1
    else:
        print("Cell already hit")

    return ships_sunk