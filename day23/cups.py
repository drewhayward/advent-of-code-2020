from tqdm import trange

def find(xs, x):
    try:
        return xs.index(x)
    except ValueError:
        return -1


def move(cups, current_cup):
    #print(f"cups: {' '.join([f'({cup})' if cup == current_cup else str(cup) for cup in cups])}")

    max_value = max(cups)
    list_len =len(cups)
    curr_idx = cups.index(current_cup)
    group = cups[curr_idx + 1:curr_idx + 4]
    if len(group) < 3:
        group.extend(cups[:(curr_idx + 3) % 4])

    cups = cups[:curr_idx+1] + cups[curr_idx + 4:]
    if len(cups) > (list_len - 3):
        cups = cups[(curr_idx + 3) % 4:]

    #print(f"pick up: {', '.join([str(g) for g in group])}")

    target = (((current_cup - 1) - 1) % max_value) + 1
    idx = find(cups, target)
    while idx == -1:
        target = (((target - 1) - 1) % max_value) + 1
        idx = find(cups, target)

    #print(f"destination: {target}")

    cups = cups[:idx+1] + group + cups[idx+1:]

    curr_idx = (cups.index(current_cup) + 1) % len(cups)
    current_cup = cups[curr_idx]
    return cups, current_cup

def part_1():
    cups = [int(char) for char in '586439172']
    current_cup = cups[0]

    for i in range(100):
        #print(f'-- move {i+1} --')
        cups, current_cup = move(cups, current_cup)
        #print()

    start = cups.index(1) + 1
    return ''.join(str(cup) for cup in cups[start:] + cups[:start])

def part_2():
    cups = [int(char) for char in '586439172']

    # Extend cups
    max_cup = max(cups)
    cups.extend(range(max_cup + 1, 1000001))

    current_cup = cups[0]

    for i in trange(1000000):
    
        #print(f'-- move {i+1} --')
        cups, current_cup = move(cups, current_cup)
        #print()

    
    inx = cups.index(current_cup)
    return cups[idx + 1] * cups[idx + 2]

if __name__ == "__main__":
    print(part_1())
    print(part_2())