
instruction = []
# Extract data
with open('input.txt', 'r') as file:
    for row in file:
        instruction = row.replace('\n', '').replace(',', '').split(' ')

# Part 1.
direction, vertical, horizontal = 0, 0, 0
for row in instruction:
    direction = (direction - 1)%4 if row[0] == 'L' else (direction + 1)%4

    # North
    if direction == 0:
        vertical += int(row[1:])
    
    # South
    elif direction == 2:
        vertical -= int(row[1:])
    
    # West
    elif direction == 1:
        horizontal += int(row[1:])

    # East
    elif direction == 3:
        horizontal -= int(row[1:])

print('Part 1:', abs(vertical)+abs(horizontal))


# Part 2.
direction, x, y, pos, isOkey = 0, 0, 0, [], False
for row in instruction:
    direction = (direction - 1)%4 if row[0] == 'L' else (direction + 1)%4

    # North
    if direction == 0:
        valX, valY = 0, 1
    
    # South
    elif direction == 2:
        valX, valY = 0, -1
        
    # West
    elif direction == 1:
        valX, valY = 1, 0

    # East
    elif direction == 3:
        valX, valY = -1, 0
        
    for _ in range(0,int(row[1:])):
            x += valX
            y += valY
            
            if (x,y) in pos:
                isOkey = True
                break
            pos.append((x,y))
    if isOkey: break
print('Part 2:', abs(x)+abs(y))

