import math


def get_player_pos() -> None:
    s = True
    while s:
        try:
            pos = input("Enter new coordinates as floats in format x,y,z:")
            part = pos.split(",")
            if len(part) != 3:
                raise ValueError
            a = float(part[0])
            b = float(part[1])
            c = float(part[2])
            s = False
        except ValueError:
            print("Invalid syntax")

    print(f"Got a first tuple: ({part[0]}, {part[1]}, {part[2]})")
    print(f"It includes: X={part[0]}, Y={part[1]}, Z={part[2]}")
    center = math.sqrt((a*a)+(b*b)+(c*c))
    print(f"Distance to center: {round(center, 4)}")

    print("Get a second set of coordinates")
    t = True
    while t:
        try:
            sec = input("Enter new coordinates as floats in format x,y,z:")
            secpart = sec.split(",")
            if len(secpart) != 3:
                raise ValueError
            for p in secpart:
                float(p)
            a1 = float(secpart[0])
            b1 = float(secpart[1])
            c1 = float(secpart[2])
            break
        except ValueError:
            print(f"Error on parameter {p}: could not convert to float")

    dis2 = math.sqrt((a1-a)**2 + (b1-b)**2 + (c1-c)**2)
    print(f"Distance between the 2 sets of coordinates: {round(dis2, 4)}")
    return


get_player_pos()
