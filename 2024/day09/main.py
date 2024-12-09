# Parse data.
data = []

with open("input.txt", "r") as file:
    for row in file:
        data = [int(a) for a in list(row.replace("\n", ""))]
        

# Part 1.
cpt = 0
disk = []
current_id = 0
for i, number in enumerate(data):
    for j in range(0, number):
        disk.append("." if i % 2 == 1 else str(current_id))
    
    if i % 2 == 0: current_id = current_id + 1

count_points_fix = disk.count(".")
on_fly = 0

while on_fly != count_points_fix:

    pos_point = 0
    for i in range(0, len(disk)-1):
        if disk[i] == ".":
            pos_point = i
            break

    pos_digit, digit = 0, ""
    for i in range(len(disk)-1, -1, -1):
        if disk[i] != ".":
            pos_digit, digit = i, disk[i]
            break


    disk[pos_point] = digit
    disk[pos_digit] = '.'

    on_fly = disk[pos_digit:].count(".")


for i, elt in enumerate(list(disk)):
    if elt == ".": continue
    cpt += i * int(elt)


print("Part 1:", cpt)

# Part 2.
cpt = 0
disk = []
current_id = 0
for i, number in enumerate(data):
    tmp = []
    for j in range(0, number):
        tmp.append("." if i % 2 == 1 else str(current_id))
    if len(tmp) != 0:
        disk.append(tmp)
    if i % 2 == 0: current_id = current_id + 1

findPose = True
count = 0
while findPose:
    isParse, findPose = False, False
    count += 1
    for i, elt in enumerate(disk[::-1]):
        if '.' in elt: continue
        for j, points in enumerate(disk):
            if '.' not in points: continue
            digit_pos = len(disk) -1 -i
            if j > digit_pos: continue
            if len(points) < len(elt): continue
            
            points_remind = ['.' for _ in range(len(points) - len(elt))]

            if len(points_remind):
                disk = disk[:digit_pos] + [['.' for _ in range(len(elt))]] + disk[digit_pos+1:]
                disk = disk[:j] + [elt] + [points_remind] + disk[j+1:] 
            else:
                disk = disk[:digit_pos] + [['.' for _ in range(len(elt))]] + disk[digit_pos+1:]
                disk = disk[:j] + [elt] + disk[j+1:] 

            isParse = True
            break

        if isParse:
            findPose = True
            break
    

index = 0
for elt in disk:
    for sub_elt in elt:
        if "." not in sub_elt:
            cpt += index * int(sub_elt)
        index += 1


print("Part 2:", cpt)


