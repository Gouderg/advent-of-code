# Extract data.
instructions = []
with open("input.txt", "r") as file:
    for row in file:
        instructions.append(row.replace('\n', ''))

def check(cycle, X):
    if cycle in [20, 60, 100, 140, 180, 220]:
        return cycle * X
    return 0

# Part 1.
signal, cycle, X = 0, 1, 1
for row in instructions:
    if "noop" in row:
        cycle += 1
        signal += check(cycle, X)
    else:
        cycle += 1
        signal += check(cycle, X)
        cycle += 1
        X += int(row.split(' ')[1])
        signal += check(cycle, X)

print("Part 1:", signal)

# Part 2.
def incr_crt(crt, display, X):
    crt += "#" if len(crt) in [X, X+1, X-1] else "."
    if len(crt) == 40:
        display.append(crt)
        crt = ""

    return crt, display
display = []
signal, cycle, X = 0, 1, 1
crt = ""
for row in instructions:
    if "noop" in row:
        crt, display = incr_crt(crt, display, X)
        cycle += 1
        signal += check(cycle, X)
    else:
        crt, display = incr_crt(crt, display, X)
        cycle += 1
        signal += check(cycle, X)
        
        crt, display = incr_crt(crt, display, X)
        cycle += 1
        X += int(row.split(' ')[1])
        signal += check(cycle, X)

print("Part 2:")
[print(row) for row in display]