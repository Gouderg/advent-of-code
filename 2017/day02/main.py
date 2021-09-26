
# Extract data.
data = []
with open('input.txt', 'r') as file:
    for row in file:
        row = row.replace('\n', '').split('\t')
        row = [int(a) for a in row]
        data.append(row)

# Part 1.
checksum = 0
for row in data:
    checksum += (max(row) - min(row))

print('Part 1:', checksum)

# Part 2.
checksum = 0
for row in data:
    isOkey = False
    for i in range(0,len(row)):
        for j in range(0, len(row)):
            if row[i]%row[j] == 0 and i != j:
                # print(row[i], row[j])
                checksum += row[i]//row[j]
                isOkey = True
                break
        if isOkey:
            break
print('Part 2:', checksum)
