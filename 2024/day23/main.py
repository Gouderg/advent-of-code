# Parse data.
data = []
with open("input.txt", "r") as file:
    for row in file:
        row = row.replace("\n", "").split("-")
        data.append(row)

# Part 1.
cpt = 0
three_spot = {}
for l1, r1 in data:
    all_l1_match = []
    all_r1_match = []
    for l2, r2 in data:
        if l1 == l2 and r1 == r2: continue
        if l1 == l2:
            all_l1_match.append(r2)
        if l1 == r2:
            all_l1_match.append(l2)
        if r1 == r2:
            all_r1_match.append(l2)
        if r1 == l2:
            all_r1_match.append(r2)

    inter = set(all_l1_match) & set(all_r1_match)
    if len(inter) < 1: continue
    for c1 in list(inter):
        tmp = tuple(sorted([l1, r1, c1]))
        if tmp not in three_spot:
            three_spot[tmp] = 1

for a, b, c in three_spot:
    if a[0] == 't' or b[0] == 't' or c[0] == 't':
        cpt += 1

print("Part 1:", cpt)

# Part 2.
cpt = 0
aled = {}
for l1, r1 in data:
    all_l1_match = []
    all_r1_match = []
    for l2, r2 in data:
        if l1 == l2 and r1 == r2: continue
        if l1 == l2:
            all_l1_match.append(r2)
        if l1 == r2:
            all_l1_match.append(l2)
        if r1 == r2:
            all_r1_match.append(l2)
        if r1 == l2:
            all_r1_match.append(r2)

    inter = set(all_l1_match) & set(all_r1_match)


    if len(inter) < 1: continue
    tmp = tuple(sorted([l1, r1, *list(inter)]))
    if tmp not in aled:
        aled[tmp] = 0
    aled[tmp] += 1

max_val, hehe = 0, ""
for key in aled:
    nb_cote = (len(key) * (len(key) - 1)) // 2

    if nb_cote != aled[key]: continue
    if max_val < len(key):
        max_val = len(key)
        hehe = key

print("Part 2:", ','.join(hehe))