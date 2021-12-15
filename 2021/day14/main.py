
# Extract data.
template, data, isOkey = "", {}, True
with open('input2.txt', 'r') as file:
    for row in file:
        if row == "\n":
            isOkey = False
        elif isOkey:
            template = row.replace('\n', '')
        else:
            row = row.replace('\n', '').split(' -> ')
            data[row[0]] = row[1]


def solve(base, itera):
    templa = {}
    # On crée un dictionnaire avec les paires possibles.
    for i in range(0, len(base)):
        if i+1 < len(base):
            if base[i]+base[i+1] not in templa: templa[base[i]+base[i+1]] = 0
            templa[base[i]+base[i+1]] += 1

    # On itère le nombre de fois requit
    for _ in range(itera):
        temp = {}
        for key in templa:
            q = data[key]
            # On ajoute les nouvelles paires que l'on trouve
            if key[0]+q not in temp: temp[key[0]+q] = 0
            temp[key[0]+q] += templa[key]

            
            if q+key[1] not in temp: temp[q+key[1]] = 0
            temp[q+key[1]] += templa[key]


        templa = temp.copy()

    # On compte chaque occurence de lettres.
    left, right = {}, {}
    for key in templa:
        if key[0] not in left: left[key[0]] = 0
        if key[1] not in right: right[key[1]] = 0
        left[key[0]] += templa[key]
        right[key[1]] += templa[key]

    # On garde que le plus grand nombre de lettre (doublon car une même lettre peut apparaître plusieurs fois dans des paire différentes: NC et CB => on ne compte le C qu'une fois).
    count = {}
    for x in set(left) | set(right):
        count[x] = max(left.get(x, 0), right.get(x, 0))

    return max(count.values()) - min(count.values())


# Part 1.
print("Part 1:", solve(template, 10))

# Part 2.
print("Part 2:", solve(template, 40))
