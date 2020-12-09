import re

data, temp = [],[]

with open("input.txt", "r") as file:
    for row in file:
        if row != "\n":
            row = row.split()
            for elt in row:
                    temp.append(elt)
        else:
            data.append(temp)
            temp = []
    row = 'hgt:183cm cid:187 byr:2019 ecl:xry iyr:2013 pid:164cm hcl:#18171d eyr:2021'
    row = row.split()
    data.append(row)



nbPassport = 0
for elts in data:
    size = 0
    isHere = False
    for elt in elts:
        if 'cid' in elt:
            isHere = True
        size += 1

    if size == 8 or (size == 7 and not(isHere)):
        isValid = True
        for elt in elts:
            elt = elt.split(':')
            if 'byr' == elt[0]:
                if int(elt[1]) < 1920 or int(elt[1]) > 2002:
                    isValid = False

            if 'iyr' == elt[0]:
                if int(elt[1]) < 2010 or int(elt[1]) > 2020:
                    isValid = False
            
            if 'eyr' == elt[0]:
                if int(elt[1]) < 2020 or int(elt[1]) > 2030:
                    isValid = False
            
            if 'hgt' == elt[0]:
                if 'cm' in elt[1]:
                    if int(elt[1][:-2]) < 150 or int(elt[1][:-2]) > 193:
                        isValid = False
                
                if 'in' in elt[1]:
                    if int(elt[1][:-2]) < 59 or int(elt[1][:-2]) > 76:
                        isValid = False
                    
            if 'hcl' == elt[0]:
                if not(re.search("^#[a-z0-9]{6}$", elt[1])):
                    isValid = False
            
            if 'ecl' == elt[0]:
                color = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
                if len(elt[1]) == 3 and elt[1] in color:
                    pass
                else:
                    isValid = False

            if 'pid' == elt[0]:
                if not(re.search("^[0-9]{9}$", elt[1])):
                    isValid = False
     
        if isValid:
            nbPassport += 1

print("Part 2:", nbPassport - 1)