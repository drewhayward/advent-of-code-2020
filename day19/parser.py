from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor

def process_rules(rule_strings):
    rules = {}
    for rule_str in rule_strings:
        key, rule = rule_str.split(':')
        rule = rule.strip()
        if rule.startswith('"'):
            rules[int(key)] = rule.strip('"')
        else:
            rules[int(key)] = [[int(num) for num in prod.strip().split(' ')] for prod in rule.split('|')]

    return rules

def get_input():
    with open('day19/input2') as f:

        rule_strings = []

        line = f.readline().strip()
        while line:
            rule_strings.append(line)
            line = f.readline().strip()

        rules = process_rules(rule_strings)


        strings = []
        line = f.readline().strip()
        while line:
            strings.append(line)
            line = f.readline().strip()

    return rules, strings

def shift_reduce_parse(rules, string):
    stack = []
    buffer = [char for char in string]

    # Flip production rules
    bu_rules = {}
    for key, prods in rules.items():
        for prod in prods:
            prod_key = ','.join([str(num) for num in prod])
            if prod_key in bu_rules:
                print('hey')
            bu_rules[prod_key] = key
    

    while buffer:
        pass
        # look for reduce
        # shift

    # check if stack is accepting

def normalize_rules(rules):
    unchanged = False
    while not unchanged:
        unchanged = True
        for nonterm, prods in rules.items():
            if isinstance(prods, str):
                continue
            for i in range(len(prods)):
                if len(prods[i]) == 1 and not isinstance(prods[i], str):
                    unchanged = False
                    rules[nonterm] += rules[prods[i][0]]
                    del rules[nonterm][i]
    
    return rules

def cky_parse(rules, string, pbar):
    N = len(string)
    R = len(rules)
    p_table = [
        [
            [False for _ in range(R)]
            for _ in range(N)
        ]
        for _ in range(N)
    ]

    # Initialize the first "row" of the parser
    for s in range(N):
        for key, prods in rules.items():
            if isinstance(prods, str) and string[s] == prods:
                p_table[0][s][key] = True
                continue

            for prod in prods:
                if isinstance(prod, str) and string[s] == prod:
                    p_table[0][s][key] = True

            

    for length in range(2, N + 1):
        for start in range(N - length + 1):
            for p in range(1, length):
                for rule, prods in rules.items():
                    if isinstance(prods, str):
                        continue
                    for prod in prods:
                        if isinstance(prod, str):
                            continue
                        if p_table[p - 1][start][prod[0]] and p_table[length - p - 1][start + p][prod[1]]:
                            p_table[length - 1][start][rule] = True

    pbar.update(1)
    return p_table[-1][0][0]

def part_1():
    rules, strings = get_input()
    rules = normalize_rules(rules)

    
    total = 0
    with tqdm(total=len(strings)) as pbar:
        with ThreadPoolExecutor(5) as executor:
            def curried_parser(strings):
                return cky_parse(rules, strings, pbar=pbar)
            accepted = executor.map(curried_parser, strings)

    # accepted = []
    # for string in tqdm(strings):
    #     accepted.append(cky_parse(rules, string))

    # return False
    return sum([1 for accept in accepted if accept])


if __name__ == "__main__":
    print(part_1())