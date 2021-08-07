import json



def walk(tableau):
    somme = 0

    if type(tableau) == list:
        for row in tableau:
            
            if type(row) == dict or type(row) == list:
                somme += walk(row)
            elif type(row) == int:
                somme += row
    
    elif type(tableau) == dict:
        for key in tableau:

            if type(tableau[key]) == dict or type(tableau[key]) == list:
                somme += walk(tableau[key])
            
            elif type(tableau[key]) == int:
                somme += tableau[key]
    return somme

def walk2(tableau):
    somme = 0

    if type(tableau) == list:
        for row in tableau:
            
            if type(row) == dict or type(row) == list:
                somme += walk2(row)
            elif type(row) == int:
                somme += row
    
    elif type(tableau) == dict:
        isOkey = True
        for key in tableau:
            if type(tableau[key]) == str and tableau[key] == 'red':
                isOkey = False
        if isOkey:
            for key in tableau:
                
                if type(tableau[key]) == dict or type(tableau[key]) == list:
                    somme += walk2(tableau[key])
                
                elif type(tableau[key]) == int:
                    somme += tableau[key]
    
    return somme


tab = json

# Extract data.
with open('input.json', 'r') as file:
    tab = json.load(file)


print("Part 1:", walk(tab))

print("Part 2:", walk2(tab))
