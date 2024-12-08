# Parse data.
data = []

with open("input.txt", "r") as file:
    for row in file:
        data.append(list(row.replace("\n", "")))

# Extract antennas.
antennas = {}
for i in range(0, len(data)):
    for j in range(0, len(data[0])):
        if data[i][j] == '.': continue

        if data[i][j]not in antennas:
            antennas[data[i][j]] = []
        antennas[data[i][j]].append((i,j))

# Part 1.
antinodes = []
for key in antennas:
    if len(antennas[key]) == 1 or key == "#": continue

    for i_1, j_1 in antennas[key]:
        for i_2, j_2 in antennas[key]:
            if i_1 == i_2 and j_1 == j_2: continue
            dist_x = i_1 - i_2
            dist_y = j_1 - j_2
            
            x = i_1 + dist_x
            y = j_1 + dist_y

            if x < 0 or x >= len(data) or y < 0 or y >= len(data[0]): continue
            if (x, y) not in antinodes:
                antinodes.append((x, y))

print("Part 1:", len(antinodes))


# Part 2.
antinodes = []
for key in antennas:
    if len(antennas[key]) == 1 or key == "#": continue

    for i_1, j_1 in antennas[key]:
        for i_2, j_2 in antennas[key]:
            if i_1 == i_2 and j_1 == j_2: continue
            dist_x = i_1 - i_2
            dist_y = j_1 - j_2

            if (i_2, j_2) not in antinodes:
                    antinodes.append((i_2, j_2))

            x = i_1 + dist_x
            y = j_1 + dist_y

            while x >= 0 and x < len(data) and y >= 0 and y < len(data[0]):
                if (x, y) not in antinodes:
                    antinodes.append((x, y))
                
                x = x + dist_x
                y = y + dist_y

print("Part 2:", len(antinodes))


