
# Cherche la paire de nombre dans la liste preambleValue qui est la somme de value
def findNumber(value,preambleValue):
    for elt1 in preambleValue:
        for elt2 in preambleValue:
            if (elt1 + elt2 == value) and elt1 != elt2:
                return value          
    
    return False

if __name__ == "__main__":
    
    data = []

    with open("input.txt", "r") as file:
        for row in file:
            row = row.replace("\n",'')
            data.append(int(row))

    ## Part 1
    offset, preambleValue, invalid = 25, [], 0

    for i,value in enumerate(data):
        # Charge les premières valeurs
        if i < offset:
            preambleValue.append(value)

        else:
            response = findNumber(value, preambleValue)
            # Si on nous renvoie une valeur, on supprime la première et on rajoute la dernière pour avoir les 5 valeurs
            if response:
                preambleValue.pop(0)
                preambleValue.append(response)
            else:
                invalid = value
                break 
    print("Part 1:", invalid)

    
    ## Part 2
    j, resultat = 0, 0
    while True:
        somme = []
        for i,value in enumerate(data):
            if i >= j and sum(somme) < invalid:
                somme.append(value)

            if sum(somme) >= invalid:
                break

        if sum(somme) == invalid:
            resultat = (min(somme) + max(somme))
            break
        j += 1
    print("Part 2:", resultat)