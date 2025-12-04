

data = []
data2 = []

with open("input.txt", "r") as file:
    for row in file:
        row = row.replace("\n", "")
        data.append(list(row))
        data2.append(list(row))


# Part 1.
cpt = 0
for i in range(0, len(data)):
    for j in range(0, len(data[0])):
        if data[i][j] != "@": continue

        tmp_cpt = 0
        for x in (-1, 0, 1):
            n_i = i+x
            if n_i < 0 or n_i >= len(data): continue

            for y in (-1, 0, 1):
                n_j = j+y
                if n_j < 0 or n_j >= len(data[0]): continue

                if data[n_i][n_j] == "@": 
                    tmp_cpt += 1
        
        if tmp_cpt <= 4:
            cpt += 1


print("Part 1:", cpt)


# Part 2.
cpt = 0
while True:
    tmptmp_cpt = 0
    for i in range(0, len(data)):
        for j in range(0, len(data[0])):
            if data[i][j] != "@": continue

            tmp_cpt = 0
            for x in (-1, 0, 1):
                n_i = i+x
                if n_i < 0 or n_i >= len(data): continue

                for y in (-1, 0, 1):
                    n_j = j+y
                    if n_j < 0 or n_j >= len(data[0]): continue

                    if data[n_i][n_j] == "@": 
                        tmp_cpt += 1
            
            if tmp_cpt <= 4:
                tmptmp_cpt += 1
                data2[i][j] = '.'
    
    data = data2.copy()
    
    if tmptmp_cpt == 0: break
    cpt += tmptmp_cpt
   


print("Part 2:", cpt)