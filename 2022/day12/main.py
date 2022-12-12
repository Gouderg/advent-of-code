# Extract data.
data = []
with open("input2.txt", "r") as file:
    for row in file:
        data.append(list(row.replace('\n', '')))


def recursion(i, j, value, already, score, best_score):


    return best_score

# Part 1.
# Get the start position.
start, isOkey = [], False
for i in range(0, len(data)):
    for j in range(0, len(data[i])):
        if data[i][j] == 'S':
            start, isOkey = [i, j], True
            break
    if isOkey: break

# Get the stop position.
stop, isOkey = [], False
for i in range(0, len(data)):
    for j in range(0, len(data[i])):
        if data[i][j] == 'E':
            stop, isOkey = [i, j], True
            break
    if isOkey: break



print("Part 1:", start, stop)

# Part 2.
print("Part 2:")
