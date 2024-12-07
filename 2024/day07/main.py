from itertools import product

# Parse data.
data = []

with open("input.txt", "r") as file:
    for row in file:
        left, right = row.replace("\n", "").split(": ")
        data.append((int(left), [int(a) for a in right.split(" ")]))

# Part 1.
cpt = 0
for total, subseq in data:

    for a in product([0,1], repeat=len(subseq)-1):
        sub_total = subseq[0]
        
        for index, sign in enumerate(a):
            sub_total = sub_total * subseq[index+1] if sign == 0 else sub_total + subseq[index+1]

        if sub_total == total:
            cpt += total
            break

print("Part 1:", cpt)

# Part 2.
cpt = 0
for total, subseq in data:

    for a in product([0,1,2], repeat=len(subseq)-1):
        sub_total = subseq[0]
        
        for index, sign in enumerate(a):
            if sign == 0:
                sub_total = sub_total * subseq[index+1]
            elif sign == 1:
                sub_total = sub_total + subseq[index+1]
            else:
                sub_total = int(str(sub_total)+str(subseq[index+1]))

        if sub_total == total:
            cpt += total
            break

print("Part 2:", cpt)


