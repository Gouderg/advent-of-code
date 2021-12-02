# Extract data.
data = []
with open('input.txt', 'r') as file:
    for row in file:
        data.append(row.replace('\n', '').split(' '))


# Part 1.
hoz, depth = 0, 0

for row in data:
    if row[0] == "up":
        depth -= int(row[1])
    elif row[0] == "down":
        depth += int(row[1])
    elif row[0] == "forward":
        hoz += int(row[1])

print('Part 1:', hoz * depth)


# Part 2.
hoz, depth, aim = 0, 0, 0

for row in data:
    if row[0] == "up":
        aim -= int(row[1])

    elif row[0] == "down":
        aim += int(row[1])
    
    elif row[0] == "forward":
        hoz += int(row[1])
        depth += aim * int(row[1])

print('Part 2:', hoz * depth)