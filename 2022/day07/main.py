# Extract data.
data = []
with open("input.txt", "r") as file:
    for row in file:
        data.append(row.replace('\n', ''))

# Part 1.
path = []
size = {'/': 0}
needTo = []
for row in data:
    if "$ cd" in row:
        if ".." in row:
            path.pop()
        elif "/" in row:
            path = ['/']
        else:
            path.append(row.split(' ')[2])
            if '/'.join(path) not in size:
                size['/'.join(path)] = 0

    elif "$ ls" in row:
        continue
    
    elif "dir" in row:
        row = row.split(' ')
        if "/".join(path)+"/"+row[1] not in list(size.keys()):
            needTo.append(["/".join(path), row[1]])

    else:
        row = row.split(' ')
        size['/'.join(path)] += int(row[0])

for p, d in needTo[::-1]:
    size[p] += size[p+'/'+d]

count = 0
for key in size:
    if size[key] <= 100000:
        count += size[key]
print("Part 1:", count)

# Part 2.

min_size = 30000000 - (70000000 - size['/'])
best_choice = "/"
for key in size:
    if size[key] > min_size and size[key] < size[best_choice]:
        best_choice = key
print("Part 2:", size[best_choice])