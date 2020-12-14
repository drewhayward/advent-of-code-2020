import re

def get_input():
    with open('day14/input') as f:
        lines = [line.strip() for line in f.readlines()]

    return lines

def mask_num(num, mask):
    result = ""
    for num_bit, mask_bit in zip(num, mask):
        if mask_bit == "X":
            result += num_bit
        else:
            result += mask_bit
    return int(result, base=2)

def num_to_bin(num: int):
    return bin(num)[2:].zfill(36)

def starting_value(lines):
    memory = {}
    mask = None
    for line in lines:
        if line.startswith('mask'):
            mask = line.split(' ')[-1]
        else:

            _, addr, value = [item for item in re.split('[ ,\[\]=]', line) if item]
            addr = int(addr)
            value = int(value)
            memory[addr] = mask_num(num_to_bin(value), mask)

    return sum(v for _, v in memory.items())

def generate_addresses(addr, mask):
    prefix = ''
    for addr_bit, mask_bit in zip(addr, mask):
        if mask_bit == 'X':
            suffixes = generate_addresses(addr[(len(prefix) + 1):], mask[(len(prefix) + 1):])
            return [prefix + '0' + suffix for suffix in suffixes] + [prefix + '1' + suffix for suffix in suffixes]
        else:
            if mask_bit == '1':
                prefix += '1'
            else:
                prefix += addr_bit

    return [prefix]

def version2(lines):
    memory = {}
    mask = None
    for line in lines:
        if line.startswith('mask'):
            mask = line.split(' ')[-1]
        else:
            _, addr, value = [item for item in re.split('[ ,\[\]=]', line) if item]
            addr = int(addr)
            value = int(value)

            for address in generate_addresses(num_to_bin(addr), mask):
                memory[address] = value

    return sum(v for _, v in memory.items())

if __name__ == "__main__":
    print(starting_value(get_input()))
    print(version2(get_input()))