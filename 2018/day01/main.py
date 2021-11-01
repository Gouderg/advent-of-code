
# Extract data.
data = []
with open('input.txt', 'r') as file:
    for row in file:
        data.append(int(row.replace('\n', '')))


# Part 1.
count = 0
for elt in data:
    count += elt

print("Part 1:", count)

# Part 2.
count, i = 0, 0
pos = [count]
while True:
    count += data[i]
    if count in pos:
        break
    pos.append(count)
    i = (i + 1) % len(data)

print("Part 2:", count)