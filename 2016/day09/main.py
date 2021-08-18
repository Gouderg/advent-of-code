def decompress(word):
    
    if '(' not in word:
        return len(word)
    
    count = 0
    while '(' in word:
        count += word.find('(')
        word = word[word.find('('):]
        pattern = word[1:word.find(')')].split('x')
        word = word[word.find(')') + 1:]
        count += decompress(word[:int(pattern[0])]) * int(pattern[1])
        word = word[int(pattern[0]):]
    
    count += len(word)
    
    return count

# Extract data.
data = []
with open('input.txt', 'r') as file:
    for row in file:
        data.append(row.replace('\n', ''))

# Part 1.
for row in data:
    word = ''
    i = 0
    while i < len(row):

        if row[i] == '(':
            pattern = ''
            i += 1
            while row[i] != ')':
                pattern += row[i]
                i += 1
            i += 1
            pattern = pattern.split('x')
            for j in range(0,int(pattern[1])):
                word += row[i:i+int(pattern[0])]
            i += int(pattern[0])
            
        else:
            word += row[i]
            i += 1
    print('Part 1:', len(word))

# Part 2.
for row in data:
    print('Part 2:', decompress(row))