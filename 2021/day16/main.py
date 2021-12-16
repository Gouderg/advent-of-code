from functools import reduce

# Extract data.
data = []
with open('input.txt', 'r') as file:
    for row in file:
        data = row.replace('\n', '')

hexa = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
data_bin = ""
for elt in data:
    data_bin += hexa[elt]

def choice(type_id, packets):
    if type_id == 0: return sum(packets)
    
    elif type_id == 1: return reduce(lambda x, y: x * y, packets)
    
    elif type_id == 2: return min(packets)
    
    elif type_id == 3: return max(packets)
    
    elif type_id == 5: return 1 if packets[0] > packets[1] else 0
    
    elif type_id == 6: return 1 if packets[0] < packets[1] else 0

    elif type_id == 7: return 1 if packets[0] == packets[1] else 0

def iter_type_4(index, somme_version):

    somme_version += int(data_bin[index:index+3], 2)
    index += 6
    num = ""
    while True:
        packet = data_bin[index:index+5]
        num += packet[1:5]
        index += 5
        if packet[0] == '0':
            return index, somme_version, int(num, 2)

def iter_type_not_I(index, somme_version):
    somme_version += int(data_bin[index:index+3], 2)
    tid = int(data_bin[index+3:index+6], 2)
    index += 8
    L = int(data_bin[index: index+14], 2)
    index += 14
    length, packets = 0, []

    while length < L:
        type_id, last =  int(data_bin[index+3:index+6], 2), index

        if type_id == 4:
            index, somme_version, val = iter_type_4(index, somme_version)

        elif data_bin[index+6] == '1':
            index, somme_version, val = iter_type_I(index, somme_version)

        else:
            index, somme_version, val = iter_type_not_I(index, somme_version)

        length += index - last
        packets.append(val)
    return index, somme_version, choice(tid, packets)


def iter_type_I(index, somme_version):
    somme_version += int(data_bin[index:index+3], 2)
    tid = int(data_bin[index+3:index+6], 2)
    index += 8
    L = int(data_bin[index: index+10], 2)
    index += 10
    count, packets = 0, []

    while count < L:
        type_id =  int(data_bin[index+3:index+6], 2)

        if type_id == 4:
            index, somme_version, val = iter_type_4(index, somme_version)

        elif data_bin[index+6] == '1':
            index, somme_version, val = iter_type_I(index, somme_version)

        else:
            index, somme_version, val = iter_type_not_I(index, somme_version)

        count += 1
        packets.append(val)

    return index, somme_version, choice(tid, packets)


# First iteration.
type_id =  int(data_bin[3:6], 2)


if type_id == 4:
    _, somme_version, result = iter_type_4(0, 0)

elif data_bin[6] == '1':
    _, somme_version, result = iter_type_I(0, 0)

else:
    _, somme_version, result = iter_type_not_I(0, 0)

print("Part 1:", somme_version)
print("Part 2:", result)