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

def n_impaire(n):
    nb = 1
    for _ in range(n):
        nb += 2
    return nb

def getRow(y_to_find):
    already = []
    known = 0
    for xs, ys, xb, yb in beacons:
        if ys == y_to_find and [xs, xs] not in already:
            already.append([xs, xs])
            known += 1
        if yb == y_to_find and [xb, xb] not in already:
            already.append([xb, xb])
            known += 1

        distance = dist((xs, ys), (xb, yb))

        if (ys <= y_to_find and y_to_find <= ys + distance) or (ys >= y_to_find and y_to_find >= ys - distance):
            n_val = n_impaire(distance - abs(ys-y_to_find))
            already.append([xs-n_val//2, xs+n_val//2])


    already = sorted(already)
    queu = []
    for l, h in already:
        if not queu:
            queu.append([l, h])
            continue

        ql, qh = queu[-1]

        if l > qh + 1:
            queu.append([l, h])
            continue
        
        queu[-1][1] = max(qh, h)

    return queu, known

# Part 1.

y_to_find = 2000000
y_to_find = 10
     
part1, known = getRow(y_to_find)       

print("Part 1:", sum([abs(y - x) for x, y in part1]) - known + 1)

# Part 2.
max_range = 4000000

index = 0
while index < max_range:
    v1, _ = getRow(index)

    x = 0
    for l, h in v1:
        if x < l:
            print("Part 2:", x*max_range+index)
            exit(0)
        x = max(x, h+1)
        if x > max_range: break

    index += 1