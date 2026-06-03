import sys


if len(sys.argv) != 2:
    print("Usage: ft_ancient_text.py <file>")
    sys.exit(1)
print("=== Cyber Archives Recovery ===")
print(f"Accessing file {sys.argv[1]}")
try:
    file = open(sys.argv[1])
    content = file.read()
    print("---\n"
          f"{content}\n"
          "---")
    print(f"File {sys.argv[1]} closed.")
    file.close()
except FileNotFoundError as e:
    print(f"Error opening file {sys.argv[1]}:{e}")
    sys.exit(1)
except PermissionError as e:
    print(f"Error opening file {sys.argv[1]}: {e}")
