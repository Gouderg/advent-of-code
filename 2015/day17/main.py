
def combination(datas, pos, combi, litre, value):
    if litre > 150:
        return value
    elif litre == 150:
        value.append(combi[:])
        return value

    for i in range(pos+1, len(datas)):
        combi.append(datas[i])
        value = combination(datas, i, combi, litre + data[i], value)
        combi.pop(-1)
    
    return value


# Extract data.
data = []
with open('input.txt', 'r') as file:
    for row in file:
        data.append(int(row.replace('\n','')))

# Part 1.
values = []
combis = []
for j in range(0, len(data)):
    combis.append(data[j])
    values = combination(data, j, combis, data[j], values)
    combis.pop(-1)

print("Part 1:", len(values))

# Part 2.
# On cherche la plus petite combinaison
mins = len(data)
for row in values:
    if len(row) < mins:
        mins = len(row)

# On compte chaque combinaison egale a la taille de mins
count = 0
for row in values:
    if len(row) == mins:
        count += 1
print('Part 2:', count)