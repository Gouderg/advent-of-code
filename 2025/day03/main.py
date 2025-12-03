

data = []
with open("input.txt", "r") as file:
    for row in file:
        row = row.replace("\n", "")
        data.append(row)

# Part 1.
cpt = 0
for row in data:
    max_v, index = 0, 0
    for i, v in enumerate(list(row)):
        v = int(v)
        if max_v < v and i != len(row) - 1:
            max_v, index = v, i

    max_v_2, index_2 = 0, 0
    for j, v in enumerate(list(row)[index+1:]):
        v = int(v)
        if max_v_2 < v:
            max_v_2, index_2 = v, i

    cpt += int(str(max_v) + str(max_v_2))
    

print("Part 1:", cpt)


# Part 2.
cpt = 0

for row in data:
    k = 0
    word = ""
    index = -1
    while k < 12:
        max_v, tmp_i = 0, 0
        for i, v in enumerate(list(row)[index+1:]):
            v = int(v)
            if max_v < v and i < len(row) - 12 + k - index:
                
                max_v, tmp_i = v, i

        index += 1 + tmp_i
        k += 1
        word += str(max_v)
    cpt += int(word)
    


print("Part 2:", cpt)