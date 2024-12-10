
# Parse data.
mountains = []

with open("input.txt", "r") as file:
    for row in file:
        row = [int(a) for a in list(row.replace("\n", ""))]
        mountains.append(row)

# Part 1 & 2.
cpt1, cpt2 = 0, 0

# Find starting trailheads
starting_position = {}
for i in range(len(mountains)):
    for j in range(len(mountains[0])):
        if mountains[i][j] != 0: continue
        starting_position[(i, j)] = 1

def find_possible_way(x, y, current_sum, seen = {}):
    # stop recursion
    if mountains[x][y] == 9:
        if (x, y) not in seen:
            seen[(x, y)] = 0
        seen[(x, y)] += 1
        return seen

    possible_ways = []
    if x+1 < len(mountains) and mountains[x+1][y] == current_sum + 1:
        possible_ways.append((x+1, y))
    if y+1 < len(mountains[0]) and mountains[x][y+1] == current_sum + 1:
        possible_ways.append((x, y+1))
    if x-1 >= 0 and mountains[x-1][y] == current_sum + 1:
        possible_ways.append((x-1, y))
    if y-1 >=0 and mountains[x][y-1] == current_sum + 1:
        possible_ways.append((x, y-1))
    
    for x_next, y_next in possible_ways:
        seen = find_possible_way(x_next, y_next, mountains[x_next][y_next], seen)

    return seen

# iter on each stating position.
for x, y in starting_position:
    seen = find_possible_way(x, y, 0, {})
    cpt1 += len(seen)
    for a in seen:
        cpt2 += seen[a]

print("Part 1:", cpt1)
print("Part 2:", cpt2)
