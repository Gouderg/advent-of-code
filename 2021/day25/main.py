

def step(board, old_board):
    lock = {}
    for i in range(len(board)-1, -1, -1):
        for j in range(len(board[0]) -1, -1, -1):

            # print(board[i][j], board[(i+1)%len(board)][j], board[i][(j+1)%len(board[0])])
            # return board

            if board[i][j] == 'v' and board[(i+1)%len(board)][j] == '.' and old_board[(i+1)%len(board)][j] != 'v' and (i, j) not in lock:
                lock[(i,j)] = 1
                lock[((i+1)%len(board),j)] = 1

                board[(i+1)%len(board)][j] = 'v'
                board[i][j] = '.'

            elif board[i][j] == '>' and board[i][(j+1)%len(board[0])] == '.' and old_board[i][(j+1)%len(board[0])] != '>' and (i, j) not in lock: 
                lock[(i,j)] = 1
                lock[(i,(j+1)%len(board[0]))] = 1

                board[i][j] = '.'
                board[i][(j+1)%len(board[0])] = '>'

    return board

def compare(board, old_board):
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j] != old_board[i][j]:
                return False

    return True

def copy(board):
    new_board = []
    for elt in board:
        temp = []
        for a in elt:
            temp.append(a)
        new_board.append(temp)
    return new_board


# Extract data.
board = []
with open('input2.txt', 'r') as file:
    for row in file:
        board.append(list(row.replace('\n', '')))


# Part 1.
step_counter = 0

while True:
    step_counter += 1
    old_board = copy(board)

    # [print(row) for row in board]
    # print()
    board = step(board, old_board)
    [print(''.join(row)) for row in old_board]
    print()
    [print(''.join(row)) for row in board]


    if compare(board, old_board):
        break
    break
    # print(step_counter)


print("Part 1:", step_counter)

