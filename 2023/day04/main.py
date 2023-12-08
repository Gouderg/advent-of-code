# Extract data.
win = []
points = []
card = {}
with open("input.txt", "r") as file:
    for i, row in enumerate(file):
        row = row.replace('\n', '').split(": ")[1].split(" | ")
        win.append([int(a) for a in list(filter(lambda x: x != '', row[0].split(' ')))])
        points.append([int(a) for a in list(filter(lambda x: x != '', row[1].split(' ')))])
        card[i+1] = 1

# Part 1.
count = 0

for i in range(len(win)):
    cpt = 0
    for pt in points[i]:
        if pt in win[i]:
            cpt = 1 if cpt == 0 else cpt * 2
    count += cpt
print("Part 1:", count)

# Part 2.
for i in range(len(win)):
    key = i+2
    cpt = 0
    for pt in points[i]:
        if pt in win[i]:
            cpt += 1

    for inc in range(key, key+cpt):
        card[inc] += card[i+1]

count = sum([card[key] for key in card])
print("Part 2:", count)
