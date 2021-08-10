
instructions = []
# Extract data.
with open('input.txt', 'r') as file:
    for row in file:
        instructions.append(row.replace('\n', '').split())

time = 2503

# Part 1.
reindeer = {}
for row in instructions:
    km, move, rest = int(row[3]), int(row[6]), int(row[13])
    distance = 0

    for i in range(0,time):
        if i % (move+rest) < move:
            distance += km
    
    reindeer[row[0]] = distance

print(max(reindeer.values()))

# Part 2.
reindeer, points = {}, {}
# Init.
for row in instructions:
    reindeer[row[0]] = 0
    points[row[0]] = 0

for i in range(0, time):
    for row in instructions:
        km, move, rest = int(row[3]), int(row[6]), int(row[13])
        if i % (move+rest) < move:
            reindeer[row[0]] += km
   
    # Lead
    value = max(reindeer.values())
    for key in reindeer:
        if reindeer[key] == value:
            points[key] += 1

print(max(points.values()))