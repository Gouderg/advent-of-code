
# Extract data.
data = []
with open('input.txt', 'r') as file:
    for row in file:
        data.append(row.replace('\n', ''))

# Part 1 & 2.
for row in data:
    ouverture, score, garbage, count = 0, 0, 0, 0
    needPass = False 
    for l in row:
        if needPass:
            needPass = False
            continue

        if l == '!' and garbage:
            needPass = True
        
        if l == '{' and garbage == 0:
            ouverture += 1
        elif l == '}' and garbage == 0:
            score += ouverture
            ouverture -= 1

        if garbage and not(needPass) and l != '>':
            count += 1

        if l == '<':
            garbage = 1
        elif l == '>':
            garbage = 0
        
    print('Part 1:', score)
    print('Part 2:', count)