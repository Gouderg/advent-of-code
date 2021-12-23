# Extract data.
scanners = []
origins = [(0,0,0)]

with open("input.txt", "r") as file:
    data = file.read()
    for s in data.split("\n\n"):
        s = s.splitlines()[1:]
        scanners.append([tuple(map(int, k.split(","))) for k in s])

# Part 1.
def rotations(s):
    k = []
    for _ in range(4):
        for _ in range(4):
            k.append(s)
            s = [(z, y, -x) for x, y, z in s]
        k.append([(y, -x, z) for x, y, z in s])
        k.append([(-y, x, z) for x, y, z in s])
        s = [(x, z, -y) for x, y, z in s]
    return k

def sub(x, y):
    result = []
    for a, b in zip(x, y):
        result.append(a - b)
    return tuple(result)

def checkAll(s1, s2):
    for s2 in rotations(s2):
        for a in s1:         
            for b in s2:       
                origine_scanner = sub(b, a)     
                c = []      
                for j in s2:
                    c.append(sub(j, origine_scanner))

                if len(set(s1) & set(c)) >= 12:
                    origins.append(origine_scanner)
                    return set(c)


beacons = scanners[0]
others = scanners[1:]

while others:
    k = checkAll(beacons, others[0])
    if k:
        for elt in k:
            if elt not in beacons:
                beacons.append(elt)
        others.pop(0)
    else:
        others.append(others.pop(0))
    
print("Part 1:", len(beacons))



# Part 2.

def manhattan(ori1, ori2):
    somme = 0
    for i in range(0, len(ori1)):
        somme += abs(ori1[i] - ori2[i])
    return somme

all_distance = []
for ori1 in origins:
    for ori2 in origins:
        all_distance.append(manhattan(ori1, ori2))

print("Part 2:", max(all_distance))

'''
    scanners = [
        [(1,0,0), (2,3,4)],         => scanner 0
        [(1,0,0), (2,3,4)],         => scanner 1
    ]


    beacons = scanners[0]

    et les autres = reste des scanners

    Tant qu'il reste des scanners dans les autres:
        tu appeles une fonction qui cherche les points communs entre les beacons et le premiers scanner des autres
        Si la fonction te renvoie les points communs
            tu les ajoutes au beacons sans faire de doublons
            tu enleves le premier scanner des autres
        sinon
            tu enleves le premier scanner des autres et tu le pousses a la fin des autres ( 1, 2, 3 => 2, 3, 1)
    



    fun checkall(s1, s2) avec s1 liste des beacons et s2 liste des points du premier scanner des autres

        Tu parcours toutes les rotations possibles
            Tu parcours tous les points s1
                Tu parcours tous les points s2
                    Tu calcules l'offset (point s2 -  point s1)

                    Tu reparcours tous les points de s2
                    result = tu stockes la difference entre l'offset et le point de s2 (b - offset)
                    
                    Si le nombres de points en commun entre s1 et result >= 12
                        tu renvoies result
                        

    

'''