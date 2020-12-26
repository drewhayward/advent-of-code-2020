
def part_1(slope_step):
    with open('day3/input', 'r') as f:
        hill = [line.strip() for line in f.readlines()]

    x_pos = 0
    slope_size = len(hill[0])
    trees = 0
    for level in hill:
        if level[x_pos] == '#':
            trees += 1
        
        x_pos = (x_pos + slope_step) % slope_size

    return trees

def part_2(slope_step):
    with open('day3/input', 'r') as f:
        hill = [line.strip() for line in f.readlines()]

    x_pos = 0
    slope_size = len(hill[0])
    trees = 0
    for i, level in enumerate(hill):
        if i % 2 == 1:
            continue
        if level[x_pos] == '#':
            trees += 1
        
        x_pos = (x_pos + slope_step) % slope_size

    return trees
        


if __name__ == "__main__":
    total = 1
    for step in [1,3,5,7]:
        total *= part_1(step)

    print(total * part_2(1))