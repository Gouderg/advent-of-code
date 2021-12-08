# Extract data.
data = []
with open('input.txt', 'r') as file:
    for row in file:
        data.append(row.replace('\n', '').split(' | '))


# Part 1.
count = 0
for row in data:
    for elt in row[1].split(' '):
        if len(elt) >= 2 and len(elt) <= 4 or len(elt) == 7:
            count += 1

print('Part 1:', count)


# Part 2.
count = 0
for row in data:
    unique = {}

    # Search position
    for elt in row[0].split(' '):
        if len(elt) == 2:       # Add 2.
            unique[1] = elt
        
        elif len(elt) == 3:     # Add 7.
            unique[7] = elt
        
        elif len(elt) == 4:     # Add 4.
            unique[4] = elt

        elif len(elt) == 7:     # Add 8.
            unique[8] = elt
    
   
    # Add 3.
    for elt in row[0].split(' '):
        if len(set(elt) & set(unique[7])) == 3 and len(elt) == 5:
            unique[3] = elt
            break
    
    # Add 9.
    unique[9] = ''.join(set(unique[3]) | set(unique[4]))

    # Add 6.
    for elt in row[0].split(' '):
        if sorted(set(elt)) != sorted(set(unique[9])) and len(set(elt) & set(unique[7])) == 2 and len(elt) == 6:
            unique[6] = elt
            break

    # Add 0.
    for elt in row[0].split(' '):
        if sorted(set(elt)) != sorted(set(unique[9])) and sorted(set(elt)) != sorted(set(unique[6])) and len(elt) == 6:
            unique[0] = elt

    # Add 5.
    for elt in row[0].split(' '):
        if len(elt) == 5 and sorted(set(elt)) != sorted(set(unique[3])) and len(set(elt) & set(unique[6])) == 5:
            unique[5] = elt

    # Add 2.
    for elt in row[0].split(' '):
        if sorted(set(elt)) != sorted(set(unique[3])) and sorted(set(elt)) != sorted(set(unique[5])) and len(elt) == 5:
            unique[2] = elt
            break
    
    new_tab = {}
    for key in unique:
        new_tab[''.join(sorted(unique[key]))] = key

    # Count value
    val = ''
    for elt in row[1].split(' '):
        val += str(new_tab[''.join(sorted(set(elt)))])
    count += int(val)

print('Part 2:', count)