from itertools import permutations

def gv(d, mode, i):
    return i if mode else d[i]

def intcode(params):

    data = []

    with open("input.txt", "r") as file:
        for row in file:
            row = row.replace("\n", "")
            data = [int(a) for a in row.split(",")]
    
    pos, index_p = 0, 0
    try:
        while True:
            opt_code = data[pos] % 10
            p3, p2, p1 = data[pos] % 100000 // 10000, data[pos] % 10000 // 1000, data[pos] % 1000 // 100

            if opt_code == 1:
                data[gv(data, p3, pos+3)] = data[gv(data, p2, pos+2)] + data[gv(data, p1, pos+1)] 
            
            elif opt_code == 2:
                data[gv(data, p3, pos+3)] = data[gv(data, p2, pos+2)] * data[gv(data, p1, pos+1)] 
            
            elif opt_code == 3:
                data[gv(data, p1, pos+1)] = params[index_p]
                index_p += 1
            
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
    


# Part 1.
all_thruster = []
for parameters in permutations('01234', 5):
    out = 0

    for p in parameters:
        out = intcode((int(p), out))

    all_thruster.append(out)


print("Part 1:", max(all_thruster))



class IntCode:

    def __init__(self, phase: str):
        self.data = self.load_data()
        self.pos = 0
        self.phase_settings = int(phase)
        self.is_used = False
    
    def load_data(self):
        data = []
        with open("input.txt", "r") as file:
            for row in file:
                row = row.replace("\n", "")
                data = [int(a) for a in row.split(",")]
        return data

    def iter_int_code(self, params):
        index_p = 0
        # try:
        while True:
            opt_code = self.data[self.pos] % 10 if self.data[self.pos] != 99 else 99
            p3, p2, p1 = self.data[self.pos] % 100000 // 10000, self.data[self.pos] % 10000 // 1000, self.data[self.pos] % 1000 // 100

            if opt_code == 1:
                self.data[gv(self.data, p3, self.pos+3)] = self.data[gv(self.data, p2, self.pos+2)] + self.data[gv(self.data, p1, self.pos+1)] 
            
            elif opt_code == 2:
                self.data[gv(self.data, p3, self.pos+3)] = self.data[gv(self.data, p2, self.pos+2)] * self.data[gv(self.data, p1, self.pos+1)] 
            
            elif opt_code == 3:
                if not self.is_used:
                    self.is_used = True
                    self.data[gv(self.data, p1, self.pos+1)] = self.phase_settings
                else:
                    self.data[gv(self.data, p1, self.pos+1)] = params[index_p]
                    index_p += 1
            
            elif opt_code == 4:
                val_to_return = self.data[gv(self.data, p1, self.pos+1)]
                self.pos += 2
                return val_to_return
            
            elif opt_code == 5:
                self.pos = self.data[gv(self.data, p2, self.pos+2)] if self.data[gv(self.data, p1, self.pos+1)] != 0 else self.pos + 3
            
            elif opt_code == 6:
                self.pos = self.data[gv(self.data, p2, self.pos+2)] if self.data[gv(self.data, p1, self.pos+1)] == 0 else self.pos + 3

            
            elif opt_code == 7:
                self.data[gv(self.data, p3, self.pos+3)] = 1 if self.data[gv(self.data, p1, self.pos+1)] < self.data[gv(self.data, p2, self.pos+2)] else 0
            
            elif opt_code == 8:
                self.data[gv(self.data, p3, self.pos+3)] = 1 if self.data[gv(self.data, p1, self.pos+1)] == self.data[gv(self.data, p2, self.pos+2)] else 0
            
            elif opt_code == 99:
                break
            else:
                raise NameError("Aled")
            
            if opt_code in [3, 4]:
                self.pos += 2
            elif opt_code in [1, 2, 7, 8]:
                self.pos += 4
        # except Exception as e:
        #     pass
    


# Part 2.
all_thruster = []
for p in permutations('56789', 5):
    out = 0

    A, B, C, D, E = IntCode(p[0]), IntCode(p[1]), IntCode(p[2]), IntCode(p[3]), IntCode(p[4])
    o, last_o = 0, None
    for i in range(10000):
        o = A.iter_int_code([o])
        if o == None: break
        o = B.iter_int_code([o])
        if o == None: break
        
        o = C.iter_int_code([o])
        if o == None: break
        
        o = D.iter_int_code([o])
        if o == None: break
        o = E.iter_int_code([o])
        if o == None: break
        last_o = o
    all_thruster.append(last_o)
    
print("Part 2:", max(all_thruster))