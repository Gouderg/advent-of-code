import collections

# Extract data.
data = []
with open('input.txt', 'r') as file:
    for row in file:
        data.append(list(row.replace('\n', '')))

# Part 1.
output = ''
for i in range(0,len(data[0])):
    column = ''
    for j in range(0, len(data)):
        column += data[j][i]
    output += collections.Counter(column).most_common(1)[0][0]

print('Part 1:', output)

# Part 2.
output = ''
for i in range(0,len(data[0])):
    column = ''
    for j in range(0, len(data)):
        column += data[j][i]
    output += collections.Counter(column).most_common()[-1][0]

print('Part 2:', output)