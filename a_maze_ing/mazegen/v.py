from enum import Enum
from .maze_generator import MazeGenerator
from .pattern import pattern_cells
from .shortest_path import shortest_path


DARK_RED = "\033[48;2;94;28;35m"
LAVENDER = "\033[48;2;180;167;214m"
ORANGE = "\033[38;2;255;165;0m"
BABY_PINK = "\033[48;2;223;115;149m"


class Chars(Enum):
    WALL = "█"
    HWALL = "██"


def convert_to_binary(output_file: str):
    with open(output_file, "r") as file:
        binary = []
        for line in file:
            # print("READ:", repr(line))
            if line.startswith("("):
                break
            for digit in line.strip():
                # print("DIGIT:", repr(line))
                b = int(digit, 16)
                b = bin(b)[2:]
                binary.append(b.zfill(4))
    return binary


def put_the_walls(binary):
    walls = []
    i = 0
    for i in binary:
        cell = []
        if i[0] == "1":
            cell.append("N")
        if i[1] == "1":
            cell.append("E")
        if i[2] == "1":
            cell.append("S")
        if i[3] == "1":
            cell.append("W")
        walls.append(cell)
    return walls


def canvas(width, height):
    width = width * 2 + 1
    height = height * 2 + 1

    canvas = [[" "] * width for _ in range(height)]

    # top
    for t in range(width):
        canvas[0][t] = Chars.WALL.value

    # bottom
    for b in range(width):
        canvas[height - 1][b] = Chars.WALL.value

    # left
    for le in range(height):
        canvas[le][0] = Chars.WALL.value

    # right
    for r in range(height):
        canvas[r][width - 1] = Chars.WALL.value

    return canvas


def print_walls(canvas, walls, width):
    for i, cell_walls in enumerate(walls):
        row = i // width
        col = i % width

        x = col * 2 + 1
        y = row * 2 + 1

        for wall in cell_walls:
            if wall == "N":
                canvas[y - 1][x] = Chars.WALL.value
                canvas[y - 1][x + 1] = Chars.WALL.value

            elif wall == "S":
                canvas[y + 1][x] = Chars.WALL.value
                canvas[y + 1][x + 1] = Chars.WALL.value

            elif wall == "W":
                canvas[y][x - 1] = Chars.WALL.value

            elif wall == "E":
                canvas[y][x + 1] = Chars.WALL.value

    return canvas


def coloring_entry_exit(canvas: list[list[str]], maze: "MazeGenerator",
                        color: str):
    RESET = "\033[0m"
    entr_row = maze.start[0] * 2 + 1
    entr_col = maze.start[1] * 2 + 1

    exit_row = maze.end[0] * 2 + 1
    exit_col = maze.end[1] * 2 + 1

    canvas[entr_row][entr_col] = f"{color} {RESET}"
    canvas[exit_row][exit_col] = f"{color} {RESET}"

    return canvas


def coloring_42(
    canvas: list[list[str]],
    maze: "MazeGenerator",
    color: str,
) -> list[list[str]]:
    RESET = "\033[0m"
    pattern = set(pattern_cells(maze))

    for row, col in pattern:
        canvas_row = row * 2 + 1
        canvas_col = col * 2 + 1

        # Color the cell itself
        canvas[canvas_row][canvas_col] = f"{color} {RESET}"

        # Connect to the cell on the right, but never paint over a wall
        if ((row, col + 1) in pattern
           and canvas[canvas_row][canvas_col + 1] != Chars.WALL.value):

            canvas[canvas_row][canvas_col + 1] = f"{color} {RESET}"

        # Connect to the cell below, but never paint over a wall
        if ((row + 1, col) in pattern
           and canvas[canvas_row + 1][canvas_col] != Chars.WALL.value):

            canvas[canvas_row + 1][canvas_col] = f"{color} {RESET}"

    return canvas


def color_walls(canvas: list[list[str]], color: str) -> list[list[str]]:
    RESET = "\033[0m"

    rows = len(canvas)
    cols = len(canvas[0])
    for r in range(rows):
        for c in range(cols):
            is_cell_center = (r % 2 == 1 and c % 2 == 1)
            if is_cell_center:
                continue
            if canvas[r][c] == Chars.WALL.value:
                canvas[r][c] = f"{color}{Chars.WALL.value}{RESET}"
    return canvas


def colored_path(
    canvas: list[list[str]],
    path: list[tuple[int, int]],
    color: str,
) -> list[list[str]]:

    RESET = "\033[0m"
    for i in range(len(path)):
        row, col = path[i]

        canvas_row = row * 2 + 1
        canvas_col = col * 2 + 1

        # Color the cell
        canvas[canvas_row][canvas_col] = f"{color} {RESET}"

        # Connect to the next cell
        if i + 1 < len(path):
            next_row, next_col = path[i + 1]

            if next_col == col + 1:      # moving right
                canvas[canvas_row][canvas_col + 1] = f"{color} {RESET}"
            elif next_col == col - 1:    # moving left
                canvas[canvas_row][canvas_col - 1] = f"{color} {RESET}"
            elif next_row == row + 1:    # moving down
                canvas[canvas_row + 1][canvas_col] = f"{color} {RESET}"
            elif next_row == row - 1:    # moving up
                canvas[canvas_row - 1][canvas_col] = f"{color} {RESET}"

    return canvas


def validate_path(
    maze: MazeGenerator,
    path: list[tuple[int, int]],
) -> None:
    """Verify that every path step crosses an open wall."""
    direction_map = {
        (-1, 0): "N",
        (0, 1): "E",
        (1, 0): "S",
        (0, -1): "W",
    }

    for current, following in zip(path, path[1:]):
        row, col = current
        next_row, next_col = following

        movement = (next_row - row, next_col - col)

        if movement not in direction_map:
            raise ValueError(
                f"Invalid path movement: {current} -> {following}"
            )

        direction = direction_map[movement]

        if maze.grid.cells[row][col].walls[direction]:
            raise ValueError(
                f"Path crosses a closed wall: "
                f"{current} -> {following}"
            )


def draw_maze(maze: MazeGenerator, output_filee,
              color42, wcolor, ecolor, pcolor):

    '''
    maze = MazeGenerator(
                       height,
                       width,
                       perfect,
                       entry,
                       exit,
                       seed,
        )

    maze.generator()

    '''
    s = shortest_path(maze)
    validate_path(maze, s)
    b = convert_to_binary(output_filee)
    p = put_the_walls(b)
    c = canvas(maze.grid.colm, maze.grid.row)
    print_walls(c, p, maze.grid.colm)
    coloring_42(c, maze, color42)
    color_walls(c, wcolor)
    colored_path(c, s, pcolor)
    coloring_entry_exit(c, maze, ecolor)

    for row in c:
        print("".join(character * 2 for character in row))


if __name__ == "__main__":
    maze = MazeGenerator(
                       20,
                       20,
                       True,
                       (0, 0),
                       (19, 15),
                       None,
        )

    draw_maze(maze, "output_maze.txt", DARK_RED, LAVENDER, ORANGE, BABY_PINK)
