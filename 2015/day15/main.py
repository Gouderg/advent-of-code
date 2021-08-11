
def checkCalorie(data, i):
    a, b, c, d = i//1000000%100, i//10000%100, i//100%100, i%100
    if (data[0][4] * a + data[1][4] * b + data[2][4] * c + data[3][4] * d) == 500:
        return True
    return False


def calcul(data, i):
    a, b, c, d, re = i//1000000%100, i//10000%100, i//100%100, i%100, 1
    
    for j in range(0,4):
        temp = (data[0][j] * a + data[1][j] * b + data[2][j] * c + data[3][j] * d)
        if temp < 0:
            return 0
        re *= temp
    return re
    

# Extract data.
recette = []
with open('input.txt', 'r') as file :
    for row in file:
        recette.append(row.replace('\n', '').replace(',', '').split(' '))

# Part 1.
result = []
data = []
for row in recette:
    data.append([int(row[2]), int(row[4]), int(row[6]), int(row[8]), int(row[10])])

for i in range(100**len(recette)):
    if i%100 + (i//100%100) + i//1000000%100 + i//10000%100 == 100:
        result.append(calcul(data, i))

print('Part 1:', max(result))

# Part 2.
result = []
for i in range(100**len(recette)):
    if i%100 + (i//100%100) + i//1000000%100 + i//10000%100 == 100 and checkCalorie(data, i):
        result.append(calcul(data, i))

print('Part 2:', max(result))