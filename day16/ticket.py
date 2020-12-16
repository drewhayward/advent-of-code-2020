import re
from tqdm import tqdm

def get_input():
    fields = {}
    with open('day16/input') as f:
        line = f.readline().strip()
        while line:
            match = re.match('([\w ]+): ([\d\-]+) or ([\d\-]+)', line)
            ranges = []
            field_key = match.groups()[0]
            for group in match.groups()[1:]:
                start, end = group.split('-')
                ranges.append((int(start), int(end)))
                fields[field_key] = ranges
            line = f.readline().strip()
        
        # Your ticket
        _ = f.readline()
        my_ticket = [int(num) for num in f.readline().strip().split(',')]
        f.readline()

        # nearby tickets
        f.readline()
        line = f.readline().strip()
        nearby_tickets = []
        while line:
            nearby_tickets.append([int(num) for num in line.split(',')])
            line = f.readline().strip()

        return fields, my_ticket, nearby_tickets


def part_1():
    fields, _, nearby_tickets = get_input()

    # Reduce fields
    ranges = [r for field in fields.values() for r in field]

    total = 0
    invalid_tickets = set()
    for i, ticket in enumerate(nearby_tickets):
        for num in ticket:
            valid = False
            for r in ranges:
                for r in ranges:
                    if r[0] <= num <= r[1]:
                        valid = True
                        break
            if not valid:
                invalid_tickets.add(i)
                total += num
    return total, invalid_tickets

def part_2():
    fields, my_ticket, nearby_tickets = get_input()

    _, invalid_tickets = part_1()

    # filter invalid tickets
    nearby_tickets = [ticket for i, ticket in enumerate(nearby_tickets) if i not in invalid_tickets]

    # Find possible placements for all fields
    field_assignment = [set() for _ in range(len(fields))]
    for fieldname, ranges in fields.items():
        # try every unclaimed field until it works
        for field_id, field_value in enumerate(field_assignment):
            # if field_value is not None:
            #     continue
            valid_column = True
            for ticket in nearby_tickets:
                valid_num = False
                for r in ranges:
                    if (r[0] <= ticket[field_id] <= r[1]):
                        valid_num = True
                        break
                
                # if a single number is invalid, this cannot be the column
                if not valid_num:
                    valid_column = False
                    break
            if valid_column:
                field_assignment[field_id].add(fieldname)

    # Sudoku the possibilities
    placed = set()
    while len([a for a in field_assignment if len(a) > 1]):
        for i in range(len(field_assignment)):
            placed = set(item for j, items in enumerate(field_assignment) for item in items if j != i and len(items) == 1)
            field_assignment[i].difference_update(placed)

    field_assignment = [list(a)[0] for a in field_assignment]

    total = 1
    for field_idx, fieldname in enumerate(field_assignment):
        if fieldname.startswith('departure'):
            total *= my_ticket[field_idx]

    return total

if __name__ == "__main__":
    print(part_1()[0])
    print(part_2())