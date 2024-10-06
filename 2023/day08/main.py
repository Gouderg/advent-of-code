from math import lcm

data = {}
instructions = ""
directions = {"L": 0, "R": 1}

with open("input.txt", "r") as file:

    instructions = file.readline().replace("\n", "")

    for row in file:
        if row == "\n": continue
        index, values = row.replace("\n", "").split(" = ")
        left, right = values.replace("(", "").replace(")", "").split(", ") 
        data[index] = [left, right]


# Part 1.
i = 0
carac = 'AAA'
while carac != 'ZZZ':
    ins = instructions[i%len(instructions)]
    carac = data[carac][directions[ins]]
    i += 1

print("Part 1:", i)

# Part 2.

def get_index(carac):
    i = 0
    while carac[-1] != 'Z':
        ins = instructions[i%len(instructions)]
        carac = data[carac][directions[ins]]
        i += 1
    return carac, i

i = 0
carac = [x for x in data if x[-1] == 'A']
ap = []
for a in carac:
    c, i = get_index(a)
    ap.append(i)

print("Part 2:", lcm(*ap))

