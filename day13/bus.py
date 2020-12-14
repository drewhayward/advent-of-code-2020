
def get_input():
    with open('day13/input') as f:
        start = int(f.readline())
        buses = [int(num) for num in f.readline().split(',') if num != 'x']
    return start, buses

def get_input_2():
    with open('day13/input') as f:
        start = int(f.readline())
        buses = [int(num) if num != 'x' else num for num in f.readline().split(',')]
    return buses

def part_1(start, buses):
    time = start
    while True:
        for bus in buses:
            if time % bus == 0:
                return (time - start) * bus
        time += 1

def part_2(buses):
    time = buses[0]
    while True:
        found = True
        for i, bus in enumerate(buses):
            if bus == 'x':
                continue
            if (time + i) % bus != 0:
                found = False
                break
            
        if not found:
            time += buses[0]
            continue
        else:
            print('answer:', time)
            for i, bus in enumerate(buses):
                if bus == 'x':
                    continue
                print(f'{bus}:{(time + i) % bus}')
        
        return time

        

if __name__ == "__main__":

    start, buses = get_input()
    print(part_1(start, buses))

    buses = get_input_2()
    print(part_2(buses))