from math import inf

def listInstruction(ligne):
    instru = []
    temp = [0,0]
    for elt in ligne:
        pas = int(elt[1::]) 
        for i in range(0, pas):
            if elt[0] == 'U':
                temp[1] += 1

            elif elt[0] == 'D':
                temp[1] -= 1
            
            elif elt[0] == 'L':
               temp[0] -= 1
            
            elif elt[0] == 'R':
                temp[0] += 1
            
            instru.append(temp[:])
    return instru


ligne1, ligne2, intersection = [], [], []
coord1, coord2 = [0,0], [0,0]


with open("input.txt","r") as file:
    temp = []
    for row in file:
        temp.append(row)
    ligne1 = temp[0].split(',')
    ligne2 = temp[1].split(',')

# ligne1 = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
# ligne2 = ['U62','R66','U55','R34','D71','R55','D58','R83']
# # ligne1 = ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']
# # ligne2 = ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']
instruc1 = listInstruction(ligne1)
instruc2 = listInstruction(ligne2)

print("Je mouline...")

print(len(instruc1))
print(len(instruc2))

for indice1 in range(0,len(instruc1)):
    for indice2 in range(0,len(instruc2)):
        if instruc1[indice1][:] == instruc2[indice2][:]:
            intersection.append(instruc1[indice1])

print("Je cherche l'intersection la plus courte")

print(intersection)
minimum = inf
for elt in intersection:
      nb = abs(elt[0]) + abs(elt[1])
      if nb < minimum:
          minimum = nb
print(minimum)