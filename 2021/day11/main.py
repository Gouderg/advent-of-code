# Extract data.
data = []
with open('input.txt', 'r') as file:
    for row in file:
        row = [int(a) for a in row.replace('\n', '')]
        data.append(row)

def increase_around(i, j):

    if i-1 >= 0 and j-1 >= 0:
        data[i-1][j-1] += 1
    
    if i-1 >= 0:
        data[i-1][j] += 1
    
    if i-1 >= 0 and j+1 < len(data[0]):
        data[i-1][j+1] += 1

    if j-1 >= 0:
        data[i][j-1] += 1

    if j+1 < len(data[0]):
        data[i][j+1] += 1
    
    if i+1 < len(data) and j-1 >= 0:
        data[i+1][j-1] += 1
    
    if i+1 < len(data):
        data[i+1][j] += 1
    
    if i+1 < len(data) and j+1 < len(data[0]):
        data[i+1][j+1] += 1


# Part 1.
flash = 0
for _ in range(100):
    
    # Increase All by One.
    for i in range(len(data)):
        for j in range(len(data[0])):
            data[i][j] += 1
    
    not_nine = []
    while True:
        isOkey = True
        # Increase Around.
        for i in range(len(data)):
            for j in range(len(data[0])):
                if data[i][j] > 9 and (i,j) not in not_nine:
                    flash += 1
                    increase_around(i, j)
                    isOkey = False
                    not_nine.append((i,j))
        if isOkey:
            break

    # Set to 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] > 9:
                data[i][j] = 0

print('Part 1:', flash)