import heapq

def moves_available(x, y, tab):
    move = []

    if x+1 < len(tab): move.append((x+1, y))
    if y+1 < len(tab[0]): move.append((x, y+1))
    if x-1 >= 0: move.append((x-1, y))
    if y-1 >= 0: move.append((x, y-1))
    
    return move

def Dijkstra(X, Y, tab):
    # On initialise un tableau avec les valeurs (val, x, y)
    queu = [(0, 0, 0)]
    visited = [[0] * len(row) for row in tab]


    while True:
        # On extrait le plus petit élément.
        risk, x, y = heapq.heappop(queu)
        
        # Condition de sortie.
        if (x, y) == (X, Y):
            return risk

        # Si un noeud n'est pas visité.
        if not(visited[x][y]): 
            visited[x][y] = 1
            # On parcourt ses voisins et s'ils ne sont pas visité, on les ajoute à la queue.
            for nx, ny in moves_available(x, y, tab):
                if visited[nx][ny] == 0:
                    heapq.heappush(queu, (risk + tab[nx][ny], nx, ny))

# Extract data.
board = []
with open('input.txt', 'r') as file:
    for row in file:
        row = [int(a) for a in row.replace('\n', '')]
        board.append(row)

# Part 1.
print('Part 1:', Dijkstra(len(board) - 1, len(board[0]) - 1, board))


# Part 2.
# On récupère chaque variante du tableau de départ.
temp = [board]
for i in range(0, 8):
    temp.append([list(map(lambda x: (x+1) if x < 9 else 1,elt)) for elt in temp[i]])

# On crée un super tableau avec toutes les variantes.
l_board = []
for i in range(0,5):
    for j in range(0, len(temp[0])):
        l_board.append([*temp[i][j], *temp[i+1][j], *temp[i+2][j], *temp[i+3][j], *temp[i+4][j]])

print('Part 2:', Dijkstra(len(l_board) - 1, len(l_board[0]) - 1, l_board))
