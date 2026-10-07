*This activity has been created as part of the 42 curriculum by oalabed, leobeida.*

# A-Maze-ing

## Description

A-Maze-ing is a Python maze generator and visualizer.

The program reads a configuration file, generates a valid maze, writes
it using the required hexadecimal wall format, and draws it in the
terminal with its entry, its exit and the shortest path between them.

Features:

* Perfect mazes with exactly one path between any two cells.
* Imperfect ("playable") mazes with loops, like a Pac-Man board, with
  the four corners and the centre open and almost no dead ends.
* A "42" sign made of fully closed cells, omitted with a message when
  the maze is too small for it.
* Reproducible generation with a seed: the same configuration always
  gives the same maze.
* Shortest-path calculation with breadth-first search.
* Terminal drawing with ANSI colors: entry, exit, solution path and
  the "42" sign are colored, three color themes are available.
* Interactions: re-generate a new maze, show/hide the path, change the
  colors, toggle the colors of the "42" sign.

## Instructions

### Requirements

* Python 3.10 or newer
* flake8
* mypy

### Run

From the repository root:

```bash
python3 a_maze_ing.py config.txt
```

The program reads the configuration file, generates the maze, writes
the output file, and displays the maze with a small menu:

```text
1] Re-generate a new maze
2] Show/hide the shortest path
3] Change the colors
4] Toggle the colors of the '42' pattern
5] Quit
```

Every re-generation prints the seed that was used, so it can be put
back into the configuration file to reproduce that exact maze.

### Makefile

```bash
make install    # install flake8, mypy and build
make run        # run the program with the default config
make debug      # run the program under the Python debugger
make test       # run the unit tests
make lint       # flake8 + mypy with the required options
make lint-strict  # flake8 + mypy --strict
make clean      # remove caches, build directories and output file
```

`make lint` runs flake8 and mypy with the options required by the
subject:

```text
--warn-return-any --warn-unused-ignores --ignore-missing-imports
--disallow-untyped-defs --check-untyped-defs
```

## Configuration

The configuration file uses one `KEY = VALUE` pair per line. Lines
that are empty or that start with `#` are comments. Unknown keys are
ignored with a warning so extra notes can stay in the file.

Example:

```text
WIDTH=20
HEIGHT=20
ENTRY=0,0
EXIT=19,18
OUTPUT_FILE=maze.txt
PERFECT=False
SEED=42
```

| Key           | Required | Description                                  |
| ------------- | -------- | -------------------------------------------- |
| `WIDTH`       | yes      | Number of cells horizontally                 |
| `HEIGHT`      | yes      | Number of cells vertically                   |
| `ENTRY`       | yes      | Entry coordinates `(x,y)`, inside the maze   |
| `EXIT`        | yes      | Exit coordinates `(x,y)`, different from entry |
| `OUTPUT_FILE` | yes      | Name of the output file                      |
| `PERFECT`     | yes      | `True` for a perfect maze, `False` for a board |
| `SEED`        | no       | Seed of the random generator, for reproducible mazes |

Errors are reported with a clear message and a non-zero exit status:
a missing file, a line without `=`, a missing mandatory key, a bad
value, or a position outside the maze.

## Maze Generation Algorithm

The generator uses **Depth-First Search (DFS)**, also known as the
**recursive backtracker**, to carve a perfect maze.

Starting from the entry, the algorithm randomly picks an unvisited
neighbour, removes the wall between the two cells and continues. When
a cell has no unvisited neighbour left, the search backtracks. The
result is a spanning tree of the grid: exactly one path between any
two cells and no loop.

DFS was chosen because it is simple, fast, easy to reproduce with a
random seed, and it naturally creates long corridors and few dead
ends.

The other rules of the subject are applied on top of the tree:

* The cells of the "42" sign are reserved before carving; afterwards
  the remaining corridor components are joined by opening walls
  between different groups, which never creates a loop, so a perfect
  maze stays perfect.
* The three-by-three rule is enforced by opening a wall only when it
  does not create a fully open 3x3 area.
* In playable mode, extra walls are opened to remove dead ends, to
  give the four corners and the centre at least two openings, and to
  guarantee at least two independent loops.

The shortest path is then computed with **Breadth-First Search
(BFS)**: the first time the exit is reached, the path kept is already
a shortest one.

## Output Format

Each maze cell is stored as one hexadecimal digit.

| Bit | Direction |
| --- | --------- |
| `0` | North     |
| `1` | East      |
| `2` | South     |
| `3` | West      |

Bit 0 is the least significant bit, and a bit set to `1` means that
the wall is closed. After the maze rows, the output file contains one
empty line, the entry as `(x, y)`, the exit as `(x, y)`, and the
shortest path as a sequence of `N`, `E`, `S` and `W` movements. Every
line ends with a line feed.

## Reusable Code

The reusable part of the project is the `MazeGenerator` class. It
lives in a single file, `mazegen.py`, at the root of the repository,
so it can be installed on its own with pip and imported by any other
Python project.

Build the package:

```bash
python3 -m build --wheel --no-isolation --outdir .
```

This produces `mazegen-1.0.0-py3-none-any.whl` at the root of the
repository. Install it with:

```bash
pip install mazegen-1.0.0-py3-none-any.whl
```

Use it from another project:

```python
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
solution = maze.solve()      # list of (row, column) cells
loops = maze.count_loops()   # 0 for a perfect maze
```

* `maze.grid.cells[row][col]` gives the `Cell` objects and their
  `walls` dictionaries (`"N"`, `"E"`, `"S"`, `"W"`, `True` = closed).
* `maze.pattern` is the set of cells of the closed "42" sign.
* `shortest_path(maze)` is also available as a module function.

Everything else in `maze_app/` belongs to the activity itself:
`parser.py` reads the configuration file, `output_file.py` writes the
hexadecimal file, and `render.py` draws the maze in the terminal.

## Tests

The `tests/` directory contains a unit test suite (standard library
`unittest`, no extra dependency):

```bash
python3 -m unittest discover -s tests -v
```

It checks the hexadecimal bit order, the structure of the output
file, the shortest path against an independent BFS, connectivity,
the rules of the perfect and playable modes (loops, 3x3 rule, border
walls, shared walls, spawns, dead ends, "42" cells), seed
reproducibility, the configuration parser errors, and the renderer.

## Project Structure

```text
.
├── mazegen.py           # reusable single-file maze generator
├── maze_app/
│   ├── __init__.py
│   ├── parser.py        # configuration file parser
│   ├── output_file.py   # hexadecimal output file
│   └── render.py        # terminal drawing with ANSI colors
├── a_maze_ing.py        # main program and menu
├── config.txt           # default configuration
├── tests/
│   └── test_maze.py     # unit tests
├── mazegen-1.0.0-py3-none-any.whl   # built package
├── Makefile
├── pyproject.toml
├── LICENSE.md
├── .gitignore
└── README.md
```

## Resources

* Python Documentation — https://docs.python.org/3/
* Python `random` module — random number generation and seeds
* Depth-First Search — graph traversal and maze generation
* Breadth-First Search — shortest-path calculation
* PEP 8 / flake8 — Python coding style
* PEP 257 — docstring conventions
* mypy — Python static type checking
* Python packaging guide — https://packaging.python.org/

### AI Usage

AI was used as a learning and development assistant during the
project (OpenAI ChatGPT and the opencode coding assistant). It was
used to:

* understand maze-generation algorithms (DFS, BFS, cycle rank);
* explain Python concepts, type hints and docstring conventions;
* review the hexadecimal output format and the rendering logic;
* debug errors and suggest refactoring of the configuration parser;
* check the Makefile, packaging and README against the subject.

All suggestions were reviewed, tested, corrected when wrong, and
understood before being kept in the project; the unit tests were
written to verify them independently.

## Team & Project Management

### Team and Roles

* **oalabed** — maze generation algorithms (`mazegen.py`),
  shortest path, hexadecimal output format, packaging (pyproject,
  wheel) and the Makefile.
* **leobeida** — configuration parser, terminal renderer and ANSI
  colors, menu and interactions, unit tests, README and documentation.

### Planning

The project was developed in stages:

1. Configuration parsing and clear error messages.
2. Cell and grid data structures.
3. Perfect maze generation with DFS.
4. "42" pattern and connectivity repair.
5. Playable mode: loops, spawns and dead ends.
6. Shortest path with BFS.
7. Hexadecimal output file.
8. Terminal visualization, colors and menu.
9. Unit tests, linting, packaging and documentation.

The plan evolved during development: the three-by-three rule and the
spawn requirements came from the subject review, and the rendering
was redesigned to draw from the maze in memory instead of re-reading
the output file.

### What Worked Well

* Separating the reusable generator (`mazegen.py`) from the activity
  code (`maze_app/`), which made both parts easy to test alone.
* Using seeds, so every failing maze could be reproduced exactly.
* Writing tests for each rule of the subject as soon as it was
  implemented, instead of at the end.

### What Could Be Improved

* Earlier integration testing would have reduced debugging time.
* The renderer could have been designed before the generator, to
  catch display bugs sooner.
* More edge-case tests (very small mazes, unusual seeds) could be
  added.

### Tools Used

* Python 3
* Git / GitHub
* Visual Studio Code
* flake8 and mypy
* Python packaging tools (`build`, `setuptools`)
* unittest
* AI assistance for learning, debugging and review
