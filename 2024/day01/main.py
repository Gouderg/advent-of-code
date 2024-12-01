# Parse data.
def parse():
    left, right = [], []

    with open("input.txt", "r") as file:
        for row in file:
            l, r = row.replace("\n", "").split("   ")
            left.append(int(l))
            right.append(int(r))

    return left, right

# Part 1.
cpt = 0
left, right = parse()

for i in range(len(left)):

    l_min = left.pop(left.index(min(left)))
    r_min = right.pop(right.index(min(right)))

    cpt += abs(r_min - l_min)

print("Part 1:", cpt)

# Part 2.
cpt = 0
left, right = parse()

for i in range(len(left)):

    l_min = left.pop(left.index(min(left)))
    r_cpt = right.count(l_min)

    cpt += l_min * r_cpt

print("Part 2:", cpt)

