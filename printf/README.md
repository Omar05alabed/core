*This activity has been created as part of the 42 curriculum by omaral_abed.*

## Description

ft_printf is a recreation of the C standard library function `printf()`. This project implements a function that handles various format specifiers (%c, %s, %p, %d, %i, %u, %x, %X, %%) and returns the number of characters printed.

The goal is to create a static library `libftprintf.a` containing the `ft_printf()` function.

## Instructions

### Compilation

```bash
make        # Compile the library
make clean  # Remove object files
make fclean # Remove object files and library
make re     # Recompile everything
```

### Usage

```bash
# Compile your program with the library
cc your_program.c libftprintf.a -o your_program

# Run
./your_program
```

### Example

```c
#include "ft_printf.h"

int main(void)
{
    ft_printf("Hello %s!\n", "World");
    ft_printf("Number: %d, Hex: %x\n", 42, 255);
    return 0;
}
```

## Supported Conversions

- `%c` - Character
- `%s` - String
- `%p` - Pointer address
- `%d` - Decimal number
- `%i` - Integer
- `%u` - Unsigned decimal
- `%x` - Hexadecimal (lowercase)
- `%X` - Hexadecimal (uppercase)
- `%%` - Percent sign

## Resources

**Documentation:**
- [printf man page](https://man7.org/linux/man-pages/man3/printf.3.html)
- [Variadic functions in C](https://en.cppreference.com/w/c/variadic)
- [Creating static libraries](https://www.geeksforgeeks.org/static-vs-dynamic-libraries/)

**AI Usage:**
- Used to understand variadic functions (va_start, va_arg, va_end)
- Used to understand hexadecimal conversion algorithms
- Used for debugging compilation errors
- NOT used to write complete functions or solve core problems

## Algorithm and Data Structure

### Main Algorithm
1. Parse format string character by character
2. When '%' is found, identify the conversion specifier
3. Call appropriate print function for that specifier
4. Count all printed characters
5. Return total count

### Number Conversion (Recursive Division)
To print a number in base 10 or 16:
- Divide number by base
- Recursively print quotient
- Print remainder as digit

Example: 255 to hex → 255÷16=15 remainder 15(F), 15÷16=0 remainder 15(F) → "FF"

### Design Choices
- **Recursion for numbers**: Avoids buffer allocation, prints digits in correct order
- **Direct write() calls**: No buffering needed, simpler implementation
- **Separate functions**: Each conversion has its own function for modularity
