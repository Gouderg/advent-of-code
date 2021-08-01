
# Extract data.
strings = []
with open('input.txt', 'r') as file:
    for row in file:
        # strings.append(row.replace('\n', ''))
        strings.append(row)


# Part 1.
litterals, memory = 0, 0
for row in strings:
    litterals += len(row)
    isOkey = 0
    newString = str()
    for i, elt in enumerate(row):
        if elt == '\\' and not(isOkey):
            if row[i+1] == '\\':
                isOkey = 1
                newString += '\\'
            elif row[i+1] == '"':
                newString += '"'
                isOkey = 1
            elif row[i+1] == 'x':
                isOkey = 3
                newString += 'c'
        elif isOkey:
            isOkey -= 1
        else:
            newString += elt
    #print(newString, len(newString)-2)
    memory += (len(newString) - 2)

print(litterals, memory, litterals - memory)

# Part 2.
litterals, encoding = 0, 0
for row in strings:
    litterals += len(row)
    isOkey = 0
    newString = '\\"\\"'
    for i, elt in enumerate(row):
        if elt == '\\' and not(isOkey):
            if row[i+1] == '\\':
               newString += 'cc'
               isOkey = 1
            elif row[i+1] == '"':
                newString += 'cc'
            elif row[i+1] == 'x':
                newString += 'c'
        elif isOkey:
            isOkey -= 1
        newString += elt
    #print(newString, len(newString)-2)
    print(row, newString)
    encoding += (len(newString))

print(litterals, encoding, encoding - litterals)