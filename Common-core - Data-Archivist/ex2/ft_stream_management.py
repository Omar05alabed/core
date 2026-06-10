import sys


if len(sys.argv) != 2:
    print("Usage: ft_ancient_text.py <file>")
    sys.exit(1)
print("=== Cyber Archives Recovery & Preservation ===")
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
    sys.stderr.write(f"Error opening file {sys.argv[1]}:{e}\n")
    sys.exit(1)
except PermissionError as e:
    sys.stderr.write(f"Error opening file {sys.argv[1]}: {e}\n")
lines = content.splitlines()
modified = []
for line in lines:
    modified.append(line + "#")
result = "\n".join(modified)
print("---")
print(result)
print("---")
sys.stdout.write("Enter new file name (or empty): ")
sys.stdout.flush()

new_file_name = sys.stdin.readline().rstrip("\n")
if new_file_name == "":
    out = sys.stdout.write("Not saving data.\n")
    print(out)
    sys.exit(1)
try:
    print(f"Saving data to {new_file_name}")
    new_file = open(new_file_name, "w")
    new_file.write(result)
    new_file.close()
    print(f"Data saved in file {new_file_name}")
    print(result)
except PermissionError as e:
    sys.stderr.write(f"Error opening file {sys.argv[1]}: {e}\n")
    print("Data not saved.")
