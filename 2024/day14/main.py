
# Parse data.
robots = []

input_text = "input.txt"
with open(input_text, "r") as file:
    for row in file:
        row = row.replace("\n", "").split(" ")
        
        p = [int(a) for a in row[0].replace('p=', "").split(',')]
        v = [int(a) for a in row[1].replace('v=', "").split(',')]
        robots.append((p, v))


# Part 1.
cpt = 1
quadrant = [0, 0, 0, 0]
NB_seconds = 100
width = 101 if input_text == "input.txt" else 11
height = 103 if input_text == "input.txt" else 7
data = [['.' for _ in range(width)] for _ in range(height)]

for robot in robots:
    p, v = robot
    
    p_100_x = (p[1] + (v[1] * NB_seconds)) % height
    p_100_y = (p[0] + (v[0] * NB_seconds)) % width

    data[p_100_x][p_100_y] = data[p_100_x][p_100_y] + 1 if data[p_100_x][p_100_y] != '.' else 1

    # left top
    if p_100_y < width // 2 and p_100_x < height // 2:
        quadrant[0] += 1
    
    elif p_100_y < width // 2 and p_100_x > height // 2:
        quadrant[1] += 1
    
    elif p_100_y > width // 2 and p_100_x < height // 2:
        quadrant[2] += 1

    elif p_100_y > width // 2 and p_100_x > height // 2:
        quadrant[3] += 1


for q in quadrant:
    if q == 0:
        continue
    cpt *= q

print("Part 1:", cpt)


# Part 2.
cpt = 0
memory = {}
NB_seconds = 0
while True:
    NB_seconds += 1
    data = [[' ' for _ in range(width)] for _ in range(height)]
    for robot in robots:
        p, v = robot
        
        p_100_x = (p[1] + (v[1] * NB_seconds)) % height
        p_100_y = (p[0] + (v[0] * NB_seconds)) % width

        data[p_100_x][p_100_y] = data[p_100_x][p_100_y] + 1 if data[p_100_x][p_100_y] != ' ' else 1

    key = ''.join([''.join([str(a) for a in row]) for row in data])
 

    if '1111111111111111111111111111111' in key:
        print("Part 2:", NB_seconds)
        break


