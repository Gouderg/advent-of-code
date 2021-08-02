entry = "3113322113"

# Part 1.
for _ in range(40):

    newChaine, i, lastValue, count = "", 0, "", 1
    # On parrcours la chaine
    while i < len(entry):

        if i+1 < len(entry) and entry[i] == entry[i+1]:
            count += 1
        else:
            newChaine += str(count)+entry[i]
            count = 1
        i += 1
    entry = newChaine
    

print("Part 1:", len(entry))

# Part 2.
entry = "3113322113"
for _ in range(50):

    newChaine, i, lastValue, count = "", 0, "", 1
    # On parrcours la chaine
    while i < len(entry):

        if i+1 < len(entry) and entry[i] == entry[i+1]:
            count += 1
        else:
            newChaine += str(count)+entry[i]
            count = 1
        i += 1
    entry = newChaine
    

print("Part 2:", len(entry))