

# Part 1.
count = 20151125
row, column = 2978, 3083
for i in range(2, 7000):
    for j in range(1, i+1):
        count = count * 252533 % 33554393
        if i-(j-1) == 2978 and j == 3083:
            print('Part 1:', count)
            break
