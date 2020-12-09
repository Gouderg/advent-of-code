inputs = []

with open("input.txt","r") as file:
    for row in file:
        row = row.replace('\n', '')
        inputs.append(int(row))

for nb1 in range(len(inputs)):
    for nb2 in range(nb1,len(inputs)):
        if inputs[nb1] + inputs[nb2] == 2020:
            print("Part 1:", inputs[nb1] * inputs[nb2])
        for nb3 in range(nb2,len(inputs)):
            if inputs[nb1] + inputs[nb2] + inputs[nb3] == 2020:
                print("Part 2:",inputs[nb1] * inputs[nb2] * inputs[nb3])