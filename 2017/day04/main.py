from itertools import permutations

# Extract data.
data = []
with open('input.txt', 'r') as file:
    for row in file:
        data.append(row.replace('\n', '').split(' '))

# Part 1.
count = 0
for row in data:
    mdp, isOkey = [], True
    for elt in row:
        if elt not in mdp:
            mdp.append(elt)
        else:
            isOkey = False
            break
    if isOkey:
        count += 1

print('Part 1:', count)

# Part 2.
count = 0
for row in data:
    mdp, isOkey = [], True
    for elt in row:
        notIn = True
        for combi in permutations(elt, len(elt)):
            combi = ''.join(combi).lower()
            if combi in mdp:
                notIn = False
                break
        if notIn:
            mdp.append(elt)
        else:
            isOkey = False
            break
    if isOkey:
        count += 1

print('Part 2:', count)