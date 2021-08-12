import string
# Extract molecul chain.
chain = str()
with open('molecule.txt', 'r') as file:
    for row in file:
        chain = row.replace('\n', '')

# Extract data.
data = []
with open('input.txt', 'r') as file:
    for row in file:
        data.append(row.replace('\n', '').split(' => '))

# Part 1.
molecule = []
for ato in data:
    for i in range(0, len(chain)):
        if chain[i:i+len(ato[0])] == ato[0]:
            temp = chain[:i] + ato[1] + chain[i+len(ato[0]):]
            if temp not in molecule:
                molecule.append(temp)

print('Part 1:', len(molecule))

# Part 2.
# After some search on internet, I found : Numberofsymbol - #Rn - #Ar - 2*Y - 1
count = 0
for l in chain:
    if l.isupper():
        count += 1
print('Part 2:', count - chain.count('Rn') - chain.count('Ar') - chain.count('Y')*2 - 1)