ranges = []
tocheck = []
isplit = False
with open("input.txt", "r") as file:
    for row in file:
        row = row.replace("\n", "")
        if row == "":
            isplit = True
            continue
        if not isplit:
            ranges.append([int(a) for a in row.split("-")])
        else:
            tocheck.append(int(row))

ranges = sorted(ranges)

# Part 1.
cpt = 0
for fruit in tocheck:
    isFresh = False
    for a, b in ranges:
        if fruit >= a and fruit <= b:
            isFresh = True
            break

    if isFresh:
        cpt += 1

print("Part 1:", cpt)


# Part 2.
cpt = 0
while True:
    isBreak = False
    for i in range(0, len(ranges)-1):
        if ranges[i][1] < ranges[i+1][0]: 
            continue
        
        if ranges[i+1][0] >= ranges[i][0] and ranges[i+1][1] <= ranges[i][1]:
            ranges.pop(i+1)
            isBreak = True
            break

        ranges[i] = [ranges[i][0], ranges[i+1][1]]
        ranges.pop(i+1)

        isBreak = True
        break
    if not isBreak: break

for a, b in ranges:
    cpt += (b-a+1)

print("Part 2:", cpt)