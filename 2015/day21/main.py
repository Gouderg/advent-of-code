
def battle(heros, boss, artefact):
    turnHero = True
    # Attack and armor
    heros['attack'] += artefact['attack']
    heros['armor'] += artefact['armor']
    
    # Ring 1
    if artefact['ring1'] <= 0:
        heros['armor'] += (-artefact['ring1'])
    else:
        heros['attack'] += artefact['ring1']

    # Ring 2
    if artefact['ring2'] <= 0:
        heros['armor'] += (-artefact['ring2'])
    else:
        heros['attack'] += artefact['ring2']
    
    # Update damage
    herosDamage = 1 if (heros['attack'] - boss['armor']) <= 1 else (heros['attack'] - boss['armor'])
    bossDamage = 1 if (boss['attack'] - heros['armor']) <= 1 else (boss['attack'] - heros['armor'])
    
    while True:
        if turnHero:
            boss['hit'] -= herosDamage
            turnHero = False
        else:
            heros['hit'] -= bossDamage
            turnHero = True

        if boss['hit'] <= 0 or heros['hit'] <= 0:
            # print(boss, heros, not(turnHero))
           return not(turnHero)

shop = {}
label, i, isOkey = ['weapons', 'armor', 'ring1', 'ring2'], -1, False
# Extract shop
with open('shop.txt', 'r') as file:
    for row in file:
        row = row.replace('\n', '').split(',')
        if row[0] == '.':       
            isOkey = False
            i += 1
            shop[label[i]] = []
        
        # On passe sur la premiere ligne
        elif not(isOkey):
            isOkey = True
        
        elif isOkey:
            shop[label[i]].append((row[0], int(row[1]), int(row[2]), int(row[3])))


# Part 1 & 2.
heros1 = {'hit': 100, 'attack': 0, 'armor': 0}
boss1 = {'hit': 104, 'attack': 8, 'armor': 1}
gold, minGold, maxGold = 0, 10000, 0

for weapon in shop['weapons']:
    for armor in shop['armor']:
        for ring1 in shop['ring1']:
            for ring2 in shop['ring2']:
                if ring2[0] == 'Tampon' or ring2[0] != ring1[0]:
                    gold = weapon[1] + armor[1] + ring1[1] + ring2[1]
                    artefact = {'attack': weapon[2], 'armor': armor[3], 'ring1': ring1[2], 'ring2': ring2[2]}
                    winner = battle(heros1.copy(), boss1.copy(), artefact)
                    if winner and gold < minGold:
                        minGold = gold
                    if not(winner) and gold > maxGold:
                        maxGold = gold


print("Part 1:", minGold)
print("Part 2:", maxGold)