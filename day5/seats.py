import math

def get_codes():
    with open('day5/input', 'r') as f:
        return [line.strip() for line in f.readlines()]

def high_low(chars, size, low_char, high_char):
    space = [0,size-1]
    for char in chars:
        middle = (space[1]+space[0])/2
        if char == high_char:
           space[0] = math.ceil(middle)
        elif char == low_char:
            space[1] = math.floor(middle)
        else:
            raise Exception('Character doesn\'t match low or high char')

    return space[0]

def decode(seat: str):
    rows = seat[:-3]
    columns = seat[-3:]

    return high_low(rows, 128, 'F', 'B'), high_low(columns, 8, 'L', 'R')

def part_1():
    
    best = 0
    for code in get_codes():
        row, column = decode(code)
        seat_id = row*8 + column
        if seat_id > best:
            best = seat_id
    return best


def part_2():
    NUM_SEATS = 128 * 8
    seats = set()
    for code in get_codes():
        row, column = decode(code)
        seat_id = row*8 + column
        seats.add(seat_id)
    
    for i in range(1, NUM_SEATS - 1):
        if (i - 1) in seats and i not in seats and (i + 1) in seats:
            return i

if __name__ == "__main__":
    print(part_1())
    print(part_2())