mdp = []
nbPassword1 = 0
nbPassword2 = 0

with open("input.txt","r") as file:
    for row in file:
        mdp.append(row)


for row in mdp:
    info = row.split(':')
    infos = info[0].split(' ')
    count = info[1].count(infos[1])
    borne = infos[0].split('-')

    if count <= int(borne[1]) and count >= int(borne[0]):
        nbPassword1 += 1
    
    # On teste le premier caractère:
    if info[1][int(borne[0])] == infos[1] and info[1][int(borne[1])] != infos[1]:
        nbPassword2 += 1
    elif info[1][int(borne[0])] != infos[1] and info[1][int(borne[1])] == infos[1]:
        nbPassword2 += 1

print("Part 1:",nbPassword1)
print("Part 2:", nbPassword2)