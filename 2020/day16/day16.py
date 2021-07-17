import random

def checkPos(pos, nearbyTicket, rules):
    isOkey, num = True, 0
    for numbers in nearbyTicket:
        isHere = True
        for i,number in enumerate(numbers):  
            if not(rules[pos[i]-1][0][0] <= number <= rules[pos[i]-1][0][1] or rules[pos[i]-1][1][0] <= number <= rules[pos[i]-1][1][1]):
                isHere = False
                num = i
        if not(isHere):
            isOkey = False
            break

    if isOkey:
        return True, num
    return False, num 

if __name__ == "__main__":
    rules, myTicket, nearbyTicket = [], [], []
    previousLine = ""
    with open("input.txt", "r") as file:
        for row in file:
            row = row.replace('\n', '')
            if ':' in row and '-' in row:
                rules.append(row.split(':'))
            elif "your ticket" in previousLine:
                row = row.split(',')
                row = [int(elt) for elt in row]
                myTicket.append(row)
            elif "nearby tickets" in previousLine:
                row = row.split(',')
                row = [int(elt) for elt in row]
                nearbyTicket.append(row)

            if previousLine == "nearby tickets:":
                pass
            else:
                previousLine = row
    
    #[print(row) for row in rules]

    ## Part 1
    error = 0
    rules = [rule[1].split(' or ') for rule in rules]
    for i,rule in enumerate(rules):
        for j,elt in enumerate(rule):
            elt = elt.split("-")
            elt = (int(elt[0]),int(elt[1]))
            rules[i][j] = elt 

    lineToSuppr = []
    for i,numbers in enumerate(nearbyTicket):
        for number in numbers:
            isHere = False
            for rule in rules:
                if rule[0][0] <= number <= rule[0][1] or rule[1][0] <= number <= rule[1][1]:
                    isHere = True
            if not(isHere):
                error += number
                lineToSuppr.append(i)

    print("Part 1: {}".format(error))
    ## Part 2
    lineToSuppr.reverse()
    for elt in lineToSuppr:
        nearbyTicket.pop(elt)
    pos = [i for i in range(1,21)]
    #pos = [i for i in range(1,4)]
    while True:
        state, num = checkPos(pos, nearbyTicket, rules)
        if state:
            print(pos)
            break
        else:
            print(pos[num])

    #print(myTicket[pos.index(1)] * myTicket[pos.index(2)] * myTicket[pos.index(3)] * myTicket[pos.index(4)] * myTicket[pos.index(5)] * myTicket[pos.index(6)])
    

    
