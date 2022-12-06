# Extract data.
data = []
with open("input.txt", "r") as file:
    for row in file:
        data = list(row.replace('\n', ''))

# Part 1.
last = data[0:4]
marker = 0
for i in range(4, len(data)):
    if len(set(last)) == 4:
        marker = i
        break
    
    for j in range (1, 4):
        last[j - 1] = last[j]
    last[3] = data[i]

print("Part 1:", marker)


# Part 2.
last = data[0:14]
marker = 0
for i in range(14, len(data)):
    if len(set(last)) == 14:
        marker = i
        break
    
    for j in range (1, 14):
        last[j - 1] = last[j]
    last[13] = data[i]

print("Part 2:", marker)