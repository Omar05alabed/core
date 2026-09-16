# this creats a grid, checks its neighbour and shows them
# we want to check if the cell is visited and (move to it)


import pygame
import random


class create_grid:
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.isvisited = False
        self.walls = [True, True, True, True]
        self.grid = []
        self.neighbour = []

    def create_grid(self):
        for x in range(self.width):
            rows = []
            for y in range(self.height):
                rows.append(y)
            self.grid.append(rows)
        return self.grid

    def check_neighbour(self, x, y):
        top = self.grid[x][y - 1]
        right = self.grid[x + 1][y]
        bottom = self.grid[x][y + 1]
        left = self.grid[x - 1][y]
# this part is wrong
        if self.isvisited:
            self.neighbour.append(top)
        if self.isvisited:
            self.neighbour.append(right)
        if self.isvisited:
            self.neighbour.append(bottom)
        if self.isvisited:
            self.neighbour.append(left)

        if len(self.neighbour) > 0:
            return random.choice(self.neighbour)

    def show(self):
        current = (0, 0)
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("my_maze")
        d = 50
        for x in range(self.width):
            for y in range(self.height):
                px = x * d
                py = y * d
                if self.walls[0]:
                    pygame.draw.line(screen, (0, 255, 255), (px, py), (px + d, py))
                if self.walls[1]:
                    pygame.draw.line(screen, (0, 255, 255), (px + d, py), (px + d, py + d))
                if self.walls[2]:
                    pygame.draw.line(screen, (0, 255, 255), (px + d, py + d), (px, py + d))
                if self.walls[3]:
                    pygame.draw.line(screen, (0, 255, 255), (px, py + d), (px, py))
        print(x)
        for cell in self.grid:
            print(cell)
            i, j = current
            self.grid[i][j]
            self.check_neighbour(i, j)
            pygame.draw.rect(screen, (255, 255, 255),
                             ((d * i,
                               d * j,
                               50,
                               50)))

        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()


p = create_grid(5, 5)
print(p.create_grid())
p.show()
