def read_file (name, strip = True):
    with open(name) as f:
        content = f.readlines()
    if strip:
        return [x.strip() for x in content]
    return content

def isinrange (tab, n):
    for c in tab:
        if (c[0] <= n <= c[1]):
            return True, None

    return False, n

def part1 (fa):
    conditions = []
    nearbyTicket = []
    i = 0
    isHeader = True

    for l in fa:
        if l:
            if i == 0:
                s = l.split(':')
                s = s[1].split()
                v = [int(x) for x in s[0].split('-')]
                v2 = [int(x) for x in s[2].split('-')]

                conditions.append(v)
                conditions.append(v2)
            elif i == 1:
                if not isHeader:
                    li = [int(x) for x in l.split(',')]
                else:
                    isHeader = False
            elif i == 2:
                if not isHeader:
                    li = [int(x) for x in l.split(',')]
                    nearbyTicket.append(li)
                else:
                    isHeader = False
            else:
                break
        else:
            isHeader = True
            i += 1

    numsInvalid = []
    for t in nearbyTicket:
        valid = True
        for n in t:
            isvalid, num = isinrange(conditions, n)
            if not isvalid:
                valid = False
                break
        if not valid:
            numsInvalid.append(num)

    return sum(numsInvalid)


def isin4range(cond, col, n):
    return n in range(cond[col][0][0], cond[col][0][1]) or n in range(cond[col][1][0], cond[col][1][1])

def invalid_sum(fields, ticket, extra):
    header = [x for x in fields.keys()]
    total = 0
    for p in ticket:
        valid = False
        for f in header:
            if p >= fields[f][0][0] and p <= fields[f][0][1]: valid = True
            if p >= fields[f][1][0] and p <= fields[f][1][1]: valid = True
        if valid == False:
            total += (p + extra)
            # Perfect for Part 1, massive bug in Part 2 due to 0
            # value in some ticket being invalid. So add on an extra bit to fix.
            #total += p
    return total

def part2 (fb):
    cond = {}
    myTicket = []
    nearbyTicket = []
    i = 0
    isHeader = True

    for l in fb:
        if l:
            if i == 0:
                s = l.split(':')
                cat = s[0]
                s = s[1].split()
                v = [int(x) for x in s[0].split('-')]
                v2 = [int(x) for x in s[2].split('-')]
                cond[cat] = ([v[0], v[1] + 1], [v2[0], v2[1] + 1])
            elif i == 1:
                if not isHeader:
                    li = [int(x) for x in l.split(',')]
                    myTicket = li
                else:
                    isHeader = False
            elif i == 2:
                if not isHeader:
                    li = [int(x) for x in l.split(',')]
                    nearbyTicket.append(li)
                else:
                    isHeader = False
            else:
                break
        else:
            isHeader = True
            i += 1

    validTickets = [t for t in nearbyTicket if invalid_sum(cond, t, 1) == 0]
    rules = []
    for c in cond:
        positions = {p for p in range(len(myTicket))}
        for t in validTickets:
            m =  {p for p in range(len(t)) if isin4range(cond, c, t[p])}
            positions = positions.intersection(m)
        rules.append(positions)

    result  = 1
    result2 = set()
    found   = set()
    header = [x for x in cond.keys()]
    for k in range(len(myTicket)):
        for i in range(len(rules)):
            if len(rules[i]) == 1:
                if header[i].startswith('departure'):
                    p = list(rules[i])[0]
                    result = result * myTicket[p]
                    result2.add(p)
                found = found.union(rules[i])

        for j in range(len(rules)):
            rules[j] = rules[j] - found

    return result

def main ():
    f = read_file('input.txt')
    

    res = [part1(f), part2(f)]
    print(f"Part 1 = {res[0]}\nPart 2 = {res[1]}")

main()