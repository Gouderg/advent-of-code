calcul = []

def findParanthese(row):
    buffer = []
    lastIndex, index, isHere = 0, 0, False
    for j,elt in enumerate(row):
        if isHere:
            if j == index:
                isHere = False
        elif elt == '(':
            isHere = True
            value, index = findParanthese(row[1+j:])
            index += j
            buffer.append(value)
        elif elt == ')':
            lastIndex = j + 1
            break
        else:
            buffer.append(elt)

    
    # On calcule les additions
    bufferAdd, indexAdd, isHere = [], -1, False
    for j,elt in enumerate(buffer):
        if isHere:
            isHere = False
        elif elt == '+':
            bufferAdd[indexAdd] = int(bufferAdd[indexAdd]) + int(buffer[j+1])
            isHere = True
        else:
            bufferAdd.append(elt)
            indexAdd += 1

    somme = int(bufferAdd[0])
    for j,elt in enumerate(bufferAdd):
        if elt == '*':
            somme *= int(bufferAdd[j+1])

    return somme,lastIndex

# Traitement du fichier
with open('input.txt' , 'r') as file:
    for row in file:
        calcul.append(list(row.replace('\n', '').replace(' ', '')))

part2 = 0
for row in calcul:
    # On cherche les parentheses
    newRow = []
    lastIndex, value, isHere = 0, 0, False
    for i,elt in enumerate(row):
        if isHere:
            if i == lastIndex:
                isHere = False
        elif elt == '(':
            isHere = True
            value, lastIndex = findParanthese(row[1+i:])
            lastIndex += i
            newRow.append(value)
        else:
            newRow.append(elt)
    
    # On calcule les additions
    bufferAdd, indexAdd, isHere = [], -1, False
    for j,elt in enumerate(newRow):
        if isHere:
            isHere = False
        elif elt == '+':
            bufferAdd[indexAdd] = int(bufferAdd[indexAdd]) + int(newRow[j+1])
            isHere = True
        else:
            bufferAdd.append(elt)
            indexAdd += 1

    somme = int(bufferAdd[0])
    for j,elt in enumerate(bufferAdd):
        if elt == '*':
            somme *= int(bufferAdd[j+1])
    part2 += somme

print("Le resultat de la partie 2 est ", part2)