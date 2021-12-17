import itertools

def solve(board, p2):
    # Number of cycle.
    for _ in range(6):
        new_board, check_board = set(), set()

        # On récupère tous les voisins
        for (x, y, z, w) in board:
            for dx, dy, dz, dw in itertools.product([-1,0,1], repeat=4):
                if w + dw == 0 or p2:
                    check_board.add((x+dx, y+dy, z+dz, w+dw))

        # On parcours chaque voisins
        for (x, y, z, w) in check_board:
            nbr = 0
            # Pour chaque voisin on regarde le nombre de voisins
            for dx, dy, dz, dw in itertools.product([-1,0,1], repeat=4):
                if dx != 0 or dy != 0 or dz != 0 or dw != 0:
                    if (x+dx, y+dy, z+dz, w+dw) in board:
                        nbr += 1
            # Règles de Conway.
            if (x, y, z, w) not in board and nbr == 3:
                new_board.add((x, y, z, w))
            if (x, y, z, w) in board and nbr in [2,3]:
                new_board.add((x, y, z, w))

        board = new_board
    return board


# Extract data.
board = set()
with open('input.txt', 'r') as file:
    for i, row in enumerate(file):
        for j, car in enumerate(row):
            if car == "#":
                board.add((i, j, 0, 0))


print("Part 1:", len(solve(board, False)))
print("Part 2:", len(solve(board, True)))
