# Extract data.
instructions = []

with open('input.txt', 'r') as file:
    for row in file:
        instructions.append(row.replace('\n', ''))

# Part 1.
on_boot = {}
for row in instructions:


    # Parse.
    state = row.split(' ')[0]
    temp = row.split(' ')[1].split(',')
    coor = {}
    for elt in temp:
        c = elt.split('=')[0]
        elt = elt.split('=')[1].split('..')
        coor[c] = (int(elt[0]), int(elt[1]))
    
    # Selection.
    if (coor['x'][0] > 50 or coor['x'][1] < -50) or (coor['y'][0] > 50 or coor['y'][1] < -50) or (coor['z'][0] > 50 or coor['z'][1] < -50):
        continue

    if state == 'on':
        for x in range(coor['x'][0], coor['x'][1]+1):
            for y in range(coor['y'][0], coor['y'][1]+1):
                for z in range(coor['z'][0], coor['z'][1]+1):
                    if (x, y, z) not in on_boot:
                        on_boot[(x, y, z)] = 1
    else:
        for x in range(coor['x'][0], coor['x'][1]+1):
            for y in range(coor['y'][0], coor['y'][1]+1):
                for z in range(coor['z'][0], coor['z'][1]+1):
                    if (x, y, z) in on_boot:
                        del on_boot[(x, y, z)]

count = 0
for x in range(-50, 50):
    for y in range(-50, 50):
        for z in range(-50, 50):
            if (x, y, z) in on_boot:
                count += 1

print('Part 1:', count)

# Part 2.

cubes = []

for row in instructions:

    # Parse.
    state = row.split(' ')[0]
    temp = row.split(' ')[1].split(',')
    coor = {}
    for elt in temp:
        c = elt.split('=')[0]
        elt = elt.split('=')[1].split('..')
        coor[c] = (int(elt[0]), int(elt[1]))

    for cube in range(0, len(cubes)):
        [ux2, vx2, uy2, vy2, uz2, vz2] = cubes[cube]

        # Si aucune des 2 zones ne s'overlappent
        if coor['x'][0] > vx2 or coor['x'][1] < ux2 or coor['y'][0] > vy2 or coor['y'][1] < uy2 or coor['z'][0] > vz2 or coor['z'][1] < uz2:
            continue

        cubes[cube] = None

        if coor['x'][0] > ux2:
            cubes.append((ux2, coor['x'][0] - 1, uy2, vy2, uz2, vz2))
        if coor['x'][1] < vx2:
            cubes.append((coor['x'][1] + 1, vx2, uy2, vy2, uz2, vz2))
        if coor['y'][0] > uy2:
            cubes.append((max(ux2, coor['x'][0]), min(vx2, coor['x'][1]), uy2, coor['y'][0] - 1, uz2, vz2))
        if coor['y'][1] < vy2:
            cubes.append((max(ux2, coor['x'][0]), min(vx2, coor['x'][1]), coor['y'][1] + 1, vy2, uz2, vz2))
        if coor['z'][0] > uz2:
            cubes.append((max(ux2, coor['x'][0]), min(vx2, coor['x'][1]), max(uy2, coor['y'][0]), min(vy2, coor['y'][1]), uz2, coor['z'][0] - 1))
        if coor['z'][1] < vz2:
            cubes.append((max(ux2, coor['x'][0]), min(vx2, coor['x'][1]), max(uy2, coor['y'][0]), min(vy2, coor['y'][1]), coor['z'][1] + 1, vz2))

    if state == 'on':
        cubes.append((coor['x'][0], coor['x'][1], coor['y'][0], coor['y'][1], coor['z'][0], coor['z'][1]))


    cubes = [cube for cube in cubes if cube is not None]

count = 0
for cube in cubes:
    [ux, vx, uy, vy, uz, vz] = cube
    count += (vx - ux + 1) * (vy - uy + 1) * (vz - uz + 1)

print('Part 2:', count)