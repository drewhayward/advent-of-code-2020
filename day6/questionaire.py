
def get_group_answers():
    answers = []
    with open('day6/input', 'r') as f:
        group_answers = set()
        for line in f.readlines():
            line = line.strip()
            if line:
                for char in line:
                    group_answers.add(char)
            else:
                answers.append(group_answers)
                group_answers = set()
        if group_answers:
            answers.append(group_answers)
    return answers


def part_1():
    return sum(len(group) for group in get_group_answers())

def part_2():
    answers = []
    with open('day6/input', 'r') as f:
        group_answers = set(chr(i) for i in range(97, 97+26, 1))
        for line in f.readlines():
            line = line.strip()
            if line:
                individual_answer = set(char for char in line)
                group_answers.intersection_update(individual_answer)
            else:
                answers.append(group_answers)
                group_answers = set(chr(i) for i in range(97, 97+26, 1))
        if group_answers:
            answers.append(group_answers)
    return sum([len(group) for group in answers])


if __name__ == "__main__":
    print(part_1())
    print(part_2())