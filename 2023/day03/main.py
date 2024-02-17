# Extract data.
data = []
with open("input.txt", "r") as file:
    for row in file:
        row = row.replace('\n', '')
        data.append(list(row))

# [print(list(row)) for row in data]

def getFullNumber(i, j):
    nb = data[i][j]

    a = j - 1
    while a >= 0 and data[i][a].isdigit():
        nb = data[i][a] + nb
        a -= 1

    a = j + 1
    while a < len(data) and data[i][a].isdigit():
        nb += data[i][a]
        a += 1

    return nb
def main():

    parts = []
    for i in range(0, len(data)):
        for j in range(0, len(data[i])):
            # Try to find a symbol.
            if data[i][j].isdigit() or data[i][j] == ".": continue
            a =[]
            if i - 1 >= 0 and j - 1 >= 0 and data[i-1][j-1].isdigit():
                part = getFullNumber(i-1, j-1)
                if part not in a: a.append(part)
            
            if i - 1 >= 0 and data[i-1][j].isdigit():
                part = getFullNumber(i-1, j)
                if part not in a: a.append(part)
            
            if i - 1 >= 0 and j + 1 < len(data[i]) and data[i-1][j+1].isdigit():
                part = getFullNumber(i-1, j+1)
                if part not in a: a.append(part)
            
            if j - 1 >= 0 and data[i][j-1].isdigit():
                part = getFullNumber(i, j-1)
                if part not in a: a.append(part)
            
            if j + 1 < len(data[i]) and data[i][j+1].isdigit():
                part = getFullNumber(i, j+1)
                if part not in a: a.append(part)
            
            if i + 1 < len(data) and j - 1 >= 0 and data[i+1][j-1].isdigit():
                part = getFullNumber(i+1, j-1)
                if part not in a: a.append(part)
            
            if i + 1 < len(data) and data[i+1][j].isdigit():
                part = getFullNumber(i+1, j)
                if part not in a: a.append(part)
            
            if i + 1 < len(data) and j + 1 < len(data[i]) and data[i+1][j+1].isdigit():
                part = getFullNumber(i+1, j+1)
                if part not in a: a.append(part)
            
            parts = parts + a
    return parts

# Part 1.
parts = main()
print("Part 1:", sum([int(a) for a in parts]))


def main2():
    parts = []
    for i in range(0, len(data)):
        for j in range(0, len(data[i])):
            # Try to find a symbol.
            if data[i][j] != "*": continue
            a =[]
            if i - 1 >= 0 and j - 1 >= 0 and data[i-1][j-1].isdigit():
                part = getFullNumber(i-1, j-1)
                if part not in a: a.append(part)
            
            if i - 1 >= 0 and data[i-1][j].isdigit():
                part = getFullNumber(i-1, j)
                if part not in a: a.append(part)
            
            if i - 1 >= 0 and j + 1 < len(data[i]) and data[i-1][j+1].isdigit():
                part = getFullNumber(i-1, j+1)
                if part not in a: a.append(part)
            
            if j - 1 >= 0 and data[i][j-1].isdigit():
                part = getFullNumber(i, j-1)
                if part not in a: a.append(part)
            
            if j + 1 < len(data[i]) and data[i][j+1].isdigit():
                part = getFullNumber(i, j+1)
                if part not in a: a.append(part)
            
            if i + 1 < len(data) and j - 1 >= 0 and data[i+1][j-1].isdigit():
                part = getFullNumber(i+1, j-1)
                if part not in a: a.append(part)
            
            if i + 1 < len(data) and data[i+1][j].isdigit():
                part = getFullNumber(i+1, j)
                if part not in a: a.append(part)
            
            if i + 1 < len(data) and j + 1 < len(data[i]) and data[i+1][j+1].isdigit():
                part = getFullNumber(i+1, j+1)
                if part not in a: a.append(part)
            if len(a) == 2:
                parts.append(int(a[0]) * int(a[1]))
    return parts
# Part 2.
gear = main2()
print("Part 2:", sum(gear))
