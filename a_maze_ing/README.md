*This activity has been created as part of the 42 curriculum by oalabed, leobeida.*

# A-Maze-ing

## Description

A-Maze-ing is a Python maze generator and visualizer.

The program reads a configuration file, generates a valid maze, saves it using the required hexadecimal wall format, and displays it in the terminal.

The project supports:

* Perfect mazes with a unique path between cells.
* Imperfect/playable mazes with multiple routes.
* Configurable entry and exit.
* Reproducible generation using a seed.
* Shortest-path calculation.
* Terminal visualization with colors.
* Interactive maze regeneration, path visibility, and wall-color changes.

## Instructions

### Requirements

* Python 3.10+
* flake8
* mypy

### Run

From the `mazegen` directory:

```bash
python3 a_maze_ing.py config.txt
```

The program reads the configuration file, generates the maze, writes the output file, and displays the maze.

### Makefile

```bash
make install
make run
make debug
make lint
make clean
```

`make lint` runs flake8 and mypy with the required options.

## Configuration

The configuration file uses one `KEY=VALUE` pair per line. Lines beginning with `#` are comments.

Example:

```text
WIDTH=20
HEIGHT=15
ENTRY=0,0
EXIT=19,14
OUTPUT_FILE=maze.txt
PERFECT=True
SEED=42
```

Required keys:

| Key           | Description                  |
| ------------- | ---------------------------- |
| `WIDTH`       | Number of cells horizontally |
| `HEIGHT`      | Number of cells vertically   |
| `ENTRY`       | Entry coordinates `(x,y)`    |
| `EXIT`        | Exit coordinates `(x,y)`     |
| `OUTPUT_FILE` | Output maze filename         |
| `PERFECT`     | `True` or `False`            |

`SEED` is optional. When provided, it makes maze generation reproducible.

## Maze Generation Algorithm

The project uses **Depth-First Search (DFS)**, also known as the **recursive backtracker**, for perfect maze generation.

The algorithm starts from a cell, randomly selects an unvisited neighbour, removes the wall between them, and continues until all cells have been visited. Backtracking is used when a cell has no unvisited neighbours.

DFS was chosen because it is simple to understand, produces connected mazes with no loops in perfect mode, and is easy to reproduce using a random seed.

For imperfect mode, additional connections are opened to create loops and alternative routes.

## Output Format

Each maze cell is stored as one hexadecimal digit.

The wall bits are:

| Bit | Direction |
| --- | --------- |
| `0` | North     |
| `1` | East      |
| `2` | South     |
| `3` | West      |

A value of `1` means the wall is closed.

After the maze rows, the output file contains:

1. Entry coordinates
2. Exit coordinates
3. Shortest path using `N`, `E`, `S`, and `W`

## Reusable Code

The reusable part of the project is the `MazeGenerator` class.

It is located in the `mazegen` package and can be imported by another Python project.

Example:

```python
from mazegen.maze_generator import MazeGenerator

maze = MazeGenerator(
    height=10,
    width=10,
    perfect=True,
    entry=(0, 0),
    exit=(9, 9),
    seed=42
)

maze.generator()
```

The generated maze structure can be accessed through the generator's grid and cells. The shortest path can also be calculated using the provided path functionality.

The reusable package can be built with:

```bash
python3 -m build
```

This produces a `mazegen-*` `.whl` and/or `.tar.gz` package.

## Project Structure

```text
.
├── mazegen/
│   ├── a_maze_ing.py
│   ├── maze_generator.py
│   ├── grid.py
│   ├── cell.py
│   ├── dfs.py
│   ├── imperfect.py
│   ├── shortest_path.py
│   ├── parser.py
│   ├── output_file.py
│   ├── render.py
│   └── ...
├── config.txt
├── Makefile
├── pyproject.toml
├── LICENSE.md
├── .gitignore
└── README.md
```

## Resources

* Python Documentation — https://docs.python.org/3/
* Python `random` module — random number generation and seeds.
* Depth-First Search — graph traversal and maze generation.
* Breadth-First Search — shortest-path calculation.
* PEP 8 / flake8 — Python coding style.
* mypy — Python static type checking.

### AI Usage

AI was used as a learning and development assistant during the project. It helped with:

* Understanding maze-generation algorithms.
* Explaining Python concepts and type hints.
* Debugging errors and improving code structure.
* Understanding terminal rendering and ANSI colors.
* Reviewing configuration, Makefile, and packaging requirements.

All generated suggestions were reviewed, tested, modified when necessary, and understood before being used in the project.

## Team & Project Management

### Team

* **oalabed** — Maze generation, parsing, shortest path, output format, rendering, testing, and packaging.

### Planning

The project was developed in stages:

1. Configuration parsing.
2. Maze and cell data structures.
3. Perfect maze generation.
4. Imperfect maze generation.
5. Shortest-path calculation.
6. Hexadecimal output.
7. Terminal visualization and interaction.
8. Packaging, testing, linting, and documentation.

The plan evolved during development as bugs and rendering requirements were discovered.

### What Worked Well

* Separating maze generation from rendering and output.
* Using a dedicated `MazeGenerator` class for reusability.
* Using seeds to reproduce generated mazes.
* Testing generation and pathfinding independently.

### What Could Be Improved

* Earlier integration testing would have reduced debugging time.
* The rendering system could have been designed earlier.
* More automated tests could be added for edge cases and configuration errors.

### Tools Used

* Python
* Git / GitHub
* VS Code
* WSL / Fedora Linux
* flake8
* mypy
* Make
* Python packaging tools
* AI assistance for learning, debugging, and review
