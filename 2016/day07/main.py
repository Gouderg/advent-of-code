
# Extract data.
data = []
with open('input.txt', 'r') as file:
    for row in file:
        data.append(row.replace('\n', '').replace(']', '[').split('['))

# Part 1.
count = 0
for row in data:
    isOkey = False
    for i, elt in enumerate(row):
        
        # Check if reverse
        ispalin = False
        for j in range(0, len(elt)):
            if j+4 <= len(elt) and elt[j:j+2] == elt[j+2:j+4][::-1] and elt[j] != elt[j+1]:
                ispalin = True
                break
        
        if i % 2 != 0 and ispalin:
            isOkey = False
            break
        elif i % 2 == 0 and ispalin:
            isOkey = True
    if isOkey:
        count += 1

print('Part 1:', count)

# Part 2.
count = 0
for row in data:
    for i, elt in enumerate(row):
        if i%2:
            for j in range(0,len(elt)):
                if j + 2 < len(elt) and elt[j] == elt[j+2] and elt[j] != elt[j+1]:
                    a = elt[j+1]+elt[j]+elt[j+1] 
                    if a in row[0] or a in row[2] or len(row) > 3 and a in row[4] or len(row) > 6 and a in row[6]:
                        count += 1
                        break
                       


print('Part 2:', count)