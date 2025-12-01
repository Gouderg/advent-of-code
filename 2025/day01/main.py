

data = []
with open("input.txt", "r") as file:
    for row in file:
        row = row.replace("\n", "")
        data.append(row)



# Part 1.
cpt = 50
cpt_0 = 0
for dial in data:

    number = int(dial[1:])

    for _ in range(number):
        if dial[0] == "L": 
            cpt -= 1
        else:
            cpt += 1

        if cpt == -1:
            cpt = 99
        elif cpt == 100:
            cpt = 0

    if cpt == 0:
        cpt_0 += 1

print("Part 1:", cpt_0)


# Part 2.
cpt = 50
cpt_0 = 0

for dial in data:

    number = int(dial[1:])

    for _ in range(number):
        if dial[0] == "L": 
            cpt -= 1
        else:
            cpt += 1
        
        if cpt == -1:
            cpt = 99
        elif cpt == 100:
            cpt = 0
            cpt_0 += 1
        elif cpt == 0:
            cpt_0 += 1

print("Part 2:", cpt_0)