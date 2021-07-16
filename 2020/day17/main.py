
# Number of cycle
cycle = 6

#Tqbleau de cellules active et non active
cell = []

# Fonction qui compte le nombre de case active
def countActive(cell):
    pass

with open("input.txt", "r") as file:
    for row in file:
        cell.append(list(row.replace('\n','')))

print(cell)