def gv(d, mode, i):
    return i if mode else d[i]

# Part 1.


def part1():

    data = []

    with open("input.txt", "r") as file:
        for row in file:
            row = row.replace("\n", "")
            data = [int(a) for a in row.split(",")]

    parameters, pos = 1, 0

    try:
        while True:
            opt_code = data[pos] % 10
            p3, p2, p1 = data[pos] % 100000 // 10000, data[pos] % 10000 // 1000, data[pos] % 1000 // 100

            if opt_code == 1:
                data[gv(data, p3, pos+3)] = data[gv(data, p2, pos+2)] + data[gv(data, p1, pos+1)] 
            elif opt_code == 2:
                data[gv(data, p3, pos+3)] = data[gv(data, p2, pos+2)] * data[gv(data, p1, pos+1)] 
            elif opt_code == 3:
                data[gv(data, p1, pos+1)] = parameters
            elif opt_code == 4:
                to_show = data[gv(data, p1, pos+1)]
                if to_show != 0:
                   return to_show
            elif opt_code == 99:
                break

            pos += 2 if opt_code in [3, 4] else 4
    except:
        pass


print("Part 1:", part1())


# Part 2.
def part2():

    data = []

    with open("input.txt", "r") as file:
        for row in file:
            row = row.replace("\n", "")
            data = [int(a) for a in row.split(",")]

    parameters, pos = 5, 0

    try:
        while True:
            opt_code = data[pos] % 10
            p3, p2, p1 = data[pos] % 100000 // 10000, data[pos] % 10000 // 1000, data[pos] % 1000 // 100

            if opt_code == 1:
                data[gv(data, p3, pos+3)] = data[gv(data, p2, pos+2)] + data[gv(data, p1, pos+1)] 
            
            elif opt_code == 2:
                data[gv(data, p3, pos+3)] = data[gv(data, p2, pos+2)] * data[gv(data, p1, pos+1)] 
            
            elif opt_code == 3:
                data[gv(data, p1, pos+1)] = parameters
            
            elif opt_code == 4:
                return data[gv(data, p1, pos+1)]
            
            elif opt_code == 5:
                pos = data[gv(data, p2, pos+2)] if data[gv(data, p1, pos+1)] != 0 else pos + 3
            
            elif opt_code == 6:
                pos = data[gv(data, p2, pos+2)] if data[gv(data, p1, pos+1)] == 0 else pos + 3

            
            elif opt_code == 7:
                data[gv(data, p3, pos+3)] = 1 if data[gv(data, p1, pos+1)] < data[gv(data, p2, pos+2)] else 0
            
            elif opt_code == 8:
                data[gv(data, p3, pos+3)] = 1 if data[gv(data, p1, pos+1)] == data[gv(data, p2, pos+2)] else 0
            
            elif opt_code == 99:
                break
            
            if opt_code in [3, 4]:
                pos += 2
            elif opt_code in [1, 2, 7, 8]:
                pos += 4
    except:
        pass
    
print("Part 2:", part2())
