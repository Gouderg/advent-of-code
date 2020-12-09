
maps = []
nbTree1, nbTree2, nbTree3, nbTree4, nbTree5 = 0,0,0,0,0

with open("input.txt", "r") as file:
    for row in file:
        row = row.replace('\n','')
        temp = row
        maps.append(row)

horizontal1,horizontal2, horizontal3, horizontal4, horizontal5 = 0,0,0,0,0

for i in range(1,len(maps)):
    horizontal1 = (horizontal1 + 1) % len(maps[0])
    horizontal2 = (horizontal2 + 3) % len(maps[0])
    horizontal3 = (horizontal3 + 5) % len(maps[0])
    horizontal4 = (horizontal4 + 7) % len(maps[0])
    
    if maps[i][horizontal1] == '#':
        nbTree1 += 1
    if maps[i][horizontal2] == '#':
        nbTree2 += 1
    if maps[i][horizontal3] == '#':
        nbTree3 += 1
    if maps[i][horizontal4] == '#':
        nbTree4 += 1

for i in range(2,len(maps),2):

    horizontal5 = (horizontal5 + 1) % len(maps[0])
    if maps[i][horizontal5] == '#':
        nbTree5 += 1

print("Part 1:", max(nbTree1, nbTree2, nbTree3,nbTree4,nbTree5))
print("Part 2:", nbTree1*nbTree2*nbTree3*nbTree4*nbTree5)

