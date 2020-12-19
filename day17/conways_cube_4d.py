from copy import deepcopy
from functools import reduce
from itertools import product
from tqdm import tqdm

DIMS = 4
CUBE_SIZE = 25

def get_input():
    start_slice = []
    with open('day17/input') as f:
        for line in f.readlines():
            start_slice.append([char == "#" for char in line.strip()])

    return start_slice

def index_tensor(tensor, coord):
    result = tensor
    return reduce(lambda res, idx: res[idx], [tensor] + list(coord))

def assign_tensor(tensor, coord, value):
    if len(coord) != tensor_dim(tensor):
        raise Exception("cord doesn't match tensor dim")
    l = tensor
    for dim, i in enumerate(coord):
        if dim == len(coord) - 1:
            l[i] = value
        else:
            l = l[i]


def tensor_dim(tensor):
    if isinstance(tensor, list):
        return 1 + tensor_dim(tensor[0])
    else:
        return 0

def num_neighbors(tensor, coord):
    total = 0
    position = [0] * DIMS
    for offset in product(range(-1, 2, 1), repeat=len(coord)):
        for i in range(DIMS):
            position[i] = offset[i] + coord[i]
        in_bounds = all(0 <= i < CUBE_SIZE for i in position)
        is_self = all(i == 0 for i in offset)
        if in_bounds and not is_self and index_tensor(tensor, position):
            total += 1
    
    return total

def step_cube(cube):
    newcube = deepcopy(cube)
    for point in product(range(CUBE_SIZE), repeat=tensor_dim(cube)):
        active = index_tensor(cube, point)
        num_n = num_neighbors(cube, point)
        if active and not (2 <= num_n <= 3):
            assign_tensor(newcube, point, False)
        elif not active and num_n == 3:
            assign_tensor(newcube, point, True)
    
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

def make_hypercube(size, dim):
    if dim == 0:
        return False
    else:
        return [make_hypercube(size, dim - 1) for _ in range(size)]

def sum_tensor(tensor):
    if isinstance(tensor, list):
        return sum([sum_tensor(child) for child in tensor])
    else:
        if tensor:
            return 1
        return 0

def part_2(steps):
    cube = make_hypercube(CUBE_SIZE, DIMS)

    start_slice = get_input()
    offset = (CUBE_SIZE - len(start_slice)) // 2

    if offset < steps:
        print('Might not have enough offset to capture full activity')

    # Initialize cube
    for y, row in enumerate(start_slice):
        for x, cell in enumerate(row):
            point = [offset for _ in range(DIMS)]
            point[0] += x
            point[1] += y
            assign_tensor(cube, point, cell)

    for _ in tqdm(range(steps)):
        cube = step_cube(cube)

    return sum_tensor(cube)

if __name__ == "__main__":
    print(part_2(6))