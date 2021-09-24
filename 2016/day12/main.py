
def execute(initializer):
    index = 0
    register = {'a': 0, 'b': 0, 'c': initializer, 'd': 0}
    while (index < len(data)):

        temp = data[index].split(' ')
        
        if len(temp) == 3:
            if temp[0] == 'cpy':
                if temp[1].isnumeric():
                    register[temp[2]] = int(temp[1])
                else:
                    register[temp[2]] = register[temp[1]]
                index += 1
            else:
                if temp[1].isnumeric() and int(temp[1]) != 0 or register[temp[1]] != 0:
                    index += int(temp[2])
                else:
                    index += 1
        else:
            if temp[0] == 'inc':
                register[temp[1]] += 1
            else:
                register[temp[1]] -= 1

            index += 1
    return register['a']

# Extract data.
data = []
with open('input.txt', 'r') as file:
    for row in file:
        data.append(row.replace('\n', ''))


# Part 1.
print('Part 1:', execute(0))

# Part 2.
print('Part 2:', execute(1))