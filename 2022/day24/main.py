import math

# Extract data.
board = []
with open("input.txt", "r") as file:
    for row in file:
        row = row.replace('\n', '')
        board.append(list(row))

# Constante.
direction = {'>': 0, 'v': 1, '<': 2, '^': 3}
width, height = len(board[0]) - 2, len(board) - 2
lcm = height * width // math.gcd(height, width)

# Get the coordinate of each blizzard.
blizzard = [set() for _ in range(4)]
for i in range(len(board)):
    for j in range(len(board[0])):
        if board[i][j] in ['>', '<', '^', 'v']:
            blizzard[direction[board[i][j]]].add((i-1, j-1))

def crossing_blizzard(amount_time, start, target):
    si, sj = start
    q = [(si, sj, amount_time)]
    already = set()

    while q:
        i, j, t = q.pop(0)
        t += 1

        # Explore the neighboors.
        for di, dj in [(0, 1), (0, -1), (-1, 0), (1, 0), (0, 0)]:
            ni = i + di
            nj = j + dj
        
            # If the target.
            if (ni, nj) == target:
                return t
            
            # Out the map.
            if (ni < 0 or nj < 0 or ni >= height or nj >= width) and not (ni, nj) == (-1, 0):
                continue
            # Check the blizzard.
            for index, ti, tj in ((0, 0, 1), (1, 1, 0), (2, 0, -1), (3, -1, 0)):
                if ((ni - ti * t) % height, (nj - tj * t) % width) in blizzard[index]:
                    break
            else:
                key = (ni, nj, t % lcm)
                if key not in already:
                    already.add(key)
                    q.append((ni, nj, t))

# Part 1.
start = (-1, 0)
end = (height, width - 1)
l1 = crossing_blizzard(0, start, end)
print("Part 1:", l1)

# Part 2.
l2 = crossing_blizzard(l1, end, start)
print("Part 2:", crossing_blizzard(l2, start, end))
