# Parse data.
data = []

with open("input.txt", "r") as file:
    for row in file:
        row = row.replace("\n", "")
        data.append(list(row))

def get_guard_pos():
    for i in range(0, len(data)):
        for j in range(0, len(data[0])):
            if data[i][j] == "^":
                data[i][j] = '.'
                return (i, j)
    

# Part 1.
initial_x, initial_y = get_guard_pos()
p_x, p_y = initial_x, initial_y
dir = 0
distinct = {}
distinct[(p_x, p_y)] = 1

while True:

    if dir == 0 and p_x-1 < 0 or dir == 1 and p_y+1 >= len(data[0]) or dir == 2 and p_x+1 >= len(data) or dir == 3 and p_y-1 < 0: break
    
    if dir == 0:
        if data[p_x-1][p_y] == ".":
            p_x -= 1
        else:
            dir = (dir + 1) % 4

    elif dir == 1:
        if data[p_x][p_y+1] == ".":
            p_y += 1
        else:
            dir = (dir + 1) % 4

    elif dir == 2:
        if data[p_x+1][p_y] == ".":
            p_x += 1
        else:
            dir = (dir + 1) % 4

    elif dir == 3:
        if data[p_x][p_y-1] == ".":
            p_y -= 1
        else:
            dir = (dir + 1) % 4

    if (p_x, p_y) not in distinct:
        distinct[(p_x, p_y)] = 1


print("Part 1:", len(distinct))

# Part 2.

cpt_stuck = 0
for i in range(0, len(data)):
    for j in range(0, len(data[0])):

        if i == initial_x and j == initial_y: continue
        if data[i][j] != ".": continue

        data[i][j] = "O"
        max_loop, dir = 0, 0
        p_x, p_y = initial_x, initial_y
        isEscape = False
        
        while True:

            if max_loop > 10000: break
            max_loop += 1

            if dir == 0 and p_x-1 < 0 or dir == 1 and p_y+1 >= len(data[0]) or dir == 2 and p_x+1 >= len(data) or dir == 3 and p_y-1 < 0:
                isEscape = True
                break

            if dir == 0:
                if data[p_x-1][p_y] == ".":
                    p_x -= 1
                else:
                    dir = (dir + 1) % 4

            elif dir == 1:
                if data[p_x][p_y+1] == ".":
                    p_y += 1
                else:
                    dir = (dir + 1) % 4

            elif dir == 2:
                if data[p_x+1][p_y] == ".":
                    p_x += 1
                else:
                    dir = (dir + 1) % 4

            elif dir == 3:
                if data[p_x][p_y-1] == ".":
                    p_y -= 1
                else:
                    dir = (dir + 1) % 4

        data[i][j] = "."

        if not isEscape:
            cpt_stuck += 1

print("Part 2:", cpt_stuck)