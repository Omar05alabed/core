*This activity has been created as part of the 42 curriculum by <oalabed>.*

# Get Next Line

## Description

The **get_next_line** project implements a function that reads a single line from a file descriptor. Each call returns the next available line, including the newline character (`\n`) if it exists.

This project explores:
- File descriptor handling
- Buffered reading using `read()`
- Dynamic memory management
- Static variables
- Edge case handling (empty files, large buffers, no newline, etc.)

The goal is to build a robust and memory-safe function capable of reading files or standard input line by line without loading the entire file into memory.

---

## Instructions

### Compilation

Use the following command to compile:

```bash
cc -Wall -Wextra -Werror -D BUFFER_SIZE=42 get_next_line.c get_next_line_utils.c
