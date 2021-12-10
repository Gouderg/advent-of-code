def tcheck__around(i, j, data, val):
    count = 0
    
    if i-1 >= 0 and data[i-1][j] <= val:
        count += 1
    
    if j-1 >= 0 and data[i][j-1] <= val:
        count += 1
    
    if i + 1 < len(data) and data[i+1][j] <= val:
        count += 1
    
    if j + 1 < len(data[0]) and data[i][j+1] <= val:
        count += 1

    return count

# Extract data.
data = []
with open('input.txt', 'r') as file:
    for row in file:
        row = [int(a) for a in row.replace('\n', '')]
        data.append(row)


# Part 1.
somme = 0
low_coor = []

for i in range(0, len(data)):
    for j in range(0, len(data[0])):
        if tcheck__around(i, j, data, data[i][j]) == 0:
            low_coor.append((i,j))
            somme += (data[i][j] + 1)
print('Part 1:', somme)

# Part 2.
basim = []
already = {}

def move_available(i, j, val):

    result = []
    for n in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x, y = (i + n[0], j + n[1])
        if y < 0 or x < 0 or y > 99 or x > 99:
            continue
        result.append((x, y))
    return result

def solve(i, j):
    points = [(i,j)]
    for (x,y) in move_available(i, j, data[i][j]):
        if (x,y) in already or data[x][y] >= 9:
            continue
        already[(x,y)] = 1
        points += solve(x, y)

    return points

for coor in low_coor:
    already[coor] = 1
    basim.append(len(solve(coor[0], coor[1])))

basim = sorted(basim, reverse=True)
print('Part 2:', basim[0] * basim[1] * basim[2])
