
# Extract data.
data, data2 = [], []
with open('input.txt', 'r') as file:
    for row in file:
        data.append(int(row.replace('\n', '')))
        data2.append(int(row.replace('\n', '')))


# Part 1.
i = 0
count = 0
while i < len(data):
    prevI = i
    i += data[i]
    data[prevI] += 1
    count += 1
print('Part 1:', count)

# Part 2.
i = 0
count = 0
while i < len(data2):
    prevI = i
    i += data2[i]
    data2[prevI] = data2[prevI] + 1 if data2[prevI] < 3 else data2[prevI] - 1
    count += 1

print('Part 2:', count)