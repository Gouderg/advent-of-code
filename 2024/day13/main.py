
# Parse data.
machines = []

with open("input.txt", "r") as file:
    machine = {}
    for row in file:
        row = row.replace("\n", "")
        
        if row == "":
            machines.append(machine)
            machine = {}

        elif "Button A:" in row:
            row = row.replace("Button A: ", "").split(", ")
            machine['A'] = [int(row[0].replace("X+", "")), int(row[1].replace("Y+", ""))]
        elif "Button B:" in row:
            row = row.replace("Button B: ", "").split(", ")
            machine['B'] = [int(row[0].replace("X+", "")), int(row[1].replace("Y+", ""))]
        elif "Prize:" in row:
            row = row.replace("Prize: ", "").split(", ")
            machine['Prize'] = [int(row[0].replace("X=", "")), int(row[1].replace("Y=", ""))]

    machines.append(machine)

def check(machine):
    Px, Py = machine['Prize'][0], machine['Prize'][1]
    Xa, Xb = machine['A'][0], machine['B'][0]
    Ya, Yb = machine['A'][1], machine['B'][1]


    n2 = (Px*Ya-Py*Xa) // (Xb*Ya-Yb*Xa)
    n1 = (Py*Xb-Px*Yb) // (Xb*Ya-Yb*Xa)        
    
    if (n1 * Xa + n2*Xb) == Px and (n1 * Ya + n2*Yb) == Py: return n1 * 3 + n2

    return 0
# Part 1.
cpt = 0
for machine in machines:
    cpt += check(machine)
    
print("Part 1:", cpt)


# Part 2.
cpt = 0
for machine in machines:
    machine['Prize'][0] += 10000000000000
    machine['Prize'][1] += 10000000000000

    cpt += check(machine)

print("Part 2:", cpt)
