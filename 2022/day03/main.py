
# Extract data.
data = []
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
with open("input.txt", "r") as file:
    for row in file:
        data.append(row.replace("\n", ""))


# Part 1.
count = 0
for row in data:
    half = len(row) // 2
    for l in row[:half]:
        if l in row[half:]:
            count += letters.index(l) + 1
            break

print("Part 1:", count)



# Part 2.
count = 0
for i in range(0, len(data)-2, 3):
    for l in data[i]:
        if l in data[i+1] and l in data[i+2]:
            count += letters.index(l) + 1
            break

print("Part 2:", count)