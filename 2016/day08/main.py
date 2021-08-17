
# Extract data.
data = []
with open('input.txt', 'r') as file:
    for row in file:
        data.append(row.replace('\n', ''))

# Part 1.
count = 0
for row in data:
    if 'rect' in row:
        row = row.replace('x', ' ').split(' ')
        count += int(row[1]) * int(row[2])

print('Part 1:', count)

# Part 2.
WIDTH, HEIGHT = 50, 6

# board = [['.'] * 50 for i in range(6)]
board = [[' '] * WIDTH for i in range(HEIGHT)]

for row in data:
    if 'rect' in row:
        row = row.replace('x', ' ').split(' ')
        for i in range(0,int(row[2])):
            for j in range(0, int(row[1])):
                board[i][j] = '#'
        
    elif 'row' in row:
        row = row.replace('=', ' ').split(' ')
        temp = []
        for i in range(0, WIDTH):
            temp.append(board[int(row[3])][i])
        
        for i in range(0, WIDTH):
            board[int(row[3])][(i + int(row[5])) % WIDTH] = temp[i]

    elif 'column' in row:
        row = row.replace('=', ' ').split(' ')
        temp = []
        for i in range(0,HEIGHT):
            temp.append(board[i][int(row[3])])
        
        for i in range(0,HEIGHT):
            board[(i + int(row[5])) % HEIGHT][int(row[3])] = temp[i]

print('Part 2: RURUCEOEIL')       
[print(a) for a in board]
print()
