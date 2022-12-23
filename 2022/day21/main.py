import sympy

# Extract data.
data = {}
inst = []
with open("input.txt", "r") as file:
    for row in file:
        hea, cor = row.replace('\n', '').split(': ')
        data[hea] = cor
        inst.append(row.replace('\n', ''))

# Part 1.
def find(name):
    if data[name].isnumeric(): return int(data[name])

    t1, sym, t2 = data[name].split(' ')

    if sym == "+": return find(t1) + find(t2)
    if sym == "-": return find(t1) - find(t2)
    if sym == "*": return find(t1) * find(t2)
    if sym == "/": return find(t1) // find(t2)
    if sym == "=": return find(t1) == find(t2)

part1 = find('root')
print("Part 1:", part1)
    
# Part 2.
# int => sympy.Integer(expr)
monkeys = {'humn': sympy.Symbol("x")}

operation = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}

for elt in inst:
    hea, cor = elt.split(': ')
    if hea in monkeys: continue
    if cor.isnumeric(): monkeys[hea] = sympy.Integer(cor)

    else:
        t1, sym, t2 = cor.split(' ')
        if t1 in monkeys and t2 in monkeys:
            if hea == 'root':
                print("Part 2:", sympy.solve(monkeys[t1] - monkeys[t2])[0])
                break
            else:
                monkeys[hea] = operation[sym](monkeys[t1], monkeys[t2])
        else:
            inst.append(elt)

