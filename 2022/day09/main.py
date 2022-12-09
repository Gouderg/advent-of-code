# Extract data.
data = []
with open("input.txt", "r") as file:
    for row in file:
        row = row.replace('\n', '')
        data.append(row.split(' '))

def distance_manhattan(x1, x2):
    return abs(x1[0] - x2[0]) + abs(x1[1] - x2[1])

def update(head, tail):
    if distance_manhattan(head, tail) == 2:
            # Same row.
            if tail[0] == head[0]:
                tail[1] = tail[1] + 1 if head[1] > tail[1] else tail[1] - 1
            
            # Same col.
            elif tail[1] == head[1]:
                tail[0] = tail[0] + 1 if head[0] > tail[0] else tail[0] - 1
            
    elif distance_manhattan(head, tail) == 3 or distance_manhattan(head, tail) == 4:
        # Up.
        if head[0] > tail[0]:
            tail[0] += 1    
            tail[1] = tail[1] + 1 if head[1] > tail[1] else tail[1] - 1
        
        # Down.
        else:
            tail[0] -= 1
            tail[1] = tail[1] + 1 if head[1] > tail[1] else tail[1] - 1
    return tail

# Part 1.

tail_vis = [(0,0)]
head = [0,0]
tail = [0,0]

for row in data:
    direction, distance = row[0], int(row[1])
    for i in range(distance):
        
        if direction == "U":
            head[1] += 1
        elif direction == "D":
            head[1] -= 1
        elif direction == "R":
            head[0] += 1
        elif direction == "L":
            head[0] -= 1
        
        tail = update(head, tail)

        if tuple(tail) not in tail_vis:
            tail_vis.append(tuple(tail))

print("Part 1:", len(tail_vis))


# Part 2.


tail_vis = [(0,0)]
tail = [[0,0] for i in range(10)]

for row in data:
    direction, distance = row[0], int(row[1])

    for i in range(distance):
        
        if direction == "U":
            tail[0][1] += 1
        elif direction == "D":
            tail[0][1] -= 1
        elif direction == "R":
            tail[0][0] += 1
        elif direction == "L":
            tail[0][0] -= 1
        
        for i in range(1, 10):
            tail[i] = update(tail[i-1], tail[i])

        if tuple(tail[9]) not in tail_vis:
            tail_vis.append(tuple(tail[9]))

print("Part 2:", len(tail_vis))