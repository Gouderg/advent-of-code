from copy import deepcopy

# Extract data.
rule = {
    1: ['Q', 'M', 'G', 'C', 'L'],
    2: ['R', 'D', 'L', 'C', 'T', 'F', 'H', 'G'],
    3: ['V', 'J', 'F', 'N', 'M', 'T', 'W', 'R'],
    4: ['J', 'F', 'D', 'V', 'Q', 'R'],
    5: ['N', 'F', 'M', 'S', 'L', 'B', 'T'],
    6: ['R', 'N', 'V', 'H', 'C', 'D', 'P'],
    7: ['H', 'C', 'T'],
    8: ['G', 'S', 'J', 'V', 'Z', 'N', 'H', 'P'],
    9: ['Z', 'F', 'H', 'G']
}

instruction = []
with open("input.txt", "r") as file:
    for row in file:
        instruction.append([int(a) for a in row.replace('\n', '').split(',')])

# Part 1.
rule1 = deepcopy(rule)
for row in instruction:
    for i in range(row[0]):
        rule1[row[2]].append(rule1[row[1]].pop())

last = ''
for key in rule1:
    last += rule1[key][-1]

print("Part 1:", last)


# Part 2.
for row in instruction:

    a = len(rule[row[1]])
    rule[row[2]] += rule[row[1]][a-row[0]:]
    rule[row[1]] = rule[row[1]][:a-row[0]]


last = ''
for key in rule:
    last += rule[key][-1]
print("Part 2:", last)