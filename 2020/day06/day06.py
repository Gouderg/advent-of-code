data = []

with open("input.txt","r") as file:
    for row in file:
        row = row.replace('\n','')
        data.append(row)

count1, count2 = 0,0
alphabet0, alphabet1 = [],[]

for row in data:
    if row != '':
        alphabet0.append(row)
        for elt in row:
            if elt not in alphabet1:
                alphabet1.append(elt)
    else:
        count1 += len(alphabet1)
        count2 += len(list(set.intersection(*map(set, alphabet0))))
        alphabet0, alphabet1 = [],[]

count1 += len(alphabet1)
count2 += len(list(set.intersection(*map(set, alphabet0))))
print("Part 1:", count1) 
print("Part 2:", count2)
