def apply(data, board, size):
    for i in range(0, size):
        for j in range(0, size):
            if (i,j) not in data:
                nb, mins, ids = -1, 1000, 0
                for k,pos in enumerate(data):
                    temp = manhattan((i,j), pos)
                    if temp < mins:
                        nb = 0
                        mins, ids = temp, k
                    elif temp == mins:
                        nb += 1
                if nb >= 2:
                    board[j][i] = '.'
                elif nb == 0:
                    board[j][i] = str(ids)
    return board

def apply2(data, board, size, limit):
    for i in range(0, size):
        for j in range(0, size):
            # if (i,j) not in data:
            somme = 0
            for k,pos in enumerate(data):
                somme += manhattan((i,j), pos)
            if somme < limit:
                board[j][i] = '#'
    return board

def manhattan(x1, x2):
    return abs(x2[0] - x1[0]) + abs(x2[1] - x1[1])

def initBoard(size):
    return [list('.' * size) for i in range(size)]

# Extract data.
data = []
with open("input.txt", "r") as file:
    for row in file:
        row = row.replace('\n', '').split(', ')
        data.append((int(row[0]), int(row[1])))

# Part 1.
size = 400
board, board2 = initBoard(size), initBoard(size+2)
i = 0
newData = []
for pos in data:
    board[pos[1]][pos[0]] = str(i)
    board2[pos[1]+1][pos[0]+1] = str(i)
    newData.append((pos[0]+1, pos[1]+1))
    i += 1

board = apply(data, board, size)
board2 = apply(newData, board2, size+2)

count = []
for i in range(0, len(data)):
    # Count board 1
    count1, count2 = 0, 0
    for j in range(0, len(board[0])):
        count1 += board[j].count(str(i))

    for j in range(0, len(board2[0])):
        count2 += board2[j].count(str(i))
    
    if count1 == count2:
        count.append(count1)

print("Part 1:", max(count))

# Part 2.
board = initBoard(size)
i = 0
for pos in data:
    board[pos[1]][pos[0]] = str(i)
    i += 1

board = apply2(data, board, size, 10000)

count = 0
for elt in board:
    count += elt.count('#')

print("Part 2:", count)
