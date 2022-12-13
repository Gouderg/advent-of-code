# Extract data.
data, line = [], []
with open("input.txt", "r") as file:
    for row in file:
        row = row.replace('\n', '')
        if row == "":
            data.append(line)
            line = []
        else:
            line.append(row)
data.append(line)

# Part 1.
def search(l1, l2):
    if type(l1) == int:
        if type(l2) == int:
            return l1 - l2
        else:
            return search([l1], l2)
    else:
        if type(l2) == int:
            return search(l1, [l2])
    
    for let1, let2 in zip(l1, l2):
        value = search(let1, let2)
        if value: return value

    return len(l1) - len(l2)
    

score = 0
for index, (line1, line2) in enumerate(data):
    if search(eval(line1), eval(line2)) < 0:
        score += index + 1



print("Part 1:", score)

# Part 2.
data = []
data2 = []
with open("input2.txt", "r") as file:
    for row in file:
        row = row.replace("\n", "")
        if row != "":
            data.append(row)
            data2.append(row)

already = []
print(len(data2))

for i in range(len(data)):
    for j in range(len(data)):
        if data[i] == data[j]:
            continue
        if search(eval(data[i]), eval(data[j])) < 0:
            i1 = data2.index(data[i])
            i2 = data2.index(data[j])
            print(data[i], data[j])
            data2 = data2[:i1+1] + data2[i2:] + data2[i1+1:i2]
            print(len(data2), data2)
    break
score = 1
for i, elt in enumerate(data2):
    if len(elt) == 5 and elt[0:2] == "[[" and elt[3:5] == "]]":
        score *= (i+1)

print("Part 2:", score)