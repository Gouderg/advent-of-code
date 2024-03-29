from collections import Counter

# Extract data.
data = []
with open('input.txt', 'r') as file:
    for row in file:
        data.append(row.replace('\n', ''))


# Part 1.
epsilon, gamma = "", ""

for j in range(0, len(data[0])):
    temp = [data[i][j] for i in range(0, len(data))]
    c = Counter(temp)
    gamma += max(c, key=lambda key: c[key])
    epsilon += min(c, key=lambda key: c[key])

print('Part 1:', int(gamma, 2) * int(epsilon, 2))


# Part 2.

oxy, co2 = data.copy(), data.copy()
index = 0

while len(oxy) > 1 or len(co2) > 1:

    if len(oxy) > 1:

        # Find the count of bits in each column.
        temp = [oxy[i][index] for i in range(0, len(oxy))]
        c = Counter(temp)

        # Keep 1 if same distribution else the one with the max of occurrence.
        catMax = '1' if c[max(c, key=lambda key: c[key])] == c[min(c, key=lambda key: c[key])] else max(c, key=lambda key: c[key])
        
        # Delete the wrong one.
        for i in range(len(oxy)-1, -1, -1):
            if oxy[i][index] != catMax:
                oxy.pop(i)
    
    if len(co2) > 1:
        # Find the count of bits in each column.
        temp = [co2[i][index] for i in range(0, len(co2))]
        c = Counter(temp)

        # Keep 1 if same distribution else the one with the max of occurrence.
        catMin = '0' if c[max(c, key=lambda key: c[key])] == c[min(c, key=lambda key: c[key])] else min(c, key=lambda key: c[key])

        # Delete the wrong one.
        for i in range(len(co2)-1, -1, -1):
            if co2[i][index] != catMin:
                co2.pop(i)

    index += 1

print('Part 2:', int(oxy[0], 2) * int(co2[0], 2))