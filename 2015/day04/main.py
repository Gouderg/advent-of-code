import hashlib

# Input.
puzzle = 'iwrupvqb'

# Part 1.
i = 0
while True:
    str2hash = puzzle + str(i)
    result = hashlib.md5(str2hash.encode())
    if result.hexdigest()[0:5] == '00000':
        print("Part 1:", i)
        break
    i += 1

# Part 2.
i = 0
while True:
    str2hash = puzzle + str(i)
    result = hashlib.md5(str2hash.encode())
    if result.hexdigest()[0:6] == '000000':
        print("Part 2:", i)
        break
    i += 1