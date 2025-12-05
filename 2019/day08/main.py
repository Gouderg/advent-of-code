
data = ""
INPUT_TXT = "input.txt"
with open(INPUT_TXT, "r") as file:
    for row in file:
        row = row.replace("\n", "")
        data = row

w, h = (2, 2) if INPUT_TXT != "input.txt" else (25, 6)

# Part 1.
cpt = 0
layers = []
for i in range(0, len(data), w*h):
    layers.append(data[i:i+w*h])

least_0_layer, num_0 = [], 10000000
for layer in layers:
    if layer.count('0') < num_0:
        least_0_layer, num_0 = layer, layer.count('0')

print("Part 1:", least_0_layer.count('1') * least_0_layer.count('2'))

# Part 2.
cpt = 0

final_layer = ['2' for _ in range(0, w*h)]
for layer in layers:
    for i in range(0, len(layer)):
        if final_layer[i] == '2' and layer[i] != '2':
            final_layer[i] = layer[i]

print("Part 2: ")
[print(''.join(final_layer[w*i:w*i+w]).replace('0', ' ').replace('1', '⣿')) for i in range(0, h)]

