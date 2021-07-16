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

    
    # On calcule les sommes
    somme = int(buffer[0])
    for j,elt in enumerate(buffer):
        if elt == '*':
            somme *= int(buffer[j+1])
        elif elt == '+':
            somme += int(buffer[j+1])

    return somme,lastIndex

# Traitement du fichier
with open('input.txt' , 'r') as file:
    for row in file:
        calcul.append(list(row.replace('\n', '').replace(' ', '')))

part1 = 0
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
    
    # On calcule les sommes
    somme = int(newRow[0])
    for j,elt in enumerate(newRow):
        if elt == '*':
            somme *= int(newRow[j+1])
        elif elt == '+':
            somme +=  int(newRow[j+1])
    
    part1 += somme

print("Le resultat de la partie 1 est ", part1)