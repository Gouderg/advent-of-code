from math import inf

instruction = []
node = {}
# Extract Data.
with open('input.txt', 'r') as file:
    for row in file:
        instruction.append(row.replace('\n','').split(' = '))


def createDict():
    for row in instruction:
        city = row[0].split(' ')
        if city[0] not in node:
            node[city[0]] = []
        if city[2] not in node:
            node[city[2]] = []
        
        node[city[0]].append((city[2], int(row[1])))
        node[city[2]].append((city[0], int(row[1])))


def recursion(distance, citys, distance_min_local):

    if len(citys) == 8:
        distance_min_local = distance if distance < distance_min_local else distance_min_local
        return distance_min_local, citys

    # On parcourt tous les associes
    for sommet in node[citys[len(citys)-1]]:
        if sommet[0] not in citys:
            distance += sommet[1]
            citys.append(sommet[0])
            distance_min_local, citys = recursion(distance, citys, distance_min_local)
            distance -= sommet[1]
            citys.remove(sommet[0])            

    return distance_min_local, citys
 

def algo():
    # Variable initiale
    distance_min = inf

    # On applique l'algorithme a tous les noeuds pour trouver la solution.
    for city in node:
        # On sauvegarde la ville dans laquelle on est et on initialise la distance parcourue
        citys, distance = [city], 0
        distance, citys = recursion(distance, citys, inf)
        if distance != -1 and distance < distance_min:
            distance_min = distance
    return distance_min


def recursion2(distance, citys, distance_max_local):

    if len(citys) == 8:
        distance_max_local = distance if distance > distance_max_local else distance_max_local
        return distance_max_local, citys

    # On parcourt tous les associes
    for sommet in node[citys[len(citys)-1]]:
        if sommet[0] not in citys:
            distance += sommet[1]
            citys.append(sommet[0])
            distance_max_local, citys = recursion2(distance, citys, distance_max_local)
            distance -= sommet[1]
            citys.remove(sommet[0])            

    return distance_max_local, citys
 

def algo2():
    # Variable initiale
    distance_max = 0

    # On applique l'algorithme a tous les noeuds pour trouver la solution.
    for city in node:
        # On sauvegarde la ville dans laquelle on est et on initialise la distance parcourue
        citys, distance = [city], 0
        distance, citys = recursion2(distance, citys, 0)
        if distance > distance_max:
            distance_max = distance
    return distance_max


createDict()

# Part 1.
lessDist = algo()
print("Part 1:", lessDist)

# Part 2.
moreDist = algo2()
print("Part 2:", moreDist)


