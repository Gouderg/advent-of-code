def bouclePart2(data):
    acc, i = 0, 0
    isHere = [0 for i in range(len(data))]

    while True:
        if(i == len(data)):
            break
        elif not(isHere[i]):
            isHere[i] = 1
        else:
            break

        elt = data[i].split()
        if elt[0] == 'acc':
            acc += int(elt[1])
            i += 1
        elif elt[0] == 'nop':
            i += 1
        elif elt[0] == 'jmp':
            i += int(elt[1])
    

    if i == (len(data)):
        return acc
    return 0

if __name__ == "__main__":
    
    data = []

    with open("input.txt", "r") as file:
        for row in file:
            row = row.replace('\n','')
            data.append(row)

    ## Part 1
    acc, i = 0, 0
    isHere = [0 for i in range(len(data))]

    while True:
        
        if(i == len(data)):
            break
        elif not(isHere[i]):
            isHere[i] = 1
        else:
            break

        elt = data[i].split()
        if elt[0] == 'acc':
            acc += int(elt[1])
            i += 1
        elif elt[0] == 'nop':
            i += 1
        elif elt[0] == 'jmp':
            i += int(elt[1])

    print("Part 1:", acc)

    ## Part 2
    nop, jmp = [], []
    #find the nop,jmp
    for i in range(len(data)):
        elt = data[i].split()
        if elt[0] == 'nop':
            nop.append(i)
        elif elt[0] == 'jmp':
            jmp.append(i)

    j, acc, stopMePlease = 0, 0, 0

    while not(stopMePlease):
        if j in nop:
            elt = data[j].split()
            data[j] = 'jmp '+elt[1]
        elif j in jmp:
            elt = data[j].split()
            data[j] = 'nop '+elt[1]

        stopMePlease=bouclePart2(data)

        if j in nop:
            elt = data[j].split()
            data[j] = 'nop '+elt[1]
        elif j in jmp:
            elt = data[j].split()
            data[j] = 'jmp '+elt[1]
        j += 1
        
    print("Part 2:", stopMePlease)
