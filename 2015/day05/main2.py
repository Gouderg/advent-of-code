data = []

# Extract data.
with open('input.txt', 'r') as file:
    for row in file:
        data.append(row.replace('\n', ''))

# Part 2.
count = 0
for row in data:
    isOkey = True

    # Rule 1.
    isTwice = False
    for i in range(0,len(row)):
        if i+2 < len(row) and row[i:i+2] in row[i+2:]:  
            isTwice = True
    # Rule 2. 
    isDouble = False
    for i,letter in enumerate(row):
        if i+2 < len(row) and letter == row[i+2] and letter != row[i+1]:
            isDouble = True
            

    
    if isTwice and isDouble:
        # print(row)
        count += 1

print('Part 2:', count)