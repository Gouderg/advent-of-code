# Parse data.
rules_after, rules_before, pages = {}, {}, []

with open("input.txt", "r") as file:
    for row in file:
        row = row.replace("\n", "")

        if row == "": continue

        elif '|' in row:
            a, b = [int(c) for c in row.split("|")]

            if a not in rules_before:
                rules_before[a] = []
            rules_before[a].append(b) 

            if b not in rules_after:
                rules_after[b] = []
            rules_after[b].append(a) 

        else:
            pages.append([int(a) for a in row.split(",")])
    
def check(p):
    for i in range(0, len(p)):
        for elt in p[i+1:]:
            if p[i] in rules_before and elt not in rules_before[p[i]]:
                return False
        
        for elt in p[0:i]:
            if p[i] in rules_after and elt not in rules_after[p[i]]:
                return False
    return True

# Part 1.
cpt = 0
pages_to_sort = []
for page in pages:

    if check(page):
        cpt += page[len(page)//2]
    else:
        pages_to_sort.append(page)

print("Part 1:", cpt)


# Part 2.
cpt = 0

for page in pages_to_sort:

    while not check(page):

        for i in range(0, len(page)):
            needBreak = False
            for j in range(0,len(page[i+1:])):
                if page[i] in rules_before and page[i+1+j] not in rules_before[page[i]]:
                    page[i], page[i+1+j] = page[i+1+j], page[i]
                    needBreak = True
                    break
            
            for j in range(0,len(page[0:i])):
                if page[i] in rules_after and page[j] not in rules_after[page[i]]:
                    page[i], page[j] = page[j], page[i]
                    needBreak = True
                    break
            if needBreak: break

    cpt += page[len(page)//2]

print("Part 2:", cpt)