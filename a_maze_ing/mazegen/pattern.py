from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .maze_generator import MazeGenerator

PAT_H = 8
PAT_W = 14

closed_cells = [
    # 4
    (0, 0), (0, 4),
    (1, 0), (1, 4),
    (2, 0), (2, 4),
    (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5),
    (4, 4),
    (5, 4),
    (6, 4),
    (7, 4),

    # 2
    (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (0, 12), (0, 13),
    (1, 13),
    (2, 13),
    (3, 7), (3, 8), (3, 9), (3, 10), (3, 11), (3, 12), (3, 13),
    (4, 7),
    (5, 7),
    (6, 7), (6, 8), (6, 9), (6, 10), (6, 11), (6, 12), (6, 13),
]


def pattern_origin(maze: "MazeGenerator") -> tuple[int, int]:
    """
    Calculate the top-left position of the 42 pattern.
    The pattern is positioned approximately in the center of the maze.
    Args: maze: The MazeGenerator containing the maze dimensions.
    Returns: A ``(row, column)`` tuple representing the top-left position
    of the 42 pattern.
"""
    row0 = (maze.grid.row - PAT_H) // 2
    col0 = maze.grid.colm // 2 - 6
    return row0, col0


def pattern_cells(maze: "MazeGenerator") -> set[tuple[int, int]]:
    """
    Return the maze coordinates occupied by the 42 pattern.
    The coordinates stored in ``closed_cells`` are relative
    to the pattern's origin.
    They are converted into actual maze coordinates using ``pattern_origin()``.
    Args: maze: The MazeGenerator containing the maze dimensions.
    Returns: A set of ``(row, column)`` coordinates belonging
    to the 42 pattern.
"""
    row0, col0 = pattern_origin(maze)
    return {(row0 + r, col0 + c) for r, c in closed_cells}


def in_42_pattern(maze: "MazeGenerator", point: tuple[int, int]) -> bool:
    """
    Check whether a coordinate belongs to the 42 pattern.
    Args: maze: The MazeGenerator containing the maze dimensions.
    point: The ``(row, column)`` coordinate to check.
    Returns: ``True`` if the coordinate belongs to the 42 pattern,
    otherwise ``False``.
"""
    return point in pattern_cells(maze)


def check_42(maze: "MazeGenerator") -> None:
    """
    Check the maze size and reserve the 42 pattern.

    Skips the pattern if the maze is too small and raises an error if
    the entry or exit is inside the pattern. Pattern cells are marked
    as visited so maze generation does not use them.
    """
    row0, col0 = pattern_origin(maze)

    too_small = (
        row0 < 1
        or col0 < 1
        or row0 + PAT_H > maze.grid.row - 1
        or col0 + PAT_W > maze.grid.colm - 1
    )
    if too_small:
        print("Error: maze too small for the 42 pattern, it will be omitted.")
        return

    cells = pattern_cells(maze)
    if maze.start in cells or maze.end in cells:
        raise ValueError(
            "ENTRY or EXIT is inside the 42 pattern, choose other coordinates."
        )

    for r, c in cells:
        maze.grid.cells[r][c].visited = True
