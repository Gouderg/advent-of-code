
def check(types, value):
    if types == 'cats' or types == 'trees':
        return clues[types] < int(value)

    elif types == 'pomeranians' or types == 'goldfish':
        return clues[types] > int(value)

    return clues[types] == int(value)

# Extract ticket taper.
clues = {}
with open('ticker_tape.txt', 'r') as file:
    for row in file:
        row = row.replace('\n','').replace(':','').split(' ')
        clues[row[0]] = int(row[1])

data = []
# Extract data.
with open('input.txt', 'r') as file:
    for row in file:
        data.append(row.replace('\n','').replace(':','').replace(',','').split(' '))

# Part 1.
for row in data:
    if clues[row[2]] == int(row[3]) and clues[row[4]] == int(row[5]) and clues[row[6]] == int(row[7]):
        print('Part 1:', int(row[1]))

# Part 2.
for row in data:
    if check(row[2], row[3]) and check(row[4], row[5]) and check(row[6], row[7]):
        print('Part 2:', int(row[1]))