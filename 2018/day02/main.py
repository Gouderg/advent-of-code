from collections import Counter

# Extract data.
data = []
with open('input.txt', 'r') as file:
    for row in file:
        data.append(row.replace('\n', ''))

# Part 1.
twice, three = 0, 0
for row in data:
    isTwice, isThree = True, True
    c = Counter(row)
    for elt in c:
        if c[elt] == 2 and isTwice:
            isTwice = False
            twice += 1
        elif c[elt] == 3 and isThree:
            isThree = False
            three += 1

print('Part 1:', three*twice)

# Part 2.
pos = ""
for i in range(0, len(data)):
    for j in range(i+1, len(data)):
        temp = ''
        for k in range(0, len(data[i])):
            if data[i][k] == data[j][k]:
                temp += data[i][k]
        if len(temp) > len(pos):
            pos = temp

print("Part 2:", pos)