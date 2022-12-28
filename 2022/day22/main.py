# Extract data.
correct = ['.', '<', '>', '^', 'v', 'x']
def load():
    board = []
    instructions = ""
    with open("input.txt", "r") as file:
        isBoard = True
        best_len = 0
        for row in file:
            row = row.replace('\n', '')
            if row == "": isBoard = False
            if isBoard:
                board.append(list(row))
                best_len = max(best_len, len(row))
            else:
                instructions = row
        
        for i in range(len(board)):
            board[i] = list(''.join(board[i]).ljust(best_len, ' '))
    return board, instructions

board, instructions = load()

def findPointOnLineStart(i):
    for j in range(len(board[i])):
        if board[i][j] in correct:
            return j
        elif board[i][j] == "#": return None

def findPointOnLineEnd(i):
    for j in range(len(board[i])-1, -1, -1):
        if board[i][j] in correct: return j
        elif board[i][j] == "#": return None
        

def findPointOnColumnStart(j):
    for i, row in enumerate(board):
        if row[j] in correct:
            return i
        elif row[j] == "#": return None

def findPointOnColumnEnd(j):
    for i, row in enumerate(board[::-1]):
        if row[j] in correct:
            return len(board) - i - 1
        elif row[j] == "#": return None
        

def getFacing(facing):
    if facing == 0: return '>'
    if facing == 1: return 'v'
    if facing == 2: return '<'
    return '^'

# Part 1.
i, j = 0, findPointOnLineStart(0)
board[i][j] = 'x'
index = 0
facing = 0
while index < len(instructions):
    # Get instructions for forward.
    last_index = index
    while index <= len(instructions)-1 and instructions[index].isnumeric(): index += 1
    forward = int(instructions[last_index:index])

    # Lets go.
    isRunning = True
    while forward > 0:
        if facing == 0 and isRunning:
            nj = j + 1

            if nj >= len(board[i]) or board[i][nj] == " ": 
                nj = findPointOnLineStart(i)
                if nj == None: 
                    isRunning = False
                    continue

            if board[i][nj] in correct:
                board[i][j] = getFacing(facing)
                j = nj
            else: isRunning = False

        elif facing == 2 and isRunning:
            nj = j - 1
            if nj == -1 or board[i][nj] == " ":
                nj = findPointOnLineEnd(i)
                if nj == None: 
                    isRunning = False
                    continue

            if board[i][nj] in correct: 
                board[i][j] = getFacing(facing)
                j = nj
            else: isRunning = False
        
        elif facing == 1 and isRunning:
            ni = i + 1
            if ni >= len(board) or board[ni][j] == " ":
                ni = findPointOnColumnStart(j)
                if ni == None:
                    isRunning = False
                    continue

            if board[ni][j] in correct: 
                board[i][j] = getFacing(facing)
                i = ni
            else: isRunning = False

        elif facing == 3 and isRunning:
            ni = i - 1
            if ni == -1 or board[ni][j] == " ":
                ni = findPointOnColumnEnd(j)
                if ni == None: 
                    isRunning = False
                    continue

            if board[ni][j] in correct:
                board[i][j] = getFacing(facing)
                i = ni
            else: isRunning = False
        
        forward -= 1

    # Get the turn instructions.
    if index < len(instructions):
        facing = (facing + 1) % 4 if instructions[index] == "R" else (facing - 1) % 4
        index += 1
board[i][j] = getFacing(facing)

print("Part 1:", (i+1) * 1000 + (j+1) * 4 + facing)

# Part 2.
'''
      |  G  |  D  |
      |F 2  |  1 B|     
      |     |  A  |
      -------------
      |     |      
      |E 3 A|
      |     |
-------------
|  E  |     |
|F 5  |  4 B| 
|     |  C  |
-------------
|     |
|G 6 C|
|  D  |
-------
'''

def getBorderFromCube(i, j, facing):

    # A Border.
    if i == 49 and j >= 100 and j < 150 and facing == 1: return (j - 50, 99, 2) if board[j - 50][99] in correct else (None, None, None)
    if j == 99 and i >= 50 and i < 100 and facing == 0: return (49, 50 + i , 3) if board[49][50 + i] in correct else (None, None, None)

    # B Border.
    if j == 149 and i >= 0 and i < 50 and facing == 0:  return (149 - i, 99, 2) if board[149 - i][99] in correct else (None, None, None)
    if j == 99 and i >= 100 and i < 150 and facing == 0:  return (149 - i, 149, 2) if board[149 - i][149] in correct else (None, None, None)
    
    # C Border.
    if i == 149 and j >= 50 and j < 100 and facing == 1:  return (j + 100, 49, 2) if board[j + 100][49] in correct else (None, None, None)
    if j == 49 and i >= 150 and i < 200 and facing == 0:  return (149, i - 100, 3) if board[149][i - 100] in correct else (None, None, None)

    # D Border.
    if i == 0 and j >= 100 and j < 150 and facing == 3:  return (199, j - 100, 3) if board[199][j - 100] in correct else (None, None, None)
    if i == 199 and j >= 0 and j < 50 and facing == 1:  return (0, j + 100, 1) if board[0][j + 100] in correct else (None, None, None)

    # E Border.
    if j == 50 and i >= 50 and i < 100 and facing == 2:  return (100, i - 50, 1) if board[100][i - 50] in correct else (None, None, None)
    if i == 100 and j >= 0 and j < 50 and facing == 3:  return (j + 50, 50, 0) if board[j + 50][50] in correct else (None, None, None)

    # F Border.
    if j == 50 and i >= 0 and i < 50 and facing == 2:  return (149 - i, 0, 0) if board[149 - i][0] in correct else (None, None, None)
    if j == 0 and i >= 100 and i < 150 and facing == 2:  return (149 - i, 50, 0) if board[149 - i][50] in correct else (None, None, None)

    # G Border.
    if i == 0 and j >= 50 and j < 100 and facing == 3:  return (j + 100, 0, 0) if board[j + 100][0] in correct else (None, None, None)
    if j == 0 and i >= 150 and i < 200 and facing == 2: return (0, i - 100, 1) if board[0][i - 100] in correct else (None, None, None)



board, instructions = load()
i, j = 0, findPointOnLineStart(0)
board[i][j] = 'x'
index = 0
facing = 0
while index < len(instructions):
    # Get instructions for forward.
    last_index = index
    while index <= len(instructions)-1 and instructions[index].isnumeric(): index += 1
    forward = int(instructions[last_index:index])

    # Lets go.
    isRunning = True
    while forward > 0 and isRunning:
        ni, nj, nfacing = i, j, facing
        if facing == 0: nj += 1
        elif facing == 1: ni += 1
        elif facing == 2: nj -= 1
        else: ni -= 1

        if nj >= len(board[i]) or ni >= len(board) or ni < 0 or nj < 0 or board[ni][nj] == " ": 
            ni, nj, nfacing = getBorderFromCube(i, j, facing)
            if nj == None: 
                isRunning = False
                continue

        if board[ni][nj] in correct:
            board[i][j] = getFacing(facing)
            i, j, facing = ni, nj, nfacing

        else: isRunning = False
        
        forward -= 1

    # Get the turn instructions.
    if index < len(instructions):
        facing = (facing + 1) % 4 if instructions[index] == "R" else (facing - 1) % 4
        index += 1

board[i][j] = getFacing(facing)
board[i][j] = 'x'

print("Part 2:", (i+1) * 1000 + (j+1) * 4 + facing)