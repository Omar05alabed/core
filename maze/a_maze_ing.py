#!/usr/bin/env python3
"""A-Maze-ing: generate, print and explore a maze.

Usage:
    python3 a_maze_ing.py config.txt
"""

from __future__ import annotations

import random
import sys

from maze_app.output_file import write_maze
from maze_app.parser import Config, parse_config
from maze_app.render import THEMES, clear_screen, render_maze
from mazegen import MazeGenerator

USAGE = "Usage: python3 a_maze_ing.py <configuration file>"
MAX_SEED = 1 << 31


def build_maze(config: Config, seed: int | None) -> MazeGenerator:
    """Generate the maze described by ``config``.

    The configuration uses ``(x, y)`` coordinates while the
    generator works with ``(row, column)`` positions.

    Args:
        config: Parsed configuration of the maze.
        seed: Seed of the random generator.

    Returns:
        The generated maze.

    Raises:
        ValueError: If a position is invalid or if the entry or the
            exit lies inside the "42" pattern.
    """
    start = (config.entry[1], config.entry[0])
    end = (config.exit[1], config.exit[0])
    maze = MazeGenerator(
        config.height,
        config.width,
        config.perfect,
        start,
        end,
        seed,
    )
    maze.generate()
    return maze


def _force_utf8() -> None:
    """Make sure the box drawing characters can be printed."""
    reconfigure = getattr(sys.stdout, "reconfigure", None)
    if reconfigure is not None:
        reconfigure(encoding="utf-8")


def _menu() -> str:
    """Print the menu and return the choice of the user.

    Returns:
        The raw answer of the user.
    """
    print("1] Re-generate a new maze")
    print("2] Show/hide the shortest path")
    print("3] Change the colors")
    print("4] Toggle the colors of the '42' pattern")
    print("5] Quit")
    return input("Choice: ").strip()


def main(argv: list[str]) -> int:
    """Run the A-Maze-ing program.

    Args:
        argv: Command line arguments, the script name first.

    Returns:
        ``0`` on success, ``1`` on a usage or configuration error.
    """
    _force_utf8()
    if len(argv) != 2:
        print(USAGE)
        return 1

    try:
        config = parse_config(argv[1])
    except ValueError as error:
        print(f"Error: {error}")
        return 1

    seed = config.seed
    if seed is None:
        seed = random.randrange(MAX_SEED)

    show_path = False
    theme_index = 0
    color_pattern = True

    try:
        maze = build_maze(config, seed)
        path = maze.solve()
        write_maze(maze, path, config.output_file)

        while True:
            clear_screen()
            theme = THEMES[theme_index]
            print(
                render_maze(
                    maze, path, show_path, theme, color_pattern
                )
            )
            print(
                f"\n{config.width}x{config.height} maze, "
                f"seed {seed}, output file "
                f"'{config.output_file}'"
            )
            print(f"Colors: {theme.name}\n")
            choice = _menu()
            if choice == "1":
                seed = random.randrange(MAX_SEED)
                maze = build_maze(config, seed)
                path = maze.solve()
                write_maze(maze, path, config.output_file)
            elif choice == "2":
                show_path = not show_path
            elif choice == "3":
                theme_index = (theme_index + 1) % len(THEMES)
            elif choice == "4":
                color_pattern = not color_pattern
            elif choice == "5":
                print("Goodbye!")
                return 0
            else:
                print("Unknown choice.")
                input("Press enter to continue...")
    except (ValueError, OSError) as error:
        print(f"Error: {error}")
        return 1
    except (EOFError, KeyboardInterrupt):
        print("\nGoodbye!")
        return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
