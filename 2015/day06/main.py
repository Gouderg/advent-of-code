
instruction = []
SIZE = 1000

def setup(size):
    light = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(0)
        light.append(row)
    return light

# Extract data.
with open('input.txt', 'r') as file:
    for row in file:
        instruction.append(row.replace('\n',''))

# Part 1.
light = setup(SIZE)
for row in instruction:
    row = row.split(' ')

    if row[0] == 'toggle':
        xS, yS = row[1].split(',')
        xE, yE = row[3].split(',')
        xS, yS, xE, yE = int(xS), int(yS), int(xE), int(yE)
        for j in range(yS,yE+1):
            for i in range(xS,xE+1):
                light[i][j] = 1 - light[i][j]
    
    elif row[0] == 'turn':
        value = 1 if row[1] == 'on' else 0
        xS, yS = row[2].split(',')
        xE, yE = row[4].split(',')
        xS, yS, xE, yE = int(xS), int(yS), int(xE), int(yE)
        for j in range(yS,yE+1):
            for i in range(xS,xE+1):
                light[i][j] = value

count = 0
for row in light:
    count += row.count(1)
print('Part 1:', count)

# Part 2.
light = setup(SIZE)
for row in instruction:
    row = row.split(' ')

    if row[0] == 'toggle':
        xS, yS = row[1].split(',')
        xE, yE = row[3].split(',')
        xS, yS, xE, yE = int(xS), int(yS), int(xE), int(yE)
        for j in range(yS,yE+1):
            for i in range(xS,xE+1):
                light[i][j] += 2
    
    elif row[0] == 'turn':
        value = 1 if row[1] == 'on' else -1
        xS, yS = row[2].split(',')
        xE, yE = row[4].split(',')
        xS, yS, xE, yE = int(xS), int(yS), int(xE), int(yE)
        for j in range(yS,yE+1):
            for i in range(xS,xE+1):
                light[i][j] += value
                if light[i][j] < 0: light[i][j] = 0

count = 0
for row in light:
    for elt in row:
        count += elt
print('Part 2:', count)