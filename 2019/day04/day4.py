
encadrement = [199999,599999]
nbPassword = 0

for i in range(199999,599999+1):
    nb = []
    nb[:0] = str(i)
    nb = [int(nb[k]) for k in range(0,len(nb))]
    if int(nb[5]) >= int(nb[4]) >= int(nb[3]) >= int(nb[2]) >= int(nb[1]) >= int(nb[0]):
        nbPlace = []
        for j in range(1,10):
            if nb.count(j) != 0:
                nbPlace.append(nb.count(j))
        if 2 in nbPlace:
            nbPassword += 1
             

print(nbPassword)