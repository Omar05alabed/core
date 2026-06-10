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

except FileNotFoundError as e:
    print(f"Error opening file {sys.argv[1]}:{e}")
    sys.exit(1)
except PermissionError as e:
    print(f"Error opening file {sys.argv[1]}: {e}")
finally:
    print(f"File {sys.argv[1]} closed.")
    file.close()
lines = content.splitlines()
modified = []
for line in lines:
    modified.append(line + "#")
result = "\n".join(modified)
print("---")
print(result)
print("---")

new_file_name = input("Enter new file name (or empty):")
if new_file_name == "":
    print("Not saving data.")
    sys.exit(1)
print(f"Saving data to {new_file_name}")
new_file = open(new_file_name, "w")
new_file.write(result)
new_file.close()
print(f"Data saved in file {new_file_name}")
print(result)
