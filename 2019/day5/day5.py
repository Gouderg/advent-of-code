
opcode = []

with open("input.txt","r") as file:
    opcode = file.readline().split(',')
    opcode = [int(opcode[i]) for i in range(len(opcode))]

i = 0
while True:

    if opcode[i] == 3 or opcode[i] == 4:
        i += 2
    elif opcode[i] >= 0 and opcode[i] <= 2 or len(opcode) >= 4:
        i += 4

    if opcode[i] == 99:
        break
    
    print(opcode[i])


    