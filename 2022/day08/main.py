# Extract data.
data = []
with open("input.txt", "r") as file:
    for row in file:
        row = list(row.replace('\n', ''))
        row = [int(a) for a in row]
        data.append(row)



def checkEdge(data, i, j):

    isOkey = True

    # X
    for k in range(0, len(data)):
        if k < i and data[k][j] >= data[i][j]: 
            isOkey = False
        if k == i: 
            if isOkey:
                return True
            else: 
                isOkey = True
        if k > i and data[k][j] >= data[i][j]:
            isOkey = False
            
    if isOkey:
        return True
    else: 
        isOkey = True

    # Y
    for k in range(0, len(data[0])):
        if k < j and data[i][k] >= data[i][j]: 
            isOkey = False
        if k == j:
            if isOkey:
                return True
            else: 
                isOkey = True
        if k > j and data[i][k] >= data[i][j]: 
            isOkey = False

    return isOkey

# Part 1.
count = len(data[0]) * 2 + (len(data) - 2) * 2

for i in range(1, len(data)-1):
    for j in range(1, len(data[i])-1):
        if checkEdge(data, i, j):
            count += 1
print("Part 1:", count)

# Part 2.
def getScenicScore(data, i, j):
    scenic = 1
    view = -1
    
    # X
    for k in range(0, len(data)):
        if k < i and data[k][j] >= data[i][j]: 
            view = k
        if k == i:

            if view == -1: 
                scenic *= i
            else:
                scenic *= i - view
            view = -1
        if view == -1 and k > i and data[k][j] >= data[i][j]:
            view = k

    if view == -1: view = len(data) - 1
    scenic *= view - i


    # Y
    view = -1
    for k in range(0, len(data[0])):
        if k < j and data[i][k] >= data[i][j]: 
            view = k
        if k == j:
            if view == -1: 
                scenic *= j
            else:
                scenic *= j - view
            view = -1
        if view == -1 and k > j and data[i][k] >= data[i][j]: 
            view = k
    
    if view == -1: view = len(data[0])-1
    
    scenic *= view - j
    return scenic

scenic = []
for i in range(1, len(data)-1):
    for j in range(1, len(data[i])-1):
        scenic.append(getScenicScore(data, i, j))


print("Part 2:", max(scenic))