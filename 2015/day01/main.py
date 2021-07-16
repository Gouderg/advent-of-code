
# Extract input.
data = []
with open('input.txt', 'r') as file:
    for row in file:
        data = list(row)


# Part 1.
count = 0
for elt in data:
    if elt == '(': 
        count += 1
    else:
        count -= 1
    
print('Part 1:', count)

# Part 2.
count = 0
for j,elt in enumerate(data):
    if elt == '(': 
        count += 1
    else:
        count -= 1
    
    if count == -1:
        break
print('Part 2:', j+1)