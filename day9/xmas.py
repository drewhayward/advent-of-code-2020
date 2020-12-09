
def get_input(size=25):
    with open('day9/input') as f:
        preamble = []
        numbers = []
        for line in f.readlines():
            line = line.strip()
            if len(preamble) < size:
                preamble.append(int(line))
            else:
                numbers.append(int(line))


        return preamble + numbers


def part_1():
    preamble_size = 25
    numbers = get_input()
    
    for i in range(preamble_size, len(numbers)):
        num = numbers[i]
        
        # is this number valid?
        valid = False
        for j in range(i - preamble_size, i):
            for k in range(i - preamble_size, i):
                if j == k:
                    continue

                if numbers[j] + numbers[k] == num:
                    valid = True
                    break
            if valid:
                break

        if not valid:
            return num

def part_2():
    target_sum = part_1()
    numbers = get_input()

    
    start = 0
    end = 2
    total = sum(numbers[start:end])
    while total != target_sum:
        if total < target_sum:
            end += 1
        elif total > target_sum:
            start += 1

        total = sum(numbers[start:end])
    
    return min(numbers[start:end]), max(numbers[start:end])

if __name__ == "__main__":
    print(part_1())
    print(part_2())