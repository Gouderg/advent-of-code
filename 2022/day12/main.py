# Extract data.
data = []
with open("input.txt", "r") as file:
    for row in file:
        data.append(list(row.replace('\n', '')))



# Part 1.
# Get the start position.
start, stop = [], []
for i in range(0, len(data)):
    for j in range(0, len(data[i])):
        if data[i][j] == 'S':
            start_i, start_j = i, j
            data[i][j] = "a"
        if data[i][j] == 'E':
            stop_i, stop_j = i, j
            data[i][j] = "z"


already_visited = [(start_i, start_j)]
queu = [(0, start_i, start_j)]
isOkey = False
while len(queu) > 0 and not(isOkey):
    distance, i, j = queu.pop(0)
    for next_i, next_j in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:

        if (next_i, next_j) in already_visited:
            continue

        if next_j >= len(data[0]) or next_i >= len(data) or next_i < 0 or next_j < 0:
            continue
        
        if ord(data[next_i][next_j]) - ord(data[i][j]) > 1:
            continue

        if next_i == stop_i and next_j == stop_j:
            print("Part 1:", distance+1)
            isOkey = True
            break
        
        queu.append((distance+1 , next_i, next_j))
        already_visited.append((next_i, next_j))

# Part 2.
already_visited = [(stop_i, stop_j)]
queu = [(0, stop_i, stop_j)]
isOkey = False
while len(queu) > 0 and not(isOkey):
    distance, i, j = queu.pop(0)
    for next_i, next_j in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:

        if (next_i, next_j) in already_visited:
            continue

        if next_j >= len(data[0]) or next_i >= len(data) or next_i < 0 or next_j < 0:
            continue
        
        if ord(data[i][j]) - ord(data[next_i][next_j]) > 1:
            continue

        if data[next_i][next_j] == "a":
            print("Part 2:", distance+1)
            isOkey = True
            break
        
        queu.append((distance+1 , next_i, next_j))
        already_visited.append((next_i, next_j))