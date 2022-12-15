# Extract data.
beacons = []

with open("input.txt", "r") as file:
    for row in file:
        row = row.replace("\n", "").split(' ')
        x1 = int(row[2].replace('x=', '').replace(',', ''))
        y1 = int(row[3].replace('y=', '').replace(':', ''))
        x2 = int(row[8].replace('x=', '').replace(',', ''))
        y2 = int(row[9].replace('y=', '').replace(':', ''))
        beacons.append((x1, y1, x2, y2))

def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def getRow(y_to_find):
    already = []
    for xs, ys, xb, yb in beacons:

        distance = dist((xs,ys),(xb,yb))
        if (ys <= y_to_find and y_to_find <= ys + distance) or (ys >= y_to_find and y_to_find >= ys - distance):
            n_val = distance - abs(ys-y_to_find)
            already.append([xs-n_val, xs+n_val])


    already = sorted(already)

    queu = []
    for l, h in already:
        if not queu:
            queu.append([l, h])
            continue

        _ , qh = queu[-1]

        if l >= qh + 1:
            queu.append([l, h])
            continue
        
        queu[-1][1] = max(qh, h)

    return queu

# Part 1.
print("Part 1:", sum([abs(y - x) for x, y in getRow(2000000)]) )

# Part 2.
max_range = 4000000
index = 0
while index <= max_range:
    x = 0
    for l, h in getRow(index):
        if x < l:
            print("Part 2:", x*max_range+index)
            exit(0)

        x = max(x, h+1)
        if x >= max_range: break

    index += 1