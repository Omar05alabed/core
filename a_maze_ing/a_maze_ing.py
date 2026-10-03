import sys
from mazegen.parser import parsing
from mazegen.maze_generator import MazeGenerator
from mazegen.shortest_path import shortest_path
from mazegen.output_file import output_file
from mazegen.v import draw_maze

DARK_RED = "\033[48;2;94;28;35m"

NAVY = "\033[38;2;24;36;51m"
TEAL = "\033[48;2;58;140;140m"
GOLD = "\033[48;2;232;184;109m"

DARK_GREEN = "\033[38;2;41;73;54m"
SAGE = "\033[48;2;115;159;96m"
CREAM = "\033[48;2;255;242;204m"

PURPLE = "\033[38;2;91;58;140m"
BLUE = "\033[48;2;57;118;168m"
PINK = "\033[48;2;214;107;160m"


WALL_COLORS = [NAVY, DARK_GREEN, PURPLE]
ECOLOR = [TEAL, SAGE, BLUE]
PATHCOLOR = [GOLD, CREAM, PINK]


def main_maze() -> None:
    try:
        config_file = sys.argv[1]
    except IndexError:
        print("Usage: python3 a_maze_ing.py config.txt")
        sys.exit()
    config = parsing(config_file)
    entry = (config["ENTRY"][1], config["ENTRY"][0])
    exit = (config["EXIT"][1], config["EXIT"][0])

    maze = MazeGenerator(
        config["HEIGHT"],
        config["WIDTH"],
        config["PERFECT"],
        entry,
        exit,
        config.get("SEED"),
        )
    show = False
    theme = 0
    try:
        maze.generator()

        path = shortest_path(maze)
        output_file(maze, config["OUTPUT_FILE"], path)

        draw_maze(maze, config["OUTPUT_FILE"], DARK_RED,
                  WALL_COLORS[theme], ECOLOR[theme], "")
        print(config["OUTPUT_FILE"])
        while True:
            user = input("1] press 1 to Re-generate a new maze\n"
                         "2] press 2 to show/Hide the shortest path\n"
                         "3] press 3 to change the maze colour\n"
                         "4] press 4 to exit\n")
            if user == "1":
                main_maze()
            elif user == "2":
                show = not show
                if show:
                    print("VISIABLE!")
                    draw_maze(maze, config["OUTPUT_FILE"], DARK_RED,
                              WALL_COLORS[theme], ECOLOR[theme],
                              PATHCOLOR[theme],)
                else:
                    print("HIDDEN!")
                    draw_maze(maze, config["OUTPUT_FILE"], DARK_RED,
                              WALL_COLORS[theme], ECOLOR[theme],
                              "")
            elif user == "3":
                print("\nTHE AVAILABLE THEMES:")
                print("[1]. SEA-PEACHE")
                print("[2.  CHRISMAS")
                print("[3]. SUMMER")
                choice = input("\nCHOOSE ONE PLEASE: ")

                if choice == "1":
                    theme = 0
                elif choice == "2":
                    theme = 1
                elif choice == "3":
                    theme = 2
                else:
                    print("Wrong insertion.")
                    continue
                draw_maze(maze, config["OUTPUT_FILE"], DARK_RED,
                          WALL_COLORS[theme], ECOLOR[theme], PATHCOLOR[theme])

            elif user == "4":
                print("you exit the program")
                sys.exit()

    except ValueError as e:
        print(e)

    except KeyboardInterrupt:
        print("you exit the program")
        sys.exit()
    except EOFError:
        sys.exit()


main_maze()
