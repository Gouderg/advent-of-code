def intcode(opcode):
    for i in range(0,len(opcode_clean),4):
        if opcode_clean[i] == 99:
            break
        
        elif opcode_clean[i] == 1:
            opcode[opcode_clean[i+3]] = opcode[opcode_clean[i+1]] + opcode[opcode_clean[i+2]]

        elif opcode_clean[i] == 2:
            opcode[opcode_clean[i+3]] = opcode[opcode_clean[i+1]] * opcode[opcode_clean[i+2]]
    
    return opcode[0]

opcode_clean, opcode  = [], []

with open("input.txt","r") as file:
    row = file.read().split(',')

    for i in row:
        opcode_clean.append(int(i))

for i in range(0,99):
    for j in range(0,99):
        opcode_clean[1] = i
        opcode_clean[2] = j
        opcode = opcode_clean[:]

        if intcode(opcode) == 19690720:
            print(100 * i + j)




