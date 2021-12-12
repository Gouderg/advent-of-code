
# Extract data.
instructions = []
with open('input.txt', 'r') as file:
    for row in file:
        instructions.append(row.replace('\n', '').split('-'))

# Create dictionnary
graph = {}
for row in instructions:

    if row[0] not in graph:
        graph[row[0]] = []
    if row[1] != 'start':
        graph[row[0]].append(row[1])
    
    if row[1] not in graph:
        graph[row[1]] = []
    if row[0] != 'start':
        graph[row[1]].append(row[0])

del graph['end']

def solve(next_elt, actual_path, path):
    
    if next_elt == 'end':
        return path + 1

    for elt in graph[next_elt]:
        if elt not in actual_path or elt.isupper():
            path = solve(elt, actual_path + [elt], path)

    return path

def solve2(next_elt, actual_path, path, isOkey):
    
    if next_elt == 'end':
        return path + 1

    for elt in graph[next_elt]:
        if elt not in actual_path or elt.isupper():
            path = solve2(elt, actual_path + [elt], path, isOkey)

        elif elt in actual_path and elt.islower() and isOkey:
            path = solve2(elt, actual_path + [elt], path, False)
            
    return path


# Part 1.
actual_path = ['start']
path = 0

for elt in graph['start']:
    path = solve(elt, actual_path + [elt], path)

print("Part 1:", path)


# Part 2.
actual_path = ['start']
path = 0

for elt in graph['start']:
    path = solve2(elt, actual_path + [elt] , path, True)

print("Part 2:", path)