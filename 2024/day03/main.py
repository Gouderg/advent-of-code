# Parse data.
data = ""
with open("input.txt", "r") as file:
    for row in file:
        data += row.replace("\n", "")

def get_result_from_subsequence(subsequence: str):
    cpt = 0
    for a in subsequence.split("mul("):
        if ',' not in a: continue
        left, rest = a.split(",")[0:2]
        
        if ')' not in rest: continue
        right, rest = rest.split(")")[0:2]


        if left.isnumeric() and right.isnumeric():
            cpt += int(left) * int(right)
    
    return cpt

# Part 1.
print("Part 1:", get_result_from_subsequence(data))


# Part 2.
cpt = 0
dont_seq = data.split("don't")

cpt += get_result_from_subsequence(dont_seq[0])

for sub in dont_seq[1:]:
    if "do" not in sub: continue

    for ssub in sub.split("do")[1:]:
        cpt += get_result_from_subsequence(ssub)

print("Part 2:", cpt)