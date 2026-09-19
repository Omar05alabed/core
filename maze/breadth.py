def shortest_path(grid, start, end):
    queue = [start]
    previous = {start: None}

    directions = {
        "N": (-1, 0),
        "E": (0, 1),
        "S": (1, 0),
        "W": (0, -1),
    }
    print(queue)
    print(previous)
    while queue:
        current = queue.pop(0)
        print("current", current)
        print("queue", queue)
        if current == end:
            break

        current_row, current_colm = current
        current_cell = grid.cells[current_row][current_colm]
        print("direc", directions)
        for direction, (row_change, colm_change) in directions.items():
            print("direction", direction)
            if current_cell.walls[direction]:
                continue

            next_position = (
                current_row + row_change,
                current_colm + colm_change,
            )

            if next_position in previous:
                continue

            previous[next_position] = current
            queue.append(next_position)
    print("s", previous)
    path = []
    current = end

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()
    return path
