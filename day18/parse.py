
def get_input():
    with open('day18/input') as f:
        return [line.strip() for line in f.readlines()]

def tokenize_expr(expr):
    paren_stack = []
    split_points = []
    for i, char in enumerate(expr):
        if char == ' ' and not paren_stack:
            split_points.append(i)
        
        if char == '(':
            paren_stack.append('(')
        elif char == ')':
            paren_stack.pop()
    
    # Split
    split_points.append(len(expr))
    start = 0
    tokens = []
    for endpoint in split_points:
        tokens.append(expr[start:endpoint])
        start = endpoint + 1

    if len(tokens) == 1 and  expr[0] == '(' and expr[-1] == ')':
        return tokenize_expr(expr[1:-1])
    return tokens

def eval_expr(expr):
    if isinstance(expr, str):
        sub_exprs = tokenize_expr(expr)
    else:
        sub_exprs = expr

    if sub_exprs[-1].isnumeric():
        rhs = int(sub_exprs[-1])
    else:
        rhs = eval_expr(sub_exprs[-1])

    if len(sub_exprs) == 1:
        return rhs
    
    if sub_exprs[-2] == '*':
        result = rhs * eval_expr(sub_exprs[:-2])
        return result
    elif sub_exprs[-2] == '+':
        result = rhs + eval_expr(sub_exprs[:-2])
        return result
    else:
        raise Exception('Unknown operator')

def eval_expr_am(expr):
    if expr.isnumeric():
        return int(expr)

    sub_exprs = tokenize_expr(expr)

    # Evaluate all sub expresion
    for i in range(0, len(sub_exprs), 2):
        sub_exprs[i] = eval_expr_am(sub_exprs[i])

    # Evaluate addition
    for i in range(1, len(sub_exprs), 2):
        if sub_exprs[i] == '+':
            sub_exprs[i + 1] = sub_exprs[i - 1] + sub_exprs[i + 1]
            sub_exprs[i] = None
            sub_exprs[i - 1] = None
    sub_exprs = [tok for tok in sub_exprs if tok is not None]

    # Evaluate Multiplication
    for i in range(1, len(sub_exprs), 2):
        if sub_exprs[i] == '*':
            sub_exprs[i + 1] = sub_exprs[i - 1] * sub_exprs[i + 1]
            sub_exprs[i] = None
            sub_exprs[i - 1] = None

    return sub_exprs[-1]
    

def part_1():
    values = [eval_expr(line) for line in get_input()]
    return sum(values)

def part_2():
    values = [eval_expr_am(line) for line in get_input()]
    return sum(values)
if __name__ == "__main__":
    print(part_1())
    print(part_2())