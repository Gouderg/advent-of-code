# Extract data.
data = {}
with open("input.txt", "r") as file:
    for row in file:
        row = row.replace("\n", "").split(": ")
        id = int(row[0].replace("Game ", ""))
        data[id] = []
        for sets in row[1].split("; "):
            blue, red, green = 0, 0, 0
            for colors in sets.split(", "):
                val, col = colors.split(" ")
                if col == "red":
                    red += int(val)
                elif col == "blue":
                    blue += int(val)
                elif col == "green":
                    green += int(val)
                else:
                    print("Error in parsing")
            data[id].append([red, green, blue])

# Part 1.
count = 0
for id in data:
    flag = 0
    for r, g, b in data[id]:
        if r > 12 or g > 13 or b > 14:
            flag = 1
            break
    if not flag:
        count += id
print("Part 1:", count)

# Part 2.
count = 0
for id in data:
    red, green, blue = 0, 0, 0
    for r, g, b in data[id]:
        red = r if r > red else red
        green = g if g > green else green
        blue = b if b > blue else blue
    count += (red * green * blue)

print("Part 2:", count)
