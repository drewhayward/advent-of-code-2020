
def get_bag_dict():
    bag_dict = {}
    with open('day7/input', 'r') as f:
        for line in f.readlines():
            line = line.strip().split(' ')
            key_bag = ' '.join(line[:3])[:-1]
            bag_dict[key_bag] = []

            contents = line[4:]
            if contents[0] == 'no':
                continue
            while contents:
                bag_dict[key_bag].append(
                    (int(contents[0]),
                    ' '.join(word.rstrip('.,s') for word in contents[1:4])
                    ))
                contents = contents[4:]
                

    return bag_dict

def part_1(target='shiny gold bag'):
    bag_dict = get_bag_dict()

    contains_shiny = set()
    num_shiny = -1
    while len(contains_shiny) != num_shiny:
        num_shiny = len(contains_shiny)
        for outer_bag, productions in bag_dict.items():
            for _, inner_bag in productions:
                if inner_bag == target:
                    contains_shiny.add(outer_bag)
                elif inner_bag in contains_shiny:
                    contains_shiny.add(outer_bag)
    
    return len(contains_shiny)

def part_2(target='shiny gold bag'):
    bag_dict = get_bag_dict()

    def count(target):
        if not bag_dict[target]:
            return 0
        else:
            return sum([ num * (1 + count(inner_bag)) for num, inner_bag in bag_dict[target]])

    return count(target)



if __name__ == "__main__":
    print(part_1())
    print(part_2())