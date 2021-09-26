
# Walk on each character.
def search(offset):
    count = 0
    for i in range(0, len(data)):
        if data[i] == data[(i+offset)%len(data)]:
            count += int(data[i])
    return count

# Extract data.
data = ''
with open('input.txt', 'r') as file:
    for row in file:
        data = row.replace('\n', '')

# Part 1.
print('Part 1:', search(1))

# Part 2.
print('Part 2:', search(len(data)//2))