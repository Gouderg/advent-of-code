


instruction = []
letters = {}

# Extract data.
with open('input.txt', 'r') as file:
    for row in file:
        row = row.replace('\n', '').split(' -> ')
        instruction.append(row)

def traitement(parse):
    parse = parse.split(' ')
    
    # Cas ou c'est une valeur numeriaue ou si c'est une variable dont on connais la valeur
    if len(parse) == 1:
        if parse[0].isnumeric():        # Number.
            return int(parse[0])
        elif parse[0] in letters:       # Variable connu.
            return letters[parse[0]]
        else:                            # Variable inconnu.
            find(parse[0])
            return letters[parse[0]]
    
    # Cas ou il y a un NOT
    elif len(parse) == 2 and parse[0] == 'NOT':
        if parse[1] not in letters:
            find(parse[1])
        return 65535 - letters[parse[1]]

    # Cas odu AND OR RSHIFT LEFTSHIFT
    elif len(parse) == 3:

        first, second = 0, 0
        # On recupere les bonnes valeurs
        if parse[0].isnumeric():        # Number.
            first = int(parse[0])
        elif parse[0] in letters:       # Variable connu.
            first = letters[parse[0]]
        else:                            # Variable inconnu.
            find(parse[0])
            first = letters[parse[0]]

        if parse[2].isnumeric():        # Number.
            second = int(parse[2])
        elif parse[2] in letters:       # Variable connu.
            second = letters[parse[2]]
        else:                            # Variable inconnu.
            find(parse[2])
            second = letters[parse[2]]


        if parse[1] == 'AND':
            return first & second
        elif parse[1] == 'OR':
            return first | second
        elif parse[1] == 'RSHIFT':
            return first >> second
        else:
            return first << second


def find(letter):
    
    # On parcours toutes les lignes et on cherche la valeur du parametre.
    for row in instruction:
        if letter == row[1]:
            letters[letter] = int(traitement(row[0]))
            break


# Step 1.

for row in instruction:
     letters[row[1]] = traitement(row[0])

print("Part 1:", letters['a'])

# Step 2.
letters = {'b': letters['a']}

for row in instruction:
    letters[row[1]] = traitement(row[0])

print("Part 2:", letters['a'])


