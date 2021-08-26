def checkPart1(bot):
    for key in bot:
        if 17 in bot[key] and 61 in bot[key]:
            print('Part 1:', key)
            return False
    return True

# Extract data.
instructions = []
with open('input.txt', 'r') as file:
    for row in file:
        instructions.append(row.strip().split(' '))

# Part 1.
bot = {}

# Find init value.
for row in instructions:
    if 'value' in row:
        if int(row[5]) not in bot:
            bot[int(row[5])] = []
        
        bot[int(row[5])].append(int(row[1]))

# Follow instructions.
while checkPart1(bot):

    # Find a bot who have 2 elt
    ids = 0
    for key in bot:
        if len(bot[key]) == 2:
            ids = key
            break

    # Find the good line
    for row in instructions:
        if 'high' in row and int(row[1]) == ids:
            if row[5] == 'bot':
                if int(row[6]) not in bot:
                    bot[int(row[6])] = []
                # print(ids)
                bot[int(row[6])].append(min(bot[ids]))
            bot[ids].remove(min(bot[ids]))
            if row[10] == 'bot':
                if int(row[11]) not in bot:
                    bot[int(row[11])] = []
                bot[int(row[11])].append(max(bot[ids]))
            bot[ids].remove(max(bot[ids]))
            break


# Part 2.
bot, nbLigne, output = {}, 0, {}

# Find init value.
for row in instructions:
    if 'value' in row:
        if int(row[5]) not in bot:
            bot[int(row[5])] = []
        
        bot[int(row[5])].append(int(row[1]))
        nbLigne += 1

# Follow instructions.
while nbLigne < len(instructions):

    # Find a bot who have 2 elt
    ids = 0
    for key in bot:
        if len(bot[key]) == 2:
            ids = key
            nbLigne += 1
            break
    
    # Find the good line
    for row in instructions:
        if 'high' in row and int(row[1]) == ids:
            
            if row[5] == 'bot':
                if int(row[6]) not in bot: bot[int(row[6])] = []
                bot[int(row[6])].append(min(bot[ids]))
            
            elif row[5] == 'output':
                output[int(row[6])] = min(bot[ids])
            
            
            if row[10] == 'bot':
                if int(row[11]) not in bot: bot[int(row[11])] = []
                bot[int(row[11])].append(max(bot[ids]))
            
            elif row[10] == 'output':
                output[int(row[11])] = max(bot[ids])
            
            bot[ids].remove(min(bot[ids]))
            bot[ids].remove(max(bot[ids]))
            break

print('Part 2:', output[0] * output[1] * output[2])
