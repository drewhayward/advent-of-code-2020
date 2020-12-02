
def part_1():
    valid = 0
    with open('day2/input', 'r') as f:
        for line in f.readlines():
            minmax, letter, password = line.strip().split(' ')
            minmax = (int(minmax.split('-')[0]), int(minmax.split('-')[1]))
            letter = letter[0]

            count = sum(1 for char in password if char == letter)

            if minmax[0] <= count <= minmax[1]:
                valid += 1

        
    print(valid)

def part_2():
    valid = 0
    with open('day2/input', 'r') as f:
        for line in f.readlines():
            minmax, letter, password = line.strip().split(' ')
            minmax = (int(minmax.split('-')[0]), int(minmax.split('-')[1]))
            letter = letter[0]

            if (password[minmax[0] - 1] == letter) != (password[minmax[1] - 1] == letter):
                valid += 1

        
    print(valid)

if __name__ == "__main__":
    part_1()
    part_2()