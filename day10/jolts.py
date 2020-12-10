
def get_input():
    with open('day10/input','r') as f:
        return [int(line.strip()) for line in f.readlines()]

def part_1():
    numbers = get_input()
    numbers.sort()
    
    current_joltage = 0
    diffs = [0, 0, 0]
    for num in numbers:
        diff = num - current_joltage

        diffs[diff - 1] += 1
        current_joltage = num
        assert(diff <= 3)

    return diffs[0]* (diffs[2] + 1)

def part_2():
    """
    Dynamic programming solution
    """
    numbers = get_input()
    numbers.sort()

    num_paths = [0] * (len(numbers) + 1)

    num_paths[0] = 1
    for i in range(1, len(num_paths)):
        num_id = i - 1
        for j in range(1, 4):
            diff = (numbers[num_id] - numbers[num_id - j])
            if i - j >= 0 and diff <= 3:
                num_paths[i] += num_paths[i - j]

    return num_paths[-1]

if __name__ == "__main__":
    print(part_1())
    print(part_2())