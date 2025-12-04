data = []

with open("input.txt", "r") as file:
    for row in file:
        data.append(row.strip())

# Part 1.
orbits_map = {}

for row in data:
    a, b = row.split(")")
    if a not in orbits_map:
        orbits_map[a] = []
    orbits_map[a].append(b)

tot = 0
def explore(p, depth):
    global tot
    
    if p not in orbits_map:
        tot += depth
        return
    
    for elt in orbits_map[p]:
        explore(elt, depth+1)
    
    tot += depth

explore("COM", 0)

print("Part 1:", tot)

# Part 2.
orbits_map = {}

for row in data:
    a, b = row.split(")")
    if a not in orbits_map:
        orbits_map[a] = []
    orbits_map[a].append(b)
    if b not in orbits_map:
        orbits_map[b] = []
    orbits_map[b].append(a)

all_sums = []
def find_transfer(p, step, seen):
    global all_sums
    if p == "SAN": 
        all_sums.append(step)
        return
    
    for elt in orbits_map[p]:
        if elt in seen: continue
        find_transfer(elt, step+1, seen+[elt])

find_transfer("YOU", 0, ["YOU"])

print("Part 2:", min(all_sums)-2)