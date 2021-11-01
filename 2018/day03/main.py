

def initBoard(size):
    return [list('.' * size) for i in range(size)]

def countX(board):
    count = 0
    for row in board:
        count += row.count('X')
    return count

def apply(ids, s_w, s_h, width, height, board):

    for i in range(s_w, s_w+width):
        for j in range(s_h, s_h+height):
            if board[j][i] == '.':
                board[j][i] = ids
            else:
                board[j][i] = 'X'

    return board

def verif(ids, s_w, s_h, width, height, board):
    for i in range(s_w, s_w+width):
        for j in range(s_h, s_h+height):
            if board[j][i] != ids:
                return 1
    return ids
# Extract data.
data = []
with open("input.txt", "r") as file:
    for row in file:
        data.append(row.replace('\n', '').replace(':', '').split(' '))


# Part 1.
board = initBoard(1000)
for row in data:
    a = row[2].split(',')
    b = row[3].split('x')
    board = apply(row[0], int(a[0]), int(a[1]), int(b[0]), int(b[1]), board)

print("Part 1:", countX(board))

# Part 2.
for row in data:
    a = row[2].split(',')
    b = row[3].split('x')
    isOkey = verif(row[0], int(a[0]), int(a[1]), int(b[0]), int(b[1]), board)
    if isOkey != 1:
        break
print("Part 2:", isOkey)