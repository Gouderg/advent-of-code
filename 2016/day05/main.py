import hashlib

# Extract data.
puzzle = 'ugkcyxxp'

# Part 1.
indice = 0
output = ''
for i in range(0,8):

    result = hashlib.md5((puzzle + str(indice)).encode()).hexdigest()
    while result[:5] != '00000':
        indice += 1
        result = hashlib.md5((puzzle + str(indice)).encode()).hexdigest()

    output += result[5]
    indice += 1

print('Part 1:', output)

# Part 2.
indice = 0
output = [0] * 8
while True:
    while True:
        result = hashlib.md5((puzzle + str(indice)).encode()).hexdigest()
        indice += 1
        if result[:5] == '00000' and result[5].isnumeric() and int(result[5]) in [0,1,2,3,4,5,6,7]:
            if output[int(result[5])] == 0:
                output[int(result[5])] = result[6]
            break
    if 0 not in output:
        break


print('Part 2:', ''.join(output))
