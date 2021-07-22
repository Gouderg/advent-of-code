# Variable.
voyelle = 'aeiou'
interdit = ['ab', 'cd', 'pq', 'xy']
data = []


# Extract data.
with open('input.txt', 'r') as file:
    for row in file:
        data.append(row.replace('\n', ''))


# Part 1.
count = 0
for row in data:
    isOkey = True

    # Vrification of ban letter
    for elt in interdit:
        if elt in row:
            isOkey = False
            break
    
    # Verify nb voyelle
    nb_voyelle = 0
    for letter in row:
        if letter in voyelle:
            nb_voyelle += 1
    if nb_voyelle < 3:
        isOkey = False

    # Check if one letter apppears twice in row
    previous_letter = ''
    isDouble = False
    for elt in row:
        if elt == previous_letter:
            isDouble = True
            break
        previous_letter = elt
    if not(isDouble):
        isOkey = False

    # Add 1 if all requirements are  validate
    if isOkey:
        count += 1

print('Part 1:', count)