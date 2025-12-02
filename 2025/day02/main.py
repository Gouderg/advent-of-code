

data = []
with open("input.txt", "r") as file:
    for row in file:
        row = row.replace("\n", "")
        data = row.split(",")

# Part 1.
cpt = 0
for elt in data:
    start, finish = [int(a) for a in elt.split("-")]

    for i in range(start, finish+1):
        if len(str(i)) % 2 == 1: continue

        a = str(i)[0:len(str(i))//2]
        b = str(i)[len(str(i))//2:]

        if a == b:
            cpt += i

print("Part 1:", cpt)


# Part 2.
cpt = 0
for elt in data:
    start, finish = [int(a) for a in elt.split("-")]

    for i in range(start, finish+1):

        for j in range(0, len(str(i))//2):

            c = str(i)[:j+1]
            if len(str(i).replace(c, "")) == 0:
                cpt += i
                break

print("Part 2:", cpt)