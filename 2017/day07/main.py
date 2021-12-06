values = {}
depthValue = {}
def recursion(node, depth):

    # On cherche l'occurence du sommet:
    for elt in data:
        elt = elt.replace(',', '').replace('(', '').replace(')', '').split(' ')
        if node == elt[0] and '->' in elt:
            break
        elif node == elt[0] and len(elt) == 2:
            return int(elt[1])

    
    leaf = int(elt[1])
    for newNode in elt[elt.index('->')+1:]:
        print(newNode, end =' ')
        leaf += recursion(newNode, depth + 1)
    print(leaf)

    if depth != 1:
        if depth not in depthValue:
            depthValue[depth] = []
        depthValue[depth].append((elt[0], leaf))
        values[elt[0]] = leaf
    return 0

# Extract data.
data = []
with open('input2.txt', 'r') as file:
    for row in file:
        data.append(row.replace('\n', ''))

# Part 1.
bottom = ''
for elt in data:
    if '->' in elt:
        elt = elt.split(' ')[0]
        isOkey = True
        for subset in data:
            if '->' in subset:
                subset = subset.split(' -> ')[1]
                if elt in subset:
                    isOkey = False
        if isOkey:
            bottom = elt
            break

print('Part 1:', bottom)

# Part 2.
value = recursion(bottom, 1)
weight, disc = 0, ''
isOkey = False
for key in depthValue:
    temp = []
    for elt in depthValue[key]:
        temp.append(elt[1])
    temp = sorted(temp)
    if temp[0] == temp[-1]:
        pass
    break


    if isOkey:
        break

for elt in data:
    elt = elt.replace(',', '').replace('(', '').replace(')', '').split(' ')
    if elt[0] == disc:
        print(elt[1], disc)
        weight += int(elt[1])
        break

print('Part 2:', weight)
