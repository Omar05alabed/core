from mazegen.maze_generator import MazeGenerator
from mazegen.cell import Cell

import random
import time


def dfs(maze: MazeGenerator):
    # start = maze.start
    # step 1
    start = maze.grid.cells[maze.start[0]][maze.start[1]]
    # curr = start
    # curr.visited = not curr.visited
    # print(start)
    # print(maze.grid.get_neighbors(maze.grid.cells[0][1]))
    # neighbour = maze.grid.get_neighbors(maze.grid.cells[0][1])
    # print(neighbour)
    start.visited = not start.visited
    unvisited = [start]
    # --------------------------------------------
    # step 2
    while unvisited:
        curr = unvisited[-1]
        print("curr =", curr)
        nb = maze.grid.get_neighbors(curr)
        for n in nb:
            print("n =", n)
            x, y, _ = n
            neighbour = maze.grid.cells[x][y]

            if neighbour.visited:
                continue
            neighbour.visited = not neighbour.visited
            unvisited.append(neighbour)
            time.sleep(1)

        '''
        for n in neighbour:
            print("n =", n)
            while not start.visited:
                t = start
                r = random.choice(neighbour)
                s.append(r)
                print(s)
                t.visited = not t.visited
                print("r =", r)
            # time.sleep(1)
        print("s =", s)
        '''


if __name__ == "__main__":
    maze = MazeGenerator(
        5,
        5,
        True,
        (1, 1),
        (5, 4),
        5,
        )
    dfs(maze)
