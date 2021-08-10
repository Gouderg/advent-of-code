  

def seat(data, last_noms, nbNoms, happiness):
    # End of recursion.
    if nbNoms == len(last_noms):
        temp = happiness


        # Last with 2-Last.
        for elt in data[last_noms[len(last_noms)-1]]:
            if elt[0] == last_noms[len(last_noms) - 2]:
                temp += elt[1]
                break

        # Last with Alice.
        for elt in data[last_noms[len(last_noms)-1]]:
            if elt[0] == 'Alice':
                temp += elt[1]
                break
        
        # Alice with last.
        for elt in data['Alice']:
            if elt[0] == last_noms[len(last_noms)-1]:
                temp += elt[1]
        
        value.append(temp)
        #print(temp, last_noms)
    
    else:
        stock = 0
        # Stockage de la valeur.
        for elt in data[last_noms[len(last_noms)-1]]:
            if elt[0] == last_noms[len(last_noms) - 2]:
                stock = elt[1]
                break

        # Appel de la nouvelle recursion.
        for elt in data[last_noms[len(last_noms)-1]]:
            if elt[0] not in last_noms:
                last_noms.append(elt[0])
                seat(data, last_noms, nbNoms, happiness+elt[1]+stock)
                last_noms.pop(-1)

def main(inp, part):
    instructions = []
    # Extract data.
    with open(inp, 'r') as file:
        for row in file:
            instructions.append(row.replace('\n', '').replace('.', '').split(' '))

    # Split in dictionnary
    data = {}
    for row in instructions:
        if row[0] not in data:
            data[row[0]] = []
        
        values = -int(row[3]) if row[2] == 'lose' else int(row[3])
        data[row[0]].append([row[10], values])

    noms = ['Alice']
    global value
    value = []
    for row in data['Alice']:
        noms.append(row[0])
        seat(data, noms, len(data), row[1])
        noms.pop(-1)

    print(part, max(value))  

# Part 1.
main('input3.txt', 'Part 1:')
main('input.txt', 'Part 2:')
