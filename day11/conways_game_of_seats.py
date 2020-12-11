from copy import deepcopy

def get_initial_state():
    state = []
    with open('day11/input') as f:
        for line in f.readlines():
            line = line.strip()
            state.append([char for char in line])
    return state

def num_occupied(board, i, j):
    num_occupied = 0
    for x_step in [-1, 0, 1]:
        for y_step in [-1, 0, 1]:
            is_inbounds = (0 <= i + x_step < len(board)) and  (0 <= j + y_step < len(board[i]))
            if (not (x_step == 0 and y_step == 0)) and is_inbounds and board[i + x_step][j + y_step] == '#':
                num_occupied += 1
    return num_occupied

def num_line_occupied(board, i, j):
    num_occupied = 0
    for x_step in [-1, 0, 1]:
        for y_step in [-1, 0, 1]:
            if x_step == 0 and y_step == 0:
                continue
            offset_x, offset_y = i + x_step, j + y_step
            # While the offset point is in bounds
            while (0 <= offset_x < len(board)) and  (0 <= offset_y < len(board[i])):
                if board[offset_x][offset_y] != '.':
                    if board[offset_x][offset_y] == '#':
                        num_occupied += 1
                    break
                else:
                    offset_x += x_step
                    offset_y += y_step
    return num_occupied

def step_cell(board, i, j):
    num_occ = num_occupied(board, i, j)

    if board[i][j] == "L" and num_occ == 0:
        return "#", True
    elif board[i][j] == "#" and num_occ >= 4:
        return "L", True
    else:
        return board[i][j], False

def step_cell_line(board, i, j):
    num_occ = num_line_occupied(board, i, j)

    if board[i][j] == "L" and num_occ == 0:
        return "#", True
    elif board[i][j] == "#" and num_occ >= 5:
        return "L", True
    else:
        return board[i][j], False

def print_board(board):
    print(''.join(['-'] * len(board[0])))
    for line in board:
        print(''.join(line))
    print(''.join(['-'] * len(board[0])))

def step_board(board, step_fn):
    updated = False
    newboard = deepcopy(board)

    for i in range(len(board)):
        for j in range(len(board[i])):
            newboard[i][j], cell_update = step_fn(board, i, j)
            updated = updated or cell_update

    return newboard, updated

def converge_board(board, step_fn=step_cell):
    updated = True
    while updated:
        #print_board(board)
        board, updated = step_board(board, step_fn)

    return sum([row.count('#') for row in board])


if __name__ == "__main__":
    print(converge_board(get_initial_state()))
    print(converge_board(get_initial_state(), step_fn=step_cell_line))
