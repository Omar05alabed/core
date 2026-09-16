import pygame


def create_grid(width, height):
    grid = []
    for x in range(width):
        rows = []
        for y in range(height):
            rows.append(y)
        grid.append(rows)
    return grid

def show():
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("my_maze")
    size = 50
    for x in range(colomn):
        for y in range(row):
            px = x * size
            py = y * size
            if walls[0]:
                pygame.draw.line(screen, (0, 255, 255), (px, py), (px + size, py))
            if walls[1]:
                pygame.draw.line(screen, (0, 255, 255), (px + size, py), (px + size, py + size))
            if walls[2]:
                pygame.draw.line(screen, (0, 255, 255), (px + size, py + size), (px, py + size))
            if walls[3]:
                pygame.draw.line(screen, (0, 255, 255), (px, py + size), (px, py))
    




def cells(x, y):
    destenation = (x, y)
    walls = [True, True, True, True]
    isvisited = False
    neighbour = [
                top = grid[x][y - 1]
                right = grid[x + 1][y]
                bottom = grid[x][y + 1]
                left = grid[x - 1][y]
    ]

