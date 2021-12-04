
def checkCol(board):
    for i in range(0, len(board[0])):
        if board[0][i] == -1 and board[1][i] == -1 and board[2][i] == -1 and board[3][i] == -1 and board[4][i] == -1:
            return True
    return False 

def checkLign(board):
    for i in range(0, len(board)):
        if board[i][0] == -1 and board[i][1] == -1 and board[i][2] == -1 and board[i][3] == -1 and board[i][4] == -1:
            return True
    return False

def unmarked(board):
    somme = 0
    for elt in board:
        for l in elt:
            if l != -1:
                somme += l
    return somme

def part1(boards, index):
    isWin = False
    count = 0
    while not(isWin):
        bingo = instructions[index]

        # Change value
        for board in boards:
            for i in range(0, len(boards[board])):
                if bingo in boards[board][i]:
                    boards[board][i][boards[board][i].index(bingo)] = -1
        
        # Verify
        for board in boards:
            a = checkCol(boards[board])
            b = checkLign(boards[board])
            if a or b:
                isWin = True
                return unmarked(boards[board]) * bingo
        
        index += 1

    return count

# Extract data.
instructions, boards = [], {}
isOkey, index = True, -1
with open('input.txt', 'r') as file:
    for row in file:
        if isOkey:
            row = row.replace('\n', '').split(',')
            instructions = [int(a) for a in row]
            isOkey = False
        elif row == '\n':
            index += 1
        else:
            if index not in boards:
                boards[index] = []

            row = row.replace('  ', ' ').replace('\n', '').split(' ')

            if row[0] == '':
                row.pop(0)
            boards[index].append([int(a) for a in row])

# Part 1.
boards2 = boards.copy()
print('Part 1:', part1(boards, 0))


# Part 2.
index = 0
while len(boards2) > 1:
    bingo = instructions[index]

    # Change value.
    for board in boards2:
        for i in range(0, len(boards2[board])):
            if bingo in boards2[board][i]:
                boards2[board][i][boards2[board][i].index(bingo)] = -1
    
    # Verify.
    topop = []
    for board in boards2:
        a = checkCol(boards2[board])
        b = checkLign(boards2[board])
        if a or b:
            topop.append(board)

    # On supprime les cles gagnantes.    
    [boards2.pop(elt) for elt in topop]

    index += 1

print('Part 2:', part1(boards2, index))