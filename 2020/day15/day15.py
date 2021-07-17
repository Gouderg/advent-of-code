if __name__ == "__main__":
    data = []

    with open("input.txt","r") as file:
        for row in file:
            row = row.replace('\n', '')
            row = row.split(',')
            row = [int(elt) for elt in row]
            data = row.copy()
    

    ## Part 1
    i, size, lastSpoken, occurence = 1, len(data), -1, [] 
    while i <= 2020:
        if data[(i-1)%size] not in occurence:
            lastSpoken = data[i-1]
            occurence.append(data[i-1])

        elif occurence.count(lastSpoken) == 1:
            lastSpoken = 0
            occurence.append(0)
        
        elif occurence.count(lastSpoken) > 1:
            lastSpoken = (i-1) - (len(occurence) - 1 - occurence[len(occurence)-2::-1].index(lastSpoken))
            occurence.append(lastSpoken)
        i += 1
    print("Part 1: {}".format(lastSpoken))

    ## Part 2
    lastSpoken = {}

    for i in range(len(data)):
        lastSpoken[data[i]] = i
    
    while (len(data) <= 30000000):
        lastValueindex = len(data) - 1
        if data[lastValueindex] not in lastSpoken.keys():
            data.append(0)
        else:
            data.append(lastValueindex - lastSpoken[data[lastValueindex]])
        
        lastSpoken[data[lastValueindex]] = lastValueindex

    print("Part 2: {}".format(data[len(data)-2]))
