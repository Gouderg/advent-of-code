# Monkey class.
class Monkey:

    def __init__(self, id, starting, operation, test_op, id_monkey_1, id_monkey_2):
        self.id = id
        self.starting = starting
        self.operation = operation
        self.test_op = test_op
        self.test_op_true = id_monkey_1
        self.test_op_false = id_monkey_2
        self.count = 0
    
    def update(self, zoo, mods=None):

        for worry in self.starting:

            self.count += 1
            worry = self.operationOnWorry(worry)

            if mods == None:
                worry = worry // 3
            else:
                worry = worry % mods

            if worry % self.test_op == 0:
                zoo[self.test_op_true].addItem(worry)
            else:
                zoo[self.test_op_false].addItem(worry)

        self.starting = []

    def operationOnWorry(self, worry):
        
        ope = self.operation.replace("old", str(worry))

        if "*" in ope:
            return int(ope.split(" * ")[0]) * int(ope.split(" * ")[1])
        
        if "+" in ope:
            return int(ope.split(" + ")[0]) + int(ope.split(" + ")[1])
        
        if "-" in ope:
            return int(ope.split(" - ")[0]) - int(ope.split(" - ")[1])
        
        if "/" in ope:
            return int(ope.split(" / ")[0]) // int(ope.split(" / ")[1])

    def addItem(self, value):
        self.starting.append(value)
    
    def __repr__(self) -> str:
        return "Count " + str(self.count)

# Extract data.
def init():
    zoo = {}
    id_monkey, starting, operation, test_op, id_monkey_1, id_monkey_2 = None, None, None, None, None, None
    mods = 1
    with open("input.txt", "r") as file:
        for row in file:
            row = row.replace("\n", "")
            if row == "":
                zoo[id_monkey] = Monkey(id_monkey, starting, operation, test_op, id_monkey_1, id_monkey_2)
                
            elif "Monkey" in row:
                id_monkey = int(row.split(' ')[1].replace(":", ""))

            elif "Starting" in row:
                starting = [int(a) for a in row.split(": ")[1].split(", ")]
            
            elif "Operation" in row:
                operation = row.split("new = ")[1]
            
            elif "Test" in row:
                test_op = int(row.split("divisible by ")[1])
                mods *= test_op

            elif "If true: throw" in row:
                id_monkey_1 = int(row.split('monkey ')[1])
            
            elif "If false: throw" in row:
                id_monkey_2 = int(row.split('monkey ')[1])
    return zoo, mods


# Part 1.
zoo, _ = init()
for round in range(20):
    for monkey in zoo:
        zoo[monkey].update(zoo)

all_value = sorted([zoo[monkey].count for monkey in zoo], reverse=True)
print("Part 1:", all_value[0] * all_value[1])

# # Part 2.
zoo, mods = init()
for round in range(10000):
    for monkey in zoo:
        zoo[monkey].update(zoo, mods=mods)
all_value = sorted([zoo[monkey].count for monkey in zoo], reverse=True)
print("Part 2:", all_value[0] * all_value[1])