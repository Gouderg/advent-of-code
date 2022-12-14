# Big love to : https://www.redblobgames.com/grids/hexagons/ and https://stackoverflow.com/questions/15919783/distance-between-2-hexagons-on-hexagon-grid

# Extract data.
data = []
with open("input.txt", "r") as file:
    for row in file:
        data = row.replace("\n", "").split(",")


def dist(p1, p2):
    y1, x1 = p1
    y2, x2 = p2
    du = x2 - x1
    dv = (y2 + x2 // 2) - (y1 + x1 // 2)
    return max(abs(du), abs(dv)) if ((du >= 0 and dv >= 0) or (du < 0 and dv < 0)) else abs(du) + abs(dv)

def update(i, j, direction):

    if direction == "nw":
        j -= 1
        i = i if j % 2 == 0 else i-1
    elif direction == "n":
        i -= 1
    elif direction == "ne":
        i = i if j % 2 == 0 else i-1
        j += 1
    elif direction == "sw":
        j -= 1
        i = i if j % 2 == 0 else i+1
    elif direction == "s":
        i += 1
    elif direction == "se":
        j += 1
        i = i if j % 2 == 0 else i+1
    return i, j
    
# Part 1.
i_init, j_init = 50, 50
i, j = i_init, j_init

for elt in data:
    i, j = update(i, j, elt)

print("Part 1:", dist((i_init, j_init), (i,j)))

# Part 2.
i_init, j_init = 0, 0
i, j = i_init, j_init
best_dist = 0
for step, elt in enumerate(data):
    i, j = update(i, j, elt)
    current_dist = dist((i_init, j_init), (i,j))
    if current_dist > best_dist:
        best_dist = current_dist

print("Part 2:", best_dist)
