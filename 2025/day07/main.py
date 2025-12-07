data = []

with open("input.txt", "r") as file:
    for row in file:
        row = row.replace("\n", "")
        data.append(list(row))


# Part 1.
cpt = 0

queu = []
for i in range(len(data[0])):
    if data[0][i] == 'S':
        y_s = i
        queu.append((1, i))

seen, block_seen = {}, {}
while len(queu) > 0:
    x, y = queu.pop(0)
    
    if (x, y) in seen: 
        continue
    else:
        seen[(x, y)] = 1


    # Check below.
    x_n = x + 1
    if x_n >= len(data): continue

    if data[x_n][y] == '.':
        queu.append((x_n, y))
    elif data[x_n][y] == '^':
        cpt += 1
        y_n_l, y_n_r = y - 1, y + 1
        queu.append((x_n, y_n_l))
        queu.append((x_n, y_n_r))

print("Part 1:", cpt)


# Part 2.
cpt = 0
blocks = [[0 for _ in range(len(data[0]))] for _ in range(len(data))]
blocks[0][y_s] = 1

for i in range(len(data)):
    if i + 1 == len(data): continue
    for j in range(len(data[i])):
        if blocks[i][j] == 0: continue

        i_n = i + 1

        if data[i_n][j] == ".":
            blocks[i_n][j] += blocks[i][j]
        
        elif data[i_n][j] == "^":
            j_n_l, j_n_r = j - 1, j + 1
            blocks[i_n][j_n_l] += blocks[i][j]
            blocks[i_n][j_n_r] += blocks[i][j]

print("Part 2:", sum(blocks[-1]))


# Infinite time
# # Part 2.
# cpt = 0

# def explore(x, y, cpt):
#     if y < 0 or y >= len(data[0]):
#         return cpt
    
#     if x == len(data)-1:
#         return cpt + 1
    
#     if (x, y) not in seen:
#         return cpt
    
#     x_n = x + 1
#     if x_n >= len(data): return cpt

#     if data[x_n][y] == '.':
#         cpt = explore(x+1, y, cpt)
#     elif data[x_n][y] == '^':
#         cpt = explore(x+1, y+1, cpt)
#         cpt = explore(x+1, y-1, cpt)

#     return cpt


# cpt = explore(1, y_s, 0)

# print("Part 2:", cpt)