# Extract data.

# Part 1.
p1 = 10
p2 = 3

score_p1, score_p2 = 0, 0
turn = True
dice_count = 0

while True:
    rolls = (dice_count%100+1) + (dice_count%100+2) + (dice_count%100+3)
    dice_count += 3
    if turn:
        p1 = (p1 + rolls - 1) % 10 + 1
        score_p1 += p1
    else:
        p2 = (p2 + rolls - 1) % 10 + 1
        score_p2 = score_p2 + 10 if p2 == 0 else score_p2 + p2


    if score_p2 >= 1000:
        break

    if score_p1 >= 1000:
        break
    turn = not(turn)

result = score_p2 * dice_count if score_p2 < 1000 else score_p1 * dice_count
print("Part 1:", result)

# Part 2.
p1 = 10
p2 = 3

pos_dice = [x + y + z for x in [1,2,3] for y in [1,2,3] for z in [1,2,3]]
cache = {}

def solve(p1, p2, score_p1, score_p2):

    key = (p1, p2, score_p1, score_p2)
    if key in cache:
        return cache[key]

    winner = [0, 0]
    for dice in pos_dice:
        p1_ = (p1 + dice - 1) % 10 + 1
        score_p1_ = p1_ + score_p1
        if score_p1_ >= 21:
            winner[0] += 1
        else:
            w1, w2 = solve(p2, p1_, score_p2, score_p1_)
            winner[0] += w2
            winner[1] += w1

    cache[key] = winner
    return winner

print("Part 2:", max(solve(p1, p2, 0, 0)))