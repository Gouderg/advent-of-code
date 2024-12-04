# Parse data.
data = []
with open("input.txt", "r") as file:
    for row in file:
        data.append(row.replace("\n", ""))


# Part 1.
cpt = 0

# left right
for i in range(0, len(data)):
    for j in range(0, len(data[0])-3):
        if data[i][j:j+4] == "XMAS" or data[i][j:j+4][::-1] == "XMAS":
            cpt += 1
    

# diag top left bottom right
for i in range(0, len(data)-3):
    for j in range(0, len(data[0])-3):
        word = data[i][j] + data[i+1][j+1] + data[i+2][j+2] + data[i+3][j+3]
        if word == "XMAS" or word[::-1] == "XMAS":
            cpt += 1

# diag top right bottom left
for i in range(0, len(data)-3):
    for j in range(len(data[0])-1, 2, -1):
        word = data[i][j] + data[i+1][j-1] + data[i+2][j-2] + data[i+3][j-3]

        if word == "XMAS" or word[::-1] == "XMAS":
            cpt += 1


# Top bottom
for i in range(0, len(data)-3):
    for j in range(0, len(data[0])):
        word = data[i][j] + data[i+1][j] + data[i+2][j] + data[i+3][j]
        if word == "XMAS" or word[::-1] == "XMAS":
            cpt += 1


print("Part 1:", cpt)


# Part 2.
cpt = 0
for i in range(0, len(data)-2):
    for j in range(0, len(data)-2):


        tl, tr = data[i][j], data[i][j+2]
        cc = data[i+1][j+1]
        bl, br = data[i+2][j], data[i+2][j+2]
        if cc != "A": continue

        """
            M.M
            .A.
            S.S
        """
        if tl == "M" and tr == "M" and bl == "S" and br == "S":
            cpt += 1

        """
            S.M
            .A.
            S.M
        """
        if tl == "S" and tr == "M" and bl == "S" and br == "M":
            cpt += 1

        """
            S.S
            .A.
            M.M
        """
        if tl == "S" and tr == "S" and bl == "M" and br == "M":
            cpt += 1

        """
            M.S
            .A.
            M.S
        """
        if tl == "M" and tr == "S" and bl == "M" and br == "S":
            cpt += 1


print("Part 2:", cpt)