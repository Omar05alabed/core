"""Hexadecimal output file of the A-Maze-ing activity.

Each cell of the maze is written as one hexadecimal digit whose bits
are the closed walls of the cell:

======  ===========
Bit     Direction
======  ===========
``0``   North
``1``   East
``2``   South
``3``   West
======  ===========

A bit set to ``1`` means that the wall is closed.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Mapping, Sequence

from mazegen import DELTAS, DIRECTIONS

if TYPE_CHECKING:
    from mazegen import MazeGenerator


def cell_to_hex(walls: Mapping[str, bool]) -> str:
    """Encode the four walls of one cell as a single hex digit.

    Args:
        walls: Wall state per direction, ``True`` when closed.

    Returns:
        One uppercase hexadecimal digit from ``0`` to ``F``.
    """
    value = 0
    for bit, direction in enumerate(DIRECTIONS):
        if walls[direction]:
            value |= 1 << bit
    return format(value, "X")


def convert_path(path: Sequence[tuple[int, int]]) -> str:
    """Turn a list of cells into movement directions.

    Args:
        path: List of ``(row, column)`` cells, entry first.

    Returns:
        A string of ``N``, ``E``, ``S`` and ``W`` movements.

    Raises:
        ValueError: If two consecutive cells are not neighbours.
    """
    moves: list[str] = []
    for (row, col), (next_row, next_col) in zip(path, path[1:]):
        delta = (next_row - row, next_col - col)
        for direction, step in DELTAS.items():
            if delta == step:
                moves.append(direction)
                break
        else:
            raise ValueError(
                f"invalid path movement: {(row, col)} -> "
                f"{(next_row, next_col)}"
            )
    return "".join(moves)


def write_maze(
    maze: "MazeGenerator",
    path: Sequence[tuple[int, int]],
    file_path: str,
) -> None:
    """Write the maze, the positions and the path to a file.

    The file contains one line of hexadecimal digits per maze row,
    one empty line, the entry as ``(x, y)``, the exit as ``(x, y)``
    and the shortest path as movement directions.  Every line ends
    with a line feed.

    Args:
        maze: The generated maze.
        path: Shortest path from the entry to the exit.
        file_path: Name of the file to write.

    Raises:
        OSError: If the file cannot be written.
    """
    lines: list[str] = []
    for row in maze.grid.cells:
        lines.append(
            "".join(cell_to_hex(cell.walls) for cell in row)
        )
    lines.append("")
    lines.append(f"({maze.start[1]}, {maze.start[0]})")
    lines.append(f"({maze.end[1]}, {maze.end[0]})")
    lines.append(convert_path(path))
    with open(file_path, "w", encoding="utf-8", newline="\n") as out:
        out.write("\n".join(lines) + "\n")
