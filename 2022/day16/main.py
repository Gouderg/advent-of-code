import heapq

# Extract data.
data = {}
with open("input2.txt", "r") as file:
    for row in file:
        row = row.replace("\n", "").split(' ')
        data[row[1]] = {"rate": int(row[4].replace('rate=', '').replace(';', ''))}
        other = [elt.replace(',','') for elt in row[9:]]
        data[row[1]]["valves"] = other


# Part 1.


# Faire une fonction qui évalue le meilleure coup à jouer. il faut maximiser les gros coups à jouer à un instant t depuis n'importe qu'elle point.
def findBestCoup(opens, starting, mins):
    best_coup = {}
    visited = []
    q = [starting]
    while(len(q) != 0) and mins > 0:

        mins -= 1
        actual_node = q.pop(0)
        
        if actual_node not in best_coup and actual_node not in opens:
            best_coup[actual_node] = mins * data[actual_node]["rate"]
        
        for node in data[actual_node]["valves"]:
            if node not in visited:
                visited.append(node)
                q.append(node)

    return sorted(best_coup.items(), key=lambda item: item[1])[-1]

def findPathDurationTo(starting, end, mins):

    q = [starting]
    visited = []
    distance = 0

    while len(q) != 0:

        distance += 1
        
        node = q.pop(0)
        if node == end:
            return distance
        
        visited.append(node)

        for elt in data[node]["valves"]:
            if elt not in visited:
                q.append(elt)




pressure = 0
mins = 31
opens = []

point, score = findBestCoup(opens, "AA", mins)

print(findPathDurationTo("BB", "JJ", mins))


print("Part 1:", pressure)

# Part 2.
print("Part 2:", )
