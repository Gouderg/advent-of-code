import re

# Extract data.
data = []
with open("input.txt", "r") as file:
    for row in file:
        row = row.replace("\n", "")
        data.append(row)

# Part 1.
values = []
p = re.compile("[0-9]")
for row in data:
    exp = p.findall(row)
    values.append(int(exp[0] + exp[-1]))
print("Part 1: ", sum(values))



# Part 2.
p2 = []
digits = ['zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
find = "[0-9]|zero|one|two|three|four|five|six|seven|eight|nine"
for row in data:
    exp = [a.group(1) for a in re.finditer("(?=("+find+"))", row)] # iter deal with overlapping word like eightwo
    a = digits.index(exp[0]) if exp[0] in digits else int(exp[0])
    b = digits.index(exp[-1]) if exp[-1] in digits else int(exp[-1])
    p2.append(int(str(a) + str(b)))

print("Part 2: ", sum(p2))
