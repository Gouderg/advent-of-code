
# Extract data.
data = []
with open('input.txt', 'r') as file:
    for row in file:
        data.append(int(row.replace('\n', ' ')))


# Part 1.
last, count = data[0], 0

for i in range(1, len(data)):
    if data[i] > last:
        count += 1
    last = data[i]

print('Part 1:', count)


# Part 2.
last = data[0] + data[1] + data[2]
count = 0
for i in range(1, len(data)):
    if i+2 < len(data):
        if (data[i] + data[i+1]+ data[i+2]) > last:
            count += 1
        last = (data[i] + data[i+1]+ data[i+2])

print('Part 2:', count)