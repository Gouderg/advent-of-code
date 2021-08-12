import math

def allDivisor(n):
    toReturn = []
    for i in range(1,int(math.sqrt(n)+1)):
        if n % i == 0:
            if n / i == i:
                toReturn.append(i)
            else:
                toReturn.append(i)
                toReturn.append(int(n/i))

    return toReturn

puzzle = 34000000

# Part 1.
n = 786200
while True:
    test, present = allDivisor(n), 0
    for elt in test:
        present += elt * 10

    if present >= puzzle:
        print('Part 1:', n)
        break
    n += 1

# Part 2.
n = 1
compte = {}
while True:
    test, present = allDivisor(n), 0
    for elt in test:
        if elt not in compte:
            compte[elt] = 1
        else:
            compte[elt] += 1
        if compte[elt] <= 50:        
            present += elt * 11

    if present >= puzzle:
        print('Part 2:', n)
        break
    n += 1
    