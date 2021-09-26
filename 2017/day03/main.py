# Part 2: Pour chaque nouveau carré, trouve tous les coups
def movesAvailable(index):
    x,y = index, index-1
    moves = [(x,y)]
    # Montée 
    for i in range(index*2-1):
        y -= 1
        moves.append((x,y))
    
    # Gauche
    for i in range(0,index*2):
        x -= 1
        moves.append((x,y))
    
    # Descente
    for i in range(0, index*2):
        y += 1
        moves.append((x,y))

    # Droite
    for i in range(0, index*2):
        x += 1
        moves.append((x,y))

    return moves

# Part 2: Trouve les valeurs voisines et renvoie la somme
def findNeigbour(pos):
    count = 0

    if (pos[0]-1, pos[1]-1) in system:
        count += system[(pos[0]-1, pos[1]-1)]
    
    if (pos[0]-1, pos[1]) in system:
        count += system[(pos[0]-1, pos[1])]
    
    if (pos[0]-1, pos[1]+1) in system:
        count += system[(pos[0]-1, pos[1]+1)]
    
    if (pos[0], pos[1]-1) in system:
        count += system[(pos[0], pos[1]-1)]
    
    if (pos[0], pos[1]) in system:
        count += system[(pos[0], pos[1])]

    if (pos[0], pos[1]+1) in system:
        count += system[(pos[0], pos[1]+1)]
    
    if (pos[0]+1, pos[1]-1) in system:
        count += system[(pos[0]+1, pos[1]-1)]
    
    if (pos[0]+1, pos[1]) in system:
        count += system[(pos[0]+1, pos[1])]
    
    if (pos[0]+1, pos[1]+1) in system:
        count += system[(pos[0]+1, pos[1]+1)]
    
    return count


# Extract data.
data = 277678

# Part 1.  
manhattan = 0
# Find belt
path = 1
while True:
    if (path*2-1)**2 >= data:
        break
    path += 1

maxNumber = (path*2-1)**2
size = path*2-1

# Find the nearest sommet
for i in (1,2,3):
    if maxNumber - (size-1) > data:
        maxNumber = maxNumber - (size-1)
    else:
        break

if maxNumber - data < data - (maxNumber - (size-1)):
    manhattan = (path-1) + (size//2 - (maxNumber - data))
else:
    manhattan = (path-1) + ((size-1)//2 - (data - (maxNumber - (size-1))))

print("Part 1:", manhattan)

# Part 2.
system = {(0,0): 1}
index, isOkey = 1, True
temp = ()
while isOkey:
    for move in movesAvailable(index):
        system[tuple(move)] = findNeigbour(move)

        if system[tuple(move)] > data:
            temp = move
            isOkey = False
            break
    
    index += 1
print('Part 2:', system[tuple(temp)])