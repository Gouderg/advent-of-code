def part1():
    # Parse data.

    data_map = []
    moves = ''
    with open("input.txt", "r") as file:
        isMap = True
        for row in file:
            row = row.replace("\n", "")        
            if row == "":
                isMap = False
            elif isMap:
                data_map.append(list(row))
            elif not isMap:
                moves += row


    # Starting position.
    x_s, y_s = 0, 0
    for i in range(0, len(data_map)):
        for j in range(0, len(data_map[0])):
            if data_map[i][j] == "@":
                x_s, y_s = i, j
                break

    # Part 1.
    cpt = 0
    for move in moves:

        x, y = 0, 0
        if move == '>':
            y += 1
        elif move == 'v':
            x += 1
        elif move == '<':
            y -= 1
        elif move == '^':
            x -= 1
        
        x_next = x_s + x
        y_next = y_s + y

        if data_map[x_next][y_next] == '.':
            data_map[x_next][y_next] = '@'
            data_map[x_s][y_s] = '.'
            x_s = x_next
            y_s = y_next
        
        elif data_map[x_next][y_next] == '#':
            continue
        elif data_map[x_next][y_next] == 'O':
            
            while True:
                x_next += x
                y_next += y

                if data_map[x_next][y_next] == 'O':
                    continue
                elif data_map[x_next][y_next] == '#':
                    break
                else:
                    step = abs(x_next-x_s) + abs(y_next-y_s)

                    for k in range(step, 0, -1):
                        data_map[x_s+x*k][y_s+y*k] = data_map[x_s+x*(k-1)][y_s+y*(k-1)] 

                    data_map[x_s][y_s] = '.'
                    x_s += x
                    y_s += y
                    break

    for i in range(0, len(data_map)):
        for j in range(0, len(data_map[0])):
            if data_map[i][j] != "O": continue
            cpt += (100 * i + j)
    
    return cpt

def part2():

    # Parse data.

    data_map_old = []
    moves = ''
    with open("input.txt", "r") as file:
        isMap = True
        for row in file:
            row = row.replace("\n", "")        
            if row == "":
                isMap = False
            elif isMap:
                data_map_old.append(list(row))
            elif not isMap:
                moves += row

    data_map = []

    for i in range(0, len(data_map_old)):
        row = []
        for j in range(0, len(data_map_old[0])):
            if data_map_old[i][j] == '@':
                row.append("@")
                row.append(".")
            elif data_map_old[i][j] == 'O':
                row.append("[")
                row.append("]")
            else:
                row.append(data_map_old[i][j])
                row.append(data_map_old[i][j])
        
        data_map.append(row)

    # Starting position.
    x_s, y_s = 0, 0
    for i in range(0, len(data_map)):
        for j in range(0, len(data_map[0])):
            if data_map[i][j] == "@":
                x_s, y_s = i, j
                break

    cpt = 0
    for move in moves:

        x, y = 0, 0
        if move == '>':
            y += 1
        elif move == 'v':
            x += 1
        elif move == '<':
            y -= 1
        elif move == '^':
            x -= 1
        
        x_next = x_s + x
        y_next = y_s + y

        if data_map[x_next][y_next] == '.':
            data_map[x_next][y_next] = '@'
            data_map[x_s][y_s] = '.'
            x_s = x_next
            y_s = y_next
        
        elif data_map[x_next][y_next] == '#':
            continue
        elif data_map[x_next][y_next] in ['[', ']']:
            
            # Two ways:
            if y != 0:
                while True:
                    x_next += x
                    y_next += y

                    if data_map[x_next][y_next] == '#':
                        break
                        
                    elif data_map[x_next][y_next] in ['[', ']']:
                        continue
                    
                    else:
                        step = abs(x_next-x_s) + abs(y_next-y_s)

                        for k in range(step, 0, -1):
                            data_map[x_s+x*k][y_s+y*k] = data_map[x_s+x*(k-1)][y_s+y*(k-1)] 

                        data_map[x_s][y_s] = '.'
                        x_s += x
                        y_s += y
                        break
                        
            else:
                pos_to_push = {0: {(x_s, y_s): 1}}
                x_cop, y_cop = x_next, y_next-1 if data_map[x_next][y_next] == ']' else y_next + 1
                pos_to_push[1] = {(x_cop, y_cop): 1, (x_next, y_next): 1}

                level = 1
                isWall = False
                while not isWall:
                    if level not in pos_to_push: break
                    for x_cop, y_cop in pos_to_push[level]:
                        x_next = x_cop + x
                        y_next = y_cop + y


                        if data_map[x_next][y_next] == '#':
                            isWall = True
                            break
                        
                        elif data_map[x_next][y_next] in ['[', ']']:
                            x_cop_sub, y_cop_sub = x_next, y_next-1 if data_map[x_next][y_next] == ']' else y_next + 1
                            if level + 1 not in pos_to_push:
                                pos_to_push[level+1] = {}
            
                            pos_to_push[level+1][(x_cop_sub, y_cop_sub)] = 1
                            pos_to_push[level+1][(x_next, y_next)] = 1
                                        

                    level += 1
                if isWall: continue

                for level in sorted(list(pos_to_push.keys()), reverse=True):
                    for x_pos, y_pos in pos_to_push[level]:
            
                        data_map[x_pos+x][y_pos+y] = data_map[x_pos][y_pos] 
                        data_map[x_pos][y_pos] = '.'

                data_map[x_s][y_s] = '.'
                x_s += x
                y_s += y


    for i in range(0, len(data_map)):
        for j in range(0, len(data_map[0])):
            if data_map[i][j] != "[": continue
            cpt += (100 * i + j)

    return cpt


# Part 1.
print("Part 1:", part1())

# Part 2.
print("Part 2:", part2())
