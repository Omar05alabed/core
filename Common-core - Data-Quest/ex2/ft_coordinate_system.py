import math


def get_player_pos() -> tuple[float, float, float]:
    while True:

        try:
            pos = input("Enter new coordinates as floats in format ’x,y,z’:")
            first = pos.split(",")
            if len(first) != 3:
                print("Invalid syntax")
                continue

            for p in first:
                float(p)

            x = float(first[0])
            y = float(first[1])
            z = float(first[2])
            return (x, y, z)

        except ValueError:
            print(f"Error on parameter {p}: could not convert to float")


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    x1, y1, z1 = get_player_pos()
    print(f"Got first tuple: {x1, y1, z1}")
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    dc = math.sqrt((x1*x1)+(y1*y1)+(z1*z1))
    print(f"Distance to center: {round(dc, 4)}")
    x2, y2, z2 = get_player_pos()
    dbt = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    print(f"Distance between the 2 sets of coordinates: {round(dbt, 4)}")
