
def calc(data, a, b):
    register = {'a': a, 'b': b}
    i = 0
    while i < len(data):    
        if data[i][0] == 'hlf':
            register[data[i][1]] = register[data[i][1]] // 2
            i += 1 
        
        elif data[i][0] == 'tpl':
            register[data[i][1]] = register[data[i][1]] * 3
            i += 1 
        
        elif data[i][0] == 'inc':
            register[data[i][1]] += 1
            i += 1
        
        elif data[i][0] == 'jmp':
            i += int(data[i][1])
        
        elif data[i][0] == 'jie':
            if register[data[i][1]] % 2 == 0:
                i += int(data[i][2])
            else:
                i += 1
        elif data[i][0] == 'jio':
            if register[data[i][1]] == 1:
                i += int(data[i][2])
            else:
                i += 1
    return register

# Extract data.
data = []
with open('input.txt', 'r') as file:
    for row in file:
        data.append(row.replace('\n','').replace(',','').split(' '))



print('Part 1:', calc(data, 0, 0)['b'])
print('Part 2:', calc(data, 1, 0)['b'])