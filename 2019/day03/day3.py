
with open("input.txt", "r") as file:
    left, right = [row.replace("\n", "") for row in file]

# Part 1.
cpt = 0

left_pair = {}
k = 0 + 0j
incr = { "R": 1j, "L": -1j, "U": 1, "D": -1 }

for elt in left.split(","):
    l, c = elt[0], int(elt[1:])
    for _ in range(c):
        k += incr[l]
        left_pair[k] = 1

k = 0
best_pair = {}
for elt in right.split(","):
    l, c = elt[0], int(elt[1:])
    for _ in range(c):
        k += incr[l]
        if k in left_pair:
            best_pair[k] = 1

best_pair_sum = [int(abs(k.real)+ abs(k.imag)) for k in best_pair]
cpt  = min(best_pair_sum)

print("Part 1:", cpt)


# Part 2.
cpt = 0

left_pair = {}
k = 0 + 0j
incr = { "R": 1j, "L": -1j, "U": 1, "D": -1 }
step = 0
for elt in left.split(","):
    l, c = elt[0], int(elt[1:])
    for _ in range(c):
        step += 1
        k += incr[l]
        if k not in left_pair:
            left_pair[k] = step

k = 0
best_pair = {}
step = 0
for elt in right.split(","):
    l, c = elt[0], int(elt[1:])
    for _ in range(c):
        k += incr[l]
        step += 1
        if k in left_pair:

            best_pair[k] = step + left_pair[k]  

best_pair_sum = [v for k, v in best_pair.items()]
cpt  = min(best_pair_sum)

print("Part 2:", cpt)