# Test
isTest = False
times = [7, 15, 30] if isTest else [53, 89, 76, 98]
distances = [9, 40, 200] if isTest else [313, 1090, 1214, 1201]

# Part 1.
count = 1
for time, best_distance in zip(times, distances):
    cpt = 0
    for hold in range(0, time):
        rest = time - hold
        dist = hold * rest
        if hold * rest > best_distance:
            cpt += 1
    if cpt > 0:
        count *= cpt
print("Part 1:", count)

# Part 2.
time = 71530 if isTest else 53897698
distance = 940200 if isTest else 313109012141201

# Part 1.
cpt = 0
for hold in range(0, time):
    rest = time - hold
    dist = hold * rest
    if hold * rest > distance:
        cpt += 1
print("Part 2:", cpt)
