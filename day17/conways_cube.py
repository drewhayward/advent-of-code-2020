from copy import deepcopy

CUBE_SIZE = 20

def get_input():
    start_slice = []
    with open('day17/input') as f:
        for line in f.readlines():
            start_slice.append([char == "#" for char in line.strip()])

    return start_slice

def num_neighbors(cube, x, y, z):
    total = 0
    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            for k in range(-1, 2, 1):
                x_n = x + i
                y_n = y + j
                z_n = z + k

                in_bounds = (0 <= x_n < CUBE_SIZE) and (0 <= y_n < CUBE_SIZE) and (0 <= z_n < CUBE_SIZE)
                is_self = (i == 0) and (j == 0) and (k == 0)
                if in_bounds and not is_self and cube[x_n][y_n][z_n]:
                    total += 1
    
    return total

def step_cube(cube):
    newcube = deepcopy(cube)
    for x in range(CUBE_SIZE):
        for y in range(CUBE_SIZE):
            for z in range(CUBE_SIZE):
                active = cube[x][y][z]
                num_n = num_neighbors(cube, x, y, z)
                if active and not (2 <= num_n <= 3):
                    newcube[x][y][z] = False
                elif not active and num_n == 3:
                    newcube[x][y][z] = True
    
    return newcube

def print_cube(cube):
    # Get slices to print
    totals = [0] * CUBE_SIZE
    for z in range(CUBE_SIZE):
        for x in range(CUBE_SIZE):
            for y in range(CUBE_SIZE):
                if cube[x][y][z]:
                    totals[z] += 1
                    break
            if totals[z] > 0:
                break

    for z in range(CUBE_SIZE):
        if totals[z] > 0:
            print(f'Layer {z}')
            # Print only slices with true cells
            for y in range(CUBE_SIZE):
                print(''.join(['#' if cube[x][y][z] else '.' for x in range(CUBE_SIZE)]))

            print()


def part_1(steps):
    cube = [
        [
            [False for _ in range(CUBE_SIZE)]
            for _ in range(CUBE_SIZE)
        ]
        for _ in range(CUBE_SIZE)
    ]

    start_slice = get_input()
    offset = (CUBE_SIZE - len(start_slice)) // 2

    if offset < steps:
        print('Might not have enough offset to capture full activity')

    # Initialize cube
    for y, row in enumerate(start_slice):
        for x, cell in enumerate(row):
            cube[x + offset][y + offset][7] = cell

    print_cube(cube)


    for _ in range(steps):
        cube = step_cube(cube)
        print_cube(cube)

    return sum([1 for plane in cube for row in plane for cell in row if cell])

if __name__ == "__main__":
    print(part_1(6))