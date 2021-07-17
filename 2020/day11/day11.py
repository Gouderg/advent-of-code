# Rule 1
def rule1(data, i, j):
    x = 0 if (i - 1) <= -1 else i-1
    y = 0 if (j - 1) <= -1 else j-1
    X = i if i + 1 >= len(data) else i+1 
    Y = j if j + 1 >= len(data[0]) else j+1 

    if (data[x][y] != '#' and data[x][j] != '#' and data[x][Y] != '#' and data[i][y] != '#' and data[i][Y] != '#' and data[X][y] != '#' and data[X][j] != '#' and data[X][Y] != '#'):
        return '#'
    
    return data[i][j]

# Rule 2
def rule2(data, i, j):
    count = 0
    
    if (i-1) > -1 and (j-1) > -1 and data[i-1][j-1] == '#':
        count += 1
    if (i-1) > -1 and data[i-1][j] == '#':
        count += 1
    if (i-1) > -1 and (j+1) < len(data[0]) and data[i-1][j+1] == '#':
        count += 1
    if (j-1) > -1 and data[i][j-1] == '#':
        count += 1
    if (j+1) < len(data[0]) and data[i][j+1] == '#':
        count += 1
    if (i+1) < len(data) and (j-1) > -1 and data[i+1][j-1] == '#':
        count += 1
    if (i+1) < len(data) and data[i+1][j] == '#':
        count += 1
    if (i+1) < len(data) and (j+1) < len(data[0]) and data[i+1][j+1] == '#':
        count += 1

    if count >= 4:
        return 'L'
    return '#'

def findCouple(data, xGod, yGod):
    couple = []
    imoins, iplus, jmoins, jplus = xGod, xGod, yGod, yGod
    nbCondition = [0] * 8
    while True:
        imoins = 0 if (imoins-1) <= -1 else imoins - 1
        jmoins = 0 if (jmoins-1) <= -1 else jmoins - 1
        iplus = iplus if (iplus+1) == len(data) else iplus + 1
        jplus = jplus if (jplus+1) == len(data[0]) else jplus + 1
        
        if  nbCondition[0] == 0 and (data[imoins][jmoins] != '.' or (imoins == 0 and jmoins == 0)):
            nbCondition[0] = 1 
            couple.append([imoins,jmoins])
        if  nbCondition[1] == 0 and (data[imoins][j] != '.' or (imoins == 0)):
            nbCondition[1] = 1 
            couple.append([imoins,j])
        if nbCondition[2] == 0 and (data[imoins][jplus] != '.' or (imoins == 0 and jplus == len(data[0])-1)):
            nbCondition[2] = 1 
            couple.append([imoins,jplus])
        if nbCondition[3] == 0 and (data[i][jmoins] != '.' or (jmoins == 0)):
            nbCondition[3] = 1 
            couple.append([i,jmoins])
        if nbCondition[4] == 0 and (data[i][jplus] != '.' or (jplus == len(data[0])-1)):
            nbCondition[4] = 1 
            couple.append([i,jplus])
        if nbCondition[5] == 0 and (data[iplus][jmoins] != '.' or (iplus == len(data)-1 and jmoins == 0)):
            nbCondition[5] = 1 
            couple.append([iplus,jmoins])
        if nbCondition[6] == 0 and (data[iplus][j] != '.' or (iplus == len(data)-1)):
            nbCondition[6] = 1
            couple.append([iplus,j])
        if nbCondition[7] == 0 and (data[iplus][jplus] != '.' or (iplus == len(data)-1 and jplus == len(data[0])-1)):
            nbCondition[7] = 1 
            couple.append([iplus,jplus])
        
        if nbCondition.count(0) == 0:
            break
        
    return couple

def rule1bis(data, i, j):
    couple = findCouple(data,i,j)
    
    isHere = True
    for elt in couple:
        if data[elt[0]][elt[1]] == '#':
            isHere = False
            break
    if isHere:
        return '#'
    return data[i][j]
    
    
def rule2bis(data,i,j):
    count = 0
    couple = findCouple(data, i, j)
    
    print(couple)
    for elt in couple:
        if data[elt[0]][elt[1]] == '#':
            count += 1

    if count >= 5:
        return 'L'
    return '#'

def getNeighbours (i, j, m, n):
    neighours = []
    if (i > 0):
        neighours.append((i - 1, j))
        if (j > 0):
            neighours.append((i - 1, j - 1))
        if (j + 1 < n):
            neighours.append((i - 1, j + 1))

    if (i + 1 < m):
        neighours.append((i + 1, j))
        if (j > 0):
            neighours.append((i + 1, j - 1))
        if (j + 1 < n):
            neighours.append((i + 1, j + 1))

    if (j > 0):
        neighours.append((i, j - 1))

    if (j + 1 < n):
        neighours.append((i, j + 1))

    return neighours

def findVisible (map, x, y, dx, dy):
    point = map[x][y]

    while (point == '.'):
        if (x + dx > len(map) - 1 or x + dx < 0) or (y + dy > len(map[0]) - 1 or y + dy < 0):
            break
        else:
            x += dx
            y += dy
            point = map[x][y]

    return (x, y)

if __name__ == "__main__":
    
    map, mp = [], []

    with open("input.txt","r") as file:
        for row in file:
            row = row.replace('\n', '')
            map.append(list(row))
            mp.append(list(row))

    ## Part 1
    # previosSeat = 0
    # while True:
    #     temp = [['.' for j in range(len(data[0]))] for i in range(len(data))]
    #     for i in range(len(data)):
    #         for j in range(len(data[0])):
    #             if data[i][j] == 'L':
    #                 temp[i][j] = rule1(data, i, j)
    #             elif data[i][j] == '#':
    #                 temp[i][j] = rule2(data, i, j)
        
    #     data = [[temp[x][y] for y in range(len(temp[0]))] for x in range(len(temp))]
        
    #     nbSeat = 0
    #     for elt in data:
    #         nbSeat += elt.count('#')
    #     if previosSeat == nbSeat:
    #         break
    #     else:
    #         previosSeat = nbSeat
    #     # [print(row) for row in data]
    # print(previosSeat)
    # # Part 2
    # previosSeat = 0
    # #while True:
    # for k in range(7):
    #     temp = [['.' for j in range(len(data[0]))] for i in range(len(data))]
    #     for i in range(len(data)):
    #         for j in range(len(data[0])):
    #             if data[i][j] == 'L':
    #                 temp[i][j] = rule1bis(data, i, j)
    #             elif data[i][j] == '#':
    #                 temp[i][j] = rule2bis(data, i, j)
        
    #     data = [[temp[x][y] for y in range(len(temp[0]))] for x in range(len(temp))]
    #     # nbSeat = 0
    #     # for elt in data:
    #     #     nbSeat += elt.count('#')
    #     # if previosSeat == nbSeat:
    #     #     break
    #     # else:
    #     #     previosSeat = nbSeat
    #     print()
    #     [print(row) for row in data]
    
    # print(previosSeat)
    moving = True

    while moving:
        moving = False
        for i in range(len(map)):
            for j in range(len(map[i])):
                adj = getNeighbours(i, j, len(map), len(map[i]))
                nbs = 0
                for m, n in adj:
                    x, y = findVisible(map, m, n, m - i, n - j)
                    if (map[x][y] == '#'):
                        nbs += 1

                if (map[i][j] == 'L') and not nbs:
                    mp[i][j] = '#'
                    moving = True
                elif (map[i][j] == '#') and nbs >= 5:
                    mp[i][j] = 'L'
                    moving = True


        map = [[mp[x][y] for y in range(len(mp[0]))] for x in range(len(mp))]
    print(sum(x.count('#') for x in map))