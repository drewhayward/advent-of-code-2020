

def get_instructions():
    instructions = []
    with open('day8/input') as f:
        for line in f.readlines():
            line = line.strip()
            command, num = line.split(' ')
            instructions.append([command, int(num)])

        return instructions

def find_loop(instructions):
    pc = 0
    acc = 0
    num_runs = [0] * len(instructions)
    while all(num < 2 for num in num_runs):
        if pc >= len(instructions):
            return acc, False
        if num_runs[pc] == 1:
            return acc, True
        num_runs[pc] += 1
        command = instructions[pc][0]
        value = instructions[pc][1]
        if command == 'nop':
            pc += 1
        elif command == 'jmp':
            pc += value
        elif command == 'acc':
            acc += value
            pc += 1

def fix_program():
    instructions = get_instructions()

    for i, instruction in enumerate(instructions):
        op, num = instruction
        instructions_copy = [inst[:] for inst in instructions]
        if op == 'jmp':
            instructions_copy[i][0] = 'nop'
        elif op == 'nop':
            instructions_copy[i][0] = 'jmp'
        else:
            continue

        acc, infinite = find_loop(instructions_copy)
        if not infinite:
            return acc, i


if __name__ == "__main__":
    print(find_loop(get_instructions()))
    print(fix_program())