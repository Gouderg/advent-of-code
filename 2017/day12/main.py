# Extract data.
graph = {}
with open("input.txt", "r") as file:
    for row in file:
        row = row.replace('\n', '').split(' <-> ')
        graph[int(row[0])] = []
        for elt in row[1].split(', '):
            graph[int(row[0])].append(int(elt))


# [print(key, ": ", graph[key]) for key in graph]

# Part 1.
already = []
queu = [0]
while len(queu) != 0:
    i = queu.pop(0)
    already.append(i)
    for point in graph[i]:
        if point not in already and point not in queu:
            queu.append(point)


print("Part 1:", len(already))

# Part 2.
already = []
group = 0
for key in graph:
    if key not in already:
        group += 1
        queu = [key]
        while len(queu) != 0:
            i = queu.pop(0)
            already.append(i)
            for point in graph[i]:
                if point not in already and point not in queu:
                    queu.append(point)

print("Part 2:", group)