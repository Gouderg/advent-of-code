def dec2bin(d,nb=8):
    if d == 0:
        return "0".zfill(nb)
    if d<0:
        d += 1<<nb
    b=""
    while d != 0:
        d, r = divmod(d, 2)
        b = "01"[r] + b
    return b.zfill(nb)

def masqueBinaire1(mask, value):
    value = dec2bin(int(value), 36)
    value = value[::-1]
    mask = mask[::-1]

    newValue = ''
    for i in range(len(mask)):
        if mask[i] == '1':
            newValue += '1'
        elif mask[i] == '0':
            newValue += '0'
        else:
            newValue += value[i]
    return newValue[::-1]

def masqueBinaire2(mask, value):
    value = dec2bin(int(value), 36)
    value = value[::-1]
    mask = mask[::-1]

    newValue = ''
    for i in range(len(mask)):
        if mask[i] == '1':
            newValue += '1'
        elif mask[i] == 'X':
            newValue += 'X'
        else:
            newValue += value[i]

    return newValue[::-1]

def allPossibilities(value, offset):
    somme = ''
    if value.isnumeric():
        return value

    for i in range(offset, len(value)):
        if value[i] == 'X':
            newValue = value[:i]+'0'+value[i+1:]
            somme+=' '+allPossibilities(newValue, i+1)
            newValue = value[:i]+'1'+value[i+1:]
            somme+=' '+allPossibilities(newValue, i+1)
    return somme


if __name__ == "__main__":
    data = []

    with open('input.txt','r') as file:
        for row in file:
            row = row.replace('\n','')
            data.append(row)

    ## Part 1
    memory, mask, = {}, ''
    for row in data:
        if 'mask' in row:
            row = row.split(' ')
            mask = row[2]
        
        elif 'mem' in row:
            row = row.split(' ')
            temp = row[0].split('[')
            num = temp[1].split(']')
            num = int(num[0])
            
            memory[num] = masqueBinaire1(mask, row[2])
    somme = 0
    for elt in memory:
        somme += int(memory[elt], 2)
    print("Part 1: {}".format(somme))

    ## Part 2
    memory, adress, tempNum, mask = {}, {}, {}, ''
    for row in data:
        if 'mask' in row:
            row = row.split(' ')
            mask = row[2]
        
        elif 'mem' in row:
            row = row.split(' ')
            temp = row[0].split('[')
            num = temp[1].split(']')
            num = int(num[0])

            listAdress = allPossibilities(masqueBinaire2(mask, num), 0)
            listAdress = listAdress.split(' ')
            for addr in listAdress:
                if addr != '':
                    memory[int(addr,2)] = int(row[2])

    print("Part 2: {}".format(sum(memory.values())))