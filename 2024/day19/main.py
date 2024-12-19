# Parse data.
from tqdm import tqdm
from functools import cache

data, available = [], []

with open("input.txt", "r") as file:
    for i, row in enumerate(file):
        row = row.replace("\n", "")
        if row == "": continue
        elif i == 0:
            available = row.split(", ")
        else:        
            data.append(row)


# Part 1.
cpt = 0

def find(start, stop, pos, seen):
    if True in seen: return
    if start == stop:
        seen.append(True)
        return seen

    for sa_n, st_n in pos:
        if start != sa_n: continue

        seen = find(st_n, stop, pos, seen)
        if True in seen: break
    return seen


for towel in tqdm(data, total=len(data)):
    index_start = []
    for a in available:
        if a not in towel: continue
        last_index = 0
        for _  in range(towel.count(a)):
            iss = towel[last_index:].find(a)
            index_start.append((last_index+iss,last_index+iss+len(a))) 
            last_index += iss + 1
    
    seen = find(0, len(towel), index_start, [])
    if True in seen:
        cpt += 1

print("Part 1:", cpt)

# Part 2.
cpt = 0
max_size = max([len(a) for a in available])

@cache
def find_pattern(towel):

    if towel == "": return 1
    counter = 0
    for i in range(min(len(towel), max_size)+1):
        if towel[:i] in available:
            counter += find_pattern(towel[i:])

    return counter


for towel in tqdm(data, total=len(data)):
    cpt += find_pattern(towel)    


print("Part 2:", cpt)
