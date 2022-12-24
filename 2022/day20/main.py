# Extract data.
part1, part2 = [], []
with open("input.txt", "r") as file:
    for index, row in enumerate(file):
        part1.append([int(row.replace('\n', '')), index])
        part2.append([int(row.replace('\n', '')) * 811589153, index])

# Part 1.
def getIndex(data, i):
    for j, elt in enumerate(data):
        if elt[1] == i:
            return j

def getScore(data):
    size = len(data)
    data = [elt[0] for elt in data]
    i1 = (data.index(0) + 1000) % size
    i2 = (data.index(0) + 2000) % size
    i3 = (data.index(0) + 3000) % size
    return data[i1] + data[i2] + data[i3]

def round(data, loop):
    size = len(data)
    for _ in range(loop):
        for i in range(size):
            index = getIndex(data, i)
            val = data[index]
            data.pop(index)
            if index + val[0] >= size:
                # offset = (val[0] // size) + 1
                index = (index + val[0]) % (size - 1)
            elif index + val[0] < 0:
                # offset = val[0] // size
                index = (index + val[0]) % (size - 1)
            else:
                index += val[0]
            data.insert(index, val)
        
    return data

part1 = round(part1, 1)
print("Part 1:", getScore(part1))

# Part 2.
part2 = round(part2, 10)
print("Part 2:", getScore(part2))