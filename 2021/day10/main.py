# Extract data.
data = []
with open('input.txt', 'r') as file:
    for row in file:
        data.append(row.replace('\n', ''))


# Part 1.
errors = 0
score = {')': 3, ']': 57, '}': 1197, '>': 25137}
rotate = {')': '(', ']': '[', '}': '{', '>': '<'}
to_remove = []
for j,row in enumerate(data):
    last_open = []
    for i, elt in enumerate(row):
        if elt in ['<', '{', '(', '[']:
            last_open.append(elt)
        
        else:
            # Good One.
            if rotate[elt] == last_open[len(last_open)-1]: 
                last_open.pop(len(last_open)-1)
                
            # Missing One.
            elif i+1 < len(row) and row[i+1] not in ['<', '{', '(', '['] and rotate[row[i+1]] != last_open[len(last_open) - 2]:
                last_open.pop(len(last_open)-1)
            
            # Wrong One.
            else:
                to_remove.append(j)
                errors += score[elt]
                break

print('Part 1:', errors)


# Part 2.

# On enlève les lignes corrupt
for i in to_remove[::-1]:
    data.pop(i)

incomplete = []
score = {'(': 1, '[': 2, '{': 3, '<': 4}

for row in data:
    last_open = []
    for i, elt in enumerate(row):
        if elt in ['<', '{', '(', '[']:
            last_open.append(elt)
        
        else:
            # Good One.
            if rotate[elt] == last_open[len(last_open)-1]: 
                last_open.pop(len(last_open)-1)
                
            # Missing One.
            elif i+1 < len(row) and row[i+1] not in ['<', '{', '(', '['] and rotate[row[i+1]] != last_open[len(last_open) - 2]:
                last_open.pop(len(last_open)-1)


    temp_score = 0
    for elt in last_open[::-1]:
        temp_score *= 5
        temp_score += score[elt]
    incomplete.append(temp_score)

incomplete = sorted(incomplete)
if (len(incomplete)%2 == 0):
    print('Part 2:', incomplete[len(incomplete)//2 + 1])
else:
    print('Part 2:', incomplete[len(incomplete)//2])
