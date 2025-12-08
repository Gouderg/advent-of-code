data = {}
with open("input.txt", "r") as file:
    for row in file:
        row = row.replace("\n", "")
        data[tuple([int(a) for a in row.split(",")])] = 1

def euclid(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)**(1/2)

pairs = {}

for p1 in data:
    for p2 in data:
        if p1 == p2: continue

        if (p1, p2) not in pairs and (p2, p1) not in pairs:
            pairs[(p1, p2)] = euclid(p1, p2)
    
sorted_pairs = dict(sorted(pairs.items(), key=lambda item: item[1]))

# Part 1.
def part1():

    circuits = []
    for i, (p1, p2) in enumerate(sorted_pairs):
        if i >= 1000: break

        is_new = True
        p1_present, p2_present = None, None
        for j, c in enumerate(circuits):
            if p1 in c and p2 in c: # Same circuit, nothing to do.
                is_new = False
                break
            if p1 in c:
                p1_present = j
                is_new = False

            if p2 in c:
                p2_present = j
                is_new = False

        if is_new:
            circuits.append([p1, p2])

        if p1_present != None and p2_present != None:
            circuits[p1_present] = list(set(circuits[p2_present] + circuits[p1_present]))
            circuits.pop(p2_present)
        
        elif p1_present != None:
            circuits[p1_present].append(p2)
        elif p2_present != None:
            circuits[p2_present].append(p1)

    size = sorted([len(c) for c in circuits], reverse=True)
    return size[0] * size[1] * size[2]


print("Part 1:", part1())


# Part 2.
def part2():
    circuits = []
    seen = set()
    
    for i, (p1, p2) in enumerate(sorted_pairs):




        is_new = True
        p1_present, p2_present = None, None
        for j, c in enumerate(circuits):
            if p1 in c and p2 in c: # Same circuit, nothing to do.
                is_new = False
                break
            if p1 in c:
                p1_present = j
                is_new = False

            if p2 in c:
                p2_present = j
                is_new = False

        if is_new:
            circuits.append([p1, p2])

        if p1_present != None and p2_present != None:
            circuits[p1_present] = list(set(circuits[p2_present] + circuits[p1_present]))
            circuits.pop(p2_present)
        
        elif p1_present != None:
            circuits[p1_present].append(p2)
        elif p2_present != None:
            circuits[p2_present].append(p1)
    

        seen.add(p1)
        seen.add(p2)

        if len(seen) == len(data) and len(circuits) == 1:
            return p1[0] * p2[0]



print("Part 2:", part2())