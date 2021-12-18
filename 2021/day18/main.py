import json
from math import ceil, floor

def find_left_neighbour(str1):
    a = []
    for j in range(0, len(str1)):
        if str1[j].isnumeric() and str1[j+1].isnumeric():
            a.append((j, j+1, int(str1[j:j+2])))
        elif str1[j].isnumeric() and not(str1[j-1].isnumeric()):
            a.append((j, j, int(str1[j])))
    if not a:
        b, c, d = None, None, None
    else:
        b, c, d = a[-1][0], a[-1][1], a[-1][2]
    return b, c, d

def find_right_neighbour(index, chaine):
    for j in range(0, len(chaine)):
        if chaine[j].isnumeric() and chaine[j+1].isnumeric():
            return index + j, index + j+1, int(chaine[j:j+2])
        elif chaine[j].isnumeric():
            return index + j, index + j, int(chaine[j])
    return None, None, None

def isValid(index, chaine):
    valid = ''
    for i in range(index+1, len(chaine)):
        if chaine[i] == ']':
            break
        valid += chaine[i]
    valid = valid.split(',')
    if valid[0].isnumeric() and valid[1].isnumeric():
        return i, int(valid[0]), int(valid[1])

    return -1, 0, 0

def addition(s1, s2):
    s3 = str([s1, s2]).replace(' ', '')

    while True:
        isExplode, isSplit = False, False
        open_bracket = 0
        
        # Explode.
        n_s3, i = "", 0
        while i < len(s3):
            if s3[i] == '[': open_bracket += 1
            elif s3[i] == ']': open_bracket -= 1
            
            if open_bracket >= 5:
                j, v1, v2 = isValid(i, s3)
                if j != -1:
                    i_L_min, i_L_max, v_L = find_left_neighbour(s3[:i])
                    i_R_min, i_R_max, v_R = find_right_neighbour(j, s3[j:])

                    if i_L_min != None:
                        n_s3 = s3[:i_L_min] + str(v_L + v1) + s3[i_L_max+1:i] + '0'
                    else:
                        n_s3 = s3[:i] + '0'
                    
                    if i_R_min != None:
                        n_s3 += s3[j+1:i_R_min] + str(v_R + v2) + s3[i_R_max+1:]
                    else:
                        n_s3 += s3[j+1:]

                    isExplode = True
                    s3 = n_s3

                    break
            i += 1
            
        # Split.
        if not(isExplode):
            n_s3 = ""
            for i in range(0, len(s3)):
                if i+2 < len(s3) and s3[i:i+2].isnumeric():
                    left = floor(int(s3[i:i+2]) / 2)
                    right = ceil(int(s3[i:i+2]) / 2)
                    n_s3 = s3[:i] + '[' + str(left) + ',' + str(right) + ']' + s3[i+2:]
                    isSplit = True
                    s3 = n_s3
                    break
        
        if not(isExplode) and not(isSplit):
            return json.loads(s3)

def isMagnitude(index, somme):
    valid = ''
    for i in range(index+1, len(somme)):
        if somme[i] == ']':
            break
        valid += somme[i]
    valid = valid.split(',')    
    if valid[0].isnumeric() and valid[1].isnumeric():
        return i, str(int(valid[0]) * 3 + int(valid[1]) * 2)
    
    return -1, None

def magnitude(somme):
    somme = str(somme).replace(' ', '')
    while True:
        i = 0
        while i < len(somme):

            if somme[i] == '[':
                j, val = isMagnitude(i, somme)
                if j != -1:
                    n_somme = somme[:i] + val + somme[j+1:]
                    somme = n_somme
                    break
            i += 1
        if somme.isnumeric():
            return int(somme)

# Extract data.
data = []
with open("input.txt", "r") as file:
    for row in file:
        data.append(json.loads(row.replace("\n", "")))


# Part 1.
somme = data[0]
for k in range(1, len(data)):
    somme = addition(somme, data[k])

print("Part 1:", magnitude(somme))


# Part 2.
magnitude_max = 0
for i in range(0, len(data)):
    for j in range(0, len(data)):
        magni = magnitude(addition(data[i], data[j]))
        if magni > magnitude_max:
            magnitude_max = magni

print("Part 2:", magnitude_max)

