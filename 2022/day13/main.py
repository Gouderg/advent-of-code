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
data = [l2 for l1 in data for l2 in l1]
data.append("[[2]]")
data.append("[[6]]")

        
n = len(data)
while n >= 1:
    nn = 0
    for i in range(1, n):
        if search(eval(data[i-1]), eval(data[i])) >= 0:
            data[i-1], data[i] = data[i], data[i - 1]
            nn = i
    n = nn

print("Part 2:", (data.index("[[2]]")+1) * (data.index("[[6]]")+1))