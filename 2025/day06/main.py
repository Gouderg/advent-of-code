def part1():
    problems = {}

    with open("input.txt", "r") as file:
        for row in file:
            row = [a for a in row.replace("\n", "").split(" ") if a != '']

            for i, elt in enumerate(row):
                if i not in problems:
                    problems[i] = []
                problems[i].append(elt)



    # Part 1.
    cpt = 0

    for p in problems.values():
        nums = [int(a) for a in p[:-1]]
        if p[-1] == '*':
            tmp = 1
            for a in nums:
                tmp *= a
            cpt += tmp
        
        else:
            cpt += sum(nums)
    print("Part 1:", cpt)


def part2():
    problems = {}

    with open("input.txt", "r") as file:
        for row in file:
            row = row.replace("\n", "")

            for i, c in enumerate(row):
                if i not in problems:
                    problems[i] = []
                problems[i].append(c)
                
    cpt, i = 0, 0
    aled = [a for a in problems.values()]

    buffer = []

    while i <= len(aled):
        if i == len(aled) or i < len(aled) and len([a for a in aled[i] if a != ' ']) == 0:
            sign = buffer[0][-1]
            buffer[0] = buffer[0][:-1]
            
            tmp = 0 if sign == "+" else 1
            for b in buffer:
                v = int(''.join([a for a in b if a != ' ']))
                if sign == "*":
                    tmp *= v
                else:
                    tmp += v
            cpt += tmp
            
            buffer = []
        else:
            buffer.append(aled[i])
        i += 1



    print("Part 2:", cpt)



part1()
part2()