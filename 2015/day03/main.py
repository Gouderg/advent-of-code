
# Extract data.
data = []
with open('input.txt', 'r') as file:
    for row in file:
        data = list(row)


# Part 1.
x, y, pos = 0, 0, []
pos.append((x,y))
for elt in data:
    # North. 
    if elt == '^':
        y += 1
    
    # East.
    elif elt == '>':
        x += 1

    # South. 
    if elt == 'v':
        y -= 1

    # West.
    elif elt == '<':
        x -= 1
    
    if (x,y) not in pos:
        pos.append((x,y))

print('Part 1:', len(pos))

# Part 2.
xS, yS, pos, xR, yR = 0, 0, [], 0, 0
pos.append((xS,yS))
for i,elt in enumerate(data):
    if i%2:
        # North. 
        if elt == '^':
            yR += 1
        
        # East.
        elif elt == '>':
            xR += 1

        # South. 
        if elt == 'v':
            yR -= 1

        # West.
        elif elt == '<':
            xR -= 1
        
        if (xR,yR) not in pos:
            pos.append((xR,yR))
    else:
        # North. 
        if elt == '^':
            yS += 1
        
        # East.
        elif elt == '>':
            xS += 1

        # South. 
        if elt == 'v':
            yS -= 1

        # West.
        elif elt == '<':
            xS -= 1
        
        if (xS,yS) not in pos:
            pos.append((xS,yS))

print('Part 1:', len(pos))