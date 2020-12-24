from tqdm import tqdm

def get_tiles():
    with open('day20/input') as f:
        data = f.read()
        tile_rows = [tile for tile in data.split('\n\n')]
        tiles = [Tile(rows.split('\n')[0][-5:-1], rows.split('\n')[1:]) for rows in tile_rows]
        return tiles
def check_match(side_1, side_2):
    match = True
    for c1, c2 in zip(side_1, side_2):
        if c1 != c2:
            match = False
            break
    if match:
        return True
    
    match = True
    for c1, c2 in zip(side_1, reversed(side_2)):
        if c1 != c2:
            match = False
            break

    return match

class Tile:
    def __init__(self, id, rows):
        self.id = int(id)
        rows = [list(row) for row in rows if row]
        self.sides = [
            rows[0],
            reversed(rows[-1]),
            [row[-1] for row in rows],
            reversed([row[0] for row in rows])
        ]
        self.data = rows
        
        self.num_neighbors = 0
        self.neighbors = [None] * 4
    
    def rotate(self):
        """
        Do a single clockwise rotation
        """
        n = len(self.data)
        new_data = [row[:] for row in self.data]

        for j in range(n):
            for i in range(n - 1, -1, -1):
                new_data[j][n - i - 1] = self.data[i][j]

        self.data = new_data
        
        rotated_neighbors = self.neighbors[:]
        rotated_neighbors[2] = self.neighbors[0]
        rotated_neighbors[3] = self.neighbors[1]
        rotated_neighbors[1] = self.neighbors[2]
        rotated_neighbors[0] = self.neighbors[3]
        self.neighbors = rotated_neighbors

        rotated_sides = self.sides[:]
        rotated_sides[2] = self.sides[0]
        rotated_sides[3] = self.sides[1]
        rotated_sides[1] = self.sides[2]
        rotated_sides[0] = self.sides[3]
        self.sides = rotated_sides


    def flip(self):
        """
        Flip the tile by transposing it
        """
        self.data = list(list(item) for item in zip(*self.data))
        self.neighbors = list(reversed(self.neighbors))
        self.sides = list(reversed(self.sides))
        # flipped_neighbors = self.neighbors[:]
        # flipped_neighbors[0] = self.neighbors[3]
        # flipped_neighbors[1] = self.neighbors[2]
        # flipped_neighbors[2] = self.neighbors[1]
        # flipped_neighbors[3] = self.neighbors[0]
        # self.neighbors = flipped_neighbors

    def __str__(self):
        return '\n'.join([''.join(row) for row in self.data])

def part_1():
    tiles = get_tiles()

    for x in range(len(tiles)):
        tile_1 = tiles[x]
        if tile_1.num_neighbors == 4:
            continue
        for y in range(x + 1, len(tiles)):
            tile_2 = tiles[y]
            if tile_2.num_neighbors == 4:
                continue

            matched = False
            for i, side_1 in enumerate(tile_1.sides):
                for j, side_2 in enumerate(tile_2.sides):
                    if check_match(side_1, side_2):
                        #print(f'{tile_1.id}:{tile_2.id} -> {side_1}:{side_2}')
                        tile_1.num_neighbors += 1
                        tile_2.num_neighbors += 1
                        tile_1.neighbors[i] = tile_2.id
                        tile_2.neighbors[j] = tile_1.id

    prod = 1
    for tile in tiles:
        if tile.num_neighbors == 2:
            prod *= tile.id

    return prod, tiles

def exact_match(side_1, side_2):
    return all([a == b for a, b in zip(side_1, reversed(side_2))])

def rotate_to_fit(target, tile, side_id):
    if exact_match(target, tile.sides[side_id]):
        return

    for _ in range(3):
        tile.rotate()
        if exact_match(target, tile.sides[side_id]):
            return

    tile.flip()
    if exact_match(target, tile.sides[side_id]):
        return

    for _ in range(3):
        tile.rotate()
        if exact_match(target, tile.sides[side_id]):
            return
    
    raise Exception('No match found')

def part_2(tiles):
    tile_map = {tile.id: tile for tile in tiles}
    # Find a corner
    corner_tile = None
    for tile in tiles:
        if tile.num_neighbors == 2:
            corner_tile = tile
            break

    # Make this tile the top left tile
    while corner_tile.neighbors[0] is not None or corner_tile[3] is not None:
        corner_tile.rotate()

    # Stitch image together
    img = []

    leftmost = corner_tile
    # For each row
    while True:
        # assuming the leftmost tile is lined up here
        rows = [row[:] for row in leftmost.data]
        current_tile = leftmost
        while True:
            # assuming the current tile is lined up here
            
            # Add the current rows
            for i in range(len(rows)):
                rows[i] += current_tile.data[i]

            # Rotate/flip the next tile to fit
            next_tile = tile_map[current_tile.neighbors[2]]
            if next_tile is None:
                break

            rotate_to_fit(current_tile.sides[2], next_tile, 3)
            current_tile = new_tile

        # add rows to img
        img += rows

        # rotate/flip new leftmost tile to fit



    # Trim border

    # Look for sea monsters in each orientation

    # return count of hashes minus the number of monsters * monster hash count



if __name__ == "__main__":
    prod, tiles = part_1()
    t = tiles[0]
    print(t)
    t.rotate()
    print('--')
    print(t)
    t.flip()
    print('--')
    print(t)
    print(prod)

