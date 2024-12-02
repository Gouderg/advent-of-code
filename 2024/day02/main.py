# Parse data.
data = []

with open("input.txt", "r") as file:
    for row in file:
        row = [int(a) for a in row.replace("\n", "").split(" ")]
        data.append(row)

def isSafe(report):
    isIncrease = report[1] - report[0] > 0
    for i in range(len(report)-1):

        diff = abs(report[i+1] - report[i])
        if diff < 1 or diff > 3: return False

        local_isIncrease = report[i+1] - report[i] > 0
        if isIncrease != local_isIncrease: return False

    return True

# Part 1.
cpt = 0

for report in data:
    cpt += 1 if isSafe(report) else 0
    
print("Part 1:", cpt)



# Part 2.
cpt = 0
for report in data:
    
    if isSafe(report):
        cpt += 1
        continue

    for i in range(len(report)):
        sub_report = report[0:i] + report[i+1:len(report)]
        if isSafe(sub_report):
            cpt += 1
            break
    
print("Part 2:", cpt)