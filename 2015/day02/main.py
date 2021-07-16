# Extract data.
data = []

with open('input.txt', 'r') as file:
    for row in file:
        row = row.replace('\n','').split('x')
        row = [int(a) for a in row]
        data.append(row)


# Part 1
result = 0
for temp in data:
    elt = temp[:]
    l,w,h = elt[0], elt[1], elt[2]
    c1 = min(elt)
    elt.remove(c1)
    c2 = min(elt)
    result += 2*l*w + 2*w*h + 2*h*l + c1*c2

print('Part 1:', result)

# Part 2.

result = 0
for temp in data:
    elt = temp[:]
    c1 = min(elt)
    elt.remove(c1)
    c2 = min(elt)
    result += c1*2 + c2*2 + c1*elt[0]*elt[1]

print('Part 2:', result)