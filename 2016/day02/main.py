
# Extract data.
instructions = []
with open('input.txt', 'r') as file:
    for row in file:
        instructions.append(list(row.replace('\n','')))


# Part 1.
digicode = [[1,2,3],[4,5,6],[7,8,9]]
x,y = 1,1
code = ''
for row in instructions:
    for l in row:
        if l == 'R':
            x = min(x+1, 2)
        
        elif l == 'L':
            x = max(x-1, 0)
        
        elif l == 'U':
            y = max(y-1, 0)
        
        elif l == 'D':
            y = min(y+1, 2)

    code += str(digicode[y][x])


print('Part 1:', int(code))

# Part 2.
digicode = [
                ['.','.','1','.','.'],
                ['.','2','3','4','.'],
                ['5','6','7','8','9'],
                ['.','A','B','C','.'],
                ['.','.','D','.','.']
            ]
x,y = 0,2
code = ''
for row in instructions:
    for l in row:
        if l == 'R':
            x = min(x+1, 4)
            if digicode[y][x] == '.': x -= 1
            
        
        elif l == 'L':
            x = max(x-1, 0)
            if digicode[y][x] == '.': x += 1
        
        elif l == 'U':
            y = max(y-1, 0)
            if digicode[y][x] == '.': y += 1
        
        elif l == 'D':
            y = min(y+1, 4)
            if digicode[y][x] == '.': y -= 1

    code += digicode[y][x]
print('Part 2:', code)