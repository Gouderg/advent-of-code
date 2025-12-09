from shapely import Polygon

data = []
with open("input.txt", "r") as file:
    for row in file:
        row = [int(a) for a in row.replace("\n", "").split(",")]
        data.append(row)

# Part 1.
cpt = 0
for i in range(0, len(data)):
    for j in range(i, len(data)):
        x1, y1, = data[i]
        x2, y2 =  data[j]
        l = (abs(x1-x2)+1) * (abs(y1-y2)+1)

        if l > cpt:
            cpt = l
print("Part 1:", cpt)

# Part 2.
cpt = 0

polygon = Polygon(data)
for i in range(0, len(data)):
    for j in range(i, len(data)):
        x1, y1, = data[i]
        x2, y2 =  data[j]
        
        l = (abs(x1-x2)+1) * (abs(y1-y2)+1)
        pol1 = Polygon(((x1, y1),  (x2, y1), (x2, y2),  (x1, y2))).convex_hull

        if l > cpt and polygon.contains(pol1):
            cpt = l
print("Part 2:", cpt)
