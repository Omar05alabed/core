import pygame

pygame.init()


def initalize(colomn, row):
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("my_maze")
    grid = []
    neighbours = []
    colomn = colomn
    row = row
    walls = [True, True, True, True]
    visited = False
    current = (0, 0)
    x = 0
    y = 0
    d = 50

    def check_neighbour(x, y):
        def boundreis(x, y):
            boundx = []
            boundy = []
            boundx.append(x + 1)
            boundx.append(x - 1)
            boundy.append(y + 1)
            boundy.append(y - 1)
            for bx in boundx:
                if (bx < 0 and bx > colomn):
                    return None
            for by in boundy:
                if (by < 0 and by > colomn):
                    return None

        boundreis(x, y)
        top = grid[x][y - 1]
        right = grid[x + 1][y]
        bottom = grid[x][y + 1]
        left = grid[x - 1][y]

        if (top and boundreis):
            neighbours.append(grid[x][y - 1])
        if right:
            neighbours.append(grid[x + 1][y])
        if bottom:
            neighbours.append(grid[x][y + 1])
        if left:
            neighbours.append(grid[x - 1][y])
        if len(neighbours) > 0:
            for n in neighbours:
                print(n * x)
                print("x", x)
                pygame.draw.rect(screen, (255, 255, 255),
                                 ((n * x,
                                   n * x,
                                   50,
                                   50)))




#    current = start
#    end = end
    for x in range(colomn):
        rows = []
        for y in range(row):
            rows.append(y)
        grid.append(rows)
    print(grid)
    for x in range(colomn):
        for y in range(row):
            px = x * d
            py = y * d
            if walls[0]:
                pygame.draw.line(screen, (0, 255, 255), (px, py), (px + d, py))
            if walls[1]:
                pygame.draw.line(screen, (0, 255, 255), (px + d, py), (px + d, py + d))
            if walls[2]:
                pygame.draw.line(screen, (0, 255, 255), (px + d, py + d), (px, py + d))
            if walls[3]:
                pygame.draw.line(screen, (0, 255, 255), (px, py + d), (px, py))





##    for y in range(colomn):
##        pygame.draw.line(screen, (0, 255, 255), (y * 50, 0), (y * 50, 450), 5)

##    for x in range(row):
##        pygame.draw.line(screen, (0, 255, 255), (0, x * 50), (450, x * 50), 5)

##    def current_cell(x, y):
##        pygame.draw.rect(screen, (255, 255, 255),
##                         ((0,
##                          0,
##                          50,
##                          50)))
##
##    current_cell(5, 6)
    check_neighbour(6, 5)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


initalize(10, 10)
