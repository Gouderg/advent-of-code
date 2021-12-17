def update(x, y, vX, vY):

    x += vX
    y += vY
    
    if vX < 0: vX += 1
    elif vX > 0: vX -= 1
    vY -= 1

    return x, y, vX, vY

def verif(x, y, vX, maxX, maxY, target_area):
    
    # In the target.
    if (x, y) in target_area:
        return 1
    
    # Impossible to reach.
    if x > maxX or vX == 0 and y < maxY:
        return -1
    
    # Incoming.
    return 0

# Extract data.
x1, x2, y1, y2 = 0, 0, 0, 0
with open('input.txt', 'r') as file:
    for row in file:
        row = row.replace('\n', '').split(': ')[1].split(', ')
        x1, x2 = list(map(int, row[0].replace('x=', '').split('..')))
        y1, y2 = list(map(int, row[1].replace('y=', '').split('..')))


target_area = {}
for x in range(x1, x2+1):
    for y in range(y1, y2+1):
        target_area[(x,y)] = 1

# Part 1.
moves = []
for i in range(x2+1, 0, -1):
    for j in range(x2+1, -x2+1, -1):
        x, y, vX, vY = 0, 0, i, j
        yMax = 0
        while True:                
            x, y, vX, vY = update(x, y, vX, vY)
            isOkey = verif(x, y, vX, x2, y1, target_area)

            if y > yMax:
                yMax = y

            if isOkey == 1:
                moves.append((i, j, yMax))
                break

            if isOkey == -1:
                break

x, y, yMax = 0, 0, 0
for xm, ym, yma in moves:
    if yma > yMax:
        x, y, yMax = xm, ym, yma

print("Part 1:", yMax)

# Part 2.
print("Part 2:", len(moves))