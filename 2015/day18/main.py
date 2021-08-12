def copy(grid, height, width):
    new = []
    for i in range(0,height):
        row = []
        for j in range(0,width):
            row.append(grid[i][j])
        new.append(row)
    return new

def checkNeighbors(oldGrid, i, j, width, height):
    voisins = 0
    # i - 1, j - 1
    if i-1 >= 0 and j-1 >= 0 and oldGrid[i-1][j-1] == '#':
        voisins += 1
    # i - 1, j
    if i-1 >= 0 and oldGrid[i-1][j] == '#':
        voisins += 1
    # i - 1, j + 1
    if i-1 >= 0 and j+1 < height and oldGrid[i-1][j+1] == '#':
        voisins += 1
    # i, j - 1
    if j-1 >= 0 and oldGrid[i][j-1] == '#':
        voisins += 1
    # i, j + 1
    if j+1 < height and oldGrid[i][j+1] == '#':
        voisins += 1
    # i + 1, j - 1
    if i+1 < width and j-1 >= 0 and oldGrid[i+1][j-1] == '#':
        voisins += 1
    # i + 1, j
    if i+1 < width and oldGrid[i+1][j] == '#':
        voisins += 1
    # i + 1, j + 1
    if i+1 < width and j+1 < height and oldGrid[i+1][j+1] == '#':
        voisins += 1


    return voisins

def rules2(oldGrid, i, j, width, height):

    if (i == 0 and j == 0) or (i == 0 and j == height-1) or (i == width-1 and j == 0) or (i == width-1 and j == height-1):
        return '#'
    
    voisins = checkNeighbors(oldGrid, i, j, width, height)
    if ((voisins == 2 or voisins == 3) and oldGrid[i][j] == '#') or (voisins == 3 and oldGrid[i][j] == '.'):
        return '#'
    return '.'

def rules(oldGrid, i, j, width, height):
    voisins = checkNeighbors(oldGrid, i, j, width, height)
    if ((voisins == 2 or voisins == 3) and oldGrid[i][j] == '#') or (voisins == 3 and oldGrid[i][j] == '.'):
        return '#'
    return '.'

def jeuvie(grid, height, width, rule2):
    oldGrid = copy(grid, height, width)
    for i in range(0,height):
        for j in range(0,width):
            if rule2:
                grid[i][j] = rules2(oldGrid, i, j, width, height)
            else:
                grid[i][j] = rules(oldGrid, i, j, width, height)
            
    
    return grid

def main(grid, part, rule, height, width, nbLap):
    for _ in range(0,nbLap):
        grid = jeuvie(grid, height, width, rule)

    # [print(''.join(row)) for row in grid]

    count = 0
    for row in grid:
        count += row.count('#')
    print(part, count)

# Extract data.
grids, nbLap = [], 100
height, width = 0, 0
with open('input.txt', 'r') as file:
    for row in file:
        height += 1
        grids.append(list(row.replace('\n','')))

    width = len(grids[0])

# Part 1.
part2grid = copy(grids, height, width)
main(grids, 'Part 1:', False, height, width, nbLap)

# Part 2.
part2grid[height-1][0] = '#'
main(part2grid, 'Part 2:', True, height, width, nbLap)
