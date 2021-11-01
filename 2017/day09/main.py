
# Extract data.
data = []
with open('input2.txt', 'r') as file:
    for row in file:
        data.append(row.replace('\n', '').replace(',',''))

# Part 1.

for instruc in data:
    ouverture, score = 0, 0
    isOkey = True
    isChapeau = False
    for letter in instruc:
        if not(isOkey) and letter == '>':
            # ouverture -= 1
            isOkey = False
        elif not(isOkey):
            isOkey = True
        
        elif letter == '!':
            isOkey = False
        elif letter == '{':
            ouverture += 1
        elif letter == '}':
            score += ouverture
            ouverture -= 1
        elif letter == '<':
            isChapeau = True

    print('Part 1:', score)