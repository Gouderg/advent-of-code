# Extract data.
data = []
with open("input.txt", "r") as file:
    for row in file:
        data.append(row.replace("\n", ""))

# Part 1.
count = 0
for row in data:
    for i, letter in enumerate(row):
        val = 1
        if letter == '-': val = -1
        elif letter == "=": val = -2
        else: val = int(letter)
        count += (val * 5**(len(row)-i-1))

snafu = ""

while count:
    r = count % 5
    count //= 5
    if r <= 2:
        snafu = str(r) + snafu
    else:
        val = "=" if r == 3 else "-"
        snafu = val + snafu
        count += 1

print("Part 1:", snafu)

