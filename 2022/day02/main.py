# Extract data.

data = []
with open("input.txt", "r") as file:
    for row in file:
        data.append(row.replace ("\n", "").split(' '))

rules = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}

total_score = 0
# Part 1.
for p1, p2 in data:
    if p1 == "C" and p2 == "X":
        total_score += (6 + rules[p2])

    elif p1 == "A" and p2 == "Z":
        total_score += rules[p2]

    elif rules[p1] < rules[p2]:
        total_score += (6 + rules[p2])
    
    elif rules[p2] < rules[p1]:
        total_score += rules[p2]

    elif rules[p2] == rules[p1]:
        total_score += (3 + rules[p2])


print("Part 1:", total_score)


# Part 2.
total_score = 0
for p1, p2 in data:
    
    if p2 == "Y":
        total_score += (3 + rules[p1])

    elif p2 == "Z":
        if p1 == "C":
            total_score += (6 + 1)
        else:
            total_score += (6 + rules[p1] + 1)

    elif p2 == "X":
        if p1 == "A":
            total_score += 3
        else:
            total_score += (rules[p1]-1)
            
print("Part 2:", total_score)
