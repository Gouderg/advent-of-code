
data = []

with open("input.txt", "r") as file:
    for row in file:
        data.append([int(a) for a in row.replace("\n", "").split(" ")])



# Part 1.
cpt = 0
for sequence in data:

    # Extract 
    arr = [sequence]
    while arr[-1].count(0) != len(arr[-1]):
        a = []
        for i in range(0, len(arr[-1])-1):
            a.append(arr[-1][i+1] - arr[-1][i])
        arr.append(a)
    
    # Extrapolate
    for i in range(len(arr)-1, 0, -1):
        arr[i-1].append(arr[i][-1]+arr[i-1][-1])

    cpt += arr[0][-1] 

print("Part 1:", cpt)

# Part 2.
cpt = 0
for sequence in data:

    # Extract 
    arr = [sequence[::-1]]
    while arr[-1].count(0) != len(arr[-1]):
        a = []
        for i in range(0, len(arr[-1])-1):
            a.append(arr[-1][i+1] - arr[-1][i])
        arr.append(a)
    
    # Extrapolate
    for i in range(len(arr)-1, 0, -1):
        arr[i-1].append(arr[i][-1]+arr[i-1][-1])

    cpt += arr[0][-1] 

print("Part 2:", cpt)