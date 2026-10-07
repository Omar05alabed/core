"""Tests of the A-Maze-ing maze generator, output file and parser."""

from __future__ import annotations

import os
import tempfile
import unittest
from collections import deque
from contextlib import redirect_stdout
from io import StringIO

from maze_app.output_file import (
    cell_to_hex,
    convert_path,
    write_maze,
)
from maze_app.parser import Config, parse_config
from maze_app.render import THEMES, render_maze
from mazegen import (
    DELTAS,
    DIRECTIONS,
    OPPOSITE,
    MazeGenerator,
)

HEX_DIGITS = "0123456789ABCDEF"


def generate(maze: MazeGenerator) -> None:
    """Generate the maze without printing on stdout."""
    with redirect_stdout(StringIO()):
        maze.generate()


def make_maze(
    height: int = 20,
    width: int = 20,
    perfect: bool = False,
    seed: int = 42,
    start: tuple[int, int] = (0, 0),
    end: tuple[int, int] | None = None,
) -> MazeGenerator:
    """Generate a maze with sensible default positions."""
    if end is None:
        end = (height - 1, width - 2)
    maze = MazeGenerator(
        height, width, perfect, start, end, seed
    )
    generate(maze)
    return maze


def bfs_distance(
    maze: MazeGenerator,
    start: tuple[int, int],
    end: tuple[int, int],
) -> int | None:
    """Return the length of a shortest path, ``None`` if none."""
    queue: deque[tuple[tuple[int, int], int]] = deque(
        [(start, 0)]
    )
    seen: set[tuple[int, int]] = {start}
    while queue:
        (row, col), distance = queue.popleft()
        if (row, col) == end:
            return distance
        cell = maze.grid.cells[row][col]
        for direction in DIRECTIONS:
            if cell.walls[direction]:
                continue
            row_change, col_change = DELTAS[direction]
            nxt = (row + row_change, col + col_change)
            if maze.grid.in_bounds(*nxt) and nxt not in seen:
                seen.add(nxt)
                queue.append((nxt, distance + 1))
    return None


def reachable(
    maze: MazeGenerator, start: tuple[int, int]
) -> set[tuple[int, int]]:
    """Return every corridor cell reachable from ``start``."""
    seen: set[tuple[int, int]] = set()
    if start in maze.pattern:
        return seen
    queue: deque[tuple[int, int]] = deque([start])
    seen.add(start)
    while queue:
        row, col = queue.popleft()
        cell = maze.grid.cells[row][col]
        for direction in DIRECTIONS:
            if cell.walls[direction]:
                continue
            row_change, col_change = DELTAS[direction]
            nxt = (row + row_change, col + col_change)
            if not maze.grid.in_bounds(*nxt):
                continue
            if nxt in maze.pattern or nxt in seen:
                continue
            seen.add(nxt)
            queue.append(nxt)
    return seen


def corridor_cells(maze: MazeGenerator) -> set[tuple[int, int]]:
    """Return every cell that is not part of the "42" sign."""
    cells: set[tuple[int, int]] = set()
    for row in maze.grid.cells:
        for cell in row:
            position = (cell.row, cell.col)
            if position not in maze.pattern:
                cells.add(position)
    return cells


def has_open_window(maze: MazeGenerator) -> bool:
    """Return ``True`` if a 3x3 area of the maze is fully open."""
    height = maze.grid.height
    width = maze.grid.width
    for top in range(height - 2):
        for left in range(width - 2):
            open_area = True
            for row in range(top, top + 3):
                for col in range(left, left + 3):
                    cell = maze.grid.cells[row][col]
                    if col < left + 2 and cell.walls["E"]:
                        open_area = False
                    if row < top + 2 and cell.walls["S"]:
                        open_area = False
            if open_area:
                return True
    return False


def border_walls_closed(maze: MazeGenerator) -> bool:
    """Return ``True`` when every border wall of the grid is closed."""
    grid = maze.grid
    for row in grid.cells:
        for cell in row:
            if cell.row == 0 and not cell.walls["N"]:
                return False
            if cell.row == grid.height - 1 and not cell.walls["S"]:
                return False
            if cell.col == 0 and not cell.walls["W"]:
                return False
            if cell.col == grid.width - 1 and not cell.walls["E"]:
                return False
    return True


def shared_walls_coherent(maze: MazeGenerator) -> bool:
    """Return ``True`` when neighbours share the same wall state."""
    grid = maze.grid
    for row in grid.cells:
        for cell in row:
            for direction, (row_c, col_c) in DELTAS.items():
                other = (
                    cell.row + row_c,
                    cell.col + col_c,
                )
                if not grid.in_bounds(*other):
                    continue
                neighbor = grid.cells[other[0]][other[1]]
                if cell.walls[direction] != neighbor.walls[
                    OPPOSITE[direction]
                ]:
                    return False
    return True


def valid_path(
    maze: MazeGenerator, path: list[tuple[int, int]]
) -> bool:
    """Return ``True`` when the path walks only through open walls."""
    if not path:
        return False
    if path[0] != maze.start or path[-1] != maze.end:
        return False
    if len(set(path)) != len(path):
        return False
    moves = {
        (-1, 0): "N",
        (1, 0): "S",
        (0, 1): "E",
        (0, -1): "W",
    }
    for (row, col), (next_row, next_col) in zip(path, path[1:]):
        direction = moves.get((next_row - row, next_col - col))
        if direction is None:
            return False
        if maze.grid.cells[row][col].walls[direction]:
            return False
    return True


def count_dead_ends(maze: MazeGenerator) -> int:
    """Count the corridor cells that have only one opening."""
    total = 0
    for row in maze.grid.cells:
        for cell in row:
            if (cell.row, cell.col) in maze.pattern:
                continue
            if cell.openings == 1:
                total += 1
    return total


class TestCellToHex(unittest.TestCase):
    """The hexadecimal encoding must follow the subject bits."""

    def test_hex_matches_spec_bits(self) -> None:
        """Bit 0 is North, bit 1 East, bit 2 South, bit 3 West."""
        for value in range(16):
            walls = {
                direction: bool(value & (1 << bit))
                for bit, direction in enumerate(DIRECTIONS)
            }
            self.assertEqual(
                cell_to_hex(walls), format(value, "X")
            )

    def test_known_values(self) -> None:
        """Values taken from the subject of the activity."""
        self.assertEqual(
            cell_to_hex(
                {"N": True, "E": True, "S": False, "W": False}
            ),
            "3",
        )
        self.assertEqual(
            cell_to_hex(
                {"N": False, "E": False, "S": True, "W": True}
            ),
            "C",
        )
        self.assertEqual(
            cell_to_hex(
                {"N": False, "E": False, "S": False, "W": False}
            ),
            "0",
        )
        self.assertEqual(
            cell_to_hex(
                {"N": True, "E": True, "S": True, "W": True}
            ),
            "F",
        )


class TestOutputFile(unittest.TestCase):
    """The output file must respect the format of the subject."""

    def setUp(self) -> None:
        """Create a maze and write it to a temporary file."""
        self.maze = make_maze(10, 12, seed=7)
        self.path = self.maze.solve()
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.file_path = os.path.join(directory.name, "maze.txt")
        write_maze(self.maze, self.path, self.file_path)
        with open(
            self.file_path, "r", encoding="utf-8"
        ) as handle:
            self.text = handle.read()
        self.lines = self.text.splitlines()

    def test_file_structure(self) -> None:
        """Rows, empty line, positions and path, all newline ended."""
        height = self.maze.grid.height
        width = self.maze.grid.width
        self.assertEqual(len(self.lines), height + 4)
        for row in self.lines[:height]:
            self.assertEqual(len(row), width)
            for char in row:
                self.assertIn(char, HEX_DIGITS)
        self.assertEqual(self.lines[height], "")
        start_row, start_col = self.maze.start
        end_row, end_col = self.maze.end
        self.assertEqual(
            self.lines[height + 1],
            f"({start_col}, {start_row})",
        )
        self.assertEqual(
            self.lines[height + 2],
            f"({end_col}, {end_row})",
        )
        for char in self.lines[height + 3]:
            self.assertIn(char, "NESW")
        self.assertTrue(self.text.endswith("\n"))
        self.assertEqual(
            self.text.count("\n"), len(self.lines)
        )

    def test_written_path_is_valid(self) -> None:
        """The path of the file walks through open walls."""
        direction_line = self.lines[-1]
        row, col = self.maze.start
        for move in direction_line:
            cell = self.maze.grid.cells[row][col]
            self.assertFalse(cell.walls[move])
            row_change, col_change = DELTAS[move]
            row += row_change
            col += col_change
        self.assertEqual((row, col), self.maze.end)

    def test_convert_path_of_known_route(self) -> None:
        """Two steps of the path become two directions."""
        moves = convert_path([(0, 0), (0, 1), (1, 1)])
        self.assertEqual(moves, "ES")

    def test_convert_path_rejects_bad_route(self) -> None:
        """Cells that are not neighbours are refused."""
        with self.assertRaises(ValueError):
            convert_path([(0, 0), (2, 2)])


class TestShortestPath(unittest.TestCase):
    """The solution must be a real shortest path."""

    def test_path_is_shortest(self) -> None:
        """No shorter path exists between entry and exit."""
        for perfect in (True, False):
            for seed in range(4):
                maze = make_maze(
                    perfect=perfect, seed=seed
                )
                path = maze.solve()
                self.assertTrue(valid_path(maze, path))
                distance = bfs_distance(
                    maze, maze.start, maze.end
                )
                self.assertEqual(
                    len(path) - 1, distance
                )

    def test_solve_without_open_wall_raises(self) -> None:
        """A closed maze has no path at all."""
        maze = MazeGenerator(4, 4, True, (0, 0), (3, 3), 1)
        with self.assertRaises(ValueError):
            maze.solve()


class TestGeneration(unittest.TestCase):
    """The generated mazes must follow every rule of the subject."""

    def test_perfect_maze_has_no_loops(self) -> None:
        """A perfect maze is a tree: zero independent loops."""
        for seed in range(5):
            maze = make_maze(perfect=True, seed=seed)
            self.assertEqual(maze.count_loops(), 0)

    def test_playable_maze_has_loops(self) -> None:
        """The playable board has at least two loops."""
        for seed in range(5):
            maze = make_maze(perfect=False, seed=seed)
            self.assertGreaterEqual(maze.count_loops(), 2)

    def test_corridors_are_fully_connected(self) -> None:
        """Every corridor cell is reachable from the entry."""
        for perfect in (True, False):
            for seed in range(4):
                maze = make_maze(
                    perfect=perfect, seed=seed
                )
                found = reachable(maze, maze.start)
                self.assertEqual(found, corridor_cells(maze))

    def test_border_walls_are_closed(self) -> None:
        """The maze never opens towards the outside."""
        for perfect in (True, False):
            maze = make_maze(perfect=perfect)
            self.assertTrue(border_walls_closed(maze))

    def test_neighbours_share_walls(self) -> None:
        """A wall between two cells belongs to both of them."""
        for perfect in (True, False):
            for seed in range(3):
                maze = make_maze(
                    perfect=perfect, seed=seed
                )
                self.assertTrue(shared_walls_coherent(maze))

    def test_no_3x3_open_area(self) -> None:
        """Corridors are never wider than two cells."""
        for perfect in (True, False):
            for seed in range(4):
                maze = make_maze(
                    perfect=perfect, seed=seed
                )
                self.assertFalse(has_open_window(maze))

    def test_playable_spawns_are_open(self) -> None:
        """The four corners and the centre are real corridors."""
        for seed in range(4):
            maze = make_maze(perfect=False, seed=seed)
            height = maze.grid.height
            width = maze.grid.width
            targets = [
                (0, 0),
                (0, width - 1),
                (height - 1, 0),
                (height - 1, width - 1),
                (height // 2, width // 2),
            ]
            for row, col in targets:
                cell = maze.grid.cells[row][col]
                self.assertGreaterEqual(cell.openings, 2)

    def test_dead_ends_are_rare(self) -> None:
        """The playable board almost never ends in a dead end."""
        for seed in range(4):
            maze = make_maze(perfect=False, seed=seed)
            corridors = len(corridor_cells(maze))
            dead_ends = count_dead_ends(maze)
            self.assertLessEqual(
                dead_ends, corridors // 5
            )

    def test_pattern_cells_are_closed(self) -> None:
        """The "42" sign is made of fully closed cells."""
        maze = make_maze()
        self.assertEqual(len(maze.pattern), 41)
        height = maze.grid.height
        width = maze.grid.width
        for row, col in maze.pattern:
            cell = maze.grid.cells[row][col]
            self.assertEqual(cell.openings, 0)
            self.assertGreater(row, 0)
            self.assertLess(row, height - 1)
            self.assertGreater(col, 0)
            self.assertLess(col, width - 1)

    def test_pattern_is_omitted_when_too_small(self) -> None:
        """A tiny maze drops the sign instead of crashing."""
        maze = make_maze(8, 10, start=(0, 0), end=(7, 8))
        self.assertEqual(maze.pattern, set())

    def test_entry_inside_pattern_raises(self) -> None:
        """The entry cannot be a cell of the sign."""
        maze = MazeGenerator(20, 20, True, (6, 4), (0, 0), 1)
        with self.assertRaises(ValueError):
            generate(maze)

    def test_positions_are_validated(self) -> None:
        """Bad entry and exit positions are refused."""
        with self.assertRaises(ValueError):
            MazeGenerator(10, 10, True, (0, 0), (0, 0), 1)
        with self.assertRaises(ValueError):
            MazeGenerator(10, 10, True, (0, 0), (42, 42), 1)


class TestReproducibility(unittest.TestCase):
    """The same seed must always give the same maze."""

    def test_same_seed_same_maze(self) -> None:
        """Two runs with one seed are identical."""
        first = make_maze(seed=123)
        second = make_maze(seed=123)
        self.assertEqual(_hex_dump(first), _hex_dump(second))

    def test_different_seeds_differ(self) -> None:
        """Two different seeds give two different mazes."""
        first = make_maze(seed=1)
        second = make_maze(seed=2)
        self.assertNotEqual(_hex_dump(first), _hex_dump(second))

    def test_generate_is_repeatable(self) -> None:
        """Generating twice on one object gives one maze."""
        maze = MazeGenerator(15, 15, True, (0, 0), (14, 13), 9)
        generate(maze)
        first = _hex_dump(maze)
        generate(maze)
        self.assertEqual(first, _hex_dump(maze))


def _hex_dump(maze: MazeGenerator) -> list[str]:
    """Return the hexadecimal rows of the maze in memory."""
    return [
        "".join(cell_to_hex(cell.walls) for cell in row)
        for row in maze.grid.cells
    ]


class TestParser(unittest.TestCase):
    """The configuration file parser must give clear errors."""

    def parse_text(self, text: str) -> Config:
        """Write ``text`` to a file and parse it."""
        handle = tempfile.NamedTemporaryFile(
            "w",
            suffix=".txt",
            delete=False,
            encoding="utf-8",
        )
        with handle:
            handle.write(text)
        self.addCleanup(os.unlink, handle.name)
        return parse_config(handle.name)

    def test_valid_config(self) -> None:
        """Every key of the subject is understood."""
        config = self.parse_text(
            "# comment\n"
            "\n"
            "WIDTH = 30\n"
            "HEIGHT = 10\n"
            "ENTRY = 0,5\n"
            "EXIT = 29,9\n"
            "OUTPUT_FILE = out.txt\n"
            "PERFECT = true\n"
            "SEED = 7\n"
        )
        self.assertEqual(config.width, 30)
        self.assertEqual(config.height, 10)
        self.assertEqual(config.entry, (0, 5))
        self.assertEqual(config.exit, (29, 9))
        self.assertEqual(config.output_file, "out.txt")
        self.assertTrue(config.perfect)
        self.assertEqual(config.seed, 7)

    def test_missing_key(self) -> None:
        """A missing mandatory key stops the program."""
        with self.assertRaises(ValueError) as caught:
            self.parse_text("WIDTH = 10\nHEIGHT = 10\n")
        self.assertIn("missing", str(caught.exception))

    def test_invalid_line(self) -> None:
        """A line without '=' is refused."""
        with self.assertRaises(ValueError):
            self.parse_text("WIDTH 10\n")

    def test_unknown_key_is_ignored(self) -> None:
        """Extra keys only print a warning."""
        output = StringIO()
        with redirect_stdout(output):
            config = self.parse_text(
                self._valid_text() + "EXTRA = 1\n"
            )
        self.assertIn("Warning", output.getvalue())
        self.assertEqual(config.width, 20)

    def test_entry_equals_exit(self) -> None:
        """Entry and exit must be different cells."""
        text = (
            self._valid_text().replace(
                "EXIT = 19,18", "EXIT = 0,0"
            )
        )
        with self.assertRaises(ValueError):
            self.parse_text(text)

    def test_position_outside_maze(self) -> None:
        """Positions must be inside the maze."""
        text = (
            self._valid_text().replace(
                "EXIT = 19,18", "EXIT = 40,40"
            )
        )
        with self.assertRaises(ValueError):
            self.parse_text(text)

    def test_bad_perfect_value(self) -> None:
        """PERFECT only accepts true or false."""
        text = self._valid_text().replace(
            "PERFECT = false", "PERFECT = maybe"
        )
        with self.assertRaises(ValueError):
            self.parse_text(text)

    def test_bad_width(self) -> None:
        """WIDTH must be a positive integer."""
        text = self._valid_text().replace(
            "WIDTH = 20", "WIDTH = wide"
        )
        with self.assertRaises(ValueError):
            self.parse_text(text)
        text = self._valid_text().replace(
            "WIDTH = 20", "WIDTH = 0"
        )
        with self.assertRaises(ValueError):
            self.parse_text(text)

    def test_missing_file(self) -> None:
        """A missing file gives a clear message."""
        with self.assertRaises(ValueError) as caught:
            parse_config("no_such_config.txt")
        self.assertIn("not found", str(caught.exception))

    @staticmethod
    def _valid_text() -> str:
        """Return a valid configuration file content."""
        return (
            "WIDTH = 20\n"
            "HEIGHT = 20\n"
            "ENTRY = 0,0\n"
            "EXIT = 19,18\n"
            "OUTPUT_FILE = maze.txt\n"
            "PERFECT = false\n"
        )


class TestRender(unittest.TestCase):
    """The terminal drawing must never crash."""

    def test_render_lines(self) -> None:
        """One line per canvas row plus the legend."""
        maze = make_maze()
        text = render_maze(maze, maze.solve(), False, THEMES[0])
        expected = (2 * maze.grid.height + 1) + 2
        self.assertEqual(len(text.splitlines()), expected)

    def test_small_maze_renders(self) -> None:
        """A maze without the "42" sign still renders."""
        maze = make_maze(8, 10, start=(0, 0), end=(7, 8))
        text = render_maze(maze, maze.solve(), True, THEMES[1])
        self.assertIn("entry", text)
        self.assertIn("exit", text)

    def test_path_can_be_hidden(self) -> None:
        """Hiding the path removes its color from the drawing."""
        maze = make_maze()
        path = maze.solve()
        theme = THEMES[0]
        shown = render_maze(maze, path, True, theme)
        hidden = render_maze(maze, path, False, theme)
        self.assertGreater(
            shown.count(theme.path_code),
            hidden.count(theme.path_code),
        )

    def test_pattern_colors_can_be_toggled(self) -> None:
        """Turning the pattern colors off removes them."""
        maze = make_maze()
        path = maze.solve()
        theme = THEMES[2]
        colored = render_maze(maze, path, False, theme, True)
        plain = render_maze(maze, path, False, theme, False)
        self.assertGreater(
            colored.count(theme.pattern_code),
            plain.count(theme.pattern_code),
        )


if __name__ == "__main__":
    unittest.main()
