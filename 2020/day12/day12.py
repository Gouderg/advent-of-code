if __name__ == "__main__":
    
    data = []

    with open("input.txt","r") as file:
        for row in file:
            row = row.replace('\n','')
            data.append(row)

    ## Part 1 & 2
    cardinalite = ['N', 'E', 'S', 'W']
    dirPart2, dirPart1 = {'EW': 10, 'NS': 1}, {'EW': 0, 'NS': 0}
    ship = {'EW': 0, 'NS': 0}
    pointer = 'E'
    offsetDirection = cardinalite[0]
    for row in data:
        actions, values = row[0], int(row[1::].strip())
        if actions == 'F':
            # Part 1
            if pointer == 'E':
                dirPart1['EW'] += values
            elif pointer == 'W':
                dirPart1['EW'] -= values
            elif pointer == 'N':
                dirPart1['NS'] += values
            elif pointer == 'S':
                dirPart1['NS'] -= values
            # Part 2
            ship['EW'] = ship['EW'] + values * dirPart2['EW']
            ship['NS'] = ship['NS'] + values * dirPart2['NS']

        elif actions == 'N':
            dirPart1['NS'] += values
            dirPart2['NS'] += values
        
        elif actions == 'E':
            dirPart1['EW'] += values
            dirPart2['EW'] += values
        
        elif actions == 'S':
            dirPart1['NS'] -= values
            dirPart2['NS'] -= values
        
        elif actions == 'W':
            dirPart1['EW'] -= values
            dirPart2['EW'] -= values

        elif actions == 'L':
            values = values // 90
            index = cardinalite.index(pointer)
            for i in range(0,values):
                index += 1
                a = -dirPart2['NS']
                dirPart2['NS'] = dirPart2['EW']
                dirPart2['EW'] = a
            index = cardinalite.index(pointer)
            index = (index - values) % 4 
            pointer = cardinalite[index]

        elif actions == 'R':
            values = values // 90
            index = cardinalite.index(pointer)
            for i in range(0,values):
                index += 1
                a = -dirPart2['EW']
                dirPart2['EW'] = dirPart2['NS']
                dirPart2['NS'] = a
            index = cardinalite.index(pointer)
            index = (index + values) % 4 
            pointer = cardinalite[index]

    manhattan1, manhattan2 = 0, 0
    for elt in dirPart1:
        manhattan1 += abs(dirPart1[elt])
    print("Part 1: {}".format(manhattan1))

    for elt in ship:
        manhattan2 += abs(ship[elt])
    print("Part 2: {}".format(manhattan2))