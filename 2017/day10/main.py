# Extract data.
data = []
with open("input.txt", "r") as file:
    for row in file:
        data = [int(a) for a in row.replace("\n", "").split(',')]



def compute(data, repeat):

    pos, skip = 0, 0
    numbers = [i for i in range(256)]
    for _ in range(repeat):
        for length in data:
            pos2 = (pos + length) % len(numbers)

            if pos2 > pos or length == 0:
                numbers[pos:pos2] = numbers[pos:pos2][::-1] 
            else:
                lt = (numbers[pos:len(numbers)] + numbers[0:pos2])[::-1]
                numbers[pos:len(numbers)] = lt[0:len(numbers)-pos]
                numbers[0:pos2] = lt[len(numbers)-pos:len(lt)]

            pos = (pos + length + skip) % len(numbers)
            skip += 1
    return numbers




# Part 1.
numbers = compute(data, 1)
print("Part 1:", numbers[0] * numbers[1])

# Part 2.
data2 = [ord(l) for l in str(data).replace(']', '').replace('[', '').replace(' ', '')] + [17, 31, 73, 47, 23]

# 64 Rounds.
numbers = compute(data2, 64)

# Dense.
new = []
for i in range(0, 256, 16):
    a = numbers[i]
    for j in range(1, 16):
        a = a ^ numbers[i+j]
    new.append(a)

# Sparse.
text = ""
for elt in new:
    text = text + "0"+hex(elt)[2] if len(hex(elt)) == 3 else text + hex(elt)[2:]

print("Part 2:", text)
