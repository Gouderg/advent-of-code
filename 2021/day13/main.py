def init(x, y):
    return [['.' for _ in range(0, x)] for _ in range(0, y)]

def dot_on_board(board):
    count = 0
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == '#':
                count += 1
    return count

# Extract data.
data = []
instructions = []
isOkey = False
with open('input.txt', 'r') as file:
    for row in file:
        if row == "\n":
            isOkey = True
        elif not(isOkey):
            row = [int(a) for a in row.replace('\n', '').split(',')]
            data.append(row)
        elif isOkey:
            instructions.append(row.replace('\n', ''))


# Part 1.
# Load all point.
x, y = 1500, 1500
board = init(x, y)
for elt in data:
    board[elt[1]][elt[0]] = '#'

isOkey = True
# Execute first fold.
for inst in instructions:
    inst = inst.split(' ')[2].split('=')
    
    # Add line to split.
    if inst[0] == 'y':
        y = int(inst[1])
        for i in range(0, len(board[0])):
            board[int(inst[1])][i] = '_'
    elif inst[0] == 'x':
        x = int(inst[1])
        for i in range(0, len(board)):
            board[i][int(inst[1])] = '|'

    # Split and overlapping dot.
    if inst[0] == 'y':
        newBoard = init(x, y)
        for i in range(0, y):
            for j in range(0, x):
                newBoard[i][j] = board[i][j]
                if newBoard[i][j] == '.':
                    newBoard[i][j] = board[(y*2) - i][j]
        board = newBoard.copy()
    
    # Split and overlapping dot.
    if inst[0] == 'x':
        newBoard = init(x, y)
        for i in range(0, y):
            for j in range(0, x):
                newBoard[i][j] = board[i][j]
                if newBoard[i][j] == '.':
                    newBoard[i][j] = board[i][(x*2) - j]
        board = newBoard.copy()

    if isOkey:
        print('Part 1:', dot_on_board(board))
    isOkey = False





# Part 2.
print('Part 2:')
[print(''.join(row)) for row in board]