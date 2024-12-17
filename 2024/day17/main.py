
# Parse data.
prog = []
register = {}
with open("input.txt", "r") as file:
    for row in file:
        row = row.replace("\n", "")
        if row == "":
            continue
        elif "Register" in row:
            letter, value = row.replace("Register ", "").split(": ")
            register[letter] = int(value)
        else:
            prog = [int(a) for a in row.split("Program: ")[1].split(",")]


# Part 1.
ptr = 0
outs = []
while ptr < len(prog):
    needIncr = True
    opcode = prog[ptr]
    operand = prog[ptr+1]
    combo_operand = operand if operand <= 3 else 7
    if operand == 4: combo_operand = register['A']
    if operand == 5: combo_operand = register['B']
    if operand == 6: combo_operand = register['C']

    if opcode == 0:
        register['A'] = register['A'] // (2**combo_operand)
    
    elif opcode == 1:
        register['B'] = register['B'] ^ operand
    
    elif opcode == 2:
        register['B'] = combo_operand % 8
    
    elif opcode == 3:
        if register['A'] != 0:
            ptr = operand
            needIncr = False
    
    elif opcode == 4:
        register['B'] = register['B'] ^ register['C']
    
    elif opcode == 5:
        outs.append(combo_operand % 8)
    
    elif opcode == 6:
        register['B'] = register['A'] // (2**combo_operand)
    
    elif opcode == 7:
        register['C'] = register['A'] // (2**combo_operand)

    if needIncr:
        ptr += 2

print("Part 1:", ','.join([str(a) for a in outs]))

