"""Terminal visualization of the maze with ANSI colors.

The maze is drawn on a canvas of ``2 * width + 1`` columns and
``2 * height + 1`` rows.  Cell centers sit on odd rows and columns,
wall segments on even lines and the corners always stay closed, so
the walls of the maze are always fully drawn.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from typing import Sequence

from mazegen import MazeGenerator

WALL_CHAR = "█"
FLOOR_CHAR = " "
RESET = "\033[0m"


def fg(red: int, green: int, blue: int) -> str:
    """Return the ANSI sequence of a text color.

    Args:
        red: Red component, from 0 to 255.
        green: Green component, from 0 to 255.
        blue: Blue component, from 0 to 255.

    Returns:
        The ANSI escape sequence.
    """
    return f"\033[38;2;{red};{green};{blue}m"


def bg(red: int, green: int, blue: int) -> str:
    """Return the ANSI sequence of a background color.

    Args:
        red: Red component, from 0 to 255.
        green: Green component, from 0 to 255.
        blue: Blue component, from 0 to 255.

    Returns:
        The ANSI escape sequence.
    """
    return f"\033[48;2;{red};{green};{blue}m"


@dataclass(frozen=True)
class Theme:
    """Color set used to draw the maze.

    Attributes:
        name: Name of the theme, shown in the menu.
        wall_code: Text color of the walls.
        path_code: Background color of the shortest path.
        entry_code: Background color of the entry.
        exit_code: Background color of the exit.
        pattern_code: Text and background color of the "42" cells.
    """

    name: str
    wall_code: str
    path_code: str
    entry_code: str
    exit_code: str
    pattern_code: str


THEMES: tuple[Theme, ...] = (
    Theme(
        name="Ocean",
        wall_code=fg(24, 36, 51),
        path_code=bg(232, 184, 109),
        entry_code=bg(58, 140, 140),
        exit_code=bg(94, 28, 35),
        pattern_code=fg(178, 34, 34) + bg(178, 34, 34),
    ),
    Theme(
        name="Christmas",
        wall_code=fg(41, 73, 54),
        path_code=bg(255, 242, 204),
        entry_code=bg(115, 159, 96),
        exit_code=bg(150, 40, 40),
        pattern_code=fg(200, 40, 40) + bg(200, 40, 40),
    ),
    Theme(
        name="Summer",
        wall_code=fg(91, 58, 140),
        path_code=bg(214, 107, 160),
        entry_code=bg(57, 118, 168),
        exit_code=bg(255, 140, 0),
        pattern_code=fg(120, 60, 160) + bg(120, 60, 160),
    ),
)


def clear_screen() -> None:
    """Clear the terminal, only when stdout is a real terminal."""
    if sys.stdout.isatty():
        print("\033[2J\033[H", end="")


def _canvas(maze: MazeGenerator) -> list[list[str]]:
    """Build the plain canvas of characters of the maze.

    Every corner and every wall starts as a block; the open walls
    and the center of every cell are then carved out.

    Args:
        maze: The generated maze.

    Returns:
        The canvas as a list of rows of single characters.
    """
    height = maze.grid.height
    width = maze.grid.width
    canvas = [
        [WALL_CHAR] * (2 * width + 1) for _ in range(2 * height + 1)
    ]
    for row in maze.grid.cells:
        for cell in row:
            line = 2 * cell.row + 1
            column = 2 * cell.col + 1
            canvas[line][column] = FLOOR_CHAR
            if not cell.walls["N"]:
                canvas[line - 1][column] = FLOOR_CHAR
            if not cell.walls["S"]:
                canvas[line + 1][column] = FLOOR_CHAR
            if not cell.walls["W"]:
                canvas[line][column - 1] = FLOOR_CHAR
            if not cell.walls["E"]:
                canvas[line][column + 1] = FLOOR_CHAR
    return canvas


def _pattern_positions(
    maze: MazeGenerator,
) -> set[tuple[int, int]]:
    """Return the canvas positions covered by the "42" pattern.

    The whole block of every pattern cell is taken, so the sign is
    drawn as a solid shape, including the closed walls around it.

    Args:
        maze: The generated maze.

    Returns:
        The set of ``(line, column)`` canvas positions.
    """
    positions: set[tuple[int, int]] = set()
    for row, col in maze.pattern:
        for line in (2 * row, 2 * row + 1, 2 * row + 2):
            for column in (2 * col, 2 * col + 1, 2 * col + 2):
                positions.add((line, column))
    return positions


def _path_positions(
    path: Sequence[tuple[int, int]],
) -> set[tuple[int, int]]:
    """Return the canvas positions covered by the solution path.

    Args:
        path: Shortest path as ``(row, column)`` cells.

    Returns:
        The set of ``(line, column)`` canvas positions.
    """
    positions: set[tuple[int, int]] = set()
    for row, col in path:
        positions.add((2 * row + 1, 2 * col + 1))
    for (row, col), (next_row, next_col) in zip(path, path[1:]):
        positions.add((row + next_row + 1, col + next_col + 1))
    return positions


def _legend(theme: Theme) -> str:
    """Return the color legend printed below the maze.

    Args:
        theme: Theme currently used to draw the maze.

    Returns:
        One line of text with a color sample per maze feature.
    """
    return (
        f"  {theme.entry_code}  {RESET}entry"
        f"  {theme.exit_code}  {RESET}exit"
        f"  {theme.path_code}  {RESET}shortest path"
        f"  {theme.pattern_code}  {RESET}42 pattern"
    )


def render_maze(
    maze: MazeGenerator,
    path: Sequence[tuple[int, int]],
    show_path: bool,
    theme: Theme,
    color_pattern: bool = True,
) -> str:
    """Render the maze as a multi-line string.

    Args:
        maze: The generated maze.
        path: Shortest path from the entry to the exit.
        show_path: ``True`` to paint the solution path.
        theme: Colors used for this drawing.
        color_pattern: ``True`` to paint the "42" sign.

    Returns:
        The maze, a blank line and the legend.
    """
    canvas = _canvas(maze)
    pattern = _pattern_positions(maze) if color_pattern else set()
    trail = _path_positions(path) if show_path else set()
    entry = (2 * maze.start[0] + 1, 2 * maze.start[1] + 1)
    exit_cell = (2 * maze.end[0] + 1, 2 * maze.end[1] + 1)

    lines: list[str] = []
    for line_index, row in enumerate(canvas):
        parts: list[str] = []
        for column_index, char in enumerate(row):
            position = (line_index, column_index)
            if position == entry:
                code = theme.entry_code
            elif position == exit_cell:
                code = theme.exit_code
            elif position in trail:
                code = theme.path_code
            elif position in pattern:
                code = theme.pattern_code
            elif char == WALL_CHAR:
                code = theme.wall_code
            else:
                code = ""
            block = char * 2
            if code:
                parts.append(f"{code}{block}{RESET}")
            else:
                parts.append(block)
        lines.append("".join(parts))
    lines.append("")
    lines.append(_legend(theme))
    return "\n".join(lines)
