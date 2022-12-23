from math import inf
# Extract data.
cubes = {}
with open("input.txt", "r") as file:
    for row in file:
        row = row.replace("\n", '').split(',')
        cubes[(int(row[0]), int(row[1]), int(row[2]))] = 1


offset = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]

# Part 1.
surface = 0

for x, y, z in cubes:
    sur = 6
    for dx, dy, dz in offset:
        if (x + dx, y + dy, z + dz) in cubes:
            sur -= 1
    surface += sur

print("Part 1:", surface)


# Part 2.
def getAllFreeAir(freecubes, cubes, mx, my, mz, Mx, My, Mz):

    q = [list(freecubes.keys())[0]]

    while len(q):
        x, y, z = q.pop(0)
        
        if x-1 >= mx-1 and (x-1, y, z) not in freecubes and (x-1, y, z) not in cubes:
            freecubes[(x-1, y, z)] = 1
            q.append((x-1, y, z))
        
        if y-1 >= my-1 and (x, y-1, z) not in freecubes and (x, y-1, z) not in cubes:
            freecubes[(x, y-1, z)] = 1
            q.append((x, y-1, z))

        if z-1 >= mz-1 and (x, y, z-1) not in freecubes and (x, y, z-1) not in cubes:
            freecubes[(x, y, z-1)] = 1
            q.append((x, y, z-1))

        if x+1 <= Mx+1 and (x+1, y, z) not in freecubes and (x+1, y, z) not in cubes:
            freecubes[(x+1, y, z)] = 1
            q.append((x+1, y, z))
        
        if y+1 <= My+1 and (x, y+1, z) not in freecubes and (x, y+1, z) not in cubes:
            freecubes[(x, y+1, z)] = 1
            q.append((x, y+1, z))

        if z+1 <= Mz+1 and (x, y, z+1) not in freecubes and (x, y, z+1) not in cubes:
            freecubes[(x, y, z+1)] = 1
            q.append((x, y, z+1))

    return freecubes

mx, my, mz = inf, inf, inf
Mx, My, Mz = -inf, -inf, -inf

# Get all the shape.
for cube in cubes:
    mx = min(mx, cube[0])
    my = min(my, cube[1]) 
    mz = min(mz, cube[2])
    Mx = max(Mx, cube[0])
    My = max(My, cube[1]) 
    Mz = max(Mz, cube[2]) 

# Labelled all value.
# 1 => cube.
# 0 => air pockey.
# 2 => free air.
freecubes = {}
freecubes[(mx-1, my-1, mz-1)] = 2
freecubes = getAllFreeAir(freecubes, cubes, mx, my, mz, Mx, My, Mz)

surface = 0


for x, y, z in cubes:
    sur = 0
    for dx, dy, dz in offset:
        if (x + dx, y + dy, z + dz) in freecubes: #and allcubes[(x + dx, y + dy, z + dz)] != 2:
            sur += 1
    surface += sur

print("Part 2:", surface)