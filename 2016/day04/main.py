import collections

# Extract data.
data = []
with open('input.txt', 'r') as file:
    for row in file:
        data.append(row.replace('\n', '').split('-'))

# Part 1 & 2.
count = 0
for row in data:
    a = row.pop(-1)
    sector, letters = int(a[:3]), a[3:].replace('[', '').replace(']','')
    compteur = collections.Counter(''.join(row))
    initial = sorted(sorted(compteur.keys()), key=lambda x: -compteur[x])
    
    if ''.join(initial[:5]) == letters:
        count += sector
        row = '-'.join(row)
        chaine = ''
        for i in range(0, len(row)):
            if row[i] == '-':
                chaine += ' '
            else:
                chaine += chr((ord(row[i]) - 97+sector)%26+97)
        
        if "northpole" in chaine:
            print("Part 2:", sector)

print('Part 1:', count)