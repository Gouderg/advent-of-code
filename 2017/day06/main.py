
# Extract data.
data = ''
with open('input.txt', 'r') as file:
    for row in file:
        row = row.replace('\n', '').split('\t')
        row = [int(a) for a in row]
        data = row

# Part 1.
memory = [data.copy()]
cycles, loops = 0, 0
while True:
    # On cherche la valeur max.
    pos = data.index(max(data))

    count = data[pos]
    data[pos] = 0
    while count > 0:
        pos = (pos + 1) % len(data)
        data[pos] += 1
        count -= 1

    # print(data, memory)
    if data not in memory:
        memory.append(data.copy())
    else:
        cycles = len(memory)
        loops = len(memory) - memory.index(data)
        break

print('Part 1:', cycles)

# Part 2.
print('Part 2:', loops)