# Extract data.
data = []
with open("input.txt", "r") as file:
    for row in file:
        row = row.replace('\n', '').split(',')
        data.append([int(a) for a in row[0].split('-') + row[1].split('-')])


# Part 1.
count = 0
for row in data:
    if row[0] <= row[2] and row[1] >= row[3] or row[2] <= row[0] and row[3] >= row[1]:
        count += 1

print("Part 1:", count)

# Part 2.
count = 0
for row in data:
    if not(row[1] < row[2] or row[3] < row[0]):
        count += 1

print("Part 2:", count)