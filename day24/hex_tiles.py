from collections import defaultdict
from tqdm import trange

UNIT_VECTORS = {
    'w': (-1, -1, 0),
    'e': (1, 1, 0),
    'nw': (-1, 0, 1),
    'ne': (0, 1, 1),
    'sw': (0, -1, -1),
    'se': (1, 0, -1)
}

def get_input():
    tile_paths = []
    with open('day24/input') as f:
        for line in f.readlines():
            line = line.strip()

            prefix = None
            steps = []
            for char in line:
                if prefix:
                    steps.append(prefix + char)
                    prefix = None
                elif char in {'s', 'n'}:
                    prefix = char
                else:
                    steps.append(char)
            tile_paths.append(steps)

    return tile_paths

def add_cord(cord_1, cord_2):
    return tuple(c1 + c2 for c1, c2 in zip(cord_1, cord_2))

def part_1():
    tile_count = defaultdict(lambda: 0)
    tile_paths = get_input()

    for path in tile_paths:
        current_position = (0, 0, 0)
        #tile_count[current_position] += 1
        for step in path:
            current_position = add_cord(current_position, UNIT_VECTORS[step])
        tile_count[current_position] += 1
    
    return len([count for count in tile_count.values() if count % 2 == 1])


def part_2():
    tile_count = defaultdict(lambda: 0)
    tile_paths = get_input()

    for path in tile_paths:
        current_position = (0, 0, 0)
        #tile_count[current_position] += 1
        for step in path:
            current_position = add_cord(current_position, UNIT_VECTORS[step])
        tile_count[current_position] += 1
        if tile_count[current_position] % 2 == 0:
            del tile_count[current_position]

    tile_count = set(tile_count.keys())

    for _ in trange(100):
        # Get all tiles to consider
        mutable_tiles = set()
        for tile in tile_count:
            mutable_tiles.add(tile)
            for coord in UNIT_VECTORS.values():
                mutable_tiles.add(add_cord(tile, coord))

        new_counts = set()
        for tile in mutable_tiles:
            black_tile = tile in tile_count
            black_neighbors = sum(1 for coord in UNIT_VECTORS.values() if add_cord(tile, coord) in tile_count)
            if black_tile and 1 <= black_neighbors <= 2:
                new_counts.add(tile)
            elif not black_tile and black_neighbors == 2:
                new_counts.add(tile)
        tile_count = new_counts

    return len(new_counts)


if __name__ == "__main__":
    print(part_1())
    print(part_2())

