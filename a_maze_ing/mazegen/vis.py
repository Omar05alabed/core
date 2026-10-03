from enum import Enum


class Chars(Enum):
    MD = "\u2533"   # ┳ middle, down
    MU = "\u253B"   # ┻ middle, up

    RRC = "\u250F"  # ┏ right upper corner
    LRC = "\u2513"  # ┓ left upper corner

    RDC = "\u2517"  # ┗ right lower corner
    LDC = "\u251B"  # ┛ left lower filecorner

    VL = "\u2503"   # ┃ vertical line
    HL = "\u2501"   # ━ horizontal line

    RHC = "\u2523"  # ┣ right half cross / vertical
    LHC = "\u252B"  # ┫ left half cross / vertical

    CC = "\u254B"   # ╋ cross


def convert_to_binary(output_file: str):
    with open(output_file, "r") as file:
        binary = []
        for line in file:
            # print("READ:", repr(line))
            if line.startswith("("):
                break
            for digit in line.strip():
                # print("DIGIT:", repr(line))
                b = int(digit, 16)
                b = bin(b)[2:]
                binary.append(b.zfill(4))
    return binary


def put_the_walls(binary):
    walls = []
    i = 0
    for i in binary:
        cell = []
        if i[0] == "1":
            cell.append("N")
        if i[1] == "1":
            cell.append("E")
        if i[2] == "1":
            cell.append("S")
        if i[3] == "1":
            cell.append("W")
        walls.append(cell)
    return walls


def canvas(width, height):
    width = width * 2 + 1
    height = height + 2
    canvas = [[" "] * (width) for _ in range(height)]
    canvas[0][0] = Chars.RRC.value
    # ro print the upper walls
    for u in range(1, width):
        canvas[0][u] = Chars.HL.value
    canvas[0][width - 1] = Chars.LRC.value

    # to print the lower
    for lo in range(1, width):
        canvas[height - 1][lo] = Chars.HL.value
    canvas[height - 1][width - 1] = Chars.LDC.value

    # to print the right side
    for r in range(1, height - 1):
        canvas[r][width - 1] = Chars.VL.value
    canvas[height - 1][width - 1] = Chars.LDC.value
    # to print the left side
    for le in range(1, height):
        canvas[le][0] = Chars.VL.value
    canvas[height - 1][0] = Chars.RDC.value

    '''
    gives somthing like this
        ┏━━━━━━━━━━━━━━━━━━━┓
        ┃                   ┃
        ┃                   ┃
        ┃                   ┃
        ┃                   ┃
        ┃                   ┃
        ┃                   ┃
        ┃                   ┃
        ┃                   ┃
        ┗━━━━━━━━━━━━━━━━━━━┛
    '''
    return canvas


def print_walls(canvas, walls, width):
    for i in range(len(walls)):

        row = i // width
        col = i % width

        x = col * 2 + 1
        y = row + 1

        for wall in walls[i]:

            if wall == "N":
                canvas[y - 1][x] = Chars.HL.value

            elif wall == "S":
                canvas[y + 1][x] = Chars.HL.value

            elif wall == "W":
                canvas[y][x - 1] = Chars.VL.value

            elif wall == "E":
                canvas[y][x + 1] = Chars.VL.value

    return canvas


def maze():
    b = convert_to_binary("output_maze.txt")
    p = put_the_walls(b)
    c = canvas(15, 15)
    print_walls(c, p, 15)

    for row in c:
        print("".join(row))


maze()
