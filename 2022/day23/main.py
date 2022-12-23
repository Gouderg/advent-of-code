from math import inf
# Extract data.
data = {}
board = []
with open("input.txt", "r") as file:
    for row in file:
        board.append(list(row.replace('\n', '')))

# Get the coordinate of each elves.
for i in range(0, len(board)):
    for j in range(0, len(board[0])):
        if board[i][j] == '#':
            data[(i,j)] = 1

# N, NE, NW.
def n(save, cx, cy):
    if (cx-1, cy-1) not in save and (cx-1, cy) not in save and (cx-1, cy+1) not in save: return True, -1, 0
    return False, 0, 0

# S, SE, SW.
def s(save, cx, cy):
    if (cx+1, cy-1) not in save and (cx+1, cy) not in save and (cx+1, cy+1) not in save: return True, 1, 0
    return False, 0, 0

# W, NW, SW.
def w(save, cx, cy):
    if (cx, cy-1) not in save and (cx-1, cy-1) not in save and (cx+1, cy-1) not in save: return True, 0, -1
    return False, 0, 0

# E, NE, SE.
def e(save, cx, cy):
    if (cx, cy+1) not in save and (cx-1, cy+1) not in save and (cx+1, cy+1) not in save: return True, 0, 1
    return False, 0, 0

def update(save, index, cx, cy):
    offset = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    # No moves.
    count = 0
    for dx, dy in offset:
        if (cx+dx, cy+dy) in save:
            count += 1

    if count == 0: return False, 0, 0

    pos = [n, s, w, e]    
    for i in range(4):
        isMove, x, y = pos[(i+index)%4](save, cx, cy)
        if isMove: return True, x, y


    return False, 0, 0

def getInterval(data):
    minX, minY, maxX, maxY = inf, inf, -inf, -inf
    for x, y in data:
        minX = min(minX, x)
        maxX = max(maxX, x)
        minY = min(minY, y)
        maxY = max(maxY, y)

    mX = (maxX - minX + 1)
    mY = (maxY - minY + 1)
    return mX, mY

# Part 1 & 2.
index = 0
isMoving = True
while isMoving:
    save = data.copy()
    moves = {}
    for cx, cy in save:
        isMove, x, y = update(save, index, cx, cy)

        if isMove:
            if (cx + x, cy + y) not in moves:
                moves[(cx + x, cy + y)] = (cx, cy, x, y)
            else:
                del moves[(cx + x, cy + y)]

    if len(moves) == 0: isMoving = False

    for nx, ny in moves:
        cx, cy, x, y = moves[(nx, ny)]
        del data[(cx, cy)]
        data[(nx, ny)] = 1

    index += 1
    if index == 10:
        mX, mY = getInterval(data)
        print("Part 1:", mX * mY - len(data))

print("Part 2:", index)