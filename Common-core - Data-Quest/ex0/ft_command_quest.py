import sys


def Command_Quest() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")

    if len(sys.argv) < 2:
        print("No arguments provided!")
        print(f"Total arguments: {len(sys.argv)}")
        return
    print(f"Arguments received: {len(sys.argv) - 1}")

    i = 1
    while i < len(sys.argv):
        print(f"Argument {i}: {sys.argv[i]}")
        i += 1

    print(f"Total arguments: {i}")


Command_Quest()
