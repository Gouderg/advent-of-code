import operator

# Extract data.
data = []
with open('input.txt', 'r') as file:
    for row in file:
        data.append(row.replace('\n', ''))

ops = {
    'dec': operator.sub,
    'inc': operator.add,
    '<': operator.lt,
    '>': operator.gt,
    '<=': operator.le,
    '>=': operator.ge,
    '==': operator.eq,
    '!=': operator.ne
}
register = {}
maxValue = 0
for row in data:
    row = row.split(' ')

    if row[0] not in register: register[row[0]] = 0
    if row[4] not in register: register[row[4]] = 0

    if ops[row[5]](register[row[4]], int(row[6])):
        register[row[0]] = ops[row[1]](register[row[0]], int(row[2]))
    
    if max(register.values()) > maxValue:
        maxValue = max(register.values())

# Part 1.
print('Part 1:', max(register.values()))

# Part 2.
print('Part 2:', maxValue)