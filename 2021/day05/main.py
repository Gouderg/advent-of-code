def init(size):
    return [[0 for _ in range(0, size)] for _ in range(0, size)]

def overlap(board):
    count = 0
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] >= 2:
                count += 1
    return count

# Extract data.
instructions = []
with open('input.txt', 'r') as file:
    for row in file:
        row = row.replace('\n', '').split(' -> ')
        n1 = [int(a) for a in row[0].split(',')]
        n2 = [int(a) for a in row[1].split(',')]

        instructions.append((n1,n2))

size = 1000
board = init(size)

# Part 1.
for elt in instructions:
    x1 = elt[0][0]
    y1 = elt[0][1]

    x2 = elt[1][0]
    y2 = elt[1][1]


    if x1 == x2:
        if y1 < y2:
            for i in range(y1, y2+1):
                board[i][x1] += 1
        else:
            for i in range(y1, y2-1, -1):
                board[i][x1] += 1


    elif y1 == y2:
        if x1 < x2:
            for i in range(x1, x2+1):
                board[y1][i] += 1
        else:
            for i in range(x1, x2-1, -1):
                board[y1][i] += 1

    
print('Part 1:', overlap(board))


# Part 2.

for elt in instructions:
    x1 = elt[0][0]
    y1 = elt[0][1]

    x2 = elt[1][0]
    y2 = elt[1][1]

    if x1 != x2 and y1 != y2:
        while True:
            board[y1][x1] += 1
            if x1 == x2 and y1 == y2:
                break

            if x1 != x2:
                x1 = x1+1 if x1 < x2 else x1 - 1
            
            if y1 != y2:
                y1 = y1+1 if y1 < y2 else y1 - 1
            

print('Part 2:', overlap(board))