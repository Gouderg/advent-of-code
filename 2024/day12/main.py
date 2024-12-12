# Parse data.
data = []

with open("input.txt", "r") as file:
    for row in file:
        row = list(row.replace("\n", ""))
        data.append(row)


def get_perimeter_from_coordinates(g):
    per = 0
    for c, b in g:
        neigh = 0
        if c-1 >= 0 and (c-1,b) in g:
               neigh += 1 
        if b-1 >= 0 and (c,b-1) in g:
               neigh += 1 
        if c+1 < len(data) and (c+1,b) in g:
               neigh += 1 
        if b+1 < len(data[0]) and (c,b+1) in g:
               neigh += 1 

        per += 4 - neigh
    return per

def get_sides_from_coordinates(g):

    vectors = {}
    for c, b in g:
        # Out of bound.
        if c-1 < 0 and ('t', -1, b) not in vectors:
            vectors[('t', -1, b)] = 1
        if b-1 < 0 and ('l', -1, c) not in vectors:
            vectors[('l', -1, c)] = 1
        if c+1 >= len(data) and ('b', len(data), b) not in vectors:
            vectors[('b', len(data), b)] = 1
        if b+1 >= len(data[0]) and ('r', len(data[0]), c) not in vectors:
            vectors[('r', len(data), c)] = 1


        # Neigh bor
        if c-1 >= 0 and data[c][b] != data[c-1][b] and ('t', c-1, b) not in vectors:
            vectors[('t', c-1, b)] = 1
        if b-1 >= 0 and data[c][b] != data[c][b-1] and ('l', b-1, c) not in vectors:
            vectors[('l', b-1, c)] = 1
        if c+1 < len(data) and data[c][b] != data[c+1][b] and ('b', c+1 ,b) not in vectors:
            vectors[('b', c+1, b)] = 1
        if b+1 < len(data[0]) and data[c][b] != data[c][b+1] and ('r', b+1, c) not in vectors:
            vectors[('r', b+1, c)] = 1
    
    
    # Reduce vectors size
    new_vectors = {}
    cpt = 0
    for key in vectors:
        a, b, c = key
        if (a, b) not in new_vectors:
            new_vectors[(a, b)] = []
        new_vectors[(a, b)].append(c)

 
    for key in new_vectors:
        s = sorted(new_vectors[key])
        cpt += 1
        for l in range(0, len(s)-1):
            if s[l] + 1 != s[l+1]:
                cpt += 1

    return cpt

def find_possible_way(x, y, char, seen = {}):

    possible_ways = []
    if x+1 < len(data) and data[x+1][y] == char and (x+1, y) not in seen:
        possible_ways.append((x+1, y))
    if y+1 < len(data[0]) and data[x][y+1] == char and (x, y+1) not in seen:
        possible_ways.append((x, y+1))
    if x-1 >= 0 and data[x-1][y] == char and (x-1, y) not in seen:
        possible_ways.append((x-1, y))
    if y-1 >=0 and data[x][y-1] == char and (x, y-1) not in seen:
        possible_ways.append((x, y-1))
    
    for x_next, y_next in possible_ways:
        seen[(x_next, y_next)] = 1
        seen = find_possible_way(x_next, y_next, char, seen)

    return seen


gardens = {}
memory = {}
for i in range(len(data)):
    for j in range(len(data[0])):
        if (i, j) in memory: continue


        # On regarde le type de jardin.
        if data[i][j] not in gardens:
            gardens[data[i][j]] = []

        s = find_possible_way(i, j, data[i][j], {(i, j): 1})
        memory = {**memory, **s}
        gardens[data[i][j]].append(s)


# Part 1.
cpt = 0
for g in gardens:
    for sub_g in gardens[g]:
        cpt += len(sub_g) * get_perimeter_from_coordinates(sub_g)

print("Part 1:", cpt)

# Part 2.
cpt = 0
for g in gardens:
    for sub_g in gardens[g]:
        cpt += len(sub_g) * get_sides_from_coordinates(sub_g)

print("Part 2:", cpt)
