"""Reusable maze generator (single file).

``mazegen`` builds random mazes and finds the shortest path between two
cells.  It is the reusable part of the ``a_maze_ing`` activity and can
be installed on its own with pip::

    pip install mazegen-1.0.0-py3-none-any.whl

Basic usage
-----------

::

    from mazegen import MazeGenerator

    maze = MazeGenerator(
        height=10,
        width=10,
        perfect=True,
        start=(0, 0),
        end=(9, 9),
        seed=42,
    )
    maze.generate()
    solution = maze.solve()

Parameters
----------

``height`` and ``width``
    Size of the grid in cells.
``perfect``
    ``True`` gives a perfect maze (exactly one path between any two
    cells), ``False`` gives a playable board with loops and almost no
    dead ends, like a Pac-Man board.
``start`` and ``end``
    Entry and exit of the maze, written as ``(row, column)``.
``seed``
    Seed of the random generator: the same seed always produces the
    same maze, which makes the generation reproducible.

Accessing the result
--------------------

* ``maze.grid.cells[row][column]`` is a :class:`Cell`; its ``walls``
  dictionary tells for each of ``"N"``, ``"E"``, ``"S"`` and ``"W"``
  whether the wall is closed (``True``) or open (``False``).
* ``maze.pattern`` is the set of fully closed cells that draw the
  ``42`` sign, or an empty set when the maze is too small for it.
* ``maze.solve()`` (or ``shortest_path(maze)``) returns the shortest
  path as a list of ``(row, column)`` tuples, entry included.

The structure kept in memory is not the same format as the hexadecimal
output file of the activity; see ``cell_to_hex`` in the activity code.

License
-------

MIT, see ``LICENSE.md`` at the root of the repository.
"""

from __future__ import annotations

import random
from collections import deque

__all__ = ["Cell", "Grid", "MazeGenerator", "shortest_path"]

DIRECTIONS: tuple[str, ...] = ("N", "E", "S", "W")
OPPOSITE: dict[str, str] = {"N": "S", "E": "W", "S": "N", "W": "E"}
DELTAS: dict[str, tuple[int, int]] = {
    "N": (-1, 0),
    "E": (0, 1),
    "S": (1, 0),
    "W": (0, -1),
}

PATTERN_HEIGHT = 8
PATTERN_WIDTH = 14

# Cells of the "42" sign, relative to the top left corner of the sign.
PATTERN_CELLS: frozenset[tuple[int, int]] = frozenset(
    (
        # the "4"
        (0, 0), (0, 4),
        (1, 0), (1, 4),
        (2, 0), (2, 4),
        (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5),
        (4, 4),
        (5, 4),
        (6, 4),
        (7, 4),
        # the "2"
        (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (0, 12),
        (0, 13),
        (1, 13),
        (2, 13),
        (3, 7), (3, 8), (3, 9), (3, 10), (3, 11), (3, 12),
        (3, 13),
        (4, 7),
        (5, 7),
        (6, 7), (6, 8), (6, 9), (6, 10), (6, 11), (6, 12),
        (6, 13),
    )
)


class Cell:
    """One cell of the maze.

    A cell stores its position, whether generation already visited it,
    and the state of its four walls.

    Attributes:
        row: Row index of the cell in the grid.
        col: Column index of the cell in the grid.
        visited: ``True`` once the generation has visited the cell.
        walls: Wall state per direction; ``True`` means closed.
    """

    def __init__(self, row: int, col: int) -> None:
        """Create a closed cell at position ``(row, col)``."""
        self.row = row
        self.col = col
        self.visited = False
        self.walls: dict[str, bool] = {d: True for d in DIRECTIONS}

    @property
    def openings(self) -> int:
        """Return how many walls of the cell are open."""
        return sum(1 for closed in self.walls.values() if not closed)


class Grid:
    """Rectangular grid of :class:`Cell` objects.

    Attributes:
        height: Number of rows in cells.
        width: Number of columns in cells.
        cells: ``cells[row][column]`` gives one :class:`Cell`.
    """

    def __init__(self, height: int, width: int) -> None:
        """Create an empty grid of ``height`` rows and ``width`` cols."""
        if height <= 0 or width <= 0:
            raise ValueError("the grid size must be strictly positive")
        self.height = height
        self.width = width
        self.cells: list[list[Cell]] = [
            [Cell(row, col) for col in range(width)]
            for row in range(height)
        ]

    def in_bounds(self, row: int, col: int) -> bool:
        """Return ``True`` when ``(row, col)`` is inside the grid."""
        return 0 <= row < self.height and 0 <= col < self.width

    def neighbors(self, cell: Cell) -> list[tuple[int, int, str]]:
        """Return the neighbours inside the grid.

        Returns:
            A list of ``(row, column, direction)`` tuples; ``direction``
            is the wall to remove to move from ``cell`` to the
            neighbour.
        """
        found: list[tuple[int, int, str]] = []
        for direction in DIRECTIONS:
            row_change, col_change = DELTAS[direction]
            row = cell.row + row_change
            col = cell.col + col_change
            if self.in_bounds(row, col):
                found.append((row, col, direction))
        return found


class MazeGenerator:
    """Generate a random maze and solve it.

    The maze is created by :meth:`generate`, the shortest path between
    ``start`` and ``end`` is returned by :meth:`solve`.

    Attributes:
        grid: The :class:`Grid` holding every :class:`Cell`.
        perfect: ``True`` for a perfect maze, ``False`` for a board.
        start: Entry of the maze as ``(row, column)``.
        end: Exit of the maze as ``(row, column)``.
        seed: Seed used for the random generation, may be ``None``.
        pattern: Cells of the closed ``42`` sign, empty if omitted.
    """

    def __init__(
        self,
        height: int,
        width: int,
        perfect: bool,
        start: tuple[int, int],
        end: tuple[int, int],
        seed: int | None = None,
    ) -> None:
        """Prepare a maze of ``height`` x ``width`` cells.

        Args:
            height: Number of cell rows.
            width: Number of cell columns.
            perfect: Generation mode of the maze.
            start: Entry of the maze as ``(row, column)``.
            end: Exit of the maze as ``(row, column)``.
            seed: Optional seed for a reproducible maze.

        Raises:
            ValueError: If the grid is empty, if a position is outside
                the grid or if ``start`` and ``end`` are equal.
        """
        self.grid = Grid(height, width)
        self.perfect = perfect
        self.start = start
        self.end = end
        self.seed = seed
        self.rng = random.Random(seed)
        self.pattern: set[tuple[int, int]] = set()
        self._check_positions()

    def _check_positions(self) -> None:
        """Validate the entry and the exit of the maze."""
        for name, position in (
            ("start", self.start),
            ("end", self.end),
        ):
            if not self.grid.in_bounds(*position):
                raise ValueError(
                    f"{name} {position} is outside a "
                    f"{self.grid.height}x{self.grid.width} maze"
                )
        if self.start == self.end:
            raise ValueError("start and end must be different cells")

    def generate(self) -> None:
        """Generate the maze.

        Every wall is closed first, then the ``42`` sign is reserved
        with fully closed cells, then the corridors are carved with a
        depth first search.  The corridors are finally repaired and
        improved so that the maze follows the rules of the activity.

        Raises:
            ValueError: If the entry or the exit lies inside the ``42``
                sign, or if the maze cannot be fully connected.
        """
        self._reset()
        self.pattern = _apply_pattern(self)
        if self.perfect:
            _carve_perfect(self)
        else:
            _carve_playable(self)
        _repair_connectivity(self)
        if not self.perfect:
            _open_dead_ends(self)
            _open_spawns(self)
            _ensure_loops(self, minimum=2)

    def _reset(self) -> None:
        """Close every wall and forget the previous generation."""
        for row in self.grid.cells:
            for cell in row:
                cell.visited = False
                for direction in DIRECTIONS:
                    cell.walls[direction] = True
        self.pattern = set()
        self.rng = random.Random(self.seed)

    def solve(self) -> list[tuple[int, int]]:
        """Return the shortest path from ``start`` to ``end``.

        Returns:
            The list of ``(row, column)`` cells of the path, entry and
            exit included.

        Raises:
            ValueError: If the exit cannot be reached from the entry.
        """
        return shortest_path(self)

    def count_loops(self) -> int:
        """Return the number of independent loops of the maze.

        Only the corridors are counted: the cells of the ``42`` sign
        are ignored.  ``0`` means the corridors form a tree, which is
        the case of a perfect maze.
        """
        components = _components(self)
        vertices = sum(len(group) for group in components)
        edges = _count_edges(self)
        return edges - vertices + len(components)

    def __repr__(self) -> str:
        """Return a short description of the maze."""
        mode = "perfect" if self.perfect else "playable"
        return (
            f"MazeGenerator({self.grid.height}x{self.grid.width}, "
            f"{mode}, seed={self.seed})"
        )


def shortest_path(maze: MazeGenerator) -> list[tuple[int, int]]:
    """Find a shortest path between the entry and the exit.

    The maze is explored with a breadth first search, so the first
    time the exit is reached the path kept is already a shortest one.

    Args:
        maze: The generated maze to solve.

    Returns:
        The list of ``(row, column)`` cells of the path.

    Raises:
        ValueError: If the exit cannot be reached from the entry.
    """
    queue: deque[tuple[int, int]] = deque([maze.start])
    previous: dict[
        tuple[int, int], tuple[int, int] | None
    ] = {maze.start: None}

    while queue:
        current = queue.popleft()
        if current == maze.end:
            break
        row, col = current
        cell = maze.grid.cells[row][col]
        for direction in DIRECTIONS:
            if cell.walls[direction]:
                continue
            row_change, col_change = DELTAS[direction]
            nxt = (row + row_change, col + col_change)
            if not maze.grid.in_bounds(*nxt):
                continue
            if nxt in previous:
                continue
            previous[nxt] = current
            queue.append(nxt)

    if maze.end not in previous:
        raise ValueError(
            f"no path exists from {maze.start} to {maze.end}"
        )

    path: list[tuple[int, int]] = []
    current_cell: tuple[int, int] | None = maze.end
    while current_cell is not None:
        path.append(current_cell)
        current_cell = previous[current_cell]
    path.reverse()
    return path


def _open_wall(cell: Cell, neighbor: Cell, direction: str) -> None:
    """Remove the wall shared by ``cell`` and ``neighbor``."""
    cell.walls[direction] = False
    neighbor.walls[OPPOSITE[direction]] = False


def _close_wall(cell: Cell, neighbor: Cell, direction: str) -> None:
    """Put the wall shared by ``cell`` and ``neighbor`` back."""
    cell.walls[direction] = True
    neighbor.walls[OPPOSITE[direction]] = True


def _pattern_origin(grid: Grid) -> tuple[int, int]:
    """Return the top left cell of the ``42`` sign."""
    row = (grid.height - PATTERN_HEIGHT) // 2
    col = grid.width // 2 - 6
    return row, col


def _apply_pattern(maze: MazeGenerator) -> set[tuple[int, int]]:
    """Reserve the cells of the ``42`` sign.

    The sign is centred in the maze.  It needs a free row and column
    around it, otherwise it is omitted and a message is printed, as the
    subject allows.

    Returns:
        The reserved cells, or an empty set when the maze is too small.

    Raises:
        ValueError: If the entry or the exit is inside the sign.
    """
    row, col = _pattern_origin(maze.grid)
    too_small = (
        row < 1
        or col < 1
        or row + PATTERN_HEIGHT > maze.grid.height - 1
        or col + PATTERN_WIDTH > maze.grid.width - 1
    )
    if too_small:
        print(
            "Warning: the maze is too small for the '42' pattern, "
            "it will be omitted."
        )
        return set()

    cells = {
        (row + rel_row, col + rel_col)
        for rel_row, rel_col in PATTERN_CELLS
    }
    if maze.start in cells or maze.end in cells:
        raise ValueError(
            "ENTRY or EXIT is inside the '42' pattern, "
            "please choose other coordinates"
        )
    for cell_row, cell_col in cells:
        maze.grid.cells[cell_row][cell_col].visited = True
    return cells


def _carve_perfect(maze: MazeGenerator) -> None:
    """Carve a perfect maze with a depth first search."""
    grid = maze.grid
    first = grid.cells[maze.start[0]][maze.start[1]]
    first.visited = True
    stack: list[Cell] = [first]

    while stack:
        current = stack[-1]
        candidates = [
            (grid.cells[row][col], direction)
            for row, col, direction in grid.neighbors(current)
            if not grid.cells[row][col].visited
        ]
        if not candidates:
            stack.pop()
            continue
        neighbor, direction = maze.rng.choice(candidates)
        neighbor.visited = True
        _open_wall(current, neighbor, direction)
        stack.append(neighbor)


def _carve_playable(maze: MazeGenerator) -> None:
    """Carve the maze of the playable (imperfect) mode."""
    _carve_perfect(maze)


def _components(maze: MazeGenerator) -> list[set[tuple[int, int]]]:
    """Group the corridors of the maze.

    The cells of the ``42`` sign are excluded because they stay fully
    closed on purpose.

    Returns:
        One set of ``(row, column)`` positions per connected group.
    """
    grid = maze.grid
    seen: set[tuple[int, int]] = set()
    groups: list[set[tuple[int, int]]] = []

    for row in range(grid.height):
        for col in range(grid.width):
            position = (row, col)
            if position in maze.pattern or position in seen:
                continue
            group: set[tuple[int, int]] = set()
            queue: deque[tuple[int, int]] = deque([position])
            seen.add(position)
            while queue:
                current = queue.popleft()
                group.add(current)
                cell = grid.cells[current[0]][current[1]]
                for direction in DIRECTIONS:
                    if cell.walls[direction]:
                        continue
                    row_change, col_change = DELTAS[direction]
                    nxt = (
                        current[0] + row_change,
                        current[1] + col_change,
                    )
                    if not grid.in_bounds(*nxt):
                        continue
                    if nxt in maze.pattern or nxt in seen:
                        continue
                    seen.add(nxt)
                    queue.append(nxt)
            groups.append(group)
    return groups


def _count_edges(maze: MazeGenerator) -> int:
    """Count the open walls between two corridor cells."""
    grid = maze.grid
    edges = 0
    for row in grid.cells:
        for cell in row:
            if (cell.row, cell.col) in maze.pattern:
                continue
            for direction in ("E", "S"):
                if cell.walls[direction]:
                    continue
                row_change, col_change = DELTAS[direction]
                nxt = (cell.row + row_change, cell.col + col_change)
                if not grid.in_bounds(*nxt):
                    continue
                if nxt in maze.pattern:
                    continue
                edges += 1
    return edges


def _walls_between_groups(
    maze: MazeGenerator,
) -> list[tuple[Cell, Cell, str]]:
    """List the closed walls joining two different corridor groups."""
    grid = maze.grid
    components = _components(maze)
    owner: dict[tuple[int, int], int] = {}
    for index, group in enumerate(components):
        for position in group:
            owner[position] = index

    found: list[tuple[Cell, Cell, str]] = []
    for row in grid.cells:
        for cell in row:
            if (cell.row, cell.col) in maze.pattern:
                continue
            for direction in ("E", "S"):
                if not cell.walls[direction]:
                    continue
                row_change, col_change = DELTAS[direction]
                nxt = (cell.row + row_change, cell.col + col_change)
                if not grid.in_bounds(*nxt):
                    continue
                if nxt in maze.pattern:
                    continue
                if owner[(cell.row, cell.col)] == owner[nxt]:
                    continue
                found.append((cell, grid.cells[nxt[0]][nxt[1]],
                              direction))
    return found


def _repair_connectivity(maze: MazeGenerator) -> None:
    """Make every corridor reachable from the entry.

    The ``42`` sign may split the grid; each missing link opens one
    wall between two groups.  Opening a wall between two different
    groups never creates a loop, so a perfect maze stays perfect.

    Raises:
        ValueError: If two groups of corridors cannot be joined.
    """
    while len(_components(maze)) > 1:
        candidates = _walls_between_groups(maze)
        if not candidates:
            raise ValueError(
                "the corridors of the maze cannot be fully connected"
            )
        cell, neighbor, direction = maze.rng.choice(candidates)
        _open_wall(cell, neighbor, direction)


def _window_is_open(
    grid: Grid, top: int, left: int
) -> bool:
    """Return ``True`` if a 3x3 area is fully open at ``top, left``."""
    for row in range(top, top + 3):
        for col in range(left, left + 3):
            cell = grid.cells[row][col]
            if col < left + 2 and cell.walls["E"]:
                return False
            if row < top + 2 and cell.walls["S"]:
                return False
    return True


def _opens_large_area(
    grid: Grid, row: int, col: int
) -> bool:
    """Return ``True`` if opening around a cell breaks the size rule."""
    for top in range(row - 2, row + 1):
        for left in range(col - 2, col + 1):
            if top < 0 or left < 0:
                continue
            if top + 2 >= grid.height or left + 2 >= grid.width:
                continue
            if _window_is_open(grid, top, left):
                return True
    return False


def _try_open(
    maze: MazeGenerator, cell: Cell, neighbor: Cell, direction: str
) -> bool:
    """Open a wall only when the maze rules stay respected.

    Returns:
        ``True`` when the wall has been opened.
    """
    if (cell.row, cell.col) in maze.pattern:
        return False
    if (neighbor.row, neighbor.col) in maze.pattern:
        return False
    if not cell.walls[direction]:
        return False
    _open_wall(cell, neighbor, direction)
    if _opens_large_area(maze.grid, cell.row, cell.col):
        _close_wall(cell, neighbor, direction)
        return False
    if _opens_large_area(maze.grid, neighbor.row, neighbor.col):
        _close_wall(cell, neighbor, direction)
        return False
    return True


def _open_dead_ends(maze: MazeGenerator) -> None:
    """Remove the dead ends of the playable mode.

    Several passes are done because opening a wall changes the number
    of openings of the neighbours.
    """
    grid = maze.grid
    for _ in range(4):
        progress = False
        for row in grid.cells:
            for cell in row:
                if cell.openings != 1:
                    continue
                if (cell.row, cell.col) in maze.pattern:
                    continue
                candidates = [
                    (grid.cells[r][c], direction)
                    for r, c, direction in grid.neighbors(cell)
                    if cell.walls[direction]
                ]
                maze.rng.shuffle(candidates)
                for neighbor, direction in candidates:
                    if _try_open(maze, cell, neighbor, direction):
                        progress = True
                        break
        if not progress:
            break


def _open_spawns(maze: MazeGenerator) -> None:
    """Make the corners and the centre proper corridors.

    Ghosts start in the corners and the player in the centre, so those
    five cells need at least two open walls.
    """
    grid = maze.grid
    targets = [
        (0, 0),
        (0, grid.width - 1),
        (grid.height - 1, 0),
        (grid.height - 1, grid.width - 1),
        (grid.height // 2, grid.width // 2),
    ]
    for row, col in targets:
        cell = grid.cells[row][col]
        if (row, col) in maze.pattern:
            continue
        while cell.openings < 2:
            candidates = [
                (grid.cells[r][c], direction)
                for r, c, direction in grid.neighbors(cell)
                if cell.walls[direction]
            ]
            maze.rng.shuffle(candidates)
            opened = False
            for neighbor, direction in candidates:
                if _try_open(maze, cell, neighbor, direction):
                    opened = True
                    break
            if not opened:
                break


def _ensure_loops(maze: MazeGenerator, minimum: int) -> None:
    """Add walls until the maze has ``minimum`` independent loops."""
    grid = maze.grid
    corridors = [
        cell
        for row in grid.cells
        for cell in row
        if (cell.row, cell.col) not in maze.pattern
    ]
    attempts = 0
    while maze.count_loops() < minimum and attempts < 5000:
        attempts += 1
        cell = maze.rng.choice(corridors)
        candidates = [
            (grid.cells[r][c], direction)
            for r, c, direction in grid.neighbors(cell)
            if cell.walls[direction]
        ]
        if not candidates:
            continue
        neighbor, direction = maze.rng.choice(candidates)
        _try_open(maze, cell, neighbor, direction)
