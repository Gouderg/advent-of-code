data = []
plane = [[0] * 8 for i in range(128)]

maxIdSeat = 0
currentIdSeat = 0

with open("input.txt", "r") as file:
    for row in file:
        row = row.replace('\n','')
        data.append(row)

for elt in data:
    rows = [0,127]
    columns = [0,7]
    rowCurrent, columnsCurrent = 0,0
    for i in range(0,7):
        if elt[i] == 'F':
            rows = [rows[0],(rows[0]+rows[1])//2]
        elif elt[i] == 'B':
            rows = [(rows[0]+rows[1])//2 +1,rows[1]]
        
        if elt[i] == 'F' and i == 6:
            rowCurrent = rows[0]
        elif elt[i] == 'B' and i == 6:
             rowCurrent = rows[1]


    for i in range(7,10):
        if elt[i] == 'L':
            columns = [columns[0],(columns[0]+columns[1])//2]
        elif elt[i] == 'R':
            columns = [(columns[0]+columns[1])//2+1,columns[1]]
        if elt[i] == 'L' and i == 9:
            columnsCurrent = columns[0]
        elif elt[i] == 'R' and i == 9:
            columnsCurrent = columns[1]

    plane[rowCurrent][columnsCurrent] = 1
    currentIdSeat = rowCurrent * 8 + columnsCurrent
   
    if currentIdSeat > maxIdSeat:
        maxIdSeat = currentIdSeat

print("Part 1:", maxIdSeat)
for i in range(len(plane)):
    if 0 in plane[i]:
        place = plane[i].index(0)

        if (place == 7 and plane[i][place-1] == 1 and plane[i+1][0] == 1) or (plane[i][place-1] == 1 and plane[i][place+1] == 1):
            print("Part 2:", i*8+place)
            break 



