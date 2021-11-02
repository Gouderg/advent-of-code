
# Extract data.
data = []
with open("input_sort.txt", 'r') as file:
    for row in file:
        data.append(row.replace('\n', ''))

# Part 1.
guards = {}
ids = -1
for row in data:
    if "Guard" in row:
        row = row.split(' ')
        ids = int(row[3].replace('#', ''))
        if ids not in guards:
            guards[ids] = []
    
    elif "asleep" in row:
        row = row.split(' ')
        minPast = int(row[1].split(':')[1].replace(']', ''))
    
    elif "wake" in row:
        row = row.split(' ')
        minNew = int(row[1].split(':')[1].replace(']', ''))
        guards[ids].append(minNew - minPast)

# Search id with ths most sleeping time.
idsMax, maxSum = 0, 0
for key in guards:
    if sum(guards[key]) > maxSum:
        maxSum = sum(guards[key])
        idsMax = key

# Count every minute.
mins = {}
i = 0
while i < len(data):
    if '#'+str(idsMax) in data[i]:
        i += 1
        while '#' not in data[i]:
            minPast = int(data[i].split(' ')[1].split(':')[1].replace(']', ''))
            minNew = int(data[i+1].split(' ')[1].split(':')[1].replace(']', ''))
            for j in range(minPast, minNew):
                if j not in mins:
                    mins[j] = 0
                mins[j] += 1
            i += 2
    i += 1

# Search key with max value
maxKey, maxTime = 0, 0
for key in mins:
    if mins[key] > maxTime:
        maxTime = mins[key]
        maxKey = key

print("Part 1:", idsMax * maxKey)

# Part 2.
guards = {}
ids = -1
for row in data:
    if "Guard" in row:
        row = row.split(' ')
        ids = int(row[3].replace('#', ''))
        if ids not in guards:
            guards[ids] = {}
    
    elif "asleep" in row:
        row = row.split(' ')
        minPast = int(row[1].split(':')[1].replace(']', ''))
    
    elif "wake" in row:
        row = row.split(' ')
        minNew = int(row[1].split(':')[1].replace(']', ''))
        for j in range(minPast, minNew):
            if j not in guards[ids]:
                guards[ids][j] = 0
            guards[ids][j] += 1

newGuard = []
for guard in guards:
    maxTime, maxKey = 0, 0
    for key in guards[guard]:
        if guards[guard][key] > maxTime:
            maxTime = guards[guard][key]
            maxKey = key
    newGuard.append((guard, maxKey, maxTime))

theguard = [0,0,0]
for elt in newGuard:
    if elt[2] > theguard[2]:
        theguard = elt

print("Part 2:", theguard[0]*theguard[1])