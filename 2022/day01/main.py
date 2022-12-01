
# Extract data.
scores, count = [], 0
with open("input.txt", "r") as file:
    for row in file:
        row = row.replace("\n", "")
        if row == "":
            scores.append(count)
            count = 0
        else:
            count += int(row)


# Part 1.
print("Part 1: ", sorted(scores)[-1])


# Part 2.
print("Part 2: ", sum(sorted(scores)[len(scores)-3:len(scores)]))
    