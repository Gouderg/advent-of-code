# Extract data.
data = [['.' for j in range(400)] for i in range(200)]
y_tab = []
data[0][100] = "+"
with open("input.txt", "r") as file:
    for row in file:
        row = row.replace("\n", "").split(" -> ")
        for i in range(len(row)-1):
            x1, y1 = [int(a) for a in row[i].split(",")]
            x2, y2 = [int(a) for a in row[i+1].split(",")]
            y_tab += [y1, y2]
            x1 -= 400
            x2 -= 400
            step_x = 1 if x1 <= x2 else -1
            step_y = 1 if y1 <= y2 else -1

            if step_y == -1: y2 -= 1
            if step_x == -1: x2 -= 1
            if step_y == 1 and y1 != y2: y2 += 1
            if step_x == 1 and x1 != x2: x2 += 1


            if x1 == x2:
                for y in range(y1, y2, step_y):
                    data[y][x1] = "#"    
            elif y1 == y2:
                for x in range(x1, x2, step_x):
                    data[y1][x] = "#"    

for x in range(0, len(data[0])):
    data[max(y_tab)+2][x] = "#"

# Part 1 & 2.
count_sand = 0
isOkey, isPart1 = True, True
while isOkey:
    # On crée un grain de sable.
    sand_x, sand_y = 100, 0

    # On fait descendre le grain.
    isNotBlock = True
    while isNotBlock:
        if data[sand_y+1][sand_x] == ".":
            sand_y += 1
        elif data[sand_y+1][sand_x-1] == ".":
            sand_y += 1
            sand_x -= 1
        elif data[sand_y+1][sand_x+1] == ".":
            sand_y += 1
            sand_x += 1
        else:
            data[sand_y][sand_x] = "o"
            isNotBlock = False
        
        if sand_y > max(y_tab) and isPart1:
            print("Part 1:", count_sand)
            isPart1 = False
            break

        if sand_y == 0:
            print("Part 2:", count_sand)
            isOkey = False
            break
      
    if isOkey: count_sand += 1



