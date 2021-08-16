
def calc(a,b,c):
    return a+b > c and b+c > a and c+a > b

# Extract data.
data = []
with open('input.txt', 'r') as file:
    for row in file:
        row = row.replace('\n', '').split(' ')
        while '' in row:
            row.remove('')
        row = [int(a) for a in row]
        data.append(row)

# Part 1.
count = 0
for row in data:
    if calc(row[0], row[1], row[2]):
        count += 1

print('Part 1:', count)

# Part 2.
count = 0
for i in (0,1,2):
    for j in range(0,len(data),3):
        if j+2 < len(data) and calc(data[j][i], data[j+1][i], data[j+2][i]):
            count += 1

print('Part 2:', count)