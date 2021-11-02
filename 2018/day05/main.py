
# Extract data.
data = ""
with open("input.txt", "r") as file:
    for row in file:
        data = row.replace('\n', '').replace(' ', '')

# Part 1.
olddata = ""
while olddata != data:
    olddata = data
    for i in range(0,26):
        data = data.replace(chr(ord("a") + i) + chr(ord("A") + i), "")
        data = data.replace(chr(ord("A") + i) + chr(ord("a") + i), "")

print("Part 1:", len(data))

# Part 2.
best = []
for j in range(0, 26):
    newData = data.replace(chr(ord("a") + j), '').replace(chr(ord("A") + j), '')
    olddata = ""
    while olddata != newData:
        olddata = newData
        for i in range(0,26):
            newData = newData.replace(chr(ord("a") + i) + chr(ord("A") + i), "")
            newData = newData.replace(chr(ord("A") + i) + chr(ord("a") + i), "")
    best.append(len(newData))

print("Part 2:", min(best))