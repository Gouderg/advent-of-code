# Extract data.
data = []
with open("input.txt", "r") as file:
    for row in file:
        data.append(list(row.replace('\n', '')))


def recursion(i, j, value, already, score, best_score):
    if value >= ord('y') and ((i-1 >= 0 and data[i-1][j] == 'E') or (i+1 < len(data) and data[i+1][j] == 'E') or (j-1 >= 0  and data[i][j-1] == 'E') or (j+1 < len(data[0]) and data[i][j+1] == 'E')):
        # print(best_score, value, data[i][j], i, j, ord('y'), value)
        best_score.append(score)
        return best_score
    
    # Right.
    if j+1 < len(data[0]) and [i, j+1] not in already and ord(data[i][j+1]) <= value+1:
        best_score = recursion(i, j+1, ord(data[i][j+1]), already + [[i, j+1]], score + 1, best_score)

    # Up.
    if i-1 >= 0 and [i-1, j] not in already and ord(data[i-1][j]) <= value+1:
        best_score = recursion(i-1, j, ord(data[i-1][j]), already + [[i-1, j]], score + 1, best_score)
    
    # Down.
    if i+1 < len(data) and [i+1, j] not in already and ord(data[i+1][j]) <= value+1:
        best_score = recursion(i+1, j, ord(data[i+1][j]), already + [[i+1, j]], score + 1, best_score)

    # Left.
    if j-1 >= 0 and [i, j-1] not in already and ord(data[i][j-1]) <= value+1:
        best_score = recursion(i, j-1, ord(data[i][j-1]), already + [[i, j-1]], score + 1, best_score)


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

score = recursion(start[0], start[1], ord('a'), [start], 1, [])


print("Part 1:", min(score))

# Part 2.
print("Part 2:")
